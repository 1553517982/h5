//场景枚举
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = this && this.__extends || function __extends(t, e) { 
 function r() { 
 this.constructor = t;
}
for (var i in e) e.hasOwnProperty(i) && (t[i] = e[i]);
r.prototype = e.prototype, t.prototype = new r();
};
/**场景基类 */
var Scene = (function (_super) {
    __extends(Scene, _super);
    function Scene() {
        return _super.call(this) || this;
    }
    Scene.prototype.onEnter = function () {
    };
    Scene.prototype.onExit = function () {
    };
    return Scene;
}(egret.DisplayObjectContainer));
__reflect(Scene.prototype, "Scene");
//# sourceMappingURL=Scene.js.map