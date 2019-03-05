var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
//登录状态
var LoginState = (function () {
    function LoginState() {
    }
    LoginState.prototype.onEnter = function () {
        console.log("进入登录状态");
        GameWorld.instance.switchScene(GameStateDef.Login);
    };
    LoginState.prototype.onExit = function () {
        console.log("离开登录状态");
    };
    return LoginState;
}());
__reflect(LoginState.prototype, "LoginState", ["GameState"]);
//# sourceMappingURL=LoginState.js.map