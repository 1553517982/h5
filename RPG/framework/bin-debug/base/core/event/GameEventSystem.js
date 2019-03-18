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
/**游戏事件通知管理中心 */
var GameEventObject = (function (_super) {
    __extends(GameEventObject, _super);
    function GameEventObject(id, eventId, callback, owner) {
        var _this = _super.call(this) || this;
        _this.eventId = eventId;
        _this.callback = callback;
        _this.isSleep = false;
        _this.owner = owner;
        return _this;
    }
    GameEventObject.prototype.trigger = function () {
        var param = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            param[_i] = arguments[_i];
        }
        (_a = this.callback).call.apply(_a, [this.owner].concat(param));
        var _a;
    };
    GameEventObject.prototype.pause = function () {
        this.isSleep = true;
    };
    GameEventObject.prototype.resume = function () {
        this.isSleep = false;
    };
    /**是否可触发 */
    GameEventObject.prototype.canTriiger = function () {
        return !this.isSleep;
    };
    return GameEventObject;
}(GameComponent));
__reflect(GameEventObject.prototype, "GameEventObject");
var GameEventSystem = (function () {
    function GameEventSystem() {
        this.$eventHandles = {};
        this.$eventIndexList = {};
        this.$eventObjList = {};
    }
    /**创建事件对象 */
    GameEventSystem.prototype.createEventObj = function (eventId, handle, thisObj) {
        var eventGenerateId = generateId();
        return new GameEventObject(eventGenerateId, eventId, handle, thisObj);
    };
    Object.defineProperty(GameEventSystem, "instance", {
        get: function () {
            if (this.$instance == null) {
                this.$instance = new GameEventSystem();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    /**添加事件监听 */
    GameEventSystem.prototype.add = function (eventId, handle, thisObj) {
        var eventObj = this.createEventObj(eventId, handle, thisObj);
        if (!this.$eventHandles[eventId]) {
            this.$eventHandles[eventId] = [];
        }
        var eventObjId = eventObj.getId();
        this.$eventObjList[eventObjId] = eventObj;
        this.$eventHandles[eventId].push(eventObjId);
        this.$eventIndexList[eventObjId] = (this.$eventHandles[eventId].length - 1);
        return eventObjId;
    };
    /**移除事件监听 */
    GameEventSystem.prototype.remove = function (eventObjID) {
        var eventObj = this.$eventObjList[eventObjID];
        if (eventObj) {
            var eventId = eventObj.eventId;
            var eventIndex = this.$eventIndexList[eventObjID];
            if (this.$eventHandles[eventId]) {
                //这里将id置0即可  不需要移除 否则下标会缩进导致下标列表有问题
                this.$eventHandles[eventId][eventIndex] = 0;
            }
            delete this.$eventIndexList[eventObjID];
            delete this.$eventObjList[eventObjID];
        }
    };
    /**暂停事件监听 */
    GameEventSystem.prototype.pause = function (eventObjID) {
        var event = this.$eventObjList[eventObjID];
        if (event) {
            event.pause();
        }
    };
    /**恢复事件监听 */
    GameEventSystem.prototype.resume = function (eventObjID) {
        var event = this.$eventObjList[eventObjID];
        if (event) {
            event.resume();
        }
    };
    /**恢复指定事件监听 */
    GameEventSystem.prototype.resumeEvent = function (eventId) {
        var objArray = this.$eventHandles[eventId];
        if (objArray && objArray.length > 0) {
            var i;
            var eventObj;
            for (i = 0; i < objArray.length; i++) {
                eventObj = objArray[i];
                eventObj.resume();
            }
        }
    };
    /**暂停指定事件 */
    GameEventSystem.prototype.pauseEvent = function (eventId) {
        var objArray = this.$eventHandles[eventId];
        if (objArray && objArray.length > 0) {
            var i;
            var eventObj;
            for (i = 0; i < objArray.length; i++) {
                eventObj = objArray[i];
                eventObj.pause();
            }
        }
    };
    /**暂停所有事件 */
    GameEventSystem.prototype.pauseAll = function () {
        var objList = this.$eventObjList;
        var eventId;
        var eventObj;
        for (eventId in objList) {
            eventObj = objList[eventId];
            eventObj.pause();
        }
    };
    /**派发事件 */
    GameEventSystem.prototype.dispatch = function (eventId) {
        var params = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            params[_i - 1] = arguments[_i];
        }
        var eventHandleList = this.$eventHandles[eventId];
        if (eventHandleList && eventHandleList.length > 0) {
            var i;
            var eventObj;
            for (i = 0; i < eventHandleList.length; i++) {
                eventObj = eventHandleList[i];
                if (eventObj) {
                    eventObj.trigger.apply(eventObj, params);
                }
            }
        }
    };
    return GameEventSystem;
}());
__reflect(GameEventSystem.prototype, "GameEventSystem");
//# sourceMappingURL=GameEventSystem.js.map