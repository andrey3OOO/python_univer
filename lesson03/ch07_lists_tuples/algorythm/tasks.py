def task01():
    names = ['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
    print(names)


def task02():
    names = ['Эйнштейн', 'Ньютон', 'Коперник', 'Кеплер']
    for name in names:
        print(name)


def task03():
    numbers1 = []
    for i in range(100):
        numbers1.append(i)
    print(numbers1)
    numbers2 = [] + numbers1
    print(numbers2)


def task05(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def task06():
    names = ['Ruby', 'Ivan', 'Serg']

    for name in names:
        if name == 'Ruby':
            message = 'Hi, Ruby'
            break
        else:
            message = 'Ruby is missing'

    print(message)


def task07():
    list1 = [40, 50, 60]
    list2 = [10, 20, 30]
    list3 = list1 + list2
    print(list3)


def task08():
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for r in range(5):
        for c in range(3):
            print("Enter number for ", [r], [c])
            matrix[r][c] = int(input())

    print(matrix)


if __name__ == "__main__":
    task08()