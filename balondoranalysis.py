import csv 

#count based on countries
#count based on clubs 
#sort winners by goals
#sort winners by ga ratio
#sort winners by trophies
#compare two winners
#extract a particular winner based on year
#extract all players that won the balon for for a club
#extract all players that won the balon for for a country

def floatconvert(data):
    newdata = []
    for stats in data:
        if data.index(stats) != 1 and (stats.rstrip().isdigit() or "." in stats.rstrip()):
            newdata.append(float(stats.rstrip()))
        elif data.index(stats) == 1:
            newdata.append(int(stats.rstrip()))
        else:
            newdata.append(stats.rstrip())
    return newdata

def load():
    with open("balonwinners.csv" ,"r" ) as f:
        c = list(csv.reader(f))
    winners = list(map(floatconvert , c[1:]))
    winners.insert(0,c[0])
    return winners


def display():
    winners = load()
    for stats in winners[1:]:
        print(f"{stats[0]:<16}\t{stats[1]:<4}\t{stats[2]:<2}\t{stats[3]:<2}\t{stats[4]:<2}\t{stats[5]:<3}\t{stats[6]:<14}\t{stats[7]:<17}\t{stats[8]}")


def grouping(index):
    """6--->Country
    7--->Club
    0--->Player
    1--->Season"""
    groups = {}
    winners = load()
    for player in winners[1:]:
        groups.setdefault(player[index] , []).append(player[0])
    if index == 0:
        playergroup = {}
        for player in groups:
            playergroup[player] = len(groups[player])
        return playergroup
    return groups

def displaygrouping(index):
    groups = grouping(index)
    if index == 0 :
        for player , freq in groups.items():
            print(f"{player} has won {freq} times")
        return
    if index == 1:
        for season in groups:
            print(f"{season}: {groups[season][0]}")
        return
    
    for country , players in groups.items():
        unique = set(players)
        print(country)
        for name in unique:
            print(name , "x" , players.count(name))
        print()

def groupbycountry():
    return displaygrouping(6)

def groupbyclub():
    return displaygrouping(7)

def groupbyname():
    return displaygrouping(0)

def groupbyseason():
    return displaygrouping(1)

def analysis(index):
    """6--->Country
    7--->Club"""
    groups = grouping(index)
    analysisdict = {}
    count = sorted(groups.keys() , key = lambda x: -len(groups[x]))
    for country in count:
        analysisdict[country] = len(groups[country])
    return analysisdict

def displaycountryanalysis():
    analysisdict = analysis(6)
    for country , freq in analysisdict.items():
        print(f"{country}\nNumber of wins:{freq}\nWinning percentage = {round(((freq/25)*100) , 2)} %")
        print()

def displayclubanalysis():
    analysisdict = analysis(7)
    for club , freq in analysisdict.items():
        print(f"{club}\nNumber of wins:{freq}\nWinning percentage = {round(((freq/25)*100) , 2)} %")
        print()

def specificanalysis(group , index):
    """6--->Country
    7--->Club
    1--->Season"""
    analysisdict = analysis(index)
    groups = grouping(index)
    if index == 1:
        if group == 2020:
            print("The Balon dor ceremony was cancelled in 2020 , No player won it in 2020.")
            return
        print(f"{group}:\n{groups[group][0]}")
        return
    if group not in groups:
        print(f"{group} has no Balon Dor winners from 2000-2025.")
        return
    unique = sorted(set(groups[group]))
    print(f"{group}\nNumber of wins:{analysisdict[group]}\nWinning percentage = {round((analysisdict[group]/25)*100 , 2)} %")
    print()
    print("WINNERS:")
    for player in unique:
        print(f"{player}x{groups[group].count(player)}")
    print()
    winners = load()
    for header in winners[0:1]:
        print(f"{header[0]:<16}\t{header[1]:<4}\t{header[2]:<2}\t{header[3]:<2}\t{header[4]:<2}\t{header[5]:<3}\t{header[6]:<14}\t{header[7]:<17}\t{header[8]}")
    for stats in winners:
        if stats[0] in unique and stats[index] == group:
            print(f"{stats[0]:<16}\t{stats[1]:<4}\t{stats[2]:<2}\t{stats[3]:<2}\t{stats[4]:<2}\t{stats[5]:<3}\t{stats[6]:<14}\t{stats[7]:<17}\t{stats[8]}")


