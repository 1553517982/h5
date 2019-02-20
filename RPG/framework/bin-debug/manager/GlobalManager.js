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
/**Manager管理类 */
var GlobalManager = (function (_super) {
    __extends(GlobalManager, _super);
    function GlobalManager() {
        var _this = _super.call(this) || this;
        _this.init();
        return _this;
    }
    /**初始化 */
    GlobalManager.prototype.init = function () {
        this.mgrList = [];
        this.registList = {};
        this.managerIndexMap = {};
    };
    /**清理 */
    GlobalManager.prototype.finit = function () {
    };
    /**重置 */
    GlobalManager.prototype.reset = function () {
    };
    Object.defineProperty(GlobalManager, "instance", {
        get: function () {
            if (!this.$instance) {
                this.$instance = new GlobalManager();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    GlobalManager.prototype.regist = function (className, GameClass) {
        this.registList[className] = GameClass;
    };
    /**获取对应的管理类 */
    GlobalManager.prototype.getManager = function (managerName) {
        var managerIndex = this.managerIndexMap[managerName];
        if (managerIndex != undefined) {
            return this.mgrList[managerIndex];
        }
        else {
            var className = this.registList[managerName];
            if (className) {
                var manager = new className();
                this.mgrList.push(manager);
                this.managerIndexMap[managerName] = (this.mgrList.length - 1);
                return manager;
            }
            else {
                console.warn(managerName, "未注册到GlobalManager！");
            }
        }
    };
    return GlobalManager;
}(Manager));
__reflect(GlobalManager.prototype, "GlobalManager");
//# sourceMappingURL=GlobalManager.js.map