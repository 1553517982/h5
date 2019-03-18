var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
// TypeScript file
var Algo = (function () {
    function Algo() {
    }
    Algo.merge = function (array, from, midel, end) {
        var arrayLeft = [];
        var arrayRight = [];
        for (var i = from; i <= midel; i++) {
            arrayLeft.push(array[i]);
        }
        //arrayLeft.push(-1)
        for (var i = midel + 1; i <= end; i++) {
            arrayRight.push(array[i]);
        }
        //arrayRight.push(-1)
        var l = 0;
        var r = 0;
        for (var k = from; k <= end; k++) {
            if (l < arrayLeft.length && (arrayLeft[l] < arrayRight[r] || r == arrayRight.length)) {
                array[k] = arrayLeft[l];
                l++;
            }
            else if (r < arrayRight.length || l == arrayLeft.length) {
                array[k] = arrayRight[r];
                r++;
            }
        }
    };
    /**归并排序 */
    Algo.mergeSort = function (array, start, end) {
        if (start < end) {
            var middle = Math.floor((end + start) / 2);
            this.mergeSort(array, start, middle);
            this.mergeSort(array, middle + 1, end);
            this.merge(array, start, middle, end);
        }
    };
    return Algo;
}());
__reflect(Algo.prototype, "Algo");
//# sourceMappingURL=Algo.js.map