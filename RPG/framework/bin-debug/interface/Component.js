var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
/**游戏组件对象基类 */
var GameComponent = (function () {
    function GameComponent() {
        this.compid = generateId();
    }
    GameComponent.prototype.getId = function () {
        return this.compid;
    };
    GameComponent.prototype.destructor = function () {
    };
    return GameComponent;
}());
__reflect(GameComponent.prototype, "GameComponent");
//# sourceMappingURL=Component.js.map