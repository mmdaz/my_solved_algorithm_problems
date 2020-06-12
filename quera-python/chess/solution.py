class Piece:
    def __init__(self, sort, color, position):
        self.sort = sort
        self.color = color
        self.position = position


class Board:
    def __init__(self):
        self.position = {}

    def add(self, piece: Piece):
        for key, value in self.position.items():
            if piece.position == key:
                print("invalid query")
                return
            if value.color == piece.color and value.sort == "K" and piece.sort == "K":
                print("invalid query")
                return
        self.position[piece.position] = piece

    def remove(self, position: tuple):
        if self.position.get(position) is None:
            print("invalid query")
            return
        if self.position.get(position).sort == "K":
            print("invalid query")
            return
        self.position.pop(position, None)

    def move(self, piece: Piece, position: tuple):
        if self.position.get(piece.position) is None:
            print("invalid query")
            return
        if self.position.get(position) is not None:
            if self.position[position].sort == "K":
                print("invalid query")
                return
            if self.position[position].color == piece.color:
                print("invalid query")
                return
        if self.position[piece.position].sort == piece.sort and self.position[
            piece.position].position == piece.position and self.position[piece.position].color == piece.color:
            self.position[position] = piece
            self.position.pop(piece.position, None)
        else:
            if self.position[position].sort == "K":
                print("invalid query")
                return

    def is_mate(self, dest_color):
        king = None
        for value in self.position.values():
            if value.sort == "K" and value.color == dest_color:
                king = value

        if self.is_safe((king.position[0], king.position[1] + 1), king.color) and self.is_safe(
                (king.position[0] + 1, king.position[1] + 1), king.color) and self.is_safe(
                (king.position[0] + 1, king.position[1]), king.color) and self.is_safe(
                (king.position[0] + 1, king.position[1] - 1), king.color) and self.is_safe(
                (king.position[0], king.position[1] - 1), king.color) and self.is_safe(
                (king.position[0] - 1, king.position[1] - 1), king.color) and self.is_safe(
                (king.position[0] - 1, king.position[1]), king.color) and self.is_safe(
                (king.position[0] - 1, king.position[1] + 1), king.color):
            return False
        else:
            return True

    def is_safe(self, position, color):
        if self.position.get(position) is None:
            return True
        if self.position[position].color == color:
            return True
        return False
