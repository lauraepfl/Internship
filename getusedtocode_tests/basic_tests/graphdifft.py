import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = open('completedata.txt', 'r') 	#download les data

#Donnes temps 1
df1 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=36, nrows=35) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df1_selection = df1.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df1_selection.head()) 

x1 = df1.iloc[:,1].values #x
d1 = df1.iloc[:,2].values #density
u1 = df1.iloc[:,3].values #velocity
p1 = df1.iloc[:,4].values #pressure

#Donnes temps 2
df2 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=310, nrows=60) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df2_selection = df2.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df2_selection.head()) 

x2 = df2.iloc[:,1].values #x
d2 = df2.iloc[:,2].values #density
u2 = df2.iloc[:,3].values #velocity
p2 = df2.iloc[:,4].values #pressure

#Donnes temps 3
df3 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=518, nrows=59) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df3_selection = df3.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df3_selection.head()) 

x3 = df3.iloc[:,1].values #x
d3 = df3.iloc[:,2].values #density
u3 = df3.iloc[:,3].values #velocity
p3 = df3.iloc[:,4].values #pressure

#Donnes temps 4
df4 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=803, nrows=61) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df4_selection = df4.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
print(df4_selection.head()) 

x4 = df4.iloc[:,1].values #x
d4 = df4.iloc[:,2].values #density
u4 = df4.iloc[:,3].values #velocity
p4 = df4.iloc[:,4].values #pressure

#Donnes temps 5
df5 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=1220, nrows=63) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df5_selection = df5.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
#print(df5_selection.head()) 

x5 = df5.iloc[:,1].values #x
d5 = df5.iloc[:,2].values #density
u5 = df5.iloc[:,3].values #velocity
p5 = df5.iloc[:,4].values #pressure

#Donnes temps 6
df6 = pd.read_csv("completedata.txt", delim_whitespace=True, skiprows=1821, nrows=65) 	#  sep=´type de separation des data´ skiprows=1821, nrows=65 selectionne les data qui nous interessent ( depuis ligne 1822 les 65 suivantes)

df6_selection = df6.iloc[:, [1, 2, 3, 4]]		#selectionne les colonnes 2345
#print(df6_selection.head()) 

x6 = df6.iloc[:,1].values #x
d6 = df6.iloc[:,2].values #density
u6 = df6.iloc[:,3].values #velocity
p6 = df6.iloc[:,4].values #pressure



############################################## GRAPHS ##########################################################
# Création du graphique
plt.plot(x1, d1, marker='x', linestyle='-',label="t1")
plt.plot(x2, d2, marker='x', linestyle='-', label="t2")
plt.plot(x3, d3, marker='x', linestyle='-', label="t3")
plt.plot(x4, d4, marker='x', linestyle='-', label="t4")
plt.plot(x5, d5, marker='x', linestyle='-', label="t5")
plt.plot(x6, d6, marker='x', linestyle='-',  label="t6")



# Personnalisation
plt.xlabel("x")
plt.ylabel("Density")
#plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.plot(x1, u1, marker='x', linestyle='-',  label="t1")
plt.plot(x2, u2, marker='x', linestyle='-',  label="t2")
plt.plot(x3, u3, marker='x', linestyle='-', label="t3")
plt.plot(x4, u4, marker='x', linestyle='-', label="t4")
plt.plot(x5, u5, marker='x', linestyle='-', label="t5")
plt.plot(x6, u6, marker='x', linestyle='-',  label="t6")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Velocity")
plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()

# Création du graphique
plt.loglog(x1, p1, marker='x', linestyle='-', label="t1")
plt.plot(x2, p2, marker='x', linestyle='-',  label="t2")
plt.plot(x3, p3, marker='x', linestyle='-',  label="t3")
plt.plot(x4, p4, marker='x', linestyle='-',  label="t4")
plt.plot(x5, p5, marker='x', linestyle='-',  label="t5")
plt.plot(x6, p6, marker='x', linestyle='-',  label="t6")

# Personnalisation
plt.xlabel("x")
plt.ylabel("Pressure")
plt.title("Graphique de données XY")
plt.legend()
plt.grid()

# Affichage
plt.show()
