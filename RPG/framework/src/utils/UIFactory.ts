/*
定义常用文本样式 
*/
const LabelStyle = {
    ["PropName"]: { color: "0x958767", size: 20 }, //属性名称 浅黄色 字号20
    ["PropValue"]: { color: "0xf3dda7", size: 20 }, //属性值 黄色 字号20
    ["Level"]: { color: "0x05e40b", size: 20 }, //等级   绿色 字号20
    ["SubTitle"]: { color: "0xa88a43", size: 22 }, //子标题 金黄色 字号22
    ["PropNameBlue"]: { color: "0x00b4ff", size: 20 }, //强化属性名称 浅蓝色 字号20
    ["PropValueBlue"]: { color: "0x00b4ff", size: 20 }, //强化属性值 深蓝色 字号20
    ["PropYellow"]: { color: "0xf4e05b", size: 20 }, //金黄色文本 金黄色 字号20  
    ["Violet"]: { color: "0xa109eb", size: 20 },           //紫色文本 紫色 字号20 
    ["ShenqiValue"]: { color: "0xcbb37b", size: 20 },           //神器属性文本 紫色 字号20  
}

class UIFactory {
    /**
     * 创建文本
     */
    public static createLabel(str: string, styleName: string = "PropName") {
        //styleName = (styleName ==null) ? styleName:"PropName"
        var styleconfig = LabelStyle[styleName];
        let label = new eui.Label();
        label.textFlow = Utils.htmlTextParse(str);
        label.fontFamily = "SimHei";
        label.size = styleconfig.size;
        label.textColor = styleconfig.color;
        return label
    }

    /**
     * 创建key:value形式的控件
     */
    public static createKeyValueLabel(keyStr: string, valueStr: string, keyStyleName: string = "PropName", valueStyleName: string = "PropValue") {
        //keyStyleName = (keyStyleName ==null) ? keyStyleName:"PropName"
        //valueStyleName = (valueStyleName ==null) ? valueStyleName:"PropValue"
        var keyStyleconfig = LabelStyle[keyStyleName];
        var valueStyleconfig = LabelStyle[valueStyleName];

        let richText = new eui.Label();
        let levStr = Utils.formatString(GameConfig.getLanStr("ui0316"), keyStyleconfig.color, keyStyleconfig.size, keyStr, valueStyleconfig.color, valueStyleconfig.size, valueStr);
        richText.textFlow = Utils.htmlTextParse(levStr);
        richText.textAlign = 'left';
        richText.size = 22;
        richText.fontFamily = Game_Font_Family;
        return richText
    }

    /**
     * 设置文本颜色
     */
    public static setLabelStyle(label: eui.Label, styleName: string) {
        styleName = (styleName == null) ? styleName : "PropName"
        var styleconfig = LabelStyle[styleName];
        label.size = styleconfig.size;
        label.textColor = styleconfig.color;
    }
}