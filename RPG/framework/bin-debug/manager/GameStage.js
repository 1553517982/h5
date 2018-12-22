var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
/**
 * 游戏主舞台，渲染根节点，把其他节点也顺便弄出来
 */
var GameStage = (function () {
    function GameStage() {
    }
    Object.defineProperty(GameStage, "instance", {
        get: function () {
            if (this.$instance == null) {
                this.$instance = new GameStage();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * 初始化舞台
     * 创建各层次节点
     */
    GameStage.prototype.init = function (stage) {
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
    };
    /**
     * 游戏正式开始
     */
    GameStage.prototype.startGame = function (main) {
    };
    return GameStage;
}());
__reflect(GameStage.prototype, "GameStage");
//# sourceMappingURL=GameStage.js.map