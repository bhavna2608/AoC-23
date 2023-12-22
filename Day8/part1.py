def follow_instructions(instruction, network):
    current_node = 'AAA'
    steps = 0

    for move in instruction:
        if move == 'L':
            current_node = network[current_node][0]
        elif move == 'R':
            current_node = network[current_node][1]

        steps += 1
        if current_node == 'ZZZ':
            print(f"Reached ZZZ on step {steps}")
            return steps
        else:
            print(f"At step {steps}, current node: {current_node}, Line: {current_node} = {network[current_node]}")

# Define the network
network = {
'MQF': ('DDG', 'LSH'),
'QJP': ('PCT', 'XKJ'),
'JXF': ('PMG', 'NBN'),
'JCK': ('QCD', 'NRG'),
  # .. and so on
}

instructions = 230*'LLLRLRLRLLRRRLRRRL' # .. and so on
steps_to_ZZZ = follow_instructions(instructions, network)

print(f"Number of steps to reach ZZZ: {steps_to_ZZZ}")
