### Rate Based Winnings (ACTIVE)
# CURRENT BUY IN: 25$
# The winning team will recieve their money back 2.4x

## Costs
# Jerseys -> Iron-On-Tees
jersey_cost = 100

## General Info
rates =  [25]     # regi. fee
income = []       # income at diff rates
payout = []       # money paid for winnings
rollover = []     # money after payout + jerseys
money_after_payout = []     # money after payout
gamble_payout = 2.4 # multiplier for winnings

i_track = 0
skaters_per_team = [7] # skaters per team ( including goalie)
num_teams = 4

for rate in rates:
    #print(f'Rate: {rate}$   Players: {skaters_per_team[0] * num_teams}')

    ## Find Income
    money_per_team = rate * skaters_per_team[0]
    winners_payout = money_per_team * gamble_payout
    payout.append(winners_payout)
    income.append(money_per_team * num_teams)

    # Excess after Payout
    money_after_payout.append(income[i_track] - winners_payout)

    # Excess after Jerseys
    rollover.append(money_after_payout[i_track] - jersey_cost)
    i_track += 1

print(f'Rates              : {rates} $')
print(f'Income             : {income} $ collected')
print(f'Total Payout Cost  : {payout} $ for winning team')
print(f'Payout Per Player  : {[skater / skaters_per_team[0] for skater in payout]} $ per winning player')
print(f'Jersey Cost        :  {jersey_cost} $')
print(f'Excess             : {rollover} $')