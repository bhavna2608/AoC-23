# i ran the code one-by-one to find different ranks for different types of cards and added it all later:

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(hands_and_bids))

def is_high_card(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [1, 1, 1, 1, 1]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
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

# -------

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 196) for i, (_, bid) in enumerate(hands_and_bids))

def is_one_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [1, 1, 1, 2]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_one_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+196, int(sorted_bids[i]))
    sum7 += (i+196)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# -------

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 440) for i, (_, bid) in enumerate(hands_and_bids))

def is_two_pair(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [1, 2, 2]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_two_pair(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+440, int(sorted_bids[i]))
    sum7 += (i+440)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ------

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 627) for i, (_, bid) in enumerate(hands_and_bids))

def is_three_of_a_kind(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [1, 1, 3]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_three_of_a_kind(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+627, int(sorted_bids[i]))
    sum7 += (i+627)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# -------

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def total_winnings(hands_and_bids):
    hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]), reverse=False)
    return sum(int(bid) * (i + 806) for i, (_, bid) in enumerate(hands_and_bids))

def is_full_house(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [2, 3]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Four of a Kind
filtered_hands_and_bids = [item for item in hands_and_bids if is_full_house(item[0])]
print(len(filtered_hands_and_bids))

filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+806, int(sorted_bids[i]))
    sum7 += (i+806)*int(sorted_bids[i])
    
print(sum7)

# Calculate total winnings for filtered hands
result = total_winnings(filtered_hands_and_bids)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")

print(f"Total Winnings for Filtered Hands: {result}")

# ----------

def get_rank(hand, hierarchy="23456789TJQKA"):
    return [hierarchy.index(card) for card in hand]

def is_full_house(hand):
    counts = [hand.count(card) for card in set(hand)]
    return sorted(counts) == [1, 4]

# Read hands and bids from the text file
with open(r"C:\Users\jaysw\OneDrive\Desktop\input.txt", "r") as file:
    hands_and_bids = [line.strip().split() for line in file]

# Filter hands with Full House
filtered_hands_and_bids = [item for item in hands_and_bids if is_full_house(item[0])]

# Sort filtered hands by hierarchy
filtered_hands_and_bids.sort(key=lambda x: (get_rank(x[0]), x[0]))

# Create a list of bids sorted by hierarchy
sorted_bids = [bid for _, bid in filtered_hands_and_bids]
sum7 = 0
for i in range(len(sorted_bids)):
    print(i+906, int(sorted_bids[i]))
    sum7 += (i+906)*int(sorted_bids[i])
    
print(sum7)

# Print sorted hands and total winnings
for hand, bid in filtered_hands_and_bids:
    print(f"Hand: {hand}, Bid: {bid}")
