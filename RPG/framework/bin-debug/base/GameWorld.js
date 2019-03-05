var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = this && this.__extends || function __extends(t, e) { 
 function r() { 
 this.constructor = t;
}
for (var i in e) e.hasOwnProperty(i) && (t[i] = e[i]);
r.prototype = e.prototype, t.prototype = new r();
};
var GameWorld = (function (_super) {
    __extends(GameWorld, _super);
    function GameWorld() {
        var _this = _super.call(this) || this;
        _this.globalMgr = GlobalManager.instance;
        return _this;
    }
    Object.defineProperty(GameWorld, "instance", {
        get: function () {
            if (!this._instance) {
                this._instance = new GameWorld();
            }
            return this._instance;
        },
        enumerable: true,
        configurable: true
    });
    //开始游戏
    GameWorld.prototype.start = function (stage) {
        this.initLayer(stage);
        this.registManagers();
        var gameStateMgr = this.globalMgr.getManager("GameStateManager");
        gameStateMgr.setState(GameStateDef.Login);
    };
    /**
     * 切换场景容器
     */
    GameWorld.prototype.switchScene = function (gameState) {
        var scene = this._sceneArray[gameState];
        if (scene) {
            var zOrder = 0;
            for (var k in this._sceneArray) {
                if (Number(k) != gameState) {
                    this._sceneRootLayer.setChildIndex(scene, zOrder);
                }
                zOrder++;
            }
            this._sceneRootLayer.setChildIndex(scene, zOrder);
        }
    };
    GameWorld.prototype.getScene = function (gameState) {
        return this._sceneArray[gameState];
    };
    GameWorld.prototype.addScene = function (sceneDef, scene) {
        this._sceneRootLayer.addChild(scene);
        this._sceneArray[sceneDef] = scene;
    };
    /**初始化层级组件 */
    GameWorld.prototype.initLayer = function (stage) {
        //场景处于游戏最底层
        this._sceneRootLayer = new egret.DisplayObjectContainer();
        this._sceneRootLayer.width = stage.width;
        this._sceneRootLayer.height = stage.height;
        stage.addChild(this._sceneRootLayer);
        //游戏场景
        this.addScene(GameStateDef.Gaming, new GameScene());
        //登录场景
        this.addScene(GameStateDef.Login, new LoginScene());
        //加载场景
        this.addScene(GameStateDef.Loading, new LoadingScene());
        //UI处于游戏最上层
        this._uiRootLayer = new egret.DisplayObjectContainer();
        this._sceneRootLayer.width = stage.width;
        this._sceneRootLayer.height = stage.height;
        stage.addChild(this._uiRootLayer);
    };
    //注册游戏管理类
    GameWorld.prototype.registManagers = function () {
        //注册游戏状态管理类
        this.globalMgr.regist("GameStateManager", GameStateManager);
    };
    return GameWorld;
}(egret.DisplayObjectContainer));
__reflect(GameWorld.prototype, "GameWorld");
//# sourceMappingURL=GameWorld.js.map