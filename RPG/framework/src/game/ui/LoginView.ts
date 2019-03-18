class LoginView extends BaseUI {

	/**登录按钮 */
	private Btn_login: eui.Button

	/**绑定事件 */
	public bindAutoEvents() {
		this.Btn_login.addEventListener(egret.TouchEvent.TOUCH_BEGIN, this.onLogin, this)
	}

	private onLogin() {
		console.log("点击登录按钮")
	}
}