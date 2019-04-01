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
/**
 * UI基类
 *
 */
var BaseUI = (function (_super) {
    __extends(BaseUI, _super);
    function BaseUI(viewName) {
        var _this = _super.call(this) || this;
        _this.viewName = viewName;
        var viewConf = UIConfig[_this.viewName];
        if (viewConf) {
            _this.skinName = viewConf.skinName;
            _this.hideDestroy = viewConf.destroy;
        }
        return _this;
    }
    BaseUI.prototype.childrenCreated = function () {
        this.onCreate();
    };
    BaseUI.prototype.onCreate = function () {
        console.log("界面创建完毕：", this.viewName);
        this.controller.onCreate();
    };
    BaseUI.prototype.onShow = function () {
        this.controller.onShow();
        console.log("打开界面" + this.viewName);
    };
    BaseUI.prototype.onHide = function () {
        this.controller.onHide();
        console.log("关闭界面" + this.viewName);
    };
    BaseUI.prototype.destroy = function () {
        this.controller.destroy();
        console.log("销毁界面" + this.viewName);
    };
    BaseUI.prototype.close = function () {
        App.UIManager.hideUI(this.viewName);
    };
    return BaseUI;
}(eui.Component));
__reflect(BaseUI.prototype, "BaseUI");
//# sourceMappingURL=BaseUI.js.map