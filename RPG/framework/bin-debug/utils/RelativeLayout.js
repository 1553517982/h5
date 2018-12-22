var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var RelativeLayout = (function () {
    function RelativeLayout() {
    }
    Object.defineProperty(RelativeLayout, "instance", {
        get: function () {
            if (this._instance == null) {
                this._instance = new RelativeLayout();
            }
            return this._instance;
        },
        enumerable: true,
        configurable: true
    });
    /**计算layout的坐标 */
    RelativeLayout.prototype.calulatePos = function (node, parent, type, offsetY) {
        var winX = node.width;
        var winY = node.height;
        var winAnpx = node.anchorOffsetX;
        var winAnpy = node.anchorOffsetY;
        var parentWidth;
        var parentHeight;
        if (parent == null) {
            parentWidth = GameStage.instance.stage.stageWidth;
            parentHeight = GameStage.instance.stage.stageHeight;
        }
        else {
            parentWidth = parent.stage.stageWidth;
            parentHeight = parent.stage.stageHeight;
        }
        // console.log("winX,winY,winAnpx,winAnpy,parentWidth,parentHeight", winX, winY, winAnpx, winAnpy, parentWidth, parentHeight)
        var pos = {
            x: 0,
            y: 0,
        };
        if (type == RelativeLayoutDef.CENTER) {
            pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX;
            pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.RCENTER) {
            pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX;
            pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.LCENTER) {
            pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX;
            pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.TCENTER) {
            pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX;
            pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.TRIGHT) {
            pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX;
            pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.TLEFT) {
            pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX;
            pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY;
        }
        else if (type == RelativeLayoutDef.DRIGHT) {
            pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX;
            pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY;
        }
        else if (type == RelativeLayoutDef.DCENTER) {
            pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX;
            pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY;
        }
        else if (type == RelativeLayoutDef.DLEFT) {
            pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX;
            pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY;
        }
        if (offsetY) {
            pos.y = pos.y - offsetY;
        }
        return pos;
    };
    return RelativeLayout;
}());
__reflect(RelativeLayout.prototype, "RelativeLayout");
/** 相对位置定义  顺时针8个方位 + 正中央一个点*/
var RelativeLayoutDef;
(function (RelativeLayoutDef) {
    RelativeLayoutDef[RelativeLayoutDef["CENTER"] = 0] = "CENTER";
    RelativeLayoutDef[RelativeLayoutDef["TCENTER"] = 1] = "TCENTER";
    RelativeLayoutDef[RelativeLayoutDef["TRIGHT"] = 2] = "TRIGHT";
    RelativeLayoutDef[RelativeLayoutDef["RCENTER"] = 3] = "RCENTER";
    RelativeLayoutDef[RelativeLayoutDef["DRIGHT"] = 4] = "DRIGHT";
    RelativeLayoutDef[RelativeLayoutDef["DCENTER"] = 5] = "DCENTER";
    RelativeLayoutDef[RelativeLayoutDef["DLEFT"] = 6] = "DLEFT";
    RelativeLayoutDef[RelativeLayoutDef["LCENTER"] = 7] = "LCENTER";
    RelativeLayoutDef[RelativeLayoutDef["TLEFT"] = 8] = "TLEFT";
})(RelativeLayoutDef || (RelativeLayoutDef = {}));
//# sourceMappingURL=RelativeLayout.js.map