class Block:    ## 블록 클래스 정의
    def __init__(self, y1, x1, y2, x2, color):  ## 블록 클래스 매개변수(x,y 좌표값, 색깔)
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.color = color

    def getDirect(self):    ##블록의 방향(가로, 세로)
        if self.x2 == self.x1 + 1 and self.y1 == self.y2:
            return "X"
        elif self.y2 == self.y1 + 1 and self.x1 == self.x2:
            return "Y"

    def move(self, str, list):  ## 블록 움직이기
        if str == "UP":
            temp = list[self.y1][self.x1]
            list[self.y2][self.x2] = 0
            self.y1 = self.y1 - 1
            self.y2 = self.y2 - 1
            list[self.y1][self.x1] = temp
            list[self.y2][self.x2] = temp
        elif str == "DOWN":
            temp = list[self.y2][self.x2]
            list[self.y1][self.x1] = 0
            self.y1 = self.y1 + 1
            self.y2 = self.y2 + 1
            list[self.y1][self.x1] = temp
            list[self.y2][self.x2] = temp
        elif str == "LEFT":
            temp = list[self.y1][self.x1]
            list[self.y2][self.x2] = 0
            self.x1 = self.x1 - 1
            self.x2 = self.x2 - 1
            list[self.y1][self.x1] = temp
            list[self.y2][self.x2] = temp
        elif str == "RIGHT":
            temp = list[self.y1][self.x1]
            list[self.y1][self.x1] = 0
            self.x1 = self.x1 + 1
            self.x2 = self.x2 + 1
            list[self.y1][self.x1] = temp
            list[self.y2][self.x2] = temp
        return list
