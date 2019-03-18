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
var Entity = (function (_super) {
    __extends(Entity, _super);
    function Entity() {
        var _this = _super.call(this) || this;
        _this.gameObjId = generateId();
        _this.components = [];
        return _this;
    }
    Entity.prototype.getId = function () {
        return this.gameObjId;
    };
    /**添加组件 */
    Entity.prototype.addComponent = function (comp) {
        this.components.push(comp);
    };
    /**移除组件 */
    Entity.prototype.removeComponent = function (comp) {
        var compId = comp.getId();
        var compList = this.components;
        var compLength = compList.length;
        for (var i = 0; i < compLength; i++) {
            if (compList[i].getId() == comp.getId()) {
                var rcomp = compList.splice(i, 1);
                rcomp[0].destructor();
                rcomp = null;
                break;
            }
        }
    };
    return Entity;
}(BaseContainer));
__reflect(Entity.prototype, "Entity", ["Componentable", "AttributesInterface"]);
//# sourceMappingURL=Entity.js.map