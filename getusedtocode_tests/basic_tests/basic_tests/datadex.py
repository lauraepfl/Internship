import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = open('data.txt', 'r') 	#download les data
df = pd.read_csv("data.txt", delim_whitespace=True, skiprows=1) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df_selection = df.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
#print(df_selection.head()) 


# Données
x = df.iloc[:,1] #x
d = df.iloc[:,2] #density
u = df.iloc[:,3] #velocity
p = df.iloc[:,4] #pressure


# Création du graphique
plt.plot(x, d, marker='x', linestyle='-', color='b', label="d(x)")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Density")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x, u, marker='x', linestyle='-', color='r', label="u(x)")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Velocity")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x, p, marker='x', linestyle='-', color='m', label="p(x)")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Pressure")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()
