class TennisGame2:
    # Wyciągnięcie mapy punktów zamiast wielu metod "if"
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        # Zmiana nazw pól punktów dla lepszej czytelności
        self.p1_points = 0
        self.p2_points = 0

    # Zmiana aktualizacja punktów na podstawie nazw graczy zamiast stałych stringów
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += 1
        elif player_name == self.player2_name:
            self.p2_points += 1

    # Rozdzielenie dużej metody score na mniejsze funkcje pomocnicze
    def score(self):
        if self.p1_points == self.p2_points:
            return self.get_equal_score()

        if self.p1_points >= 4 or self.p2_points >= 4:
            return self.get_endgame_score()

        return f"{self.SCORE_NAMES[self.p1_points]} - {self.SCORE_NAMES[self.p2_points]}"

    def get_equal_score(self):
        if self.p1_points < 3:
            return f"{self.SCORE_NAMES[self.p1_points]}-All"
        return "Deuce"

    def get_endgame_score(self):
        point_diff = self.p1_points - self.p2_points
        leader = self.player1_name if point_diff > 0 else self.player2_name

        if abs(point_diff) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"
