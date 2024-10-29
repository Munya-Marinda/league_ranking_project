from .league_table import LeagueTable


def main(input_data):
    league = LeagueTable()
    for result in input_data:
        league.process_result(result.strip())
    return league.get_rankings()


if __name__ == "__main__":
    with open("input_data/sample_input.txt", "r") as f:
        input_data = f.readlines()
    output = main(input_data)

    for line in output:
        print(line)
