var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
//游戏状态
var GamingState = (function () {
    function GamingState() {
    }
    GamingState.prototype.onEnter = function () {
        console.log("进入游戏状态");
        var scene = GameWorld.instance.getScene(GameStateDef.Gaming);
        if (scene) {
            scene.onEnter();
        }
    };
    GamingState.prototype.onExit = function () {
        console.log("离开游戏状态");
        var scene = GameWorld.instance.getScene(GameStateDef.Gaming);
        if (scene) {
            scene.onExit();
        }
    };
    return GamingState;
}());
__reflect(GamingState.prototype, "GamingState", ["GameState"]);
//# sourceMappingURL=GamingState.js.map