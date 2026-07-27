class Connect4:
    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.game_finished = False

    def play(self, col):
        if self.game_finished:
            return "Game has finished!"

        row = self.get_open_row(col)

        if row is None:
            return "Column full!"

        self.board[row][col] = self.current_player

        if self.has_won(row, col):
            self.game_finished = True
            return f"Player {self.current_player} wins!"

        result = f"Player {self.current_player} has a turn"

        if self.current_player == 1:
            self.current_player = 2
@test.describe('Example Tests')

def example_tests():
    game = Connect4()
    @test.it("Should return: Player 1 has a turn")
    def example_test_case():
        test.assert_equals(game.play(0), "Player 1 has a turn")
    @test.it("Should return: Player 2 has a turn")
    def example_test_case():
        test.assert_equals(game.play(0), "Player 2 has a turn")
    
    game = Connect4()
    @test.it("Should return: Player 1 has a turn")
    def example_test_case():
        test.assert_equals(game.play(0), "Player 1 has a turn")
    @test.it("Should return: Player 2 has a turn")
    def example_test_case():
        test.assert_equals(game.play(1), "Player 2 has a turn")
    @test.it("Should return: Player 1 has a turn")