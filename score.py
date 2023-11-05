import numpy as np
import matplotlib.pyplot as plt

player_stats = {
    "Collin Q.": {"GPG": 1.77},
    "Teddy B.": {"GPG": 3.76},
    "Graham H.": {"GPG": 1.84},
    "Hawthorne": {"GPG": 1.67},
    "Ryan K.": {"GPG": 2.18},
    "Andy": {"GPG": 2.57},
    "Anthony W.": {"GPG": 3.2},
    "Ben B.": {"GPG": 3},
    "Colin Y.": {"GPG": 4},
    "Trevor P.": {"GPG": 2.67},
}

# Rating Cut-offs for GPG
range_40 = 0
range_50 = 0.5
range_60 = 1
range_70 = 1.5
range_80 = 2
range_90 = 2.5
range_100 = 3

for player, stats in player_stats.items():
    gpg = stats.get("GPG", 0) 
    if gpg == None: 
        gpg = 0
    if gpg == range_40:
        score = 40
    if gpg >= range_50:
        score = 50
    if gpg >= range_60:
        score = 60
    if gpg >= range_70:
        score = 70
    if gpg >= range_80:
        score = 80
    if gpg >= range_90:
        score = 90
    if gpg > range_100:
        score = 100
    player_stats[player]["Rating"] = round(score, 2) 
    
    print(f"{player}: Cosmetic Rating = {round(score, 2)}")

print("Trade 'value' scores")
print("*******************\n")

# Trade scores
ts1 = 70
ts2 = 80
ts3 = 90
ts4 = 100

# Quartile Ranges
iqr_0 = 1.67
iqr_1 = 1.925
iqr_2 = 2.62
iqr_3 = 3.15
iqr_4 = 4

for player, stats in player_stats.items():
    gpg = stats.get("GPG", 0) 
    if gpg == None: 
        gpg = 0
    if gpg >= iqr_0 or gpg == 0:
        trade_score = ts1
    if gpg >= iqr_1:
        trade_score = ts2
    if gpg >= iqr_2:
        trade_score = ts3
    if gpg >= iqr_3:
        trade_score = ts4

    player_stats[player]["Trade-Score"] = round(trade_score, 2) 
    
    print(f"{player}: Trade-Score = {round(trade_score, 2)}")

players = list(player_stats.keys())
ratings = [stats["Rating"] for stats in player_stats.values()]
trade_scores = [stats["Trade-Score"] for stats in player_stats.values()]

plt.figure(figsize=(10, 6))

# Plot the Rating
plt.scatter(players, ratings, label="Rating", color="b", marker="o")

# Plot the Trade-Score
plt.scatter(players, trade_scores, label="Trade-Score", color="r", marker="x")

plt.xlabel("Players")
plt.ylabel("Rating and Trade-Score")
plt.title("Rating and Trade-Score for Players")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.grid(True)

plt.show()