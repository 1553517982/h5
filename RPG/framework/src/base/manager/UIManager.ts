/**
 * UI管理类
 */

class UIManager {
	//单例
	public static $instance: UIManager;

	public constructor() {
	}

	public static get instance(): UIManager {
		if (!this.$instance) {
			this.$instance = new UIManager();
		}
		return this.$instance
	}
	
	public showWindow(viewName: string, callback?) {

	}
}