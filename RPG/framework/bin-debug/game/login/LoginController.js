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
var LoginController = (function (_super) {
    __extends(LoginController, _super);
    function LoginController() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    //绑定事件 全部写在这里
    LoginController.prototype.onCreate = function () {
        this.bindGameEvent(GameEvent.E_ACCOUNT_LOGIN, this.onLoginSuccess, this);
        this.bindGameEvent(GameEvent.E_ENTER_SERVER, this.onEnterServerSuccess, this);
    };
    /**点击登陆按钮 */
    LoginController.prototype.onLogin = function (account, password) {
        /**
         * @todo 后台通信 获取游戏内帐号信息
         */
        LoginManager.instance.onLoginSuccess(account, password);
    };
    /**
     * 进入服务器
     */
    LoginController.prototype.onEnterServer = function (serverId) {
        LoginManager.instance.onEnterServerSuccess(serverId);
    };
    /**进入服务器成功 */
    LoginController.prototype.onEnterServerSuccess = function (serverId) {
        this.view.onEnterServerSuccess(serverId);
        App.GSManager.setState(GameStateDef.Gaming);
    };
    /**处理登陆回调 */
    LoginController.prototype.onLoginSuccess = function (response) {
        this.accountInfo = {};
        this.accountInfo.account = response.account;
        this.accountInfo.password = response.password;
        this.accountInfo.lastServerId = response.lastServerId;
        this.setServerList(response.serverlist);
        this.view.onLoginSuccess(response);
    };
    /**设置服务器列表 */
    LoginController.prototype.setServerList = function (list) {
        this.serverList = list;
    };
    return LoginController;
}(ViewController));
__reflect(LoginController.prototype, "LoginController");
