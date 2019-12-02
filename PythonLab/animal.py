class animal():
    def sound(self, say):
        print("it " + say)


class dog(animal):
    def barks(self, say):
        animal.sound(self, say)


def main():
    a = animal()
    a.sound("makes a sound.")

    a = dog()
    a.barks("barks.")


if (__name__ == "__main__"):
    main()
