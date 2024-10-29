from collections import defaultdict
from typing import List


class LeagueTable:
    def __init__(self):
        self.points = defaultdict(int)  # Stores points for each team

    def process_result(self, result: str):
        # Splits the result into team names and scores
        team1_data, team2_data = result.split(", ")
        team1, score1 = team1_data.rsplit(" ", 1)
        team2, score2 = team2_data.rsplit(" ", 1)
        score1, score2 = int(score1), int(score2)

        # Ensure both teams are added to points dictionary
        self.points[team1]  # Initialize team1
        self.points[team2]  # Initialize team2

        # Updates points based on match outcome
        if score1 > score2:
            self.points[team1] += 3
        elif score1 < score2:
            self.points[team2] += 3
        else:
            self.points[team1] += 1
            self.points[team2] += 1

    def get_rankings(self) -> List[str]:
        # Sorts teams by points (highest first) and alphabetically for ties
        sorted_teams = sorted(self.points.items(), key=lambda x: (-x[1], x[0]))

        # Builds and formats the ranking list
        rankings = []
        current_rank = 1
        for i, (team, pts) in enumerate(sorted_teams):
            if i > 0 and pts < sorted_teams[i - 1][1]:
                current_rank = i + 1
            suffix = "pt" if pts == 1 else "pts"
            rankings.append(f"{current_rank}. {team}, {pts} {suffix}")
        return rankings


def main(input_data: List[str]) -> List[str]:
    league = LeagueTable()
    for result in input_data:
        league.process_result(result)
    return league.get_rankings()
