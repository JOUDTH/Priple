# -----------------------------------------
#------------{Priple Academy }-------------
# -- Homework Assignment #3: If statment --
# -----------------------------------------
# June 19, 2021

def convert(m,n,b):
   global y 
   y = int(n)
   global z
   z = int(b)
   global x 
   x = int(m)

def logic(x,y,z): #(x,y,z) cant be parameters because they already have values
                  #That wrong because when calling this function you must code: logic(some-value,some-value,some-value)
                  #So you're changing the values of (x,y,z) that were assigned to 'em in convert(m,n,b)
    if  x == y or x == z or y == z :  
        check = True
    else:
        check = False
    print(check)


convert("3",3,1)
logic(x,y,z) #Wrong function call
print("Done !")