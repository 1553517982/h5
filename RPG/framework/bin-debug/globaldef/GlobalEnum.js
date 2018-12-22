/**事件id生成器 */
var generateID = 0;
function generateId() {
    generateID = generateID + 1;
    return generateID;
}
/**全局枚举定义 */
/**游戏内事件 */
var GameEvent;
(function (GameEvent) {
    GameEvent[GameEvent["default"] = 0] = "default"; //
})(GameEvent || (GameEvent = {}));
/**实体类型定义 */
var EntityType;
(function (EntityType) {
    EntityType[EntityType["defaul"] = 0] = "defaul";
})(EntityType || (EntityType = {}));
//# sourceMappingURL=GlobalEnum.js.map