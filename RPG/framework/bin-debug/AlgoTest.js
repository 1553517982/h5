// TypeScript file
function merge(array, from, midel, end) {
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
}
function mergeSort(array, start, end) {
    if (start < end) {
        var middle = Math.floor((end + start) / 2);
        mergeSort(array, start, middle);
        mergeSort(array, middle + 1, end);
        merge(array, start, middle, end);
    }
}
//# sourceMappingURL=AlgoTest.js.map