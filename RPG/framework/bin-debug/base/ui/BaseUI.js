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
        _this.gameEventList = {};
        _this.sysEventList = {};
        _this.viewName = viewName;
        var viewConf = UIConfig[_this.viewName];
        if (viewConf) {
            _this.skinName = viewConf.skinName;
        }
        return _this;
    }
    /**绑定事件 子类实现此函数 */
    BaseUI.prototype.bindAutoEvents = function () {
    };
    /**
     * 添加系统事件侦听
     * @param type 事件的类型。
     * @param listener 处理事件的侦听器函数。此函数必须接受 Event 对象作为其唯一的参数，并且不能返回任何结果，
     * 如下面的示例所示： function(evt:Event):void 函数可以有任何名称。
     * @param thisObject 侦听函数绑定的 this 对象。
     * @param useCapture 确定侦听器是运行于捕获阶段还是运行于目标和冒泡阶段。如果将 useCapture 设置为 true，
     * 则侦听器只在捕获阶段处理事件，而不在目标或冒泡阶段处理事件。如果 useCapture 为 false，则侦听器只在目标或冒泡阶段处理事件。
     * 要在所有三个阶段都侦听事件，请调用 addEventListener 两次：一次将 useCapture 设置为 true，一次将 useCapture 设置为 false。
     * @param priority 事件侦听器的优先级。优先级由一个带符号的 32 位整数指定。数字越大，优先级越高。优先级为 n 的所有侦听器会在
     * 优先级为 n -1 的侦听器之前得到处理。如果两个或更多个侦听器共享相同的优先级，则按照它们的添加顺序进行处理。默认优先级为 0。
     */
    BaseUI.prototype.bindEvent = function (type, listener, thisObject, useCapture, priority) {
        if (!this.sysEventList[type]) {
            this.sysEventList[type] = { type: type, listener: listener, thisObject: thisObject, useCapture: useCapture, priority: priority };
            this.addEventListener(type, listener, thisObject, useCapture, priority);
        }
    };
    /**
     * 移除系统事件侦听
     * @param type 事件的类型。
     * @param listener 处理事件的侦听器函数。此函数必须接受 Event 对象作为其唯一的参数，并且不能返回任何结果，
     * 如下面的示例所示： function(param:any):void 函数可以有任何名称。
     * @param thisObject 侦听函数绑定的 this 对象。
     */
    BaseUI.prototype.unbindEvent = function (type) {
        if (this.sysEventList[type]) {
            var eventObj = this.sysEventList[type];
            this.removeEventListener(eventObj.type, eventObj.listener, eventObj.thisObject, eventObj.useCapture);
            delete this.sysEventList[type];
        }
    };
    /**
    * 添加游戏内事件侦听
    * @param type 事件的类型。
     */
    BaseUI.prototype.bindGameEvent = function (type, listener, thisObject) {
        if (!this.gameEventList[type]) {
            var eventId = GameEventSystem.instance.add(type, listener, thisObject);
            this.gameEventList[type] = eventId;
        }
    };
    /**
    * 移除游戏内事件侦听
    * @param type 事件的类型。
     */
    BaseUI.prototype.unbindGameEvent = function (type) {
        if (this.gameEventList[type]) {
            var eventId = this.gameEventList[type];
            GameEventSystem.instance.remove(eventId);
            delete this.gameEventList[type];
        }
    };
    /**暂停所有事件监听 */
    BaseUI.prototype.pauseGameEvent = function () {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType];
            GameEventSystem.instance.pause(eventId);
        }
    };
    /**恢复所有事件监听 */
    BaseUI.prototype.resumeGameEvent = function () {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType];
            GameEventSystem.instance.resume(eventId);
        }
    };
    BaseUI.prototype.onShow = function () {
        this.bindAutoEvents();
        this.resumeGameEvent();
    };
    BaseUI.prototype.onHide = function () {
        this.pauseGameEvent();
    };
    BaseUI.prototype.close = function () {
        this.onHide();
    };
    BaseUI.prototype.releaseEvents = function () {
        var events = Object.keys(this.gameEventList);
        for (var i = 0; i < events.length; i++) {
            var eventId = this.gameEventList[events[i]];
            GameEventSystem.instance.remove(eventId);
            delete this.gameEventList[events[i]];
        }
        this.gameEventList = {};
        this.sysEventList = {};
    };
    BaseUI.prototype.destroy = function () {
        this.releaseEvents();
    };
    return BaseUI;
}(eui.Component));
__reflect(BaseUI.prototype, "BaseUI");
//# sourceMappingURL=BaseUI.js.map