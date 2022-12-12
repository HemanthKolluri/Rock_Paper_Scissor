import random
X=int(input("Press '0' for Rock '1' for Paper '2' for scissor : "))
Y=random.randint(0,2)
list=["Rock","Paper","Scissor"]
print("You choose :"+list[X-1])
print("Computer choose :"+list[Y-1])
if X>=3 or X<0:
    print("Invalid Input")
elif X==0 and Y==2:
    print("YOU WIN")
elif Y==0 and X==2:
    print("YOU LOSE")
elif(Y>X):
    print("YOU LOSE")
elif(X>Y):
    print("YOU WIN")
elif X==Y:
    print("DRAW")
elif X>=3 or X<0:
    print("Invalid Input")