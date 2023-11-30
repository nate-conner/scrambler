import Golfer as g 

def example_function(input_string):
    return (input_string)

'''
Take a list of Golfer objects as an argument
Split into two teams
Return a tuple of the two teams as lists 
'''
def make_teams_example(golfers):
    num_golfers = len(golfers)
    team1 = []
    team2 = []

    for i in range(num_golfers):
        golfer = golfers[i]
        if i%2 == 0:
            team1.append(golfer)
        else:
            team2.append(golfer)

    print("\nTEAM 1:")
    for golfer in team1:
        print(golfer.name)
    
    print("\nTEAM 2:")
    for golfer in team2:
        print(golfer.name)
    
    return (team1,team2)

'''
Select all commented code that you want to uncomment
press cmd-/ to uncomment or re-comment
'''
# example_golfers = [
#     g.Golfer("Golfer 1"),
#     g.Golfer("Golfer 2"),
#     g.Golfer("Golfer 3"),
#     g.Golfer("Golfer 4"),
#     g.Golfer("Golfer 5"),
#     g.Golfer("Golfer 6")
# ]
# make_teams_example(example_golfers)