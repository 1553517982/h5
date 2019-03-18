/**
 * UI基类
 * 
 */
class BaseUI extends eui.Component {
    /**游戏内事件监听列表 */
    private gameEventList: any;
    /**系统事件监听列表 */
    private sysEventList: any;
    /**界面名称 */
    private viewName: string

    public constructor(viewName: string) {
        super()
        this.gameEventList = {}
        this.sysEventList = {}
        this.viewName = viewName
        let viewConf = UIConfig[this.viewName]
        if (viewConf) {
            this.skinName = viewConf.skinName
        }
    }
    /**绑定事件 子类实现此函数 */
    public bindAutoEvents() {
    }

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
    public bindEvent(type: string, listener: Function, thisObject: any, useCapture?: boolean, priority?: number) {
        if (!this.sysEventList[type]) {
            this.sysEventList[type] = { type: type, listener: listener, thisObject: thisObject, useCapture: useCapture, priority: priority }
            this.addEventListener(type, listener, thisObject, useCapture, priority)
        }
    }

	/**
	 * 移除系统事件侦听
	 * @param type 事件的类型。
	 * @param listener 处理事件的侦听器函数。此函数必须接受 Event 对象作为其唯一的参数，并且不能返回任何结果，
	 * 如下面的示例所示： function(param:any):void 函数可以有任何名称。
	 * @param thisObject 侦听函数绑定的 this 对象。
	 */
    public unbindEvent(type: string) {
        if (this.sysEventList[type]) {
            var eventObj = this.sysEventList[type]
            this.removeEventListener(eventObj.type, eventObj.listener, eventObj.thisObject, eventObj.useCapture)
            delete this.sysEventList[type]
        }
    }
	/**
	* 添加游戏内事件侦听
	* @param type 事件的类型。
	 */
    public bindGameEvent(type: GameEvent, listener: Function, thisObject: any) {
        if (!this.gameEventList[type]) {
            var eventId = GameEventSystem.instance.add(type, listener, thisObject)
            this.gameEventList[type] = eventId
        }
    }
	/**
	* 移除游戏内事件侦听
	* @param type 事件的类型。
	 */
    public unbindGameEvent(type: GameEvent) {
        if (this.gameEventList[type]) {
            var eventId = this.gameEventList[type]
            GameEventSystem.instance.remove(eventId)
            delete this.gameEventList[type]
        }
    }

    /**暂停所有事件监听 */
    public pauseGameEvent() {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType]
            GameEventSystem.instance.pause(eventId)
        }
    }

    /**恢复所有事件监听 */
    public resumeGameEvent() {
        for (var eventType in this.gameEventList) {
            var eventId = this.gameEventList[eventType]
            GameEventSystem.instance.resume(eventId)
        }
    }

    public onShow() {
        this.bindAutoEvents()
        this.resumeGameEvent()
    }

    public onHide() {
        this.pauseGameEvent()
    }

    public close() {
        this.onHide()
    }

    public releaseEvents() {
        let events = Object.keys(this.gameEventList)
        for (var i = 0; i < events.length; i++) {
            var eventId = this.gameEventList[events[i]]
            GameEventSystem.instance.remove(eventId)
            delete this.gameEventList[events[i]]
        }
        
        this.gameEventList = {}
        this.sysEventList = {}
    }

    public destroy() {
        this.releaseEvents()
    }
}