#Volume of a rectangular prism
def Rectangular_volume(L,W,H):
    return L*W*H
L = int(input(" enter an integer that represents Length: "))
W = int(input(" enter an integer that represents Width: "))
H = int(input("enter an integer that represents Height: "))
print("Volume is " +str(Rectangular_volume(L,W,H)))
