### Rate Based Winnings (ACTIVE)
# BUY IN: 30$
# The winning team will recieve their money back

## Costs
# Jerseys

# 




## General Info
rates = [15,20,25,30,35,40] # regi. fee
income = []  # income at diff rates
payout = []
money_after_payout = []

i_track = 0
skaters_per_team = [5] # skaters per team (not including goalie)
num_teams = 4

for rate in rates:
    #print(f'Rate: {rate}$   Players: {skaters_per_team[0] * num_teams}')

    ## Find Income
    money_per_team = rate * skaters_per_team[0]
    payout.append(money_per_team)
    income.append(money_per_team * num_teams)

    ## Winning Team Calc.
    money_after_payout.append(income[i_track] - money_per_team)

    i_track += 1
print(f' Rates              : {rates} $')
print(f'\n Payout Cost        : {payout}')
print(f'\n Money After Payout : {money_after_payout} left over')

