#imports
import json
import os

#gets the user's intended values and saves them
datapackpath = input("File Path> ")
datapackname = input("Name> ")
datapackversion = int(input("Version> "))
datapackdescription = input("Description> ")
#datapackmaterial = input("Material> ")
#datapackbasematerial = input("Base> ")
#maxhealth = int(input("Health Modifier> "))
#knockbackresistance = int(input("Knockback Modifier> "))
#movementspeed = int(input("Speed Modifier> "))
#attackdamage = int(input("Damage Modifier> "))
#armor = int(input("Armor Modifier> "))
#armortoughness = int(input("Armor Toughness Modifier> "))
#attackspeed = int(input("Attack Speed Modifier> "))
#luck = int(input("Luck Modifier> "))


#modifies the path to remove in text quotes
datapackname = datapackname.lower()
datapackpath = datapackpath.replace('"',"")
datapackname = datapackname.replace(' ',"_")

#makes the folder structure
datafolder = os.path.join(datapackpath,"data")
minecraftfolder = os.path.join(datafolder, "minecraft")
namespacefolder = os.path.join(datafolder, datapackname)
functionstagfolder = os.path.join(os.path.join(minecraftfolder, "tags"), "functions")
functionsfolder = os.path.join(namespacefolder,"functions")
craftfolder = os.path.join(functionsfolder, "craft")
os.mkdir(datafolder)
os.mkdir(minecraftfolder)
os.mkdir(namespacefolder)
os.mkdir(os.path.join(namespacefolder, "functions"))
os.mkdir(os.path.join(minecraftfolder, "tags"))
os.mkdir(functionstagfolder)

#mcmeta file generation
mcmeta = {"pack": {"pack_format": datapackversion,"description": datapackdescription}}
with open(os.path.join(datapackpath, "pack.mcmeta"), 'w') as outfile:
    json.dump(mcmeta, outfile)


#creates the tag files
load = {"values": [f"{datapackname}:load"]}
tick = {"values": [f"{datapackname}:tick"]}


with open(os.path.join(functionstagfolder, "load.json"), 'w') as outfile:
    json.dump(load, outfile)
with open(os.path.join(functionstagfolder, "tick.json"), 'w') as outfile:
    json.dump(load, outfile)


#create the mcfunctions
load = ""
tick = ""

with open(os.path.join(functionsfolder, "load.mcfunction"),"w") as f:
    f.write(load)
f.close()

with open(os.path.join(functionsfolder, "tick.mcfunction"),"w") as f:
    f.write(tick)
f.close()
