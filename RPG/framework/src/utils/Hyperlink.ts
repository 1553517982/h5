/**
 * 超链接处理类
 * @author aXing on 2018-3-27
 */
class Hyperlink {

    private static $instance: Hyperlink;

    public static get instance(): Hyperlink {
        if (this.$instance == null) {
            this.$instance = new Hyperlink();
        }
        return this.$instance;
    }

    public constructor() {
    }

	/**
	 * 解析超链接字符串
     * <br>@前面的是命令id HyperlinkType
     * <br>后面的参数用逗号分割
	 * @param content 超链接字符串
	 */
    public parse(content: string): void {
        //var temp = content.split(":");
        var temp = content.split("|");
    }
}