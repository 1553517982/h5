class GameWorld extends egret.DisplayObjectContainer {
	//游戏世界单例
	private static _instance: GameWorld;
	//全局manager管理类
	private globalMgr: GlobalManager;

	//场景根节点
	private _sceneRootLayer: egret.DisplayObjectContainer;
	//实体根节点
	private _entityRootLayer: egret.DisplayObjectContainer;
	//UI根节点
	private _uiRootLayer: egret.DisplayObjectContainer;

	public constructor() {
		super()
		this.globalMgr = GlobalManager.instance
	}

	public static get instance(): GameWorld {
		if (!this._instance) {
			this._instance = new GameWorld()
		}
		return this._instance;
	}
	//开始游戏
	public start(stage: egret.Stage) {
		this.initLayer(stage)
		this.registManagers()
		let gameStateMgr = this.globalMgr.getManager("GameStateManager") as GameStateManager
		gameStateMgr.setState(GameStateDef.Login)
	}

	/**初始化层级组件 */
	private initLayer(stage: egret.Stage) {
		
		this._sceneRootLayer = new egret.DisplayObjectContainer()
		this._sceneRootLayer.width = stage.width
		this._sceneRootLayer.height = stage.height
		stage.addChild(this._sceneRootLayer)

		this._entityRootLayer = new egret.DisplayObjectContainer()
		this._sceneRootLayer.width = stage.width
		this._sceneRootLayer.height = stage.height
		stage.addChild(this._entityRootLayer)

		this._uiRootLayer = new egret.DisplayObjectContainer()
		this._sceneRootLayer.width = stage.width
		this._sceneRootLayer.height = stage.height
		stage.addChild(this._uiRootLayer)
	}

	//注册游戏管理类
	private registManagers() {
		//注册游戏状态管理类
		this.globalMgr.regist("GameStateManager", GameStateManager)
	}
}