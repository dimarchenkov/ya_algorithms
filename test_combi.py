def combinations(input_string):
    d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}

    if input_string == '':
        return ['']

    data = []
    word = d[input_string[-1]]

    for combination in combinations(input_string[:-1]):
        for c in word:
            data.append(combination + c)

    return data


if __name__ == '__main__':

    arr = [1,2,3]
    print(arr[-1])
    print(arr[:-1])
    print(' '.join(combinations(input())))
