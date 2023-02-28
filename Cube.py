import string


class Piece:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def move(self, position, orientation):
        self.position = position
        self.orientation = orientation


class Cube:
    def __init__(self):
        self.pieces = {
            "a": Piece(0, 0),
            "b": Piece(1, 0),
            "c": Piece(2, 0),
            "d": Piece(3, 0),
            "e": Piece(4, 0),
            "f": Piece(5, 0),
            "g": Piece(6, 0),
            "h": Piece(7, 0),
            "i": Piece(8, 0),
            "j": Piece(9, 0),
            "k": Piece(10, 0),
            "l": Piece(11, 0),
            "m": Piece(12, 0),
            "n": Piece(13, 0),
            "o": Piece(14, 0),
            "p": Piece(15, 0),
            "q": Piece(16, 0),
            "r": Piece(17, 0),
            "s": Piece(18, 0),
            "t": Piece(19, 0),
            "u": Piece(20, 0),
            "v": Piece(21, 0),
            "w": Piece(22, 0),
            "x": Piece(23, 0),
            "y": Piece(24, 0),
            "z": Piece(25, 0),
        }
        self.solved = {
            "a": Piece(0, 0),
            "b": Piece(1, 0),
            "c": Piece(2, 0),
            "d": Piece(3, 0),
            "e": Piece(4, 0),
            "f": Piece(5, 0),
            "g": Piece(6, 0),
            "h": Piece(7, 0),
            "i": Piece(8, 0),
            "j": Piece(9, 0),
            "k": Piece(10, 0),
            "l": Piece(11, 0),
            "m": Piece(12, 0),
            "n": Piece(13, 0),
            "o": Piece(14, 0),
            "p": Piece(15, 0),
            "q": Piece(16, 0),
            "r": Piece(17, 0),
            "s": Piece(18, 0),
            "t": Piece(19, 0),
            "u": Piece(20, 0),
            "v": Piece(21, 0),
            "w": Piece(22, 0),
            "x": Piece(23, 0),
            "y": Piece(24, 0),
            "z": Piece(25, 0),
        }

    def check_solved(self):  # TODO: finish Solve Check
        for i in self.pieces:
            if self.pieces[i].position == string.ascii_lowercase.index(i) and self.pieces[i].orientation == 0:
                pass
            else:
                return False
            return True

    def check_possible(self):
        if len(self.pieces) != len(set(self.pieces)):
            return "impossible"
        else:
            return "possible"

    def flip_check(self, piece, side):
        if side == "Up" or side == "Down":
            if piece == "j" or piece == "l" or piece == "o" or piece == "q":
                if self.pieces[piece].orientation == 1:
                    return 0
                else:
                    return 1
            else:
                return self.pieces[piece].orientation
        elif side == "Right" or side == "Left":
            if piece == "b" or piece == "h" or piece == "s" or piece == "y":
                if self.pieces[piece].orientation == 1:
                    return 0
                else:
                    return 1
            else:
                return self.pieces[piece].orientation
        elif side == "Front" or side == "Back":
            if piece == "d" or piece == "f" or piece == "u" or piece == "w":
                if self.pieces[piece].orientation == 1:
                    return 0
                else:
                    return 1
            else:
                return self.pieces[piece].orientation

    def corner_orientation(self, piece, rotation):
        orientation = self.pieces[piece].orientation
        if rotation == "cw":
            orientation += 1
            if orientation == 4:
                orientation = 1
            return orientation
        elif rotation == "ccw":
            orientation -= 1
            if orientation == 0:
                orientation = 3
            return orientation
        else:
            raise Exception("InputError - Expected \"cw\" or \"ccw\"")

    def collect(self, pos):
        piece_list = []
        for i in pos:
            for a in self.pieces:
                if i == self.pieces[a].position:
                    piece_list += a
        return piece_list

    def Up(self, prime=False):
        side = self.collect([0, 1, 2, 3, 5, 6, 7, 8])
        if not prime:
            self.pieces[side[0]].move(2, self.pieces[side[0]].orientation)
            self.pieces[side[1]].move(5, self.flip_check(side[1], "Up"))
            self.pieces[side[2]].move(8, self.pieces[side[0]].orientation)
            self.pieces[side[3]].move(1, self.flip_check(side[3], "Up"))
            self.pieces[side[4]].move(7, self.flip_check(side[4], "Up"))
            self.pieces[side[5]].move(0, self.pieces[side[0]].orientation)
            self.pieces[side[6]].move(3, self.flip_check(side[6], "Up"))
            self.pieces[side[7]].move(6, self.pieces[side[0]].orientation)
            print('moved side face clockwise')
        else:
            self.pieces[side[0]].move(6, self.pieces[side[0]].orientation)
            self.pieces[side[1]].move(3, self.flip_check(side[1], "Up"))
            self.pieces[side[2]].move(0, self.pieces[side[0]].orientation)
            self.pieces[side[3]].move(7, self.flip_check(side[3], "Up"))
            self.pieces[side[4]].move(1, self.flip_check(side[4], "Up"))
            self.pieces[side[5]].move(8, self.pieces[side[0]].orientation)
            self.pieces[side[6]].move(5, self.flip_check(side[6], "Up"))
            self.pieces[side[7]].move(2, self.pieces[side[0]].orientation)
            print('moved side face counterclockwise')

    def Down(self, prime=False):
        side = self.collect([17, 18, 19, 20, 22, 23, 24, 25])
        if not prime:
            self.pieces[side[0]].move(23, self.pieces[side[0]].orientation)
            self.pieces[side[1]].move(20, self.flip_check(side[1], "Down"))
            self.pieces[side[2]].move(17, self.pieces[side[0]].orientation)
            self.pieces[side[3]].move(24, self.flip_check(side[3], "Down"))
            self.pieces[side[4]].move(18, self.flip_check(side[4], "Down"))
            self.pieces[side[5]].move(25, self.pieces[side[0]].orientation)
            self.pieces[side[6]].move(22, self.flip_check(side[6], "Down"))
            self.pieces[side[7]].move(19, self.pieces[side[0]].orientation)
            print('moved bottom face clockwise')
        else:
            self.pieces[side[0]].move(19, self.pieces[side[0]].orientation)
            self.pieces[side[1]].move(22, self.flip_check(side[1], "Down"))
            self.pieces[side[2]].move(25, self.pieces[side[0]].orientation)
            self.pieces[side[3]].move(18, self.flip_check(side[3], "Down"))
            self.pieces[side[4]].move(24, self.flip_check(side[4], "Down"))
            self.pieces[side[5]].move(17, self.pieces[side[0]].orientation)
            self.pieces[side[6]].move(20, self.flip_check(side[6], "Down"))
            self.pieces[side[7]].move(23, self.pieces[side[0]].orientation)
            print('moved bottom face counterclockwise')

    def Right(self, prime=False):
        side = self.collect([2, 5, 8, 11, 16, 19, 22, 25])
        if not prime:
            self.pieces[side[0]].move(19, self.corner_orientation(self.pieces[side[0]], "ccw"))
            self.pieces[side[1]].move(11, self.flip_check(side[1], "Right"))
            self.pieces[side[2]].move(2,  self.corner_orientation(self.pieces[side[2]], "cw"))
            self.pieces[side[3]].move(22, self.flip_check(side[3], "Right"))
            self.pieces[side[4]].move(5,  self.flip_check(side[4], "Right"))
            self.pieces[side[5]].move(25, self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(16, self.flip_check(side[6], "Right"))
            self.pieces[side[7]].move(8,  self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved right face clockwise')
        else:
            self.pieces[side[0]].move(8,  self.corner_orientation(self.pieces[side[0]], "ccw"))
            self.pieces[side[1]].move(16, self.flip_check(side[1], "Right"))
            self.pieces[side[2]].move(25, self.corner_orientation(self.pieces[side[2]], "cw"))
            self.pieces[side[3]].move(5,  self.flip_check(side[3], "Right"))
            self.pieces[side[4]].move(22, self.flip_check(side[4], "Right"))
            self.pieces[side[5]].move(2,  self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(11, self.flip_check(side[6], "Right"))
            self.pieces[side[7]].move(19, self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved right face counterclockwise')

    def Left(self, prime=False):
        side = self.collect([0, 3, 6, 9, 14, 17, 20, 23])
        if not prime:
            self.pieces[side[0]].move(6,  self.corner_orientation(self.pieces[side[0]], "cw"))
            self.pieces[side[1]].move(14, self.flip_check(side[1], "Left"))
            self.pieces[side[2]].move(23, self.corner_orientation(self.pieces[side[2]], "ccw"))
            self.pieces[side[3]].move(3,  self.flip_check(side[3], "Left"))
            self.pieces[side[4]].move(20, self.flip_check(side[4], "Left"))
            self.pieces[side[5]].move(0,  self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(9,  self.flip_check(side[6], "Left"))
            self.pieces[side[7]].move(17, self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved left face clockwise')
        else:
            self.pieces[side[0]].move(17, self.corner_orientation(self.pieces[side[0]], "cw"))
            self.pieces[side[1]].move(9,  self.flip_check(side[1], "Left"))
            self.pieces[side[2]].move(0,  self.corner_orientation(self.pieces[side[2]], "ccw"))
            self.pieces[side[3]].move(20, self.flip_check(side[3], "Left"))
            self.pieces[side[4]].move(3,  self.flip_check(side[4], "Left"))
            self.pieces[side[5]].move(23, self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(14, self.flip_check(side[6], "Left"))
            self.pieces[side[7]].move(6,  self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved left face counterclockwise')

    def Front(self, prime=False):
        side = self.collect([6, 7, 8, 14, 16, 23, 24, 25])
        if not prime:
            self.pieces[side[0]].move(8,  self.corner_orientation(self.pieces[side[0]], "cw"))
            self.pieces[side[1]].move(16, self.flip_check(side[1], "Front"))
            self.pieces[side[2]].move(25, self.corner_orientation(self.pieces[side[2]], "ccw"))
            self.pieces[side[3]].move(7,  self.flip_check(side[3], "Front"))
            self.pieces[side[4]].move(24, self.flip_check(side[4], "Front"))
            self.pieces[side[5]].move(6,  self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(14, self.flip_check(side[6], "Front"))
            self.pieces[side[7]].move(23, self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved front face clockwise')
        else:
            self.pieces[side[0]].move(23, self.corner_orientation(self.pieces[side[0]], "cw"))
            self.pieces[side[1]].move(14, self.flip_check(side[1], "Front"))
            self.pieces[side[2]].move(6,  self.corner_orientation(self.pieces[side[2]], "ccw"))
            self.pieces[side[3]].move(24, self.flip_check(side[3], "Front"))
            self.pieces[side[4]].move(7,  self.flip_check(side[4], "Front"))
            self.pieces[side[5]].move(25, self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(16, self.flip_check(side[6], "Front"))
            self.pieces[side[7]].move(8,  self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved front face counterclockwise')

    def Back(self, prime=False):
        side = self.collect([0, 1, 2, 9, 11, 17, 18, 19])
        if not prime:
            self.pieces[side[0]].move(17, self.corner_orientation(self.pieces[side[0]], "ccw"))
            self.pieces[side[1]].move(9,  self.flip_check(side[1], "Back"))
            self.pieces[side[2]].move(0,  self.corner_orientation(self.pieces[side[2]], "cw"))
            self.pieces[side[3]].move(18, self.flip_check(side[3], "Back"))
            self.pieces[side[4]].move(1,  self.flip_check(side[4], "Back"))
            self.pieces[side[5]].move(19, self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(11, self.flip_check(side[6], "Back"))
            self.pieces[side[7]].move(2,  self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved right face clockwise')
        else:
            self.pieces[side[0]].move(2,  self.corner_orientation(self.pieces[side[0]], "ccw"))
            self.pieces[side[1]].move(11, self.flip_check(side[1], "Back"))
            self.pieces[side[2]].move(19, self.corner_orientation(self.pieces[side[2]], "cw"))
            self.pieces[side[3]].move(1,  self.flip_check(side[3], "Back"))
            self.pieces[side[4]].move(18, self.flip_check(side[4], "Back"))
            self.pieces[side[5]].move(0,  self.corner_orientation(self.pieces[side[5]], "cw"))
            self.pieces[side[6]].move(9,  self.flip_check(side[6], "Back"))
            self.pieces[side[7]].move(17, self.corner_orientation(self.pieces[side[7]], "ccw"))
            print('moved right face counterclockwise')

    def print(self, pieces=True, check_solved=False, check_possible=False):
        if pieces:
            for i in self.pieces:
                print(i, self.pieces[i].position, self.pieces[i].orientation)
        if check_solved:
            print(self.check_solved())
        if check_possible:
            print(self.check_possible())
