//格子宽度
let gridWidth = 30
//格子之间的间隔
let gap = 3
//地图绘制的起始x坐标
let originX = 300
//地图绘制的起始y坐标
let originY = 300
//路径宽度=格子宽度
let lineWidth = gridWidth;
//路径颜色
let lineColor = 0x0a0aff;

class Main extends eui.UILayer {
    /**记录当前地图 */
    private curMap: any[]
    /**记录已经访问了的节点 */
    private visitedList: any[];
    /**记录当前的节点x */
    private visitX: number;
    /**记录当前的节点y */
    private visitY: number;
    /**目标点x */
    private targetX: number;
    /**目标点y */
    private targetY: number;
    /**记录地图有效路径节点总数 用于判断是否完成游戏 */
    private availableNodesCount: number;

    protected createChildren(): void {
        super.createChildren();

        egret.lifecycle.addLifecycleListener((context) => {
            // custom lifecycle plugin
        })

        this.runGame().catch(e => {
            console.log(e);
        })
    }

    /**记录滑动的前置坐标点用于判断滑动方向 */
    private touchPreX: number;
    private touchPreY: number;

    /**点击开始 */
    private onUserTouchBegin(event: egret.TouchEvent) {
        this.touchPreX = event.localX
        this.touchPreY = event.localY
    }

    /**点击移动 */
    private onUserTouchMove(event: egret.TouchEvent) {
        let deltax = Math.abs(this.touchPreX - event.localX)
        let deltay = Math.abs(this.touchPreY - event.localY)
        if (deltax < gridWidth && deltay < gridWidth) {
            return
        }

        let xstep = 0
        let ystep = 0;
        //如果是横向移动 
        if (deltax > deltay) {
            xstep = (this.touchPreX - event.localX > 0) ? -1 : 1;
        } else {
            ystep = (this.touchPreY - event.localY > 0) ? -1 : 1;
        }
        this.move(xstep, ystep);
        this.touchPreX = event.localX
        this.touchPreY = event.localY
    }

    /**移动
     * @param deltax 横向移动格子
     * @param deltay 纵向移动格子
     */
    private move(deltax, deltay) {
        let x = this.visitX + deltax;
        let y = this.visitY + deltay;
        if (y >= 0 && y < this.curMap.length && x >= 0 && x < this.curMap.length) {
            if (this.curMap[y][x] <= 0) {
                this.updateVisitedList(x, y);
            }
        }
    }

    private async runGame() {
        //监听触摸移动事件
        this.addEventListener(egret.TouchEvent.TOUCH_MOVE, this.onUserTouchMove.bind(this), this)
        this.addEventListener(egret.TouchEvent.TOUCH_BEGIN, this.onUserTouchBegin.bind(this), this)
        this.createGameScene();
    }

    /**
     * 创建场景界面
     * Create scene interface
     */
    protected createGameScene(): void {
        let map = [
            [-1, 1, 0, 0, 0, 1, 0, -2],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
        ]
        this.drawMap(map)
    }
    /**更新访问节点信息 */
    protected updateVisitedList(x, y) {
        if (x == this.visitX && y == this.visitY) {
            return
        }
        //修正坐标点 差值超过2的坐标点都是非法输入值 直接忽略
        if (Math.abs(this.visitX - x) + Math.abs(this.visitY - y) > 1) {
            return
        }
        var visitedList = this.visitedList
        var bBack = false;
        for (var k = 0; k < visitedList.length; k++) {
            var point = visitedList[k]
            //如果新节点处于已遍历节点 则属于回退 
            if (point[0] == x && point[1] == y) {
                bBack = true;
                break;
            }
        }
        //如果是回退 则移除最后一个路径节点 并将最后一个当作当前访问节点
        if (bBack) {
            if (this.visitedList.length > 1) {
                this.visitedList.length = this.visitedList.length - 1;
                this.visitX = x
                this.visitY = y
            }
        } else {
            this.visitedList.push([x, y])
            this.visitX = x
            this.visitY = y
        }
        this.drawPath()
        //如果访问到目标节点 则判断是否已经访问所有可访问节点 判断游戏是否结束
        if (x == this.targetX && y == this.targetY) {
            this.checkGameFinish()
        }
    }
    /**检测是否已经完成 */
    private checkGameFinish() {
        if (this.availableNodesCount == this.visitedList.length) {
            console.log("================finished================");
        } else {
            console.log("================not finish==============");
        }
    }
    /**绘制移动轨迹 */
    protected drawPath() {
        let startX = originX + gridWidth * 0.5
        let startY = originY + gridWidth * 0.5
        let nodeName = "path"
        let pathNode = this.getChildByName(nodeName) as egret.Shape
        if (pathNode) {
            pathNode.graphics.clear();
            this.removeChild(pathNode)
        }
        let painter = new egret.Shape();
        painter.name = nodeName
        this.addChild(painter)

        painter.graphics.lineStyle(lineWidth, lineColor, 1, true, egret.StageScaleMode.SHOW_ALL, egret.CapsStyle.SQUARE)
        for (var i = 0; i < this.visitedList.length; i++) {
            var position = this.visitedList[i]
            if (i == 0) {
                painter.graphics.moveTo(startX + position[0] * (gridWidth + gap), startY + position[1] * (gridWidth + gap))
            } else {
                painter.graphics.lineTo(startX + position[0] * (gridWidth + gap), startY + position[1] * (gridWidth + gap))
            }
        }
        painter.graphics.endFill()
    }
    /**绘制关卡地图 */
    protected drawMap(map: any[]) {
        this.curMap = map
        this.visitedList = []
        this.availableNodesCount = 0;
        for (var v = 0; v < map.length; v++) {
            for (var h = 0; h < map[v].length; h++) {
                let color = 0xffffff
                if (map[v][h] > 0) {
                    color = 0x000000
                } else {
                    this.availableNodesCount = this.availableNodesCount + 1;
                    if (map[v][h] == -1) {
                        color = 0xe86d00
                        this.updateVisitedList(h, v);
                    } else if (map[v][h] == -2) {
                        color = 0x0e00b8
                        this.targetX = h;
                        this.targetY = v;
                    }
                }
                let shape = new egret.Shape()
                shape.graphics.beginFill(color);
                shape.graphics.drawRect(originX + h * (gridWidth + gap), originY + v * (gridWidth + gap), gridWidth, gridWidth)
                shape.graphics.endFill();
                this.addChild(shape)
            }
        }
    }
}
