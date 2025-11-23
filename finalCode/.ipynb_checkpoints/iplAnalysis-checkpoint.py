import pandas as pd

## Data Cleaning - Sayaji

print()

## Menu
def mainMenu():
    print("Ipl TOP 4 Teams Analysis")

    print()
    print()

    print("1. Player Stats ")
    print("2. Team Stats ")
    print("3. Rankings ")
    print("4. ROI")
    print("5. Exit")

    print()

    firstChoice=int(input("Enter your choice:"))

    print()

    if(firstChoice==1):

        ## Player Stats - Vedant Agrawal

        print("Player Stats")

        print("1. Search Player ")
        print("2. Compare Player ")
        print("3. Filter by Role ")
        print("4. Back to main menu")
        print("5. Exit")

        print()

        secondChoice=int(input("Enter your choice:"))

        print()

        if(secondChoice==1):
            ## Search Player
            print("Search Player")

        elif(secondChoice==2):
            ## Compare Player
            print("Compare Players")

        elif(secondChoice==3):
            ## Filter By role
            print("1. Batsman ")
            print("2. Wicket Keepers ")
            print("3. All rounders ")
            print("4. Bowlers ")
            print("5. Back to main menu")
            print("6. Exit")

            print()

            thirdChoice=int(input("Enter your choice:"))

            print()

            if(thirdChoice==1):
                print("Batsman")
                ## Print Batsman List

            elif(thirdChoice==2):
                print("Wicket Keepers")
                ## Print Wicket Keepers List
            
            elif(thirdChoice==3):
                print("All Rounders")
                ## Print All Rounders List
            
            elif(thirdChoice==4):
                print("Bowlers")
                ## Print Bowlers List

            elif(thirdChoice==5):
                ## Back to main menu
                print("Main Menu")
                mainMenu()
            
            elif(thirdChoice==6):
                ## Exit
                print("System Closed Succesfully")

            else:
                print("Invalid input: Enter the index as choice")
        
        elif(secondChoice==4):
                ## Back to main menu
                print("Main Menu")
                mainMenu()

        elif(secondChoice==5):
                ## Exit
                print("System Closed Succesfully")

        else:
                print("Invalid input: Enter the index as choice")

        ## End of Player Stats

    elif(firstChoice==2):

        ## Team Stats - Rugved Bajare


        print("Team Stats")

        ## Preparation

        #Teams
        players=pd.DataFrame()
        players=pd.read_csv("./iplAnalysis1.csv")

        rcb=players[players["Team"]=="RCB"]
        pbks=players[players["Team"]=="PBKS"]
        gt=players[players["Team"]=="GT"]
        mi=players[players["Team"]=="MI"]

        #Functions
        def teamStat(team):
            teamName=team["Team"].iloc[0]
            
            totalRuns=int(team["Runs scored"].sum())
                
            totalWickets=int(team["Wickets"].sum())

            battingAvg=float(round((team["Batting Avg."].sum())/(team["Batting Avg."].count()),2))
                
            bowlEco=float(round((team["BOWLING Economy"].sum())/(team["BOWLING Economy"].count()),2))
                
            batSR=float(round((team["Batting Strike Rate"].sum())/(team["Batting Strike Rate"].count()),2))
                
            maxRuns=team["Runs scored"].max()
            bestBat=team[team["Runs scored"]==maxRuns]
            bestBatStr=bestBat["Player"].to_string(index=False)
                
            maxWickets=team["Wickets"].max()
            bestBowl=team[team["Wickets"]==maxWickets]
            bestBowlStr=bestBowl["Player"].to_string(index=False)

            teamData=[teamName,totalRuns,totalWickets,battingAvg,bowlEco,batSR,bestBatStr,bestBowlStr]
            return teamData

        def TeamSummary():
            TeamSummary=pd.DataFrame(data=[teamStat(rcb),teamStat(gt),teamStat(mi),teamStat(pbks)],columns=["Team","Total Runs","Total Wickets","Bat_Avg","Eco","Bat_Sr","Best Bat","Best Bowl"],index=[1,2,3,4])
            return TeamSummary
        
        def printingTeamStat(team):
        
            team=teamStat(team)
        
            teamName=team[0]
            print("Team Name :",teamName)

            totalRuns=team[1]
            print("Total Runs :",totalRuns)

            totalWickets=team[2]
            print("Total Wickets :",totalRuns)

            battingAvg=team[3]
            print("Batting Avg :",battingAvg)

            eco=team[4]
            print("Bowling Economy :",eco)

            batSR=team[5]
            print("Bat SR :",batSR)

            bestBat=team[6]
            print("Best Batsman :",bestBat)

            bestBowl=team[7]
            print("Best Bowler :",bestBowl)

            return 0
        
        def comparetoPercentages(value1,value2):
            maxValue=max(value1,value2) 
            newValue1=(value1/maxValue)*100 
            newValue2=(value2/maxValue)*100 
            return(newValue1,newValue2)
        
        def percentageDiff(value1percentage,value2percentage):
            return(round(abs(value1percentage-value2percentage),2))
        
        
        def compareTeams(team1,team2):
        
            team1stat=teamStat(team1)

            team1Name=team1stat[0]
            team1Runs=int(team1stat[1])
            team1Wickets=int(team1stat[2])
            team1BatAvg=team1stat[3]
            team1Eco=team1stat[4]
            team1BatSR=team1stat[5]

            team2stat=teamStat(team2)

            team2Name=team2stat[0]
            team2Runs=int(team2stat[1])
            team2Wickets=int(team2stat[2])
            team2BatAvg=team2stat[3]
            team2Eco=team2stat[4]
            team2BatSR=team2stat[5]

            team1RunsPercent,team2RunsPercent=comparetoPercentages(team1Runs,team2Runs)
            team1WicketsPercent,team2WicketsPercent=comparetoPercentages(team1Wickets,team2Wickets)
            team1BatAvgPercent,team2BatAvgPercent=comparetoPercentages(team1BatAvg,team2BatAvg) 
            team1EcoPercent,team2EcoPercent=comparetoPercentages(team1Eco,team2Eco)
            team1BatSRPercent,team2batSRPercent=comparetoPercentages(team1BatSR,team2BatSR)


            CompareTeamsDf=pd.DataFrame({team1Name:{"Runs":team1Runs,"Wickets":team1Wickets,"Bat Avg":team1BatAvg,"Economy":team1Eco,"Bat SR":team1BatSR},
                                        team2Name:{"Runs":team2Runs,"Wickets":team2Wickets,"Bat Avg":team2BatAvg,"Economy":team2Eco,"Bat SR":team2BatSR},
                                        "% Diff" :{"Runs":percentageDiff(team1RunsPercent,team2RunsPercent),"Wickets":percentageDiff(team1WicketsPercent,team2WicketsPercent),
                                                "Bat Avg":percentageDiff(team1BatAvgPercent,team2BatAvgPercent),"Economy":percentageDiff(team1EcoPercent,team2EcoPercent),
                                                "Bat SR":percentageDiff(team1BatSRPercent,team2batSRPercent)}
                                        })
            print(CompareTeamsDf)



        

        
        ## Menu

        print("1. Squads ")
        print("2. Team Summary ")
        print("3. Overall Team Summary ")
        print("4. Compare Teams ")
        print("5. Playoffs Summary")
        print("6. League Team Averages")
        print("7. Back to main menu")
        print("8. Exit")

        print()

        secondChoice=int(input("Enter your choice:"))

        print()

        

        if(secondChoice==1):
            ## Squads
            print("Squads")

            print("1. RCB ")
            print("2. PBKS ")
            print("3. MI ")
            print("4. GT ")
            print("5. Back to main menu")
            print("6. Exit")

            print()

            thirdChoice=int(input("Enter your choice:"))

            print()

            if(thirdChoice==1):
                print("RCB Squad")
                print(rcb[["Player","Role"]])


            elif(thirdChoice==2):
                print("PBKS Squad")
                print(pbks[["Player","Role"]])
            
            elif(thirdChoice==3):
                print("MI Squad")
                print(mi[["Player","Role"]])
                
            
            elif(thirdChoice==4):
                print("GT Squad")
                print(gt[["Player","Role"]])

            elif(thirdChoice==5):
                ## Back to main menu
                print("Main Menu")
                mainMenu()
            
            elif(thirdChoice==6):
                ## Exit
                print("System Closed Succesfully")

            else:
                print("Invalid input: Enter the index as choice")


        elif(secondChoice==2):
            ## Team Summary

            print("Team Summary")

            print("1. RCB ")
            print("2. PBKS ")
            print("3. MI ")
            print("4. GT ")
            print("5. Back to main menu")
            print("6. Exit")

            print()

            thirdChoice=int(input("Enter your choice:"))

            print()

            if(thirdChoice==1):
                print("RCB Team Summary")
                printingTeamStat(rcb)


            elif(thirdChoice==2):
                print("PBKS Team Summary")
                printingTeamStat(pbks)
            
            elif(thirdChoice==3):
                print("MI Team Summary")
                printingTeamStat(mi)
                
            
            elif(thirdChoice==4):
                print("GT Team Summary")
                printingTeamStat(gt)

            elif(thirdChoice==5):
                ## Back to main menu
                print("Main Menu")
                mainMenu()
            
            elif(thirdChoice==6):
                ## Exit
                print("System Closed Succesfully")

            else:
                print("Invalid input: Enter the index as choice") 

                
        elif(secondChoice==3):
            ## Overall Team Summary
            print(TeamSummary())

            
        elif(secondChoice==4):

            ## Compare Teams
            
            def inputTeam():
                team=input("Enter initials of team 1(rcb,mi,gt,pbks) :")
                team=team.lower()
                if(team != "rcb" or "pbks" or "mi" or "gt"):
                    print("Invalid initials : Choose from rcb,pbks,mi and gt")
                    inputTeam()
                else:
                    return team
            
            team1=inputTeam()
            team2=input()

            compareTeams(team1,team2)


        elif(secondChoice==5):
                ##League Summary

            def printLeagueSummary():
                print("League Summary")
                print()
                
                Summary=TeamSummary()

                totalRuns=int(Summary["Total Runs"].sum()) 
                print("Total Runs :",totalRuns) 

                totalWickets=int(Summary["Total Wickets"].sum()) 
                print("Total Wickets :",totalWickets) 

                total50s=players["50+ Scores"].sum()
                print("Total half centuries :",total50s)
                
                total100s=players["100+ Scores"].sum()
                print("Total Centuries :",total100s)

                total4W=players["4W"].sum()
                print("Total 4 Wicket Hauls :",total4W)

                total5W=players["5W"].sum()
                print("Total 5 Wicket Hauls :",total5W)

                print()

                max_runs=players["Runs scored"].max()
                bestBat=players[players["Runs scored"]==max_runs] 
                bestBatList=bestBat["Player"].to_list()
                bestBatStr=" , ".join(bestBatList)
                print(f"Highest Run Scorer : {bestBatStr} ({max_runs} runs) ")

                max_wickets=players["Wickets"].max()
                bestBowl=players[players["Wickets"]==max_wickets] 
                bestBowlList=bestBowl["Player"].to_list()
                bestBowlStr=" , ".join(bestBowlList)
                print(f"Highest Wicket Taker : {bestBowlStr} ({max_wickets} wickets)")

                max_50s=players["50+ Scores"].max()
                mostFiftiesPlayer=players[players["50+ Scores"]==max_50s] 
                mostFiftiesPlayerList=mostFiftiesPlayer["Player"].to_list()
                mostFiftiesPlayerStr=" , ".join(mostFiftiesPlayerList)
                print(f"Most Half Centuries : {mostFiftiesPlayerStr}({max_50s} Half Centuries)")

                max_100s=players["100+ Scores"].max()
                mostCenturiesPlayer=players[players["100+ Scores"]==max_100s] 
                mostCenturiesPlayerList=mostCenturiesPlayer["Player"].to_list()
                mostCenturiesPlayerStr=" , ".join(mostCenturiesPlayerList)
                print(f"Most Centuries  : {mostCenturiesPlayerStr} ({max_100s} Centuries)")
            

            printLeagueSummary()


        elif(secondChoice==6):
            ## League Team Averages

            def printLeagueAverage():
                Summary=TeamSummary()

                totalRuns=int(Summary["Total Runs"].mean())
                print("Total Runs :",totalRuns)

                totalWickets=int(Summary["Total Wickets"].mean())
                print("Total Runs :",totalWickets)

                battingAvg=round(Summary["Bat_Avg"].mean(),2)
                print("Batting Avg :",battingAvg)

                eco=round(Summary["Eco"].mean(),2)
                print("Bowling Economy :",eco)

                batSR=round(Summary["Bat_Sr"].mean(),2)
                print("Bat SR :",batSR)

            printLeagueAverage()


        elif(secondChoice==5):
                ## Back to main menu
                print("Main Menu")
                mainMenu()
            
        elif(secondChoice==6):
                ## Exit
                print("System Closed Succesfully")

        else:
                print("Invalid input: Enter the index as choice") 

        print()

        
    elif(firstChoice==3):
        ## Rankings - Vard
        print("Rankings")

        players= pd.read_csv(r"C:\Users\Lenovo\Downloads\iplAnalysis1.csv" , index_col=0)

        # TOP 5 RUNSCORERS-
        top5runscorers = players.sort_values(by = 'Runs scored' , ascending=False)

        #-----------------------------------------------------------------------------------------------------------------------#
        ##TOP WICKET TAKERS-
        top5wickettakers = players.sort_values(by = 'Wickets' , ascending=False)

        #-----------------------------------------------------------------------------------------------------------------------#
        ##TOP 5 STRIKE HITTERS-
        top5strikehitters = players.sort_values(by = 'Batting Strike Rate' , ascending=False)

        #-----------------------------------------------------------------------------------------------------------------------#
        ##TOP 5 BOWLING ECONOMY-
        top5bowlingeco = players.sort_values(by = 'BOWLING Economy' , ascending=False)

        #-----------------------------------------------------------------------------------------------------------------------#
        print("1. Top 5 Run Scorers")
        print("2. Top 5 Wicket Takers")
        print("3. Top 5 Strike Hitters")
        print("4. Top 5 Bowling Eco")
        print("5. Back to main menu")
        print("Exit")
        print()

        #-----------------------------------------------------------------------------------------------------------------------#
        firstChoice=int(input("Enter Your Choice-"))
        if(firstChoice==1):
            print("Top 5 Run Scorers")
            print(top5runscorers.head(5))

            #Graph-
            import matplotlib.pyplot as plt
            import numpy as np
            
            runscorer=np.array(top5runscorers[" Sai Sudharshan "," Suryakumar Yadav "," Virat Kohli "," Shubhman Gill "," Shreyash Iyer "])
            runs=np.array(runs[486,427,454,417,345])

            plt.bar(runscorer,runs)
            plt.show()

        #-----------------------------------------------------------------------------------------------------------------------#
        elif(firstChoice==2):
            print("Top 5 Wicket Takers")
            print(top5wickettakers.head(5))

            #Graph-
            import matplotlib.pyplot as plt
            import numpy as np

            wickettaker=np.array([" Prasidh Krishna "," Hazlewood "," Trent Boult "," Arshdeep Singh "," R Sai Kishore "])
            wickets=np.array([25,22,22,21,19])

            plt.bar(wickettaker,wickets)
            plt.show()

        #-----------------------------------------------------------------------------------------------------------------------#
        elif(firstChoice==3):
            print("Top 5 Strike Hitters")
            print(top5strikehitters.head(5))

            #Graph-
            import matplotlib.pyplot as plt
            import numpy as np

            strikehitter=np.array([" Romario Shepherd "," Tim David "," Jonny Bairstow "," Naman Dhir "," Priyansh Arya "])
            strike_rate=np.array([291.666667,185.148515,184.782609,182.608696,179.245283])

            plt.bar(strikehitter,strike_rate)
            plt.show()

        #-----------------------------------------------------------------------------------------------------------------------#
        elif(firstChoice==4):
            print("Top 5 Bowling Eco")
            print(top5bowlingeco.head(5))

            #Graph-
            import matplotlib.pyplot as plt
            import numpy as np

            bowlingeconomy=np.array([" Romario Shepherd "," Arshad Khan "," Azmatullah Omarzai "," Hardik Pandya "," Yash Dayal "])
            bowlers=np.array([10.785714,10.333333,10.333333,9.771429,9.591837])

            plt.bar(bowlingeconomy,bowlers)
            plt.show()

        #-----------------------------------------------------------------------------------------------------------------------#
        elif(firstChoice==5):
            print("Back to main menu")
            print("1. Top 5 Run Scorers")
            print("2. Top 5 Wicket Takers")
            print("3. Top 5 Strike Hitters")
            print("4. Top 5 Bowling Eco")
            print("5. Back to main menu")
            print("Exit")
            firstChoice=int(input("Enter Your Choice-"))
            print()

        #-----------------------------------------------------------------------------------------------------------------------#
        elif(firstChoice==6):
            print("System Closed Successfully")

        #-----------------------------------------------------------------------------------------------------------------------#
else:
    print("Invalid input:Enter the 

    elif(firstChoice==4):
        ## ROI - Ritesh
        print("ROI (Return on investment)")

        print("1. Auction Summary ")
        print("2. Player wise ROI table ")
        print("3. Top 5 ROI Players ")
        print("4. Worst 5 ROI Players")
        print("5. Back to main menu")
        print("6. Exit")

        print()

    elif(firstChoice==5):
        ## Exit
        print("System Closed Succesfully")


    else:
        print("Invalid input: Enter the index as choice")
