class Character extends Entity implements Moveable {
	public constructor() {
		super()
	}
	
	/**移动 */
	public move(x: number, y: number): boolean {
		return false;
	}
	/**停止移动 */
	public movestop(): boolean {
		return false;
	}
	/**待机移动 */
	public idle(): boolean {
		return false;
	}
}