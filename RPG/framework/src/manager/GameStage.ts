/**
 * 游戏主舞台，渲染根节点，把其他节点也顺便弄出来
 */
class GameStage {
    /** 缩略图节点 */
    public thumbnailNode: egret.DisplayObjectContainer;
    /** 场景节点 */
    public sceneNode: egret.DisplayObjectContainer;
    /** 场景特效节点 */
    public sceneEffectNode: egret.DisplayObjectContainer;
    /** 实体节点 */
    public entityNode: egret.DisplayObjectContainer;
    /** 特效节点 */
    public effectNode: egret.DisplayObjectContainer;
    /** 名字板 */
    public billboardNode: egret.DisplayObjectContainer;
    /** 蒙板 */
    public maskNode: egret.DisplayObjectContainer;
    /** ui节点 */
    public uiNode: egret.DisplayObjectContainer;
    /** 新手引导节点 */
    public guidanceNode: egret.DisplayObjectContainer;

    /** 游戏主舞台 */
    public stage: egret.Stage;

    /**是否已经监听键盘事件 */
    private $isListeningKeyBoard: boolean;

    private static $instance: GameStage;

    public static get instance(): GameStage {
        if (this.$instance == null) {
            this.$instance = new GameStage();
        }
        return this.$instance;
    }

    public constructor() {

    }

    /** 
     * 初始化舞台 
     * 创建各层次节点
     */
    public init(stage: egret.Stage): void {
        this.stage = stage;
        this.thumbnailNode = new egret.DisplayObjectContainer();
        stage.addChild(this.thumbnailNode);
        this.sceneNode = new egret.DisplayObjectContainer();
        stage.addChild(this.sceneNode);
        this.sceneEffectNode = new egret.DisplayObjectContainer();
        stage.addChild(this.sceneEffectNode);
        this.entityNode = new egret.DisplayObjectContainer();
        stage.addChild(this.entityNode);
        this.effectNode = new egret.DisplayObjectContainer();
        stage.addChild(this.effectNode);
        this.billboardNode = new egret.DisplayObjectContainer();
        stage.addChild(this.billboardNode);
        this.maskNode = new egret.DisplayObjectContainer();
        stage.addChild(this.maskNode);
        this.uiNode = new egret.DisplayObjectContainer();
        stage.addChild(this.uiNode);
        this.guidanceNode = new egret.DisplayObjectContainer();
        stage.addChild(this.guidanceNode);
    }

    /**
     * 游戏正式开始
     */
    public startGame(main: Main): void {

    }
}