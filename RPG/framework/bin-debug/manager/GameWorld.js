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
    GameWorld.prototype.start = function () {
        this.registManagers();
        var gameStateMgr = this.globalMgr.getManager("GameStateManager");
        gameStateMgr.setState(GameStateDef.Login);
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