class ReportManager {
	/**打点地址 */
	private static BIUrl: string
	/**资源地址 */
	private static ResourceUrl: string
	/**配置更新地址 */
	private static ConfigUrl: string
	/**公告列表 */

	public static async sendHttpRequest(url: string, params, callback?, errCallback?, progressCallback?) {
		var request = new Promise(function (resolve, reject) {
			var request = new egret.HttpRequest();
			request.responseType = egret.HttpResponseType.TEXT;
			var body = params ? Utils.makesign(params) : ""
			var postBody = params ? Utils.makeBody(params) : ""
			console.log("url:", url + body)
			request.open(url + body, egret.HttpMethod.POST);
			request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
			request.send(postBody);

			function onGetComplete(event: egret.Event) {
				var request = <egret.HttpRequest>event.currentTarget
				var response = JSON.parse(request.response)
				if (response.errcode == 0) {
					resolve(response)
				} else {
					reject(response.errmsg)
				}
			}

			function onGetIOError(event: egret.IOErrorEvent) {
				reject(event)
			}

			function onGetProgress(event: egret.ProgressEvent) {
				var progress = Math.floor(100 * event.bytesLoaded / event.bytesTotal)
				if (progressCallback) {
					progressCallback(progress)
				}
			}

			request.addEventListener(egret.Event.COMPLETE, onGetComplete, this);
			request.addEventListener(egret.IOErrorEvent.IO_ERROR, onGetIOError, this);
			request.addEventListener(egret.ProgressEvent.PROGRESS, onGetProgress, this);
		}).then(function (result) {
			console.log("get data : ", result)
			if (callback) {
				callback(result)
			}
		}).catch(function (error) {
			console.log("error : ", error)
			if (errCallback) {
				errCallback(error)
			}
		})
		return request
	};
}
