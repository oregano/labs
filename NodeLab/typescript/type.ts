interface Person {
    firstName: string;
    lastName: string;
    age: number;
}

let person = { firstName: "Kaifee", lastName: "Mohammad" }

class Animal {
    animalType: string;

    constructor(type: string) {
        this.animalType = type;
    }

    speak() {
        return "I am an " + this.animalType;
    }
}

class Dog extends Animal {
    bark() {
        return "Yes, I am a dog";
    }
}

console.log(person);

let dog = new Dog("dog");

console.log(dog.speak());

console.log(dog.bark());