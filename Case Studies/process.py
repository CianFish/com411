import tui

def list_years(data):
    years = set()
    for year in data:
        extract = year[9]
        years.add(extract)

    tui.display_years(years)
    tui.completed()

def tally_medals(data):
