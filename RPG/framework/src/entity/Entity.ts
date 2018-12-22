class Entity extends egret.DisplayObjectContainer implements Componentable, AttributesInterface {
	//属性相关
	gameObjId: number
	/**名字 */
	name: string
	/**类型 */
	type: EntityType
	/**等级 */
	level: number
	/**外观类型 (静态外观 或 动态外观)*/
	bodyType: number
	/**外观 */
	bodyId: number
	/**x坐标 */
	x: number
	/**y坐标 */
	y: number
	/**朝向 */
	dir: number

	/**组件列表 */
	components: GameComponent[]

	public constructor() {
		super();
		this.gameObjId = generateId();
		this.components = [];
	}

	public getId(): number {
		return this.gameObjId;
	}

	/**添加组件 */
	public addComponent(comp: GameComponent) {
		this.components.push(comp);
	}
	/**移除组件 */
	public removeComponent(comp: GameComponent) {
		let compId = comp.getId()
		var compList = this.components
		var compLength = compList.length;
		for (var i = 0; i < compLength; i++) {
			if (compList[i].getId() == comp.getId()) {
				var rcomp = compList.splice(i, 1);
				rcomp[0].destructor();
				rcomp = null;
				break
			}
		}
	}
}