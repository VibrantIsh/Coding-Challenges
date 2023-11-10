class Game:
    def __init__(self, turns, r):
        self.t = turns
        self.res = r
        self.ascore = 0
        self.bscore = 0
        self.cs = 'A'

    def play(self):
        for o in self.res:
            if o == self.cs:
                self.ascore += 1
            else:
                self.cs = o

        if self.cs == 'B':
            self.bscore += 1

    def get_s(self):
        return self.ascore, self.bscore


def main():
    t = int(input("Enter number of test cases: "))

    for _ in range(t):
        turns = int(input("Enter number of turns: "))
        result = input("Enter result string (A/B): ")

        g = Game(turns, result)
        g.play()

        ascore, bscore = g.get_s()
        print("Final Scores:", ascore, bscore)
        print()


if __name__ == "__main__":
    main()

