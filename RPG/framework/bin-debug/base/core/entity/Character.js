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
var Character = (function (_super) {
    __extends(Character, _super);
    function Character() {
        return _super.call(this) || this;
    }
    /**移动 */
    Character.prototype.move = function (x, y) {
        return false;
    };
    /**停止移动 */
    Character.prototype.movestop = function () {
        return false;
    };
    /**待机移动 */
    Character.prototype.idle = function () {
        return false;
    };
    return Character;
}(Entity));
__reflect(Character.prototype, "Character", ["Moveable"]);
