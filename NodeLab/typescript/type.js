var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var person = { firstName: "Kaifee", lastName: "Mohammad" };
var Animal = /** @class */ (function () {
    function Animal(type) {
        this.animalType = type;
    }
    Animal.prototype.speak = function () {
        return "I am an " + this.animalType;
    };
    return Animal;
}());
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Dog.prototype.bark = function () {
        return "Yes, I am a dog";
    };
    return Dog;
}(Animal));
console.log(person);
var dog = new Dog("dog");
console.log(dog.speak());
console.log(dog.bark());
