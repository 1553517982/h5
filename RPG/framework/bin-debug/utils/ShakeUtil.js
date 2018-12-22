/**
 * 震动工具
 * @author  wh 2018-1-20
 * Example:
 * 震动目标obj，1秒内震动10次，震动最大距离10
 * ShakeUtil.getInstance().shakeObj(obj, 1, 10, 10);
 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var ShakeUtil = (function () {
    function ShakeUtil() {
        /**
         * 计时器次数
         */
        this.count = 0;
        /**
         * 定时器
         */
        this.timer = new egret.Timer(1000);
    }
    Object.defineProperty(ShakeUtil, "instance", {
        get: function () {
            if (this.$instance == null) {
                this.$instance = new ShakeUtil();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * 震动显示对象
     * @param target    震动目标对象
     * @param time      震动持续时长（秒）
     * @param rate      震动频率(一秒震动多少次)
     * @param maxDis    震动最大距离
     */
    ShakeUtil.prototype.shakeObj = function (target, time, rate, maxDis) {
        this.target = target;
        this.initX = target.x;
        this.initY = target.y;
        this.maxDis = maxDis;
        this.count = time * rate;
        this.rate = rate;
        this.timer.delay = 1000 / rate;
        this.timer.repeatCount = this.count;
        this.timer.addEventListener(egret.TimerEvent.TIMER, this.shaking, this);
        this.timer.addEventListener(egret.TimerEvent.TIMER_COMPLETE, this.shakeComplete, this);
        this.timer.reset();
        this.timer.start();
    };
    /**
     * 需要震动的对象做些动作
     */
    ShakeUtil.prototype.shaking = function () {
        egret.Tween.removeTweens(this.target);
        this.target.x = this.initX - this.maxDis + Math.random() * this.maxDis * 2;
        this.target.y = this.initY - this.maxDis + Math.random() * this.maxDis * 2;
        egret.Tween.get(this.target).to({ x: this.initX, y: this.initY }, 999 / this.rate);
    };
    /**
     * 震屏结束后恢复原来的位置,移除事件
     */
    ShakeUtil.prototype.shakeComplete = function () {
        if (this.target) {
            egret.Tween.removeTweens(this.target);
            this.target.x = this.initX;
            this.target.y = this.initY;
        }
        this.timer.removeEventListener(egret.TimerEvent.TIMER, this.shaking, this);
        this.timer.removeEventListener(egret.TimerEvent.TIMER_COMPLETE, this.shakeComplete, this);
    };
    /**停止震动 */
    ShakeUtil.prototype.stop = function () {
        this.shakeComplete();
    };
    return ShakeUtil;
}());
__reflect(ShakeUtil.prototype, "ShakeUtil");
//# sourceMappingURL=ShakeUtil.js.map