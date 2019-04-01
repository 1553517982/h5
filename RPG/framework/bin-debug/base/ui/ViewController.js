var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
/**
 * 界面controller基类
 */
var ViewController = (function () {
    function ViewController(view) {
        this.viewInstance = view;
        this.gameEventList = {};
    }
    Object.defineProperty(ViewController.prototype, "view", {
        /**返回view的实例 */
        get: function () {
            return this.viewInstance;
        },
        enumerable: true,
        configurable: true
    });
    /**
    * 添加游戏内事件侦听
    * @param type 事件的类型。
     */
    ViewController.prototype.bindGameEvent = function (type, listener, thisObject) {
        if (!this.gameEventList[type]) {
            var eventId = GameEventSystem.instance.add(type, listener, thisObject);
            this.gameEventList[type] = eventId;
        }
    };
    /**
    * 移除游戏内事件侦听
    * @param type 事件的类型。
     */
    ViewController.prototype.unbindGameEvent = function (type) {
        if (this.gameEventList[type]) {
            var eventId = this.gameEventList[type];
            GameEventSystem.instance.remove(eventId);
            delete this.gameEventList[type];
        }
    };
    /**暂停所有事件监听 */
    ViewController.prototype.pauseGameEvent = function () {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType];
            GameEventSystem.instance.pause(eventId);
        }
    };
    /**恢复所有事件监听 */
    ViewController.prototype.resumeGameEvent = function () {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType];
            GameEventSystem.instance.resume(eventId);
        }
    };
    /**界面打开时 */
    ViewController.prototype.onShow = function () {
        this.resumeGameEvent();
    };
    /**界面关闭时 */
    ViewController.prototype.onHide = function () {
        this.pauseGameEvent();
    };
    ViewController.prototype.close = function () {
        this.onHide();
    };
    /**界面销毁时 */
    ViewController.prototype.destroy = function () {
        this.releaseGameEvents();
    };
    /**界面初始化成功 */
    ViewController.prototype.onCreate = function () {
        //绑定事件 全部写在这里
    };
    /**移除事件监听 */
    ViewController.prototype.releaseGameEvents = function () {
        var events = Object.keys(this.gameEventList);
        for (var i = 0; i < events.length; i++) {
            var eventId = this.gameEventList[events[i]];
            GameEventSystem.instance.remove(eventId);
            delete this.gameEventList[events[i]];
        }
        this.gameEventList = {};
    };
    return ViewController;
}());
__reflect(ViewController.prototype, "ViewController");
