from abc import abstractmethod
from typing import Tuple, List


class ChessPiece:
    def __init__(self, name: str, color: str):
        self.x, self.y, self.name, self.color = "a", 1, name, color

    def get_pos(self) -> Tuple[str, int]:
        return self.x, self.y

    @abstractmethod
    def __repr__(self) -> str:
        return "\uFE0F"


class King(ChessPiece):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
        self.x = "e"
        self.y = 1 if color == "WHITE" else 8

    def __repr__(self):
        return "\u265A"


class Queen(ChessPiece):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
        self.x = "d"
        self.y = 1 if color == "WHITE" else 8

    def __repr__(self):
        return "\u265B"


class Bishop(ChessPiece):
    def __init__(self, x: str, name: str, color: str):
        super().__init__(name, color)
        self.x = x
        self.y = 1 if color == "WHITE" else 8

    def __repr__(self):
        return "\u265D"


class Knight(ChessPiece):
    def __init__(self, x: str, name: str, color: str):
        super().__init__(name, color)
        self.x = x
        self.y = 1 if color == "WHITE" else 8

    def __repr__(self):
        return "\u265E"


class Rook(ChessPiece):
    def __init__(self, x: str, name: str, color: str):
        super().__init__(name, color)
        self.x = x
        self.y = 1 if color == "WHITE" else 8

    def __repr__(self):
        return "\u265C"


class Pawn(ChessPiece):
    def __init__(self, x: str, name: str, color: str):
        super().__init__(name, color)
        self.x = x
        self.y = 2 if color == "WHITE" else 7

    def __repr__(self):
        return "\u265F"


def main():
    white_king: King = King(color="WHITE", name="White King")
    black_king: King = King(color="BLACK", name="Black King")
    white_queen: Queen = Queen(color="WHITE", name="White Queen")
    black_queen: Queen = Queen(color="BLACK", name="Black Queen")
    white_bishop_1: Bishop = Bishop(x="c", color="WHITE", name="White Bishop 1")
    white_bishop_2: Bishop = Bishop(x="f", color="WHITE", name="White Bishop 2")
    black_bishop_1: Bishop = Bishop(x="c", color="BLACK", name="Black Bishop 1")
    black_bishop_2: Bishop = Bishop(x="f", color="BLACK", name="Black Bishop 2")
    white_knight_1: Knight = Knight(x="b", color="WHITE", name="White Knight 1")
    white_knight_2: Knight = Knight(x="g", color="WHITE", name="White Knight 2")
    black_knight_1: Knight = Knight(x="b", color="BLACK", name="Black Knight 1")
    black_knight_2: Knight = Knight(x="g", color="BLACK", name="Black Knight 2")
    white_rook_1: Rook = Rook(x="a", color="WHITE", name="White Rook 1")
    white_rook_2: Rook = Rook(x="h", color="WHITE", name="White Rook 2")
    black_rook_1: Rook = Rook(x="a", color="BLACK", name="Black Rook 1")
    black_rook_2: Rook = Rook(x="h", color="BLACK", name="Black Rook 2")
    white_pawns: List[Pawn] = [Pawn(x=i, color="WHITE", name=f"White Pawn {i.upper()}")
                               for i in ["a", "b", "c", "d", "e", "f", "g", "h"]]
    black_pawns: List[Pawn] = [Pawn(x=i, color="BLACK", name=f"Black Pawn {i.upper()}")
                               for i in ["a", "b", "c", "d", "e", "f", "g", "h"]]


if __name__ == "__main__":
    main()
