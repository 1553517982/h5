/**Manager管理类 */
class GlobalManager extends Manager {
	/**manager列表 */
	private mgrList: Manager[];
	private registList: any;
	private managerIndexMap: any;

	/**单例 */
	static $instance: GlobalManager;

	public constructor() {
		super()
		this.init();
	}

	/**初始化 */
	public init() {
		this.mgrList = []
		this.registList = {}
		this.managerIndexMap = {}

	}

	/**清理 */
	public finit() {

	}
	/**重置 */
	public reset() {

	}

	public static get instance(): GlobalManager {
		if (!this.$instance) {
			this.$instance = new GlobalManager();
		}
		return this.$instance
	}

	public regist(className: string, GameClass: any) {
		this.registList[className] = GameClass;
	}

	/**获取对应的管理类 */
	public getManager(managerName: string): any {
		let managerIndex = this.managerIndexMap[managerName]
		if (managerIndex != undefined) {
			return this.mgrList[managerIndex];
		} else {
			var className = this.registList[managerName]
			if (className) {
				var manager = new className()
				this.mgrList.push(manager)
				this.managerIndexMap[managerName] = (this.mgrList.length - 1);
				return manager
			} else {
				console.warn(managerName, "未注册到GlobalManager！");
			}
		}
	}

}