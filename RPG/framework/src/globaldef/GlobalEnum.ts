/**事件id生成器 */
var generateID: number = 0

function generateId(): number {
	generateID = generateID + 1;
	return generateID
}


/**全局枚举定义 */




/**游戏内事件 */
enum GameEvent {
	default, //
	E_ACCOUNT_LOGIN,//帐号登录成功
	E_ENTER_SERVER,//进入服务器成功

}


/**实体类型定义 */
enum EntityType {
	defaul
}