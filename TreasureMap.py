row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1,row2,row3]
position = input("Where do you want me to insert the treasure \n")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")