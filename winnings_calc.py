import matplotlib.pyplot as plt

player_ct = 25                          # league players
ppt = 4                                 # players per team (DO NOT INCLUDE GOALIE THEY ARE FREE)
min_teams = 3                           # minimum teams in the league
league_cut = 0.1                        # %
league_profit_desired = 100             # threshold profit for league
desired_gamble = 3                     # Multiple payout (ie. 3x)
desired_gamble_2 = 2
desired_gamble_3 = 1                    # 3rd place keeps their money

num_teams = player_ct // ppt            # max teams able to be created
paying_players = num_teams * ppt        # players active in the league
entire_team = ppt + 1                   # to include the goalie who plays for free
rates = [20,25]              # $ per player
rates_ct = len(rates)                   # number of rates testing


payout_money = []
money_collected_list = []

print(f'{paying_players} paying players from {num_teams} teams with {ppt} players per team')

plt.figure(figsize=(10, 6))

### For when ONLY the #1 team wins:

### For how many teams there are...
for teams in range(min_teams,num_teams+1):
    
    print(f"{teams} teams with {entire_team} players per team (including goalies) :\n")

    ### Each team's rate...
    for rate in range(0,rates_ct):
        money_collected = ppt * rates[rate] * teams
        money_collected_list.append(money_collected)

    #league_profit = [element * league_cut for element in money_collected_list]    # % based
    league_profit = [league_profit_desired for element in money_collected_list]    # minimum based
    #payout_money =  [element - (element * league_cut) for element in money_collected_list] # % based
    payout_money =  [element - (league_profit_desired) for element in money_collected_list]   # minimum based
    player_payout = [element / entire_team for element in payout_money]                        
    # team_1_payout = [(element * desired_gamble) / (desired_gamble+desired_gamble_2+desired_gamble_3) for element in payout_money]
    # team_2_payout = [(element * desired_gamble_2) / (desired_gamble+desired_gamble_2+desired_gamble_3) for element in payout_money]
    # team_3_payout = [(element * desired_gamble_3) / (desired_gamble+desired_gamble_2+desired_gamble_3) for element in payout_money] 
    for rate in range(0,rates_ct):
        ## 
        if ((player_payout[rate] >= rates[rate]) and (league_profit[rate] >= league_profit_desired)):
            print(f'{rates[rate]}$ rate : {money_collected_list[rate]}$')
            print(f'Money Tot.  League Profit.  Excess.    Player Winnings.    Cost.    Player Net Profit')
            print(f'{money_collected_list[rate]},           {league_profit[rate]},           {payout_money[rate]},         {round(player_payout[rate],2)},           {rates[rate]},       {round(player_payout[rate] - rates[rate],2)}\n')
            
            # print(f'Team 1 payout {team_1_payout[rate]}')
            # print(f'Team 2 payout {team_2_payout[rate]}')
            # print(f'Team 3 payout {team_3_payout[rate]}')
    money_collected_list = []

    print("#########################")

##############################