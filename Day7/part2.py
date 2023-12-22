# same logic as part1. created different possible cases.

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(hands_and_bids))

def is_high_card(hand):
    counts = [hand.count(card) for card in set(hand)]
    if sorted(counts) == [1, 1, 1, 1, 1] and 'J' not in hand:
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_high_card(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+1, int(sorted_bids[i]))
    sum7 += (i+1)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ---------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 117) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [1, 1, 1, 2] and 'J' not in hand) or (sorted(counts) == [1, 1, 1, 1, 1] and hand.count('J') == 1):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+117, int(sorted_bids[i]))
    sum7 += (i+117)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# --------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 329) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [1, 2, 2] and 'J' not in hand):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+329, int(sorted_bids[i]))
    sum7 += (i+329)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# -----------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 468) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [1, 1, 1, 2] and 'J' in hand) or (sorted(counts) == [1, 1, 3] and 'J' not in hand):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+468, int(sorted_bids[i]))
    sum7 += (i+468)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ----------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 700) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [1, 2, 2] and hand.count("J") == 1) or (sorted(counts) == [2, 3] and 'J' not in hand):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+700, int(sorted_bids[i]))
    sum7 += (i+700)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ---------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 817) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [1, 4] and 'J' not in hand) or (sorted(counts) == [1, 1, 3] and 'J' in hand) or (sorted(counts) == [1, 2, 2] and hand.count('J') == 2):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+817, int(sorted_bids[i]))
    sum7 += (i+817)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ----------

def get_rank(hand, hierarchy="J23456789TQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 973) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    if (sorted(counts) == [5]) or (sorted(counts) == [1, 4] and 'J' in hand) or (sorted(counts) == [2, 3] and 'J' in hand):
        return True

# Read hands and bids from the text file
with open(r"input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+973, int(sorted_bids[i]))
    sum7 += (i+973)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")
