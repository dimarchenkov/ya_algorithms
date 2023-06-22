def compare(s, t):

    lens, lent = len(s), len(t)
    i = 0
    for j in range(lent):
        if s[i] == t[j]:
            i += 1
            if i == lens:
                return True

    return False

def main():
    s = input()
    t = input()

    print(compare(s,t))


if __name__ == '__main__':
    main()
