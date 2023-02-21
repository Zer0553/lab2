# Натуральные числа, начинающиеся с нечетной цифры и содержащие не более 2 четных цифр.
# Для каждого числа через тире вывести прописью первую цифру и четные цифры.
import re

work_buffer = ''
numbers = []


def words(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)


with open('test.txt', 'r') as f:
    b = f.readlines()
    a = []
    for i in b:
        for j in i.split():
            a.append(j)
    if not a:
        print('Файл пуст, пожалуйста выберите другой файл')
        quit()
    else:
        for i in a:
            r = re.fullmatch(r'[13579]\B[13579]*\B[24680]?\B[13579]*\B[24680]?([13579]*)|(\B[24680]?)', i)
            if r:
                numbers.append(i)
        if not numbers:
            print('Нет подходящих чисел')
            quit()
        else:
            for i in numbers:
                even = 0
                p = i + ' ' + words(int(i[0]))
                answer = []
                for j in i:
                    if int(j) % 2 == 0:
                        even += 1
                        if words(int(j)) not in answer:
                            answer.append(words(int(j)))
                if even != 0:
                    p += ' -'
                print(p, *answer)
