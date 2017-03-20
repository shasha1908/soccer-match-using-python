

import random
                   
team1 = input("team1: ")
team2 = input("team2: ")
events = False
maxInj = False
Event = ["Goal!", "Yellow Card,", "Red Card!", "Penalty!", "Injury!", "Score:", "Substitution"]

yC_team1 = []
rC_team1 = []
injury_team1 = []
sub_in_team1 = []
sub_out_team1 = []
sub_count1 = 0
rc_count1 = 0
score_count1 = 0
injury_count1 = 0
team1Stats = [team1, yC_team1, rC_team1, injury_team1, sub_in_team1, sub_out_team1, sub_count1, rc_count1, score_count1, injury_count1]

yC_team2 = []
rC_team2 = []
injury_team2 = []
sub_in_team2 = []
sub_out_team2 = []
sub_count2 = 0
rc_count2 = 0
score_count2 = 0
injury_count2 = 0
team2Stats = [team2, yC_team2, rC_team2, injury_team2, sub_in_team2, sub_out_team2, sub_count2, rc_count2, score_count2, injury_count2]



def SubChance():
    rdmint = random.randint(1,50)
    if rdmint > 41:
        return True
        
def TeamChance():
    rdmint = random.randint(0,1)
    if rdmint > .5:
        return team1Stats
    else:
        return team2Stats
        
def yCardChance():
    rdmint = random.randint(0,100)
    if rdmint > 98:
        return True
        
def rCardChance():
    rdmint = random.randint(0,300)
    if rdmint > 299:
        return True
    
def injuryChance():
    rdmint = random.randint(0,100)
    if rdmint > 99:
        return True
        
def goalChance():
    rdmint = random.randint(0,100)
    if rdmint > 96:
        return True

def penaltyChance():
    rdmint = random.randint(0,250)
    if rdmint > 249:
        return True

def penaltyBlock():
    rdmint = random.randint(0,1)
    if rdmint > .6:
        return True



def PlayerGenerator(event, team, yc, rc, injury, sub_in, sub_out):
    arsenalFirstsquad = ["No.18 Nacho Monreal", "No.6 Laurent Koscielny", "No.20 Shkodran Mustafi", 
"No.24 Hector Bellerin", "No.8 Aaron Ramsey", "No.11 Mesut Ozil", "No.29 Granit Xhaka", "No.34 Francis Coquelin", 
"No.7 Alexis Sanchez", "No.12 Olivier Giroud"]
    arsenalSubs = ["No.15 Alex Oxlade-Chamberlain", "No.19 Santi Cazorla", "No.9 Lucas Perez",
     "No.14 Theo Walcott", "No.3 Kieran Gibbs", "No.4 Per Mertesacker"]
    chelseaFirstsquad = ["No.26 John Terry", "No.24 Gary Cahill", "No.28 Cesar Azpilicueta", "No.30 David Luiz",
     "No.22 Willian", "No.11 Pedro", "No.10 Eden Hazard",
     "No.21 Nemanja Matic", "No.4 Cesc Fabregas", "No.19 Diego Costa"]
    chelseaSubs = ["No.2 Branislav Ivanovic", "No.3 Marcos Alonso", "No.15 Victor Moses", "No.16 Kenedy",
     "No.23 Michy Batshuayi", "No.7 N'Golo Kante"]
    output = []
    doubleY = False
    if team == team1:
        fs_players = arsenalFirstsquad
        subs = arsenalSubs
        yc = yC_team1
        rc = rC_team1
        injury = injury_team1
        sub_in = sub_in_team1
        sub_out = sub_out_team1
    elif team == team2:
        fs_players = chelseaFirstsquad
        subs = chelseaSubs
        yc = yC_team2
        rc = rC_team2
        injury = injury_team2
        sub_in = sub_in_team2
        sub_out = sub_out_team2
    if event == 0:
        rosterUpdate = [i for i in fs_players if i not in rc and i not in injury and i not in sub_out]
        for i in sub_in:
            rosterUpdate.append(i)
        player = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
        output = [team, player]
        return output
    elif event == 1:
        rosterUpdate = [i for i in fs_players if i not in rc and i not in injury and i not in sub_out]
        for i in sub_in:
            rosterUpdate.append(i)
        player = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
        if player[:] in yc:
            output= [team, player, 2]
            return output
        else:
            player = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
            output = [team, player]
            return output
    elif event == 2 or event == 3:
        rosterUpdate = [i for i in fs_players if i not in rc and i not in injury and i not in sub_out]
        for i in sub_in:
            rosterUpdate.append(i)
        player_out = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
        output = [team, player_out]
        return output
    elif event == 4:
        rosterUpdate = [i for i in fs_players if i not in rc and i not in injury and i not in sub_out]
        for i in sub_in:
            rosterUpdate.append(i)
        player_out = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
        subUpdate = [i for i in subs if i not in sub_in]
        player_in = subUpdate[random.randint(0, len(subUpdate)-1)]
        output = [team, player_out, player_in]
        return output
    elif event == 6:
        rosterUpdate = [i for i in fs_players if i not in rc and i not in injury and i not in sub_out]
        player_out = rosterUpdate[random.randint(0, len(rosterUpdate)-1)]
        subUpdate = [i for i in subs if i not in sub_in]
        player_in = subUpdate[random.randint(0, len(subUpdate)-1)]
        output = [team, player_out, player_in]
        return output


        
