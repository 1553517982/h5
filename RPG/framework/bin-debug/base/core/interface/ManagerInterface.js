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
var Manager = (function (_super) {
    __extends(Manager, _super);
    function Manager() {
        return _super.call(this) || this;
    }
    /**初始化 */
    Manager.prototype.init = function () {
    };
    /**清理 */
    Manager.prototype.finit = function () {
    };
    /**重置 */
    Manager.prototype.reset = function () {
    };
    return Manager;
}(GameComponent));
__reflect(Manager.prototype, "Manager", ["ManagerInterface"]);
