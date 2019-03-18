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
var LoginView = (function (_super) {
    __extends(LoginView, _super);
    function LoginView() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    /**绑定事件 */
    LoginView.prototype.bindAutoEvents = function () {
        this.Btn_login.addEventListener(egret.TouchEvent.TOUCH_BEGIN, this.onLogin, this);
    };
    LoginView.prototype.onLogin = function () {
        console.log("点击登录按钮");
    };
    return LoginView;
}(BaseUI));
__reflect(LoginView.prototype, "LoginView");
//# sourceMappingURL=LoginView.js.map