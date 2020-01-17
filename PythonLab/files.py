# write to file


def main():
    # f = open("textfile.txt", "w")

    # for i in range(10):
    #     f.write("this is line #" + str(i + 1) + "\n")

    # f.close()

    f = open("textfile.txt", "r")

    # contents = f.read()

    if f.mode == "r":
        fl = f.readlines()

        for l in fl:
            print(l)

    # print(contents)


main()
