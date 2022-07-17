import math
height  = int(input("height of wall: "))
width = int(input("width of wall: "))
coverage = 5

def wall_paint(height,width,coverage):
    cans = math.ceil((height * width)/ coverage)
    # cans = round((height * width)/ coverage)
    print(f"You will need {cans} cans of paint.")

wall_paint(height,width,coverage)


# we can import math module and use math.ceil

