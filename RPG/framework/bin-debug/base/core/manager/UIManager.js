/**
 * UI管理类
 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var UIManager = (function () {
    function UIManager() {
        this.viewList = {};
        this.openList = {};
    }
    UIManager.prototype.init = function (stage) {
        this._windowContainer = new BaseContainer();
        this._windowContainer.width = stage.width;
        this._windowContainer.height = stage.height;
        stage.addChild(this._windowContainer);
    };
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
    /**打开窗口 */
    UIManager.prototype.showUI = function (viewName, callback) {
        var viewInstance = this.viewList[viewName];
        if (!viewInstance) {
            var viewClass = egret.getDefinitionByName(viewName);
            if (viewClass) {
                viewInstance = new viewClass(viewName);
                this._windowContainer.addChild(viewInstance);
                this.viewList[viewName] = viewInstance;
            }
        }
        else {
            this._windowContainer.addChild(viewInstance);
        }
        if (viewInstance) {
            viewInstance.onShow();
            this.openList[viewName] = viewInstance;
        }
    };
    /**关闭窗口 */
    UIManager.prototype.hideUI = function (viewName) {
        var viewInstance = this.openList[viewName];
        if (viewInstance) {
            if (viewInstance.hideDestroy) {
                viewInstance.destroy();
                this._windowContainer.removeChild(viewInstance);
                delete this.openList[viewName];
                delete this.viewList[viewName];
            }
            else {
                viewInstance.onHide();
                this._windowContainer.removeChild(viewInstance);
                delete this.openList[viewName];
            }
        }
    };
    /**销毁窗口 */
    UIManager.prototype.destroyUI = function (viewName) {
        var viewInstance = this.openList[viewName] || this.viewList[viewName];
        if (viewInstance) {
            viewInstance.destroy();
            this._windowContainer.removeChild(viewInstance);
            delete this.openList[viewName];
            delete this.viewList[viewName];
        }
    };
    return UIManager;
}());
__reflect(UIManager.prototype, "UIManager");
//# sourceMappingURL=UIManager.js.map