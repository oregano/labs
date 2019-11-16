var x = 1000;

var total = 0;

for (i = 1; i < x; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
        total += i;
    }
}

console.log('total is ' + total.toString());
