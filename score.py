import numpy as np
import matplotlib.pyplot as plt

player_stats = {
    "Jack C.": {"GPG": 0, "APM": -1.33},  
    "Collin Q.": {"GPG": 1.77, "APM": -0.42},
    "Teddy B.": {"GPG": 3.76, "APM": 0.6},
    "Karl K.": {"GPG": 0.52, "APM": 0.5},  
    "Graham H.": {"GPG": 1.84, "APM": -0.04},
    "Jimmy D.": {"GPG": 0.5, "APM": -3.17}, 
    "Hawthorne": {"GPG": 1.67, "APM": -1.11},
    "Ryan K.": {"GPG": 2.18, "APM": 0.73},
    "Andy": {"GPG": 2.57, "APM": 1.71},
    "Brandon C.": {"GPG": 1, "APM": -1.32},  
    "Anthony W.": {"GPG": 3.2, "APM": -2.4},
    "Jared P.": {"GPG": 0, "APM": 2.08},  
    "Colin Y.": {"GPG": 4, "APM": 4.8},
    "Trevor P.": {"GPG": 2.67, "APM": 5.83},
    "CJ": {"GPG": 0},  
    "Skyler D.": {"GPG": 0} 
}

goalie_names = ["Brandon C.", "Jared P.", "Jack C."]

# want mean 85
# want std 5

gpg_values = [stats["GPG"] for stats in player_stats.values() if stats["GPG"] > 0]
gpg_values.sort()

mean = np.mean(gpg_values)
std = np.std(gpg_values)

neg3std = mean - 3 * std
neg2std = mean - 2 * std
neg1std = mean - 1 * std
pos1std = mean + 1 * std
pos2std = mean + 2 * std
pos3std = mean + 3 * std

for player, stats in player_stats.items():
    gpg = stats.get("GPG", 0) 
    apm = stats.get("APM",0)
    
    if gpg == 0:
        trade_score = 75
    if gpg >= neg2std:
        trade_score = 80
    if gpg >= neg1std:
        trade_score = 85
    if gpg >= mean:
        trade_score = 90
    if gpg >= pos1std:
        trade_score = 95

    # Skaters:
    if player not in goalie_names:
        if apm > 0:
            trade_score += apm % 5 // 1
        elif apm < 0:
            trade_score -= apm % 5 // 1
    # Goalies:
    else:
        if apm > 0:
            trade_score = 95
        elif apm > 4:
            trade_score = 95
        elif apm > 7:
            trade_score = 100
        elif apm < 0 and apm > -4:
            trade_score = 85
        elif apm < -4 and apm > -7:
            trade_score = 80
        elif apm < -7:
            trade_score = 75

    player_stats[player]["Trade-Score"] = round(trade_score) 
    #print(f'{player} score -> {player_stats[player]["Trade-Score"]}')

# Sort players by trade score in descending order
sorted_players = sorted(player_stats.keys(), key=lambda player: player_stats[player]["Trade-Score"], reverse=True)
sorted_trade_scores = [player_stats[player]["Trade-Score"] for player in sorted_players]

# Plot the trade scores in descending order
plt.figure(figsize=(10, 6))
plt.barh(sorted_players, sorted_trade_scores, color='skyblue')
plt.xlabel('Trade Score')
plt.title('Trade Scores for Players (Sorted)')
plt.gca().invert_yaxis()
plt.show()