def specificplayer(player):
    groups = grouping(0)
    winners  = load()
    names = set()
    for stats in winners:
        names.add(stats[0])
    if player not in names:
        print(f"{player} has never won the Balon Dor in 2000-2025")
        return
    print(f"{player} has won the balon dor {groups[player]} times.")
    for header in winners[0:1]:
        print(f"{header[0]:<16}\t{header[1]:<4}\t{header[2]:<2}\t{header[3]:<2}\t{header[4]:<2}\t{header[5]:<3}\t{header[6]:<14}\t{header[7]:<17}\t{header[8]}")
    for stats in winners[1:]:
        if stats[0].replace(" " , "") == player.replace(" " , ""):
            print(f"{stats[0]:<16}\t{stats[1]:<4}\t{stats[2]:<2}\t{stats[3]:<2}\t{stats[4]:<2}\t{stats[5]:<3}\t{stats[6]:<14}\t{stats[7]:<17}\t{stats[8]}")


def statsort(index):
    """2---->Goals
    3---->Assists
    4----->GA
    5----.GR
    8----.Trophies"""
    winners = load()
    sortedwinners = sorted(winners[1:] , key = lambda x: -x[index])
    for header in winners[0:1]:
        print(f"{header[0]:<16}\t{header[1]:<4}\t{header[2]:<2}\t{header[3]:<2}\t{header[4]:<2}\t{header[5]:<3}\t{header[6]:<14}\t{header[7]:<17}\t{header[8]}")
    for stats in sortedwinners:
        print(f"{stats[0]:<16}\t{stats[1]:<4}\t{stats[2]:<2}\t{stats[3]:<2}\t{stats[4]:<2}\t{stats[5]:<3}\t{stats[6]:<14}\t{stats[7]:<17}\t{stats[8]}")

def comparator(playerA , seasonA , playerB , seasonB):
    if seasonA>2025 or seasonA<2000 or seasonB>2025 or seasonB<2000:
        print("The program is only for 2000-2025")
        return
    if seasonA == 2020 or seasonB == 2020:
        print("Balon Dor ceremony was cancelled in 2020 due to covid , Please choose a valid season")
        return
    pointA = 0 
    pointB = 0 
    playerfreq = grouping(0)
    winners = load()
    playerAstats = []
    playerBstats = []
    for stats in winners[1:]:
        if stats[0] == playerA and stats[1] == seasonA:
            playerAstats = stats
        if stats[0] == playerB and stats[1] == seasonB:
            playerBstats = stats
    if (not playerAstats) or (not playerBstats):
        if playerA not in playerfreq:
            print(f"{playerA} has never won the balon dor (2000-2025) , Please enter a valid player.")
            return
        if playerB not in playerfreq:
            print(f"{playerB} has never won the balon dor (2000-2025) , Please enter a valid player.")
            return          
        for stats in winners:
            if stats[1] == seasonA and stats[0] != playerA:
                print(f"{playerA} did not win the balon dor in {seasonA}")  
                return
            if stats[1] == seasonB and stats[0] != playerB:
                print(f"{playerB} did not win the balon dor in {seasonB}")  
                return
    for header in winners[0:1]:
        print(f"{header[0]:<16}\t{header[1]:<4}\t{header[2]:<2}\t{header[3]:<2}\t{header[4]:<2}\t{header[5]:<3}\t{header[6]:<14}\t{header[7]:<17}\t{header[8]}")
    print(f"{playerAstats[0]:<16}\t{playerAstats[1]:<4}\t{playerAstats[2]:<2}\t{playerAstats[3]:<2}\t{playerAstats[4]:<2}\t{playerAstats[5]:<3}\t{playerAstats[6]:<14}\t{playerAstats[7]:<17}\t{playerAstats[8]}")
    print(f"{playerBstats[0]:<16}\t{playerBstats[1]:<4}\t{playerBstats[2]:<2}\t{playerBstats[3]:<2}\t{playerBstats[4]:<2}\t{playerBstats[5]:<3}\t{playerBstats[6]:<14}\t{playerBstats[7]:<17}\t{playerBstats[8]}")
    print()
    pointA += playerAstats[2] + playerAstats[3] + playerAstats[8]*2
    pointB += playerBstats[2] + playerBstats[3] + playerBstats[8]*2
    if playerAstats[5] > playerBstats[5]:
        pointA+= 10
    if playerBstats[5] > playerAstats[5]:
        pointB += 10

    winner = max(pointA , pointB)
    if pointA == pointB:
        print(f"{playerA} in {seasonA} had the same number of points as {playerB} in {seasonB}")
    if winner == pointA:
        print(f"{playerA} had a better Balon dor winning season in {seasonA} than {playerB} in {seasonB}")
        print(f"{playerA} recieved {pointA} points and {playerB} recieved {pointB} points")
        return
    if winner == pointB:
        print(f"{playerB} had a better Balon dor winning season in {seasonB} than {playerA} in {seasonA}")
        print(f"{playerB} recieved {pointB} points and {playerA} recieved {pointA} points")
        return        



def pointcalc(stats):
    player = stats[0]
    points  = 0 
    points += stats[1] + stats[2] + stats[8]*2
    if stats[5]>0.5 and stats[5]<1.0:
        points+=5
    if stats[5]> 1.0:
        points+=10
    return -points

