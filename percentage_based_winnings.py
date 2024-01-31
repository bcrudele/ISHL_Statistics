### But where is the money actually going?
    
### We actually want:
# A functional and robust prize pool
# Profit for materials + website funding
    
# referees to get paid per-game,   6 weeks (2x per week = 12 games) +
# post-season refs to get paid pg, 2 weeks (4x single-elim loser-bracket) 
# total of 16 reffed games

## General Info
rate = 35              # registration fee
skaters_per_team = [6] # skaters per team (includes goalie)
num_teams = 4

## Find Income
income = rate * skaters_per_team[0] * num_teams
print(f'Income: {income}')

## Find Prize Pool
prize_pool_rate = 0.6
prize_pool_total = prize_pool_rate * income
print(f'Price Pool: {prize_pool_total}')

## Pool Division
first_place_percent = 0.75
second_place_percent = 0.25
third_place_percent = 0

first_place = first_place_percent * prize_pool_total
second_place = second_place_percent * prize_pool_total
third_place = third_place_percent * prize_pool_total

print(f'1st Place: {first_place/skaters_per_team[0]}')
print(f'2nd Place: {second_place/skaters_per_team[0]}')
print(f'3rd Place: {third_place/skaters_per_team[0]}')

## Find Excess
excess = income - prize_pool_total
print(f'Excess {excess}')

## Find Ref Cost
ref_rate = 10           # $/hr
ref_games = 16          # reg/post season games
ref_cost = ref_rate * ref_games

print(f'Ref Cost: {ref_cost}')

## Find Left-over for Supplies
excess -= ref_cost
print(f'Materials & Extra {excess}')

## If there was a goalie discount...
g_discount = 15 # dollars off
print(f'Materials & Extra (after discount) {excess - (num_teams * g_discount)}')