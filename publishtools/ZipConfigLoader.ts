// TypeScript file
enum BinaryDateType{
    Dict=1,
    Array=2,
    String=3,
    Int=4,
    Float=5,
    Long=6,
    JsonKey=80
}

class ZipConfigLoader {
    private static config:any = {};
    private static decodeProto(byteArray:egret.ByteArray){
            var ret
            var type = byteArray.readByte()
            switch(type){
                case BinaryDateType.Dict:
                    ret = {}
                    ZipConfigLoader.decodeByteArray(byteArray,ret,type)
                    break
                case BinaryDateType.Array:
                    ret = []
                    ZipConfigLoader.decodeByteArray(byteArray,ret,type)
                    break
                case BinaryDateType.Float:
                    ret = byteArray.readDouble()
                    break
                case BinaryDateType.Int:
                    ret = byteArray.readInt()
                    break
                case BinaryDateType.Long:
                    ret = byteArray.readDouble()
                    break
                case BinaryDateType.String:
                    var len = byteArray.readInt()
                    ret = byteArray.readUTFBytes(len)
                    break
            }
            return ret
    }
    
    private static decodeByteArray(byteArray:egret.ByteArray,dic:any,type){
        switch(type){ 
            case BinaryDateType.Array:
                var size = byteArray.readInt()
                for(var i = 0;i<size;i++){
                    dic.push(ZipConfigLoader.decodeProto(byteArray))
                }
                break
            case BinaryDateType.Dict:
                var size = byteArray.readInt()
                for(var i = 0;i<size;i++){
                    var keyName = ZipConfigLoader.decodeProto(byteArray)
                    dic[keyName] = ZipConfigLoader.decodeProto(byteArray)
                }
                break
        }
    }

    public static init(){
            RES.getResByUrl("resource/assets/data.json", function(buffer:any){
                var byteArray = new egret.ByteArray(buffer)
                var fileCount = byteArray.readInt()
                for(var i = 0;i<fileCount;i++){
                    var length = byteArray.readInt()
                    var key = byteArray.readUTFBytes(length)
                    var contentLength = byteArray.readInt()
                    var fileContens = new egret.ByteArray()
                    byteArray.readBytes(fileContens,0,contentLength)
                    fileContens.position = 0

                    ZipConfigLoader.config[key] = ZipConfigLoader.decodeProto(fileContens)
                }
            }, this, RES.ResourceItem.TYPE_BIN);

    }

    /**加载压缩包内的资源文件 */
    public static getZipFile(url: string){
        return ZipConfigLoader.config[url] 
    }

    public static getConfigPath(url:string) {
        if(window.WGameResourceHost){
            return window.WGameResourceHost + url
        }else{
            return url
        }
    }
}
    