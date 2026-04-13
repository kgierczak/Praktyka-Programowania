class TennisGame3:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        # Zmiana nazw pól punktów dla lepszej czytelności
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str):
        if player_name == "player1":
            self.p1_points += 1
        elif player_name == "player2":
            self.p2_points += 1

    def score(self) -> str:
        # Standardowa punktacja
        if self._is_standard_score():
            return self._get_standard_score_label()

        # Stan równowagi
        if self.p1_points == self.p2_points:
            return "Deuce"

        # Przewaga lub Wygrana
        return self._get_end_game_status()

    # Sprawdza, czy gra jest na etapie standardowych punktów
    def _is_standard_score(self) -> bool:
        return self.p1_points < 4 and self.p2_points < 4 and (self.p1_points + self.p2_points < 6)

    def _get_standard_score_label(self) -> str:
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        p1_score = score_names[self.p1_points]

        if self.p1_points == self.p2_points:
            return f"{p1_score}-All"
        return f"{p1_score}-{score_names[self.p2_points]}"

    # Logika dla Przewagi i Wygranej
    def _get_end_game_status(self) -> str:
        leader = self.player1_name if self.p1_points > self.p2_points else self.player2_name
        point_diff = abs(self.p1_points - self.p2_points)

        if point_diff == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"