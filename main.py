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


if __name__ == '__main__':
    cool_while_loop()
    p("now doing for loop")
    cool_for_loop()
    p("done")
