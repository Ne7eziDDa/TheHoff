def check_pallindrom():
    print(f'Введите слово: ')
    w = str(input())

    i = 0
    j = -1
    try:
        while w[i] == w[j]:
            i += 1
            j -= 1
            if (j == (len(w) - 2 * len(w)) and (i == len(w) - 1)):
                print(f'{w} is a palindrom!')
    except IndexError:
        m = 1 # переменная для заполнения пустоты обработки ошибки.
    else:
        print(f'{w} is not a palindrom!') 

check_pallindrom()