var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
/*
定义常用文本样式
*/
var LabelStyle = (_a = {},
    _a["PropName"] = { color: "0x958767", size: 20 },
    _a["PropValue"] = { color: "0xf3dda7", size: 20 },
    _a["Level"] = { color: "0x05e40b", size: 20 },
    _a["SubTitle"] = { color: "0xa88a43", size: 22 },
    _a["PropNameBlue"] = { color: "0x00b4ff", size: 20 },
    _a["PropValueBlue"] = { color: "0x00b4ff", size: 20 },
    _a["PropYellow"] = { color: "0xf4e05b", size: 20 },
    _a["Violet"] = { color: "0xa109eb", size: 20 },
    _a["ShenqiValue"] = { color: "0xcbb37b", size: 20 },
    _a);
var UIFactory = (function () {
    function UIFactory() {
    }
    /**
     * 创建文本
     */
    UIFactory.createLabel = function (str, styleName) {
        if (styleName === void 0) { styleName = "PropName"; }
        //styleName = (styleName ==null) ? styleName:"PropName"
        var styleconfig = LabelStyle[styleName];
        var label = new eui.Label();
        label.textFlow = Utils.htmlTextParse(str);
        label.fontFamily = "SimHei";
        label.size = styleconfig.size;
        label.textColor = styleconfig.color;
        return label;
    };
    /**
     * 创建key:value形式的控件
     */
    UIFactory.createKeyValueLabel = function (keyStr, valueStr, keyStyleName, valueStyleName) {
        if (keyStyleName === void 0) { keyStyleName = "PropName"; }
        if (valueStyleName === void 0) { valueStyleName = "PropValue"; }
        //keyStyleName = (keyStyleName ==null) ? keyStyleName:"PropName"
        //valueStyleName = (valueStyleName ==null) ? valueStyleName:"PropValue"
        var keyStyleconfig = LabelStyle[keyStyleName];
        var valueStyleconfig = LabelStyle[valueStyleName];
        var richText = new eui.Label();
        var levStr = Utils.formatString(GameConfig.getLanStr("ui0316"), keyStyleconfig.color, keyStyleconfig.size, keyStr, valueStyleconfig.color, valueStyleconfig.size, valueStr);
        richText.textFlow = Utils.htmlTextParse(levStr);
        richText.textAlign = 'left';
        richText.size = 22;
        richText.fontFamily = Game_Font_Family;
        return richText;
    };
    /**
     * 设置文本颜色
     */
    UIFactory.setLabelStyle = function (label, styleName) {
        styleName = (styleName == null) ? styleName : "PropName";
        var styleconfig = LabelStyle[styleName];
        label.size = styleconfig.size;
        label.textColor = styleconfig.color;
    };
    return UIFactory;
}());
__reflect(UIFactory.prototype, "UIFactory");
var _a;
//# sourceMappingURL=UIFactory.js.map