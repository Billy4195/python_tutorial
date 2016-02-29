class section:
    def __init__(self,introduction):
        self.introduction = introduction
        self.finished = 0
    def play(self):
        for line in self.introduction:
            print(line)
        self.finished = 1