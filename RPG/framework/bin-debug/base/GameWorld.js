var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var GameWorld = (function () {
    function GameWorld() {
        this._sceneObjMap = {};
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
        /**初始化游戏层级 */
        this.initLayer(stage);
        /**设置游戏状态为登录 */
        App.GSManager.setState(GameStateDef.Login);
    };
    /**
     * 切换场景容器
     */
    GameWorld.prototype.switchScene = function (gameState) {
        if (this._preGameState && this._preGameState != gameState) {
            var preScene = this.getScene(gameState);
            if (preScene) {
                preScene.onExit();
            }
        }
        var scene = this.getScene(gameState);
        if (scene) {
            var zOrder = 0;
            for (var k in this._sceneObjMap) {
                if (Number(k) != gameState) {
                    this._sceneRootLayer.setChildIndex(scene, zOrder);
                }
                zOrder++;
            }
            this._sceneRootLayer.setChildIndex(scene, zOrder);
            scene.onEnter();
        }
    };
    /**获取场景 */
    GameWorld.prototype.getScene = function (gameState) {
        if (!this._sceneObjMap[gameState]) {
            if (gameState == GameStateDef.Gaming) {
                //游戏场景
                this.addScene(GameStateDef.Gaming, new GameScene());
            }
            else if (gameState == GameStateDef.Login) {
                //登录场景
                this.addScene(GameStateDef.Login, new LoginScene());
            }
            else if (gameState == GameStateDef.Loading) {
                //加载场景
                this.addScene(GameStateDef.Loading, new LoadingScene());
            }
        }
        return this._sceneObjMap[gameState];
    };
    GameWorld.prototype.addScene = function (sceneDef, scene) {
        scene.width = this._sceneRootLayer.width;
        scene.height = this._sceneRootLayer.height;
        this._sceneRootLayer.addChild(scene);
        this._sceneObjMap[sceneDef] = scene;
    };
    /**初始化层级组件 */
    GameWorld.prototype.initLayer = function (stage) {
        /**游戏场景 */
        this._sceneRootLayer = new BaseContainer();
        this._sceneRootLayer.width = stage.width;
        this._sceneRootLayer.height = stage.height;
        stage.addChild(this._sceneRootLayer);
        /**UI容器 */
        App.UIManager.init(stage);
    };
    return GameWorld;
}());
__reflect(GameWorld.prototype, "GameWorld");
