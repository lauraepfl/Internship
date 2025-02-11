import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file = open('nlevel3.txt', 'r') 	#download les data

#paramètres de base : boxlenght = 0.5
df1 = pd.read_csv("nlevel6.txt", delim_whitespace=True, skiprows=526, nrows = 64)

df1_selection = df1.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df1_selection.head()) 

x1 = df1.iloc[:,1].values #x
d1 = df1.iloc[:,2].values #density
u1 = df1.iloc[:,3].values #velocity
p1 = df1.iloc[:,4].values #pressure

#Nouveau paramètre : boxlenght = 1
df2 = pd.read_csv("boxlen1.txt", delim_whitespace=True, skiprows=463, nrows=64) 	

df2_selection = df2.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df2_selection.head()) 

x2 = df2.iloc[:,1].values #x
d2 = df2.iloc[:,2].values #density
u2 = df2.iloc[:,3].values #velocity
p2 = df2.iloc[:,4].values #pressure

#Nouveau paramètre : boxlenght = 0.1
df3 = pd.read_csv("boxlen0.1.txt", delim_whitespace=True, skiprows=11916, nrows=90) 	

df3_selection = df3.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df3_selection.head()) 

x3 = df3.iloc[:,1].values #x
d3 = df3.iloc[:,2].values #density
u3 = df3.iloc[:,3].values #velocity
p3 = df3.iloc[:,4].values #pressure

#Nouveau paramètre : boxlenght = 10
df4 = pd.read_csv("boxlen10.txt", delim_whitespace=True, skiprows=256, nrows=62) 	

df4_selection = df4.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df4_selection.head()) 

x4 = df4.iloc[:,1].values #x
d4 = df4.iloc[:,2].values #density
u4 = df4.iloc[:,3].values #velocity
p4 = df4.iloc[:,4].values #pressure



############################################## GRAPHS ##########################################################
# Création du graphique
plt.plot(x1, d1, marker='x', linestyle='-',label="boxlenght = 0.5")
plt.plot(x2, d2, marker='x', linestyle='-', label="boxlenght = 1")
plt.plot(x3, d3, marker='x', linestyle='-', label="boxlenght = 0.1")
plt.plot(x4, d4, marker='x', linestyle='-', label="boxlenght = 10")






# Personnalisation
plt.xlabel("x")
plt.ylabel("Density")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1, u1, marker='x', linestyle='-',label= "boxlenght = 0.5")
plt.plot(x2, u2, marker='x', linestyle='-', label="boxlenght = 1")
plt.plot(x3, u3, marker='x', linestyle='-', label="boxlenght = 0.1")
plt.plot(x4, u4, marker='x', linestyle='-', label="boxlenght = 10")


# Personnalisation
plt.xlabel("x")
plt.ylabel("Velocity")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1, p1, marker='x', linestyle='-',label="boxlenght =0.5")
plt.plot(x2, p2, marker='x', linestyle='-', label="boxlenght = 1")
plt.plot(x3, p3, marker='x', linestyle='-', label="boxlenght = 0.1")
plt.plot(x4, p4, marker='x', linestyle='-', label="boxlenght = 10")


# Personnalisation
plt.xlabel("x")
plt.ylabel("Pressure")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()
