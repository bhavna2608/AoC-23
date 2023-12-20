def is_possible(game, red_limit, green_limit, blue_limit):
    # Parse the cube counts for each subset
    subsets = [subset.split() for subset in game.split(';')]
    
    # Check if the cube counts are within the limits
    for subset in subsets:
        for count, color in zip(subset[0::2], subset[1::2]):
            count = int(count)
            if (color == 'red' or color == 'red,') and count > red_limit:
                return False
            elif (color == 'green' or color == 'green,') and count > green_limit:
                return False
            elif (color == 'blue' or color == 'blue,') and count > blue_limit:
                return False
    
    return True

def possible_games_from_file(file_path, red_limit, green_limit, blue_limit):
    possible_games_ids = []
    sum3 = 0
    with open(file_path, 'r') as file:
        for record in file:
            game_id, cubes = record.split(':')
            game_id = int(game_id.strip()[5:])  # Extract the game ID
            if is_possible(cubes, red_limit, green_limit, blue_limit):
                possible_games_ids.append(game_id)
                sum3 += game_id
    return sum3, possible_games_ids

# Example usage with a file
file_path = r"input.txt"
red_limit = 12
green_limit = 13
blue_limit = 14

sum3, possible_games_ids = possible_games_from_file(file_path, red_limit, green_limit, blue_limit)

# print(f"The possible games are: {possible_games_ids}")
print(f"The sum of the IDs of those games is: {sum3}")
