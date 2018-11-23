/**游戏事件通知管理中心 */
class GameEventObject {
	/**事件对象唯一id */
	id: number
	/**事件id */
	eventId: GameEvent
	/**回调函数 */
	callback: Function
	/**归属者 */
	owner: any
	/**是否休眠 */
	isSleep: boolean

	public constructor(id, eventId, callback, owner) {
		this.id = id
		this.eventId = eventId;
		this.callback = callback;
		this.isSleep = false;
		this.owner = owner;
	}

	public trigger(param?: any) {
		this.callback.call(this.owner, param);
	}

	public pause() {
		this.isSleep = true;
	}

	public resume() {
		this.isSleep = false;
	}
	/**是否可触发 */
	public canTriiger() {
		return !this.isSleep
	}
}

class GameEventSystem {
	/**事件监听列表 */
	private $eventHandles: any;
	/**事件对象列表 */
	private $eventObjList: any;
	/**事件下标索引列表 */
	private $eventIndexList: any;
	/**事件id生成器 */
	static generateID: number = 0;

	public constructor() {
		this.$eventHandles = {}
		this.$eventIndexList = {}
		this.$eventObjList = {}
	}

	/**创建事件对象 */
	private createEventObj(eventId, handle, thisObj): GameEventObject {
		GameEventSystem.generateID = GameEventSystem.generateID + 1;
		return new GameEventObject(GameEventSystem.generateID, eventId, handle, thisObj);
	}

	private static $instance: GameEventSystem;

	public static get instance(): GameEventSystem {
		if (this.$instance == null) {
			this.$instance = new GameEventSystem();
		}
		return this.$instance;
	}

	/**添加事件监听 */
	public add(eventId: GameEvent, handle: Function, thisObj?: any) {
		var eventObj = this.createEventObj(eventId, handle, thisObj)
		if (!this.$eventHandles[eventId]) {
			this.$eventHandles[eventId] = [];
		}
		this.$eventObjList[eventObj.id] = eventObj;
		this.$eventHandles[eventId].push(eventObj.id);
		this.$eventIndexList[eventObj.id] = (this.$eventHandles[eventId].length - 1);
	}

	/**移除事件监听 */
	public remove(eventObjID: number) {
		var eventObj: GameEventObject = this.$eventObjList[eventObjID];
		if (eventObj) {
			var eventId = eventObj.eventId;
			var eventIndex = this.$eventIndexList[eventObjID]
			if (this.$eventHandles[eventId]) {
				//这里将id置0即可  不需要移除 否则下标会缩进导致下标列表有问题
				this.$eventHandles[eventId][eventIndex] = 0;
			}
			delete this.$eventIndexList[eventObjID]
			delete this.$eventObjList[eventObjID]
		}
	}

	/**暂停事件监听 */
	public pause(eventObjID: number) {

	}

	/**恢复事件监听 */
	public resume(eventObjID: number) {

	}

	/**恢复指定事件监听 */
	public resumeEvent(eventId: GameEvent) {
		var objArray = this.$eventHandles[eventId];
		if (objArray && objArray.length > 0) {
			var i: number
			var eventObj: GameEventObject;
			for (i = 0; i < objArray.length; i++) {
				eventObj = objArray[i];
				eventObj.pause();
			}
		}
	}

	/**暂停指定事件 */
	public pauseEvent(eventId: GameEvent) {
		var objArray = this.$eventHandles[eventId];
		if (objArray && objArray.length > 0) {
			var i: number
			var eventObj: GameEventObject;
			for (i = 0; i < objArray.length; i++) {
				eventObj = objArray[i];
				eventObj.pause();
			}
		}
	}

	/**暂停所有事件 */
	public pauseAll() {
		var objList = this.$eventObjList;
		var eventId;
		var eventObj: GameEventObject;
		for (eventId in objList) {
			eventObj = objList[eventId];
			eventObj.pause();
		}
	}

	/**派发事件 */
	public dispatch(eventId: GameEvent, params: any) {

	}
}