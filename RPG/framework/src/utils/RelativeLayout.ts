class RelativeLayout {

	private static _instance: RelativeLayout;

	public static get instance(): RelativeLayout {
		if (this._instance == null) {
			this._instance = new RelativeLayout();
		}
		return this._instance;
	}
	public constructor() {

	}
	/**计算layout的坐标 */
	public calulatePos(node: any, parent: egret.DisplayObjectContainer, type: RelativeLayoutDef,offsetY?:number): any {
		let winX = node.width;
		let winY = node.height;
		let winAnpx = node.anchorOffsetX
		let winAnpy = node.anchorOffsetY
		let parentWidth;
		let parentHeight;
		if (parent == null) {
			parentWidth = GameStage.instance.stage.stageWidth;
			parentHeight = GameStage.instance.stage.stageHeight;
		} else {
			parentWidth = parent.stage.stageWidth;
			parentHeight = parent.stage.stageHeight;
		}

		// console.log("winX,winY,winAnpx,winAnpy,parentWidth,parentHeight", winX, winY, winAnpx, winAnpy, parentWidth, parentHeight)
		let pos = {
			x: 0,
			y: 0,
		}
		if (type == RelativeLayoutDef.CENTER)//居中
		{
			pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX
			pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY
		} else if (type == RelativeLayoutDef.RCENTER)//右边居中
		{
			pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX
			pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY

		} else if (type == RelativeLayoutDef.LCENTER)//左边居中
		{
			pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX
			pos.y = (parentHeight - winY) * 0.5 + (winAnpy - 0.0) * winY

		} else if (type == RelativeLayoutDef.TCENTER)//顶部居中
		{
			pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX
			pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY
		} else if (type == RelativeLayoutDef.TRIGHT)//顶部靠右
		{
			pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX
			pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY
		} else if (type == RelativeLayoutDef.TLEFT)//顶部靠左
		{
			pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX
			pos.y = 0.0 * parentHeight + (winAnpy - 0.0) * winY
		} else if (type == RelativeLayoutDef.DRIGHT)//底部靠右
		{
			pos.x = 1.0 * parentWidth + (winAnpx - 1.0) * winX
			pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY

		} else if (type == RelativeLayoutDef.DCENTER)//底部居中
		{
			pos.x = (parentWidth - winX) * 0.5 + (winAnpx - 0.0) * winX
			pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY

		} else if (type == RelativeLayoutDef.DLEFT)//底部靠左
		{
			pos.x = 0.0 * parentWidth + (winAnpx - 0.0) * winX
			pos.y = 1.0 * parentHeight + (winAnpy - 1.0) * winY
		}
		if(offsetY){
			pos.y = pos.y-offsetY
		}
		return pos;
	}
}

/** 相对位置定义  顺时针8个方位 + 正中央一个点*/
enum RelativeLayoutDef {
	CENTER = 0,  //居中
	TCENTER = 1,  //顶部居中
	TRIGHT = 2,  //顶部靠右
	RCENTER = 3,  //靠右居中
	DRIGHT = 4,//底部靠右
	DCENTER = 5, // 底部居中
	DLEFT = 6, //底部靠左
	LCENTER = 7,//靠左居中
	TLEFT = 8,//顶部靠左
}