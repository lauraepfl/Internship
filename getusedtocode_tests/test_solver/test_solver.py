import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file = open('nlevel3.txt', 'r') 	#download les data

#hll
df1 = pd.read_csv("hll.txt", delim_whitespace=True, skiprows=553, nrows = 63)

df1_selection = df1.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df1_selection.head()) 

x1 = df1.iloc[:,1].values #x
d1 = df1.iloc[:,2].values #density
u1 = df1.iloc[:,3].values #velocity
p1 = df1.iloc[:,4].values #pressure

#hllc
df2 = pd.read_csv("hllc.txt", delim_whitespace=True, skiprows=526, nrows=63) 	

df2_selection = df2.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df2_selection.head()) 

x2 = df2.iloc[:,1].values #x
d2 = df2.iloc[:,2].values #density
u2 = df2.iloc[:,3].values #velocity
p2 = df2.iloc[:,4].values #pressure

#llf
df3 = pd.read_csv("llf.txt", delim_whitespace=True, skiprows=532, nrows=63) 	

df3_selection = df3.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df3_selection.head()) 

x3 = df3.iloc[:,1].values #x
d3 = df3.iloc[:,2].values #density
u3 = df3.iloc[:,3].values #velocity
p3 = df3.iloc[:,4].values #pressure



############################################## GRAPHS ##########################################################
# Création du graphique
plt.plot(x1, d1, marker='x', linestyle='-',label="hll")
plt.plot(x2, d2, marker='x', linestyle='-', label="hllc")
plt.plot(x3, d3, marker='x', linestyle='-', label="llf")





# Personnalisation
plt.xlabel("x")
plt.ylabel("Density")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1, u1, marker='x', linestyle='-',label= "hll")
plt.plot(x2, u2, marker='x', linestyle='-', label="hllc")
plt.plot(x3, u3, marker='x', linestyle='-', label="llf")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Velocity")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1, p1, marker='x', linestyle='-',label="hll")
plt.plot(x2, p2, marker='x', linestyle='-', label="hllc")
plt.plot(x3, p3, marker='x', linestyle='-', label="llf")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Pressure")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()
