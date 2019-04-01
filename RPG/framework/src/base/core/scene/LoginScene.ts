/**
 * 登录场景
 * 
 * 可以在这个场景添加一些特效
*/

class LoginScene extends Scene {
	public constructor() {
		super()
	}

	public onEnter() {
		super.onEnter()
		App.UIManager.showUI("LoginView")
	}


	public onExit() {
		super.onExit()
		App.UIManager.hideUI("LoginView")
	}
}