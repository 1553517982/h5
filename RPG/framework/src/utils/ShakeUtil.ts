/**
 * 震动工具
 * @author  wh 2018-1-20
 * Example:
 * 震动目标obj，1秒内震动10次，震动最大距离10
 * ShakeUtil.getInstance().shakeObj(obj, 1, 10, 10);
 */

class ShakeUtil {
	/**
	 * 单例
	 */
	private static $instance: ShakeUtil;
	/**
	 * 初始位置 x
	 */
	private initX: number;
	/**
	 * 初始位置 y
	 */
	private initY: number;
	/**
	 * 震动目标
	 */
	private target: egret.DisplayObject;
	/**
	 * 震动距离
	 */
	private maxDis: number;
	/**
	 * 计时器次数
	 */
	private count: number = 0;
	/**
	 * 一秒震动次数
	 */
	private rate: number;
	/**
	 * 定时器
	 */
	private timer: egret.Timer = new egret.Timer(1000);

	public static get instance(): ShakeUtil {
		if (this.$instance == null) {
			this.$instance = new ShakeUtil();
		}
		return this.$instance;
	}

	public constructor() {

	}

    /**
     * 震动显示对象
     * @param target    震动目标对象
     * @param time      震动持续时长（秒）
     * @param rate      震动频率(一秒震动多少次)
     * @param maxDis    震动最大距离
     */
	public shakeObj(target: egret.DisplayObject, time: number, rate: number, maxDis: number): void {
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
	}

	/**
	 * 需要震动的对象做些动作
	 */
	private shaking(): void {
		egret.Tween.removeTweens(this.target);
		this.target.x = this.initX - this.maxDis + Math.random() * this.maxDis * 2;
		this.target.y = this.initY - this.maxDis + Math.random() * this.maxDis * 2;
		egret.Tween.get(this.target).to({ x: this.initX, y: this.initY }, 999 / this.rate);
	}

	/**
	 * 震屏结束后恢复原来的位置,移除事件
	 */
	private shakeComplete(): void {
		if (this.target) {
			egret.Tween.removeTweens(this.target);
			this.target.x = this.initX;
			this.target.y = this.initY;
		}
		this.timer.removeEventListener(egret.TimerEvent.TIMER, this.shaking, this);
		this.timer.removeEventListener(egret.TimerEvent.TIMER_COMPLETE, this.shakeComplete, this);
	}

	/**停止震动 */
	public stop() {
		this.shakeComplete();
	}

}