print(team1+" vs "+team2)
print("\nMatch Start!\n")
for min in range(1,91):
    if min > 65:
        sub = SubChance()
        if sub == True:
            teamStats = TeamChance()
            if int(teamStats[6]) + int(teamStats[9]) == 3:
                print("'"+str(min)+" min: ")
                events = True
            else:    
                playerSubs = PlayerGenerator(6, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
                teamStats[6] += 1
                print("'"+str(min)+" min: "+playerSubs[0]+" "+str(Event[6])+" : "+playerSubs[2]+" subbed in for "+"\n         "+playerSubs[1])
                teamStats[5].append(playerSubs[1])
                teamStats[4].append(playerSubs[2])
                events = True
    if events == False:
        gC = goalChance()
        if gC == True:
            teamStats = TeamChance()
            playerGoal = PlayerGenerator(0, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
            teamStats[8] += 1
            print("'"+str(min)+" min: "+str(playerGoal[0])+" "+str(Event[0])+" "+str(playerGoal[1])+"!")
            print("         "+Event[5]+" "+team1.upper()+" "+str(team1Stats[8])+" : "+team2.upper()+" "+str(team2Stats[8]))
            events = True
    if events == False:
        pC = penaltyChance()
        if pC == True:
            teamStats = TeamChance()
            playerPenalty = PlayerGenerator(3, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
            print("'"+str(min)+" min: "+str(playerPenalty[0])+" "+str(Event[3]))
            print("         "+str(playerPenalty[1])+" steps up to shoot...")
            pB = penaltyBlock()
            if pB == True:
                print("         SHOT BLOCKED!!")
                events = True
            else:
                teamStats[8] += 1
                print("         GOAL!   "+str(playerPenalty[0])+"!")
                print("         "+Event[5]+" "+team1.upper()+" "+str(team1Stats[8])+" : "+team2.upper()+" "+str(team2Stats[8]))
                events = True
    if events == False:
        yC = yCardChance()
        if yC == True:
            teamStats = TeamChance()    
            playerYellow = PlayerGenerator(1, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
            if len(playerYellow) == 3:
                teamStats[7] += 1
                print("'"+str(min)+" min: "+str(playerYellow[0])+" "+str(Event[1])+" "+str(playerYellow[1])+"\n         "+str(playerYellow[1])+"'s Second Yellow! Red Card!"+"\n         "+str(playerYellow[0])+" are down to "+str(11-(int(teamStats[7])))+" men!")
                teamStats[2].append(playerYellow[1])
                events = True
            else:
                print("'"+str(min)+" min: "+str(playerYellow[0])+" "+str(Event[1])+" "+str(playerYellow[1]))
                teamStats[1].append(playerYellow[1])
                events = True
    if events == False:
        rC = rCardChance()
        if rC == True:
            teamStats = TeamChance()    
            playerRed = PlayerGenerator(2, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
            teamStats[7] += 1
            print("'"+str(min)+" min: "+str(playerRed[0])+" "+str(Event[2])+" "+str(playerRed[1])+"\n         "+str(playerRed[0])+" are down to "+
            str(11-(int(teamStats[7])))+" men!")
            teamStats[2].append(playerRed[1])
            events = True
    if events == False and maxInj == False:
        inj = injuryChance()
        if inj == True:
            teamStats = TeamChance()   
            playerInjured = PlayerGenerator(4, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
            if teamStats[6] + teamStats[9] == 3:
                print("'"+str(min)+" min: "+str(playerInjured[0])+" "+str(Event[4])+" "+str(playerInjured[1])+", with a broken leg!!"+"\n         "+str(playerInjured[0])+" substitutions maxed out. "+str(playerInjured[0])+" are down to "+str(11-(int(teamStats[7]))-1)+" men!")
                teamStats[3].append(playerInjured[1])
                maxInj = True
            else:
                print("'"+str(min)+" min: "+str(playerInjured[0])+" "+str(Event[4])+" "+str(playerInjured[1])+", with a broken leg!!"+"\n         "+str(playerInjured[2])+" subbed in.")
                teamStats[3].append(playerInjured[1])
                teamStats[4].append(playerInjured[2])
            teamStats[9] += 1
            events = True
    if events == False:        
        print("'"+str(min)+" min: ")
    events = False        
    if min == 45:
        added = random.randint(1,5)
        print(" "+str(added)+" Minute(s) of Stoppage Time")
        s = 45
        for i in range(added):
            s += 1
            gC = goalChance()
            if gC == True:
                teamStats = TeamChance()
                playerGoal = PlayerGenerator(0, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
                teamStats[8] += 1
                print ("'"+str(s)+" min in stoppage time: "+str(playerGoal[0])+" "+str(Event[0])+" "+str(playerGoal[1])+"!")
                print("        "+Event[5]+" "+team1.upper()+" "+str(team1Stats[8])+" : "+team2.upper()+" "+str(team2Stats[8]))
                events = True
            if events == False:
                print("'"+str(s)+" min in stoppage time: ")
            events = False
        print("\nHALF TIME\n")
        print("Start of Second Half!")
    if min == 90:
        added = random.randint(1,5)
        print(" "+str(added)+" Minute(s) of Stoppage Time")
        s = 90
        for i in range(added):
            s += 1
            gC = goalChance()
            if gC == True:
                teamStats = TeamChance()
                playerGoal = PlayerGenerator(0, teamStats[0], teamStats[1], teamStats[2], teamStats[3], teamStats[4], teamStats[5])
                teamStats[8] += 1
                print("'"+str(s)+" min in stoppage time: "+str(playerGoal[0])+" "+str(Event[0])+" "+str(playerGoal[1])+"!")
                print("        "+Event[5]+" "+team1.upper()+" "+str(team1Stats[8])+" : "+team2.upper()+" "+str(team2Stats[8]))
                events = True
            if events == False:        
                print("'"+str(s)+" min in stoppage time: ")
            events = False                    
        print("\nFULL TIME\n")
        print("Final Score: "+team1.upper()+" "+str(team1Stats[8])+" : "+team2.upper()+" "+str(team2Stats[8]))