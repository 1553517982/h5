class LoginController extends ViewController {
	/**服务器列表 */
	private serverList: any
	/**账号信息 */
	private accountInfo: any

	//绑定事件 全部写在这里
	public onCreate() {
		this.bindGameEvent(GameEvent.E_ACCOUNT_LOGIN, this.onLoginSuccess, this)
		this.bindGameEvent(GameEvent.E_ENTER_SERVER, this.onEnterServerSuccess, this)

	}

	/**点击登陆按钮 */
	public onLogin(account: string, password: string) {
		/**
		 * @todo 后台通信 获取游戏内帐号信息 
		 */
		LoginManager.instance.onLoginSuccess(account, password)
	}

	/**
	 * 进入服务器
	 */
	public onEnterServer(serverId: string) {

		// 1.连接服务器
		this.connectServer(serverId)
		// 2.登录游戏帐号
		// 3.处理服务器返回的角色信息


		LoginManager.instance.onEnterServerSuccess(serverId)
	}
	/**
	 * 连接服务器
	 * @param serverId 服务器id
	 */
	private connectServer(serverId: string) {
		
	}

	/**进入服务器成功 
	 * @param roleInfo  服务器角色信息  如果没有角色 需要走创角流程
	*/
	public onEnterServerSuccess(roleInfo: any) {
		//this.view.onEnterServerSuccess(serverId)
		//App.GSManager.setState(GameStateDef.Gaming)
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