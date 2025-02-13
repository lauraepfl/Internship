import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#International system of units
df1 = pd.read_csv("SI.txt", delim_whitespace=True, skiprows=53, nrows = 8)

df1_selection = df1.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df1_selection.head()) 

x1 = df1.iloc[:,1].values #x
d1 = df1.iloc[:,2].values #density
u1 = df1.iloc[:,3].values #velocity
p1 = df1.iloc[:,4].values #pressure

#Astronomical units
df2 = pd.read_csv("UA.txt", delim_whitespace=True, skiprows=2275, nrows=65) 	

df2_selection = df2.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df2_selection.head()) 

x2 = df2.iloc[:,1].values #x
d2 = df2.iloc[:,2].values #density
u2 = df2.iloc[:,3].values #velocity
p2 = df2.iloc[:,4].values #pressure


############################################## GRAPHS ##########################################################
# Création du graphique
plt.plot(x1/149597870700, d1*149597870700/(1.9891e30) , marker='x', linestyle='-',label="IS")
plt.plot(x2, d2, marker='x', linestyle='-', label="AU")


# Personnalisation
plt.xlabel("x")
plt.ylabel("Density")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1/149597870700, u1/149597870700, marker='x', linestyle='-',label= "IS")
plt.plot(x2, u2, marker='x', linestyle='-', label="UA")


# Personnalisation
plt.xlabel("x")
plt.ylabel("Velocity")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1/149597870700, p1, marker='x', linestyle='-',label="IS")
plt.plot(x2, p2, marker='x', linestyle='-', label="UA")


# Personnalisation
plt.xlabel("x")
plt.ylabel("Pressure")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()
