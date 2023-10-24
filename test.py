play_order=[{"RR": 2,"RP": 3,"RS": 1,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0,}]
opponent_history = []
opponent_history.append("P")


my_history = "SR"
last_two = "".join(my_history[-2:])
if len(last_two) == 2:
    play_order[0][last_two] += 1

potential_plays = [
    my_history[-1] + "R",
    my_history[-1] + "P",
    my_history[-1] + "S",
]
print(potential_plays)
sub_order = {
    k: play_order[0][k]
    for k in potential_plays if k in play_order[0]
}
print(sub_order)

prediction = max(sub_order, key=sub_order.get)[-1:]
