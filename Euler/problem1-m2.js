function SumDiv(h, d) {
    var n = parseInt(h / d);
    return d * n * (n + 1) / 2;
}

console.log(SumDiv(999, 3) + SumDiv(999, 5) - SumDiv(999, 15));