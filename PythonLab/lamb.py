def add(a, b, c): return a + b - c


def divide(a, b): return a/b


print(add(1, 5, 2))

# lambda to print your name

print('Hi Ji0lani' == (lambda name: 'Hi ' + name)('Jilani'))


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

for person in people:
    print(person.split())


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


print(map(split_title_and_name, people))
