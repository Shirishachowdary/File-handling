class League:
    def __init__(self, league_id, name):
        self.league_id = league_id
        self.name = name
        self.teams = []
        self.statistics = {}

    def add_team(self, team):
        self.teams.append(team)
        self.statistics[team.name] = {"wins": 0, "losses": 0}

    def remove_team(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                self.teams.remove(team)
                del self.statistics[team_name]
                return True
        return False

    def display_details(self):
        print("League ID:", self.league_id)
        print("League Name:", self.name)
        print("Teams:")
        for team in self.teams:
            team.display_details()
        print("Statistics:")
        a=open('demo.txt','a')
        a.write('Statistics:')
        a.write('\n')
        for team_name, stats in self.statistics.items():
            print(f"Team: {team_name}, Wins: {stats['wins']}, Losses: {stats['losses']}")
            a.write(f"Team: {team_name}, Wins: {stats['wins']}, Losses: {stats['losses']}")
            a.write('\n')
        a.close()


class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def display_details(self):
        print("Team Name:", self.name)
        print("Members:", ', '.join(self.members))
        
class Statistics:
    def __init__(self, team_name):
        self.team_name = team_name

    def update_stats(self, win):
        if win:
            self.wins += 1
        else:
            self.losses += 1

    def display_stats(self):
        print("Team:", self.team_name)
        print("Wins:", self.wins)
        print("Losses:", self.losses)



leagues = []

while True:
    print("\nMenu:")
    print("1. Create League")
    print("2. Add Team to League")
    print("3. Remove Team from League")
    print("4. Update Team Members")
    print("5. Record Game Result")
    print("6. Display League Details")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        league_id = int(input("Enter League ID: "))
        league_name = input("Enter League Name: ")
        new_league = League(league_id, league_name)
        leagues.append(new_league)
        print("League created successfully.")

    elif choice == "2":
        if not leagues:
            print("No leagues available. Please create a league first.")
            continue

        league_id = int(input("Enter League ID: "))
        found = False
        for league in leagues:
            if league.league_id == league_id:
                team_name = input("Enter Team Name: ")
                num_members = int(input("Enter Number of Team Members: "))
                members = []
                for i in range(num_members):
                    member_name = input("Enter Member Name {}: ".format(i + 1))
                    members.append(member_name)
                new_team = Team(team_name, members)
                league.add_team(new_team)
                print("Team added to the league successfully.")
                found = True
                break

        if not found:
            print("League with ID", league_id, "not found.")

    elif choice == "3":
        if not leagues:
            print("No leagues available.")
            continue

        league_id = int(input("Enter League ID: "))
        found = False
        for league in leagues:
            if league.league_id == league_id:
                team_name = input("Enter Team Name to remove: ")
                if league.remove_team(team_name):
                    print("Team removed successfully.")
                else:
                    print("Team not found in the league.")
                found = True
                break

        if not found:
            print("League with ID", league_id, "not found.")

    elif choice == "4":
        if not leagues:
            print("No leagues available.")
            continue

        league_id = int(input("Enter League ID: "))
        found = False
        for league in leagues:
            if league.league_id == league_id:
                team_name = input("Enter Team Name to update: ")
                for team in league.teams:
                    if team.name == team_name:
                        num_members = int(input("Enter Number of Team Members: "))
                        members = []
                        for i in range(num_members):
                            member_name = input("Enter Member Name {}: ".format(i + 1))
                            members.append(member_name)
                        team.members = members
                        print("Team members updated successfully.")
                        found = True
                        break
                if not found:
                    print("Team not found in the league.")
                break

        if not found:
            print("League with ID", league_id, "not found.")

    elif choice == "5":
            if not leagues:
                print("No leagues available.")
                continue

            league_id = int(input("Enter League ID: "))
            found = False
            for league in leagues:
                if league.league_id == league_id:
                    team1_name = input("Enter Team 1 Name: ")
                    team2_name = input("Enter Team 2 Name: ")
                    win_team = input("Enter the winning team (1 or 2): ")
                    if win_team == "1":
                        league.statistics[team1_name]["wins"] += 1
                        league.statistics[team2_name]["losses"] += 1
                    elif win_team == "2":
                        league.statistics[team2_name]["wins"] += 1
                        league.statistics[team1_name]["losses"] += 1
                    else:
                        print("Invalid input.")
                    print("Match result recorded successfully.")
                    found = True
                    break

            if not found:
                print("League with ID", league_id, "not found.")

    elif choice == "6":
        if not leagues:
            print("No leagues available.")
            continue

        league_id = int(input("Enter League ID: "))
        found = False
        for league in leagues:
            if league.league_id == league_id:
                league.display_details()
                found = True
                break

        if not found:
            print("League with ID", league_id, "not found.")

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")