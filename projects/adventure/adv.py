from room import Room
from player import Player
from world import World

import random
from ast import literal_eval # Might NOT need it

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"   # **   <-  Main one

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# For visited rooms
visited = {}
# Keep track of the paths taken, so we can return back
return_path = []
# Opposite directions
opp_dirs = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# initialize current_room, with the first_room
current_room = player.current_room.id
# Add it to visited, with an empty dictionary
visited[current_room] = {}

# Get all available exits from current_room
available_exits = player.current_room.get_exits()

# Add each direction as a key to current_room,
# with "?" as it's value
for direction in available_exits:
    room = visited[current_room]
    room[direction] = "?"

return_path.append(current_room)

# Go to the first room that is available
for direction in ['n', 'e', 's', 'w']:
    room = visited[current_room]

    # If that direction is available, but not visited yet
    if room[direction] == "?":
        # Add it to traversal_path
        traversal_path.append(direction)  # traversal_path = ["n"]
        # Move user to that room
        player.travel(direction)
        # Stop searching for available rooms
        break

# Try to visit the rest of the rooms
while len(visited) < len(room_graph):
    # For each room

    # Set current_room 
    # as the player's current_room id
    current_room = player.current_room.id
    # Get all available exits of current_room
    current_exits = player.current_room.get_exits()

    # if room_id is not in visited
    if current_room not in visited:
        # add it to visited, with an empty dictionary
        visited[current_room] = {}
        
        # Add each direction as a key to current_room,
        # with "?" as it's value
        for direction in current_exits:
            room = visited[current_room]
            room[direction] = "?"
            # ^^   visited[current_room] = {"n" : "?"}
            
    # get the last move made, from traversal_path
    last_move =  traversal_path[-1]
    # Get it's opposite
    opp_move = opp_dirs[last_move]
    
    # if directions for previous is still "?"
    if visited[current_room][opp_move] == "?":
        # add current room as last room, direction moved
        visited[return_path[-1]][last_move] = current_room
        # add last room as current room, opposite direction
        visited[current_room][opp_move] = return_path[-1]
    
    # if any directions for current_room are "?" 
    if "?" in visited[current_room].values():
        # for each available exit
        for direction in current_exits:
            room = visited[current_room]
            
            if room[direction] != None and room[direction] == '?':
                # add current room id to path
                return_path.append(current_room)
                # store direction to move in traversal path
                traversal_path.append(direction)
                # Move player to that room
                player.travel(direction)
                # Stop looking for other rooms
                break

    # if all exits visited:
    elif len(visited) < len(room_graph):
        # if last room id on path is this room id, delete it
        if return_path[-1] == current_room:
            del return_path[-1]

        for direction in current_exits:
            room = visited[current_room]
            # find last room on path among directions
            if room[direction] != None and room[direction] == return_path[-1]:
                # add direction to traversal path
                traversal_path.append(direction)
                player.travel(direction)
                break

    #print(traversal_path)
    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#get_all_social_paths(world.starting_room)

#######
# UNCOMMENT TO WALK AROUND
#######
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
