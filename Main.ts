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

class Main extends eui.UILayer {


    protected createChildren(): void {
        super.createChildren();

        this.runGame().catch(e => {
            console.log(e);
        })
    }

    private currentArc: number = Math.PI / 2
    private eyeSight: number = Math.PI / 4
    private startX = 0
    private startY = 0
    private rand = 300

    private async runGame() {
        var stage = this.stage

        var boxs = [
            [[50, 50], [200, 50], [200, 200], [220, 220], [50, 200]],
            [[250, 50], [450, 50], [450, 100], [250, 100]],
            [[50, 300], [450, 300], [450, 250], [50, 250]],
        ]

        for (var k in boxs) {
            var box = new egret.Shape()
            box.graphics.beginFill(0x00ff00, 0.5)

            var prePos = null
            for (var idx in boxs[k]) {
                var pos = boxs[k][idx]
                if (Number(idx) == 0) {
                    box.graphics.moveTo(pos[0], pos[1])
                } else {
                    box.graphics.lineTo(pos[0], pos[1])
                    if (Number(idx) == boxs[k].length - 1) {
                        box.graphics.lineTo(boxs[k][0][0], boxs[k][0][1])
                    }
                }
            }
            box.graphics.endFill()
            box.x = this.startX
            box.y = this.startY
            stage.addChild(box)
        }

        var originPos = [this.startX, this.startY]
        var arg = new egret.Shape()
        arg.graphics.beginFill(0xffff00, 0.5)
        arg.graphics.moveTo(0, 0)
        arg.graphics.lineTo(0 + this.rand, 0 + 0);
        arg.graphics.drawArc(0, 0, this.rand, this.currentArc - this.eyeSight / 2, this.currentArc + this.eyeSight / 2)
        arg.graphics.lineTo(0, 0)
        arg.graphics.endFill()
        arg.x = 220
        arg.y = 50
        stage.addChild(arg)

        var filter = this.createEyeSightFilter(boxs)
        filter.uniforms.entityPos = { x: arg.x, y: arg.y }
        arg.filters = [filter]

        let tw = egret.Tween.get(arg, { loop: true })
        tw.to({ rotation: 360 }, 3000).to({ rotation: 0 }, 3000)
    }


    private createEyeSightFilter(boxs): egret.CustomFilter {


        let vertexSrc =
            "attribute vec2 aVertexPosition;\n" +
            "attribute vec2 aTextureCoord;\n" +
            "attribute vec2 aColor;\n" +

            "uniform vec2 projectionVector;\n" +
            "varying vec2 vPos;\n" +
            "varying vec2 vTextureCoord;\n" +
            "varying vec4 vColor;\n" +

            "const vec2 center = vec2(-1.0, 1.0);\n" +

            "void main(void) {\n" +
            "   gl_Position = vec4( (aVertexPosition / projectionVector) + center , 0.0, 1.0);\n" +
            "   vTextureCoord = aTextureCoord;\n" +
            "   vPos = vec2(gl_Position.xy);\n" +
            "   vColor = vec4(aColor.x, aColor.x, aColor.x, aColor.x);\n" +
            "}";

        let fragmentSrc4 = [
            "precision lowp float;",
            "varying vec2 vTextureCoord;",
            "varying vec2 vPos;",
            "varying vec4 vColor;",
            "uniform vec2 entityPos;",
            "uniform sampler2D uSampler;",
            "void main(void) {"
        ]
        var pointParts = []
        var width = this.stage.stageWidth / 2
        var height = this.stage.stageHeight / 2

        fragmentSrc4 = fragmentSrc4.concat([
            "    vec2 v2 = vec2(" + width + ", -" + height + "); ",
            "    vec2 c2 = vec2(-1.0, 1.0);",
            "    vec2 entityGlPos = entityPos / v2 + c2;",
            "    vec2 nextPos;"]);

        for (var boxid in boxs) {
            var box = boxs[boxid]
            var len = box.length
            pointParts.push("vec2 points" + boxid + "[" + len + "];")
            for (var k in box) {
                pointParts.push("points" + boxid + "[" + k + "]=vec2(" + (box[k][0] / width - 1) + "," + (-box[k][1] / height + 1) + ");")
            }
            pointParts = pointParts.concat([
                "for(int k=0;k<" + len + ";k++){",
                "   if(k==" + (len - 1) + "){",
                "       nextPos = points" + boxid + "[0];",
                "   }else{",
                "       nextPos = points" + boxid + "[k+1];",
                "   }",
                "   vec2 pos = points" + boxid + "[k];",
                "   if(min(vPos.x,entityGlPos.x)>=max(pos.x,nextPos.x) || max(vPos.x,entityGlPos.x)<=min(pos.x,nextPos.x) ",
                "    || min(vPos.y,entityGlPos.y)>=max(pos.y,nextPos.y) || max(vPos.y,entityGlPos.y)<=min(pos.y,nextPos.y)){",
                "       continue ;",
                "   }else{",
                "       float denom = (vPos.x - entityGlPos.x) * (nextPos.y - pos.y) - (nextPos.x - pos.x) * (vPos.y - entityGlPos.y);",
                "       bool denomPositive = (denom > 0.0);",
                "       if (denom == 0.0)",
                "            continue;",
                "       float s_numer = (vPos.x - entityGlPos.x) * (entityGlPos.y - pos.y) - (vPos.y - entityGlPos.y) * (entityGlPos.x - pos.x);",
                "       if ((s_numer < 0.0) == denomPositive)",
                "           continue ; ",
                "       float t_numer = (nextPos.x - pos.x) * (entityGlPos.y - pos.y) - (nextPos.y - pos.y) * (entityGlPos.x - pos.x);",
                "       if ((t_numer < 0.0) == denomPositive)",
                "           continue ;",
                "       if (abs(s_numer) > abs(denom) || abs(t_numer) > abs(denom))",
                "           continue ;",
                "       gl_FragColor = vec4(0, 0,0, 0);",
                "       return;",
                "   }",
                "}",
            ])
        }
        fragmentSrc4 = fragmentSrc4.concat(pointParts)
        var fragStr = fragmentSrc4.concat([
            "gl_FragColor = texture2D(uSampler, vTextureCoord);",
            "}"]).join("\n")
        console.log(fragStr)
        return new egret.CustomFilter(
            vertexSrc,
            fragStr
        );
    }
}