def pointsort():
    winners = load()
    sortedwinners = sorted(winners[1:] , key = pointcalc)
    for header in winners[0:1]:
        print(f"{header[0]:<16}\t{header[1]:<4}\t{header[2]:<2}\t{header[3]:<2}\t{header[4]:<2}\t{header[5]:<3}\t{header[6]:<14}\t{header[7]:<17}\t{header[8]}")
    for stats in sortedwinners:
        print(f"{stats[0]:<16}\t{stats[1]:<4}\t{stats[2]:<2}\t{stats[3]:<2}\t{stats[4]:<2}\t{stats[5]:<3}\t{stats[6]:<14}\t{stats[7]:<17}\t{stats[8]}")

print("------------------------")
print("This program contains dataset only from 2000-2025.\nWelcome to Balon Dor analyser")
print("------------------------")
print()
display()
while True:
    print()
    print("<<<MENU>>>")
    print()
    try:
        choice = int(input(
            "1.Winners by country\n" \
            "2.Winners by Club\n" \
            "3.How many times each player has won the balon dor (2000-2025)\n" \
            "4.Winner by years\n" \
            "5.Display Country wise stats\n" \
            "6.Display club wise stats\n" \
            "7.Specific country analysis\n" \
            "8.Specific club analysis\n" \
            "9.Which player won in a season x\n" \
            "10.Search for a specific player\n" \
            "11.Sort seasons by goals\n" \
            "12.Sort season by assists\n" \
            "13.Sort season by GA\n" \
            "14.Sort season by goal ratio\n" \
            "15.Sort season by Number of trophies\n" \
            "16.Compare two balon dor winning seasons\n" \
            "17.Sort based on best balon dor winning seasons\n" \
            "18.Exit\n" 
        ))
    except ValueError:
        print("Plase enter a valid choice.")
        continue
    if choice<1 or choice>18:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        groupbycountry()
    if choice == 2:
        groupbyclub()
    if choice == 3:
        groupbyname()
    if choice == 4:
        groupbyseason()
    if choice == 5:
        displaycountryanalysis()
    if choice == 6:
        displayclubanalysis()
    if choice == 7:
        while True:
            group = input("Enter the country you want to search: ").title()
            if group.isdigit() or "." in group:
                print("Please enter a valid country.")
            else:
                break
        specificanalysis(group , 6)
    if choice == 8:
        while True:
            group = input("Enter the club you want to search: ").title()
            if group.isdigit() or "." in group:
                print("Please enter a valid club.")
                continue
            else:
                break
        specificanalysis(group , 7)  
    if choice == 9:
        while True:
            group = int(input("Enter the season you want to search: "))
            if not isinstance(group , int):
                print("Please enter a valid season.")
                continue
            else:
                break
        specificanalysis(group , 1)     
    if choice == 10:
        while True:
            player = input("Enter a player name you want to search: ").title()
            if player.isdigit() or "." in player:
                print("Please enter a valid player name")
                continue
            else:
                break
        specificplayer(player)
    if choice == 11:
        print("SORTING BASED ON GOALS")
        print()
        statsort(2)
    if choice == 12:
        print("SORTING BASED ON ASSISTS")
        print()
        statsort(3)
    if choice == 13:
        print("SORTING BASED ON GA")
        print()
        statsort(4)
    if choice == 14:
        print("SORTING BASED ON GOAL CONTRI/GAME RATIO")
        print()
        statsort(5)
    if choice == 15:
        print("SORTING BASED ON TROPHIES")
        print()
        statsort(8)
    if choice == 16:
        while True:
            try: 
                playerA = input("Enter the name of first player: ").title()
                if playerA.isdigit() or " . " in playerA:
                    print("Please input a valid player name.")
                    continue
                seasonA = int(input("Enter the season of player 1: "))
                if not isinstance(seasonA , int):
                    print("Season must be an integer.")
                    continue
                playerB  = input("Enter the name of second player : ").title()
                if playerB.isdigit() or " . " in playerB:
                    print("Please input a valid player name.")
                    continue 
                seasonB = int(input("Enter the season of player 1: "))
                if not isinstance(seasonB , int):
                    print("Season must be an integer.")
                    continue
                else:
                    break
            except ValueError:
                print("Seasons must be integers.")
        comparator(playerA , seasonA , playerB , seasonB)
    if choice == 17:
        print("SORTING BY A POINT SYSTEM")
        print()
        print("POINTS = GOALS + ASSISTS + 2xTROPHIES\n" \
        "IF GA> 0.5 and GA<1, POINTS = POINTS + 5\n" \
        "1F GA>1 , POINTS = POINTS + 10")
        print()
        pointsort()
    if choice == 18:
        print('Exiting....')
        break




