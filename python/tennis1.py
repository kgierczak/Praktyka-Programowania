class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        # Zmiana nazw punktów dla lepszej czytelności
        self.p1_points = 0
        self.p2_points = 0

    # Zmiana aktualizacji punktów na podstawie nazw graczy zamiast stałych zmiennych
    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += 1
        elif player_name == self.player2_name:
            self.p2_points += 1

    # Rozdzielenie dużej funkcji score na mniejsze funkcje pomocnicze
    def score(self):
        if self.p1_points == self.p2_points:
            return self.get_tie_score()

        if self.p1_points >= 4 or self.p2_points >= 4:
            return self.get_advantage_or_win_score()

        return self.get_normal_score()

    def get_tie_score(self):
        tie_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }
        return tie_scores.get(self.p1_points, "Deuce")

    def get_advantage_or_win_score(self):
        point_difference = self.p1_points - self.p2_points
        leading_player = self.player1_name if point_difference > 0 else self.player2_name

        if abs(point_difference) == 1:
            return f"Advantage {leading_player}"
        return f"Win for {leading_player}"

    def get_normal_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.p1_points]}-{score_names[self.p2_points]}"
