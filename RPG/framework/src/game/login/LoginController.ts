class LoginController extends ViewController {
	/**服务器列表 */
	private serverList: any
	/**账号信息 */
	private accountInfo: any

	//绑定事件 全部写在这里
	public onCreate() {
		this.bindGameEvent(GameEvent.E_ACCOUNT_LOGIN, this.onLoginSuccess, this)
	}

	/**点击登陆按钮 */
	public onLogin(account: string, password: string) {
		/**
		 * @todo 后台通信 获取游戏内帐号信息 
		 */
		LoginManager.instance.onLoginSuccess(account, password)
	}

	/**处理登陆回调 */
	private onLoginSuccess(response: any) {
		this.accountInfo = {}
		this.accountInfo.account = response.account
		this.accountInfo.password = response.password
		this.accountInfo.lastServerId = response.lastServerId
		this.setServerList(response.serverlist)
		this.view.onLoginSuccess(response)
	}

	/**设置服务器列表 */
	private setServerList(list) {
		this.serverList = list
	}
}