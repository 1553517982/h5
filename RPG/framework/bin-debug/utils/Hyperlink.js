var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
/**
 * 超链接处理类
 * @author aXing on 2018-3-27
 */
var Hyperlink = (function () {
    function Hyperlink() {
    }
    Object.defineProperty(Hyperlink, "instance", {
        get: function () {
            if (this.$instance == null) {
                this.$instance = new Hyperlink();
            }
            return this.$instance;
        },
        enumerable: true,
        configurable: true
    });
    /**
     * 解析超链接字符串
     * <br>@前面的是命令id HyperlinkType
     * <br>后面的参数用逗号分割
     * @param content 超链接字符串
     */
    Hyperlink.prototype.parse = function (content) {
        //var temp = content.split(":");
        var temp = content.split("|");
    };
    return Hyperlink;
}());
__reflect(Hyperlink.prototype, "Hyperlink");
//# sourceMappingURL=Hyperlink.js.map