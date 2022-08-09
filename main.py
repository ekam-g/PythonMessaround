
from files.quatomCanvas import test
from test import test


def p(print_value):
    print(print_value)


def cool_while_loop():
    i = 0
    while i < 10:
        p(i)
        i += 1


def cool_for_loop():
    a = 0
    for x in range(20):
        p(a)
        a += 1


def demo():
    dic = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
    }
    print(dic['model'] + ' This is the model what is the brand?')
    whatModelGuess = (input())
    if whatModelGuess == dic['brand']:
        print('correct')
        return 0
    print('incorrect')
    return 0


def switch():
    x= 1
    
    for x in range(10):
        match x:
            case 1:
                print('case 1')

            case 2:
                print('case 2')



if __name__ == '__main__':
    test.worked_test(test)
