# # # # # # done on reeborg
# # # # # # 1st


# # # # # # actual code
# # # # # # def turn_right():
# # # # # #     turn_left()
# # # # # #     turn_left()
# # # # # #     turn_left()


# # # # # # def jump():
# # # # # #     move()
# # # # # #     turn_left()
# # # # # #     move()
# # # # # #     turn_right()
# # # # # #     move()
# # # # # #     turn_right()
# # # # # #     move()
# # # # # #     turn_left()


# # # # # # for i in range(1, 7):
# # # # # #     jump()

# # # # # # hurdle 2
# # # # # # def turn_right():
# # # # # #      turn_left()
# # # # # #      turn_left()
# # # # # #      turn_left()


# # # # # # def jump():
# # # # # #     move()
# # # # # #     turn_left()
# # # # # #     move()
# # # # # #     turn_right()
# # # # # #     move()
# # # # # #     turn_right()
# # # # # #     move()
# # # # # #     turn_left()


# # # # # # while not at_goal():
# # # # # #     jump()

# # # # # # while not at_goal():
# # # # # #     jump()

# # # # # # hurdle 3 ....1st approach

# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()


# # # # def jump():
# # # #     turn_left()
# # # #     move()
# # # #     turn_right()
# # # #     move()
# # # #     turn_right()
# # # #     move()
# # # #     turn_left()


# # # # while not at_goal():
#     # if wall_in_front() == True:
#     #     jump()
#     # else:
#     #     move()

# # # # hurdle3 ...2nd approach
# # # while not at_goal():
# # #     if front_is_clear() == True:
# # #         move()
# # #     elif wall_in_front() == True:
# # #         jump()

# most optimal solution for any hurdle(1,2,3,4):
# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()


# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
    
#     while front_is_clear():
#         move()
#     turn_left()
        
# while not at_goal():
#     if wall_in_front() == True:
#         jump()
#     else:
#         move()
   

# final maze project :reeborgs world website
# solution:
# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()
        
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()



    