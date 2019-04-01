class LoginManager extends Manager {
	private static $instance: LoginManager
	public static get instance(): LoginManager {
		if (!this.$instance) {
			this.$instance = new LoginManager()
		}
		return this.$instance
	}

	public onLoginSuccess(account: string, password: string) {
		var response = {
			account: account,
			password: password,
			lastServerId: "1",
			recommandServerId: "1",
			createTime: "1554121810",
			serverlist: {
				"1": {
					ip: "192.168.1.131",
					port: "6001",
					state: "good",
					name: "测试服"
				}
			}
		}
		GameEventSystem.instance.dispatch(GameEvent.E_ACCOUNT_LOGIN, response)
	}
}