// TypeScript file
let a = [66, 5, 2, 3, 6, 4, 8, 7, 9, 10, 22, 35]

function merge(array, from, midel, end) {
    let arrayLeft = []
    let arrayRight = []
    for (var i = from; i <= midel; i++) {
        arrayLeft.push(array[i])
    }
    arrayLeft.push(-1)
    for (var i = midel + 1; i <= end; i++) {
        arrayRight.push(array[i])
    }
    arrayRight.push(-1)
    let l = 0;
    let r = 0;
    for (var k = from; k <= end; k++) {
        if (arrayLeft[l] > arrayRight[r]) {
            array[k] = arrayLeft[l]
            l++
        } else {
            array[k] = arrayRight[r]
            r++
        }
    }
}

function mergeSort(array, start, end) {
    if (start < end) {
        let middle = Math.floor((end + start) / 2)
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)
    }
}
mergeSort(a, 0, a.length - 1)
console.log(a)