import csv

def started(msg=""):
    print("-------------------------------------------------------------------------------------")
    print(f"Operation started: {msg}...\n")

def completed():
    print("Operation completed.")
    print("-------------------------------------------------------------------------------------")

def error(msg):
    print(f"Error! {msg}")

def menu():
    print(f"""\nPlease select one of the following options:
    {"[years]":<10} List Unique Years
    {"[tally]":<10} Tally Up Medals
    {"[team]":<10} Tally Up Medals For Each Team
    {"[exit]":<10} Exit the program
    """)

    print("\nYour Selection:")
    selected_option = str(input())
    return selected_option.lower()

def display_medal_tally(tally):
    print(f"""
    {"[Gold]":<10} | {tally["Gold"]:10}
    {"[Silver]":<10} | {tally["Silver"]:5}
    {"[Bronze]":<10} | {tally["Bronze"]:2} 
    """)

def display_medal_tally(team_tally):
    for team, tally in range(team_tally):
        print(team)
        print(f"Gold: {tally['Gold']:10}, Silver: {tally['Silver']:5}, Bronze: {tally['Bronze']:2}")

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)
