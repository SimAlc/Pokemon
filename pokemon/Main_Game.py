# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:09:41 2022

@author: c2026560
"""

from ast import Break
from Mons import mons as MonsDict
import random

def main():                     #main menu
    PlayerMon=""
    while True:         #loop until exit command used
        Choice=0
        print("""~~~~~POKEMON~~~~~
        ~~~~~main menu~~~~~
        1. Select your pokemon
        2. Battle
        3. exit""")
        try:
            Choice=int(input("Select an option by giving its number: "))
        except ValueError:
            print("Your input must be an integer!")
        print("")
        if Choice==1:
            PlayerMon=pick()
            print(PlayerMon["Name"])
        elif Choice==2:
            if PlayerMon=="":
                print("Please select your pokemon first!")
            elif PlayerMon["HP"]<=0:
                print("Your pokemon has no HP!")
            else:
                BattleMenu(PlayerMon)
        elif Choice==3:
            exit()

def pick():
    x=1
    print("Starting mons:")
    mons=list(MonsDict.keys())
    for i in mons:
        print(str(x) + ":" ,i)
        x=x+1
    Choice=int(input("Choose your starting mon by giving their number: "))
    PlayerMon=dict.copy(MonsDict[mons[Choice-1]])
    return(PlayerMon)

def RandMon():
    x=random.randint(1, len(MonsDict.keys()))
    EnemyMon=list(MonsDict.keys())[x-1]
    EnemyMon=dict.copy(MonsDict[EnemyMon])
    return(EnemyMon)

def BattleMenu(PlayerMon):                      #Responsible showing user battle info and letting them select battle inputs
    EnemyMon=RandMon()                          #select enemy pokemon
    print("A wild", EnemyMon["Name"], "has appeared!")
    
    while EnemyMon["HP"] > 0 and PlayerMon["HP"] > 0:           #loop until one pokemon has run out of health
                                                                #battle layout and mon info
        print("")
        print("Opponent:")
        print(EnemyMon["Name"])
        print(int(EnemyMon["HP"]))
        print("")
        print("~~~~~~~~~~~~~~~~~~~")
        print("")
        print("Player:")
        print(PlayerMon["Name"])
        print(int(PlayerMon["HP"]))
        print("")
        print("Moves:")

        y=0                             #used for iterating dict keys
        for i in PlayerMon["Moves"]:    #display available moves
            y+=1
            print(str(y) + ".", i["Name"])

        Choice=int(input("Choose your move by pressing entering its number: "))         #take user move selection
        PlayerMove=PlayerMon["Moves"][Choice-1]
        x=random.randint(0, 3)                                                          #select random move for enemy mon
        EnemyMove=EnemyMon["Moves"][x] 
        PlayerMon,EnemyMon=BattleCalc(PlayerMon,PlayerMove,EnemyMon,EnemyMove)          #move to damage calculations
        
    if PlayerMon["HP"]<=0:
        print("Your", PlayerMon["Name"], "feinted!")
    elif EnemyMon["HP"]<=0:
        print("Enenmy", EnemyMon["Name"], "feinted!")
    print("")

def BattleCalc(PlayerMon,PlayerMove,EnemyMon,EnemyMove):
    print("")

    PlayerSpeed=(PlayerMon["Speed"]/100)*PlayerMove["Speed"]        #decide on pokemon move order, pokemon speed as percentage of move speed
    EnemySpeed=(EnemyMon["Speed"]/100)*EnemyMove["Speed"]
    if PlayerSpeed==EnemySpeed:                                     #flip a coin in case of speed tie
        flip=random.randint(1,2)
        if flip==1:
            PlayerSpeed+=1
        else:
            EnemySpeed+=1

    PlayerHit=False       #default miss
    EnemyHit=False    

    if random.randint(1,100) < PlayerMove["Accuracy"]:                      #check if player hit
        PlayerHit=True
        PlayerDamage=PlayerMove["Damage"]*(PlayerMon["Attack"]/100)         #calculate damage with mon attack
        Reduction=round((PlayerDamage/100)*EnemyMon["Defence"])             #calculate damage reduction with enemy defence
        PlayerDamage-=Reduction                                             #calculate damage after reduction

    if random.randint(1,100) < EnemyMove["Accuracy"]:                       #check if enemy hit
        EnemyHit=True
        EnemyDamage=EnemyMove["Damage"]*(EnemyMon["Attack"]/100)            #calculate damage with mon attack
        Reduction=round((EnemyDamage/100)*PlayerMon["Defence"])             #calculate damage reduction with enemy defence
        EnemyDamage-=Reduction                                              #calculate damage after reduction


    if PlayerSpeed > EnemySpeed:                        #damage calculation if player goes first

        print("Your", PlayerMon["Name"], "used", PlayerMove["Name"] + "!")
        if PlayerHit==True: 
            print("Dealt", int(PlayerDamage))
            EnemyMon["HP"]-=PlayerDamage
        else:
            print("Missed!")

        
        if EnemyHit==True and EnemyMon["HP"]>0:
            print("Enemy", EnemyMon["Name"], "used", EnemyMove["Name"] + "!")
            print("Dealt", int(EnemyDamage))
            PlayerMon["HP"]-=EnemyDamage
        elif EnemyMon["HP"]>0:
            print("Enemy", EnemyMon["Name"], "used", EnemyMove["Name"] + "!")
            print("Missed!")

    else:                                           #damage calculation if enemy goes first

        print("Enemy", EnemyMon["Name"], "used", EnemyMove["Name"] + "!")
        if EnemyHit==True:          
            print("Dealt", int(EnemyDamage))
            PlayerMon["HP"]-=EnemyDamage
        else:
            print("Missed!")
        
        
        if PlayerHit==True and PlayerMon["HP"]>0:
            print("Your", PlayerMon["Name"], "used", PlayerMove["Name"] + "!")
            print("Dealt", int(PlayerDamage))
            EnemyMon["HP"]-=PlayerDamage
        elif PlayerMon["HP"]>0:
            print("Your", PlayerMon["Name"], "used", PlayerMove["Name"] + "!")
            print("Missed!")
        
    return(PlayerMon,EnemyMon)
    

main()