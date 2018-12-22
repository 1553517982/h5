/**行为动作接口 */
interface Moveable {
	/**移动 */
	move(x: number, y: number): boolean;
	/**停止移动 */
	movestop(): boolean
	/** 待机*/
	idle(): boolean
}


interface Fighteable {
	/**攻击 */
	attack(targetHandle: number)
	/**受击 */
	underAttack(skillId: number, targetHandle: number)
}