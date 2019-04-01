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
var LoginManager = (function (_super) {
    __extends(LoginManager, _super);
    function LoginManager() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(LoginManager, "instance", {
        get: function () {
            if (!this.$instance) {
                this.$instance = new LoginManager();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    LoginManager.prototype.onLoginSuccess = function (account, password) {
        var response = {
            account: account,
            password: password,
            lastServerId: "1",
            recommandServerId: "1",
            createTime: "1554121810",
            serverlist: {
                "1": {
                    ip: "192.168.1.131",
                    port: "6001",
                    state: "good",
                    name: "测试服"
                }
            }
        };
        GameEventSystem.instance.dispatch(GameEvent.E_ACCOUNT_LOGIN, response);
    };
    return LoginManager;
}(Manager));
__reflect(LoginManager.prototype, "LoginManager");
//# sourceMappingURL=LoginManager.js.map