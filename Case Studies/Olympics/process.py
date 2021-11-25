import tui

def list_years(data):
    years = set()
    for year in data:
        extract = year[9]
        years.add(extract)

    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying Medals")
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for medal in data:
        extract = medal[14]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()