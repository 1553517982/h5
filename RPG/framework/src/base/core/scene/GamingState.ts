//游戏状态
class GamingState implements GameState {
	public onEnter() {
		console.log("进入游戏状态")
		let scene = GameWorld.instance.getScene(GameStateDef.Gaming)
		if (scene) {
			scene.onEnter()
		}
	}

	public onExit() {
		console.log("离开游戏状态")
		let scene = GameWorld.instance.getScene(GameStateDef.Gaming)
		if (scene) {
			scene.onExit()
		}
	}
}