//////////////////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2014-present, Egret Technology.
//  All rights reserved.
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//     * Neither the name of the Egret nor the
//       names of its contributors may be used to endorse or promote products
//       derived from this software without specific prior written permission.
//
//  THIS SOFTWARE IS PROVIDED BY EGRET AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
//  OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
//  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
//  IN NO EVENT SHALL EGRET AND CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
//  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
//  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;LOSS OF USE, DATA,
//  OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
//  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////////////////

class Main extends egret.DisplayObjectContainer {

    private loadResJsonFail: boolean;

    private loadThemeJsonFail: boolean;

    public constructor() {
        super();

        this.loadResJsonFail = true;
        this.loadThemeJsonFail = true;
        egret.ImageLoader.crossOrigin = "anonymous";
        this.addEventListener(egret.Event.ADDED_TO_STAGE, this.onAddToStage, this);
    }

    private onAddToStage(event: egret.Event) {
        egret.lifecycle.addLifecycleListener((context) => {
            // custom lifecycle plugin
            context.onUpdate = () => {
            }
        })

        this.runGame().catch(e => {
            console.log(e);
        })
    }

    private async runGame() {
        await this.loadResource()
    }

    private async loadGameResource(entry: any) {
        let self = this;
        if (self.loadResJsonFail) {
            self.loadResJsonFail = false;
            await RES.loadConfig(entry.configName, entry.configUrl).catch(e => {
                //入口文件加载失败 重试
                console.log("资源配置表加载失败")
                self.loadResJsonFail = true;
            })
        }
        if (self.loadResJsonFail) {
            await self.loadGameResource(entry)
            return
        }

        if (self.loadThemeJsonFail) {
            self.loadThemeJsonFail = false;
            await self.loadTheme().catch(e => {
                self.loadThemeJsonFail = true;
                console.log("皮肤表加载失败")
            })
        }
        if (self.loadThemeJsonFail) {
            await self.loadGameResource(entry)
            return
        }
        self.startGame(self)
    }

    private async loadResource() {
        try {
            //inject the custom material parser
            //注入自定义的素材解析器
            let assetAdapter = new AssetAdapter();
            egret.registerImplementation("eui.IAssetAdapter", assetAdapter);
            egret.registerImplementation("eui.IThemeAdapter", new ThemeAdapter());
            //Web模式下加载本地资源
            this.loadGameResource({
                configName: "resource/default.res.json",
                configUrl: "resource/"
            })
        }
        catch (e) {
            console.error(e);
        }
    }

    private loadTheme() {
        return new Promise((resolve, reject) => {
            // load skin theme configuration file, you can manually modify the file. And replace the default skin.
            //加载皮肤主题配置文件,可以手动修改这个文件。替换默认皮肤。
            let theme = new eui.Theme("resource/default.thm.json", this.stage);
            theme.addEventListener(eui.UIEvent.COMPLETE, () => {
                resolve();
            }, this);

        })
    }

    /**
     * 游戏开始
     */
    private startGame(main: Main): void {
        GameWorld.instance.start(this.stage)
    }
}
