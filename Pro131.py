import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")
df["Radius"] = df["Radius"].fillna(0)
df["Mass"] = df["Mass"].fillna(0)

radius = df["Radius"].to_list()
mass = df["Mass"].to_list()

gravity = []
def convert_to_SI(radius,mass):
  for i in range(0,len(radius)-1):
    radius[i] = radius[i]*6.957e+8 
    mass[i] = float(mass[i])*1.989e+30

convert_to_SI(radius,mass)

def calculate_gravity(radius,mass):
  G = 6.674e-11
  for index in range(0,len(mass)):
    if radius[index] == 0:
      g = 0
    else:
      g = G*float(mass[index])/radius[index]**2
    gravity.append(g)

calculate_gravity(radius,mass)

df ["Gravity"] = gravity

print(df["Gravity"])

#file = open("star_gravity.csv", "w+", newline ="")
#with file: 
  #write = csv.writer(file)
 # write.writerow(df["Gravity"])

df.to_csv("star_gravity.csv", index = False)
