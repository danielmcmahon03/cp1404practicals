"""
CP1404 Practical 5
Wimbledon
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = get_past_records(FILENAME)
    champion_to_count, countries = create_records(records)
    display_records(champion_to_count, countries)


def get_past_records(file):
    records = []
    with open(file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def create_records(records):
    champion_to_count = {}
    countries = []
    for record in records:
        countries.append(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_records(champion_to_count, countries):
    print("Wimbledon Champions:")
    max_length = max(len(champion) for champion in champion_to_count)
    for champion, count in champion_to_count.items():
        print(f"{champion:{max_length}} : ", count)
    country_winners = set(countries)
    print(f"These {len(country_winners)} countries have won Wimbledon")
    print(", ".join(country for country in sorted(country_winners)))


main()
