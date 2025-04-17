import numpy as np
import matplotlib.pyplot as plt 


def f(x,y,z) :
    return x**2 +y**2 +z**2 +3*x + 2*y +z

def derivation_f(x,y,z) :
    return 2*x +3,  2*y+2,  2*z+1

"""
 Initialisation des parameter 

"""
x = 1
y = 1
z = 1
learning_rate = 0.01

"""
 Calcul les Gradient 

"""

def Calcul_gradient(x,y,z,learning_rate) :
    x = x - learning_rate * derivation_f(x, y, z)[0] 
    y = y - learning_rate * derivation_f(x, y, z)[1] 
    z = z - learning_rate * derivation_f(x, y, z)[2]
    return x,y,z

new_x,new_y,new_z = Calcul_gradient(x,y,z,learning_rate)

while np.sqrt(new_x*new_x +new_y*new_y +new_z*new_z) >= 0.001 :
      print(new_x,new_y,new_z)
      new_x,new_y,new_z = Calcul_gradient(new_x,new_y,new_z,learning_rate)
    

"""
 Afficher par saisir le nombre des iterartion 
 

def affiche_iteration() :
    nbr = int(input("Donner nombre des iterations:"))
    new_x,new_y,new_z = Calcul_gradient(x,y,z,learning_rate)
    for index in range(nbr) :
        new_x,new_y,new_z = Calcul_gradient(new_x,new_y,new_z,learning_rate)
        print(new_x,new_y,new_z)
        
affiche_iteration()
"""

"""
Implementation avec Visualisation une fonction Convexe x2

"""
"""
import numpy as np
import matplotlib.pyplot as plt 

def fonction(x) :
    return x**2

def derivation_x(x) :
    return 2*x

position = (40,fonction(40))

x = np.arange(-50,50,1 )
y = fonction(x)

"""
# on passe pour tracer les gradient 

"""
learning_rate = 0.01

for _ in range(2090) :
    new_W = position[0] - learning_rate*derivation_x(position[0])
    new_y = fonction(new_W)
    position = (new_W,new_y)
    plt.plot(x, y)
    plt.scatter(position[0],position[1], color="green")
    plt.title("fonction convexe X2")
    plt.show()
    
"""