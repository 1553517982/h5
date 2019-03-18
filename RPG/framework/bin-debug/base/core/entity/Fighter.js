/**
 * 可战斗实体的基类
 *
 */
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
var Fighter = (function (_super) {
    __extends(Fighter, _super);
    function Fighter() {
        return _super.call(this) || this;
    }
    /**移动
     * @todo
    */
    Fighter.prototype.move = function (x, y) {
        return false;
    };
    /**停止移动
     *  @todo
     */
    Fighter.prototype.movestop = function () {
        return false;
    };
    /**待机移动
     *  @todo
    */
    Fighter.prototype.idle = function () {
        return false;
    };
    /**攻击
     * @todo
     */
    Fighter.prototype.attack = function (targetHandle) {
    };
    /**受击
     * @todo
    */
    Fighter.prototype.underAttack = function (skillId, sourceHandle) {
    };
    return Fighter;
}(Character));
__reflect(Fighter.prototype, "Fighter", ["Fighteable"]);
//# sourceMappingURL=Fighter.js.map