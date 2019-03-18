/**基础属性 */
interface AttributesInterface {
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
}
