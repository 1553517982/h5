/**
 * 界面controller基类
 */
class ViewController {
	/**游戏内事件监听列表 */
	private gameEventList: any;
	/**界面实例 */
	private viewInstance: any

	public constructor(view) {
		this.viewInstance = view
		this.gameEventList = {}
	}

	/**返回view的实例 */
	public get view(): any {
		return this.viewInstance
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

	/**界面打开时 */
	public onShow() {
		this.resumeGameEvent()
	}
	/**界面关闭时 */
	public onHide() {
		this.pauseGameEvent()
	}
	public close() {
		this.onHide()
	}
	/**界面销毁时 */
	public destroy() {
		this.releaseGameEvents()
	}
	/**界面初始化成功 */
	public onCreate() {
		//绑定事件 全部写在这里
	}

	/**移除事件监听 */
	public releaseGameEvents() {
		let events = Object.keys(this.gameEventList)
		for (var i = 0; i < events.length; i++) {
			var eventId = this.gameEventList[events[i]]
			GameEventSystem.instance.remove(eventId)
			delete this.gameEventList[events[i]]
		}
		this.gameEventList = {}
	}
}