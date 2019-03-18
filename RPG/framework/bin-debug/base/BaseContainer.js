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
/**
 * 容器基类  为了方便移植  游戏内的所有容器控件必须统一继承BaseContainer
 */
var BaseContainer = (function (_super) {
    __extends(BaseContainer, _super);
    function BaseContainer() {
        return _super.call(this) || this;
    }
    return BaseContainer;
}(egret.DisplayObjectContainer));
__reflect(BaseContainer.prototype, "BaseContainer");
//# sourceMappingURL=BaseContainer.js.map