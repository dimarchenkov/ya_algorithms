import random


class Intern:
    def __init__(self, name, points, fines):
        self.name = name
        self.points = points
        self.fines = fines

    def __gt__(self, other):

        if self.points == other.points:
            if self.fines == other.fines:
                return self.name < other.name
            else:
                return self.fines < other.fines
        else:
            return self.points > other.points

    def __lt__(self, other):

        if self.points == other.points:
            if self.fines == other.fines:
                return self.name > other.name
            else:
                return self.fines > other.fines
        else:
            return self.points < other.points







def main():
    intern1 = Intern('dima',  10,  2)
    intern2 = Intern('anton', 10,  0)

    intern3 = Intern('dkma', 10, 0)

    alla = Intern('alla', 4, 100),
    gena = Intern('gena', 6, 1000),
    gosha = Intern('gosha', 2, 90),
    rita = Intern('rita', 2, 90),
    timofey = Intern('timofey', 4, 80),

    print(alla > timofey)
    print(alla < timofey)

    print(gosha > rita)
    print(gosha < rita)



if __name__ == '__main__':
    main()
