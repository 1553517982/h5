/**定义全局单例管理器 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var App = (function () {
    function App() {
    }
    Object.defineProperty(App, "EventSystem", {
        /**全局事件管理器 */
        get: function () {
            return GameEventSystem.instance;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(App, "GSManager", {
        /**全局状态管理器 */
        get: function () {
            return GameStateManager.instance;
        },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(App, "UIManager", {
        /**全局窗口管理器 */
        get: function () {
            return UIManager.instance;
        },
        enumerable: true,
        configurable: true
    });
    return App;
}());
__reflect(App.prototype, "App");
