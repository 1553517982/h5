/**
 *  游戏状态管理类
 *
*/
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
var GameStateDef;
(function (GameStateDef) {
    //加载
    GameStateDef[GameStateDef["Loading"] = 0] = "Loading";
    //登录
    GameStateDef[GameStateDef["Login"] = 1] = "Login";
    //游戏中
    GameStateDef[GameStateDef["Gaming"] = 2] = "Gaming";
})(GameStateDef || (GameStateDef = {}));
var GameStateManager = (function (_super) {
    __extends(GameStateManager, _super);
    function GameStateManager() {
        var _this = _super.call(this) || this;
        _this._gameStateMap = {};
        return _this;
    }
    GameStateManager.prototype.setState = function (state) {
        if (this._gameStateType != state) {
            this._gameStateType = state;
            this.changeState(state);
        }
    };
    Object.defineProperty(GameStateManager.prototype, "state", {
        get: function () {
            return this._gameStateType;
        },
        enumerable: true,
        configurable: true
    });
    GameStateManager.prototype.changeState = function (state) {
        if (this._currentGameState) {
            this._currentGameState.onExit();
        }
        this._currentGameState = this.getGameState(state);
        if (this._currentGameState) {
            this._currentGameState.onEnter();
        }
    };
    //根据状态类型 获取游戏状态对象
    GameStateManager.prototype.getGameState = function (state) {
        if (this._gameStateMap[state]) {
            return this._gameStateMap[state];
        }
        var nState = null;
        switch (state) {
            case GameStateDef.Login:
                nState = new LoginState();
                break;
            case GameStateDef.Gaming:
                nState = new GamingState();
                break;
        }
        this._gameStateMap[state] = nState;
        return nState;
    };
    return GameStateManager;
}(Manager));
__reflect(GameStateManager.prototype, "GameStateManager");
//# sourceMappingURL=GameStateManager.js.map