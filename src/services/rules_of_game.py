class RulesOfGame:
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")


class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination


class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)

        return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)


class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        col_diff = abs(source_col - dest_col)
        row_diff = abs(source_row - dest_row)

        return col_diff <= 1 and row_diff <= 1 and source != destination


class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        diagonal_move = abs(source_col - dest_col) == abs(source_row - dest_row)
        straight_move = source_col == dest_col or source_row == dest_row

        return (diagonal_move or straight_move) and source != destination


class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return (source_col == dest_col or source_row == dest_row) and source != destination


class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        col_diff = abs(source_col - dest_col)
        row_diff = dest_row - source_row

        return (col_diff == 0 and row_diff == 1) or (col_diff == 1 and row_diff == 1)
