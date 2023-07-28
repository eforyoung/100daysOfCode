
direction = input("What is the direction i.e. either left or right \n")
lower_case_direction = direction.lower()
if lower_case_direction == "left":
     action = input("What is the next action i.e. either swim or wait\n")
     lower_case_action = action.lower()
     if lower_case_action == "wait":
          door_color = input("What is the door color i.e. either blue, red or yellow \n")
          lower_case_color = door_color.lower()
          if lower_case_color == "blue":
              print("Game Over")
          elif lower_case_color == "red":
              print("Game Over")
          else:
              print("You Win!!!")
     else:
         print("Game Over")
else:
    print("Game Over")
    

