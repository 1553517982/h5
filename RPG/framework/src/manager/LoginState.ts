//登录状态
class LoginState implements GameState {
	public onEnter() {
		console.log("进入登录状态")
		UIManager.instance.showWindow("LoginView")
	}

	public onExit() {
		console.log("离开登录状态")
	}
}