class LoginView extends BaseUI {
	/**登录按钮 */
	private Btn_login: eui.Button
	/**帐号控件 */
	private editext_account: eui.EditableText
	/**帐号控件 */
	private editext_password: eui.EditableText

	protected controller: LoginController
	public onCreate() {
		this.controller = new LoginController(this)
		this.Btn_login.addEventListener(egret.TouchEvent.TOUCH_BEGIN, this.onLogin, this)
		super.onCreate()
	}

	/**点击登录按钮 */
	private onLogin() {
		var account = this.editext_account.text
		var password = this.editext_password.text
		this.controller.onLogin(account, password)
	}
	/**登录成功回调 */
	public onLoginSuccess(response) {
		console.log(response)
		this.close()
	}
}