/**
 * UI管理类
 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var UIManager = (function () {
    function UIManager() {
    }
    Object.defineProperty(UIManager, "instance", {
        get: function () {
            if (!this.$instance) {
                this.$instance = new UIManager();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    return UIManager;
}());
__reflect(UIManager.prototype, "UIManager");
//# sourceMappingURL=UIManager.js.map