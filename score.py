import numpy as np
import matplotlib.pyplot as plt

# APM -> Average Plus Minus
# GPG -> Goals per Game
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

desired_mean = 85
desired_std = (100-desired_mean) // 3

gpg_values = [stats["GPG"] for stats in player_stats.values() if stats["GPG"] > 0]
gpg_values.sort()

mean = np.mean(gpg_values)
#print(mean)
std = np.std(gpg_values)
#print(std)
x = np.linspace(0, mean + 3*std, 100)
y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std)**2)
plt.figure(figsize=(5, 5))
#plt.scatter(range(0, len(gpg_values)), gpg_values, color='red', label='Data')
plt.plot(x, y, color='blue')
plt.xlabel('GPG')
plt.ylabel('Probability')
plt.title('GPG Gaussian Distribution')
#plt.show()


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
        trade_score = desired_mean - (2 * desired_std)
    if gpg >= neg2std:
        trade_score = desired_mean - desired_std
    if gpg >= neg1std:
        trade_score = desired_mean
    if gpg >= mean:
        trade_score = desired_mean + desired_std
    if gpg >= pos1std:
        trade_score = desired_mean + (2 * desired_std)

    # Skaters:
    if player not in goalie_names:
        if apm > 0:
            trade_score += apm // 1
        elif apm < 0:
            trade_score -= apm // 1

    # Goalies:
    else:
        if apm > 0:
            trade_score = desired_mean + (2 * desired_std)
        elif apm > 4:
            trade_score = desired_mean + (2 * desired_std)
        elif apm > 7:
            trade_score = 100
        elif apm < 0 and apm > -4:
            trade_score = desired_mean
        elif apm < -4 and apm > -7:
            trade_score = desired_mean - desired_std
        elif apm < -7:
            trade_score = desired_mean - (2 * desired_std)

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
#plt.show()


# Plot the Gaussian for trade scores
mean_score = np.mean(sorted_trade_scores)
std_score = np.std(sorted_trade_scores)
x_score = np.linspace(min(sorted_trade_scores), max(sorted_trade_scores), 100)
bin_width = x_score[1] - x_score[0]
y_score = (1 / (std_score * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_score - mean_score) / std_score)**2)
y_score = y_score * len(sorted_trade_scores) * bin_width

plt.figure(figsize=(5, 5))
plt.plot(x_score, y_score, color='red')
plt.xlabel('PPS')
plt.ylabel('Probability')
plt.title('PPS Gaussian Distribution')
#plt.show()

for key, entry in player_stats.items():
    print(key, '->', entry)
print(mean_score)
