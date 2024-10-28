let points = [40, 100, 100, 1, 5, 25, 10];
points = points.map(( ind,i) => {
    console.log(ind,i)
    return [i, ind];
})
console.log(points);

points.sort(function (a, b) {
    console.log(a,b,(a[1] - b[1])>0);
    return Number((a[1] - b[1])>0);
});
console.log(points);
