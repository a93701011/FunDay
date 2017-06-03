# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    a, b = direction
    if x+a < 0 or y+b > 9:
        hp -= 5
    else:
        x = x + a
        y = y + b 
    print(( x, y, hp))
	
move((0, 9, 5), (0, 1))