/**
 * 可战斗实体的基类
 * 
 */

class Fighter extends Character implements Fighteable {
	/**目标 */
	targetHanle: Character

	public constructor() {
		super()
	}

	/**移动 
	 * @todo 
	*/
	public move(x: number, y: number): boolean {
		return false;
	}
	/**停止移动
	 *  @todo 
	 */
	public movestop(): boolean {
		return false;
	}
	/**待机移动 
	 *  @todo 
	*/
	public idle(): boolean {
		return false;
	}
	/**攻击
	 * @todo 
	 */
	public attack(targetHandle: number) {

	}
	/**受击 
	 * @todo
	*/
	public underAttack(skillId: number, targetHandle: number) {

	}

}