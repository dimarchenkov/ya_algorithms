def skobki_gen(left, right, result):
    if left == 0 and right == 0:
        print(result)
    else:
        if left > 0:
            skobki_gen(left - 1, right, f'{result}(')
        if left < right:
            skobki_gen(left, right - 1, f'{result})')


def main():
    n = int(input())
    skobki_gen(n, n, result='')


if __name__ == '__main__':
    main()
