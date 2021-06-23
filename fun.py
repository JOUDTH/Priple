# ---------------------------------------
#------------{Priple Academy }-----------
# -- Homework Assignment #2: Functions --
# ---------------------------------------
# June 18, 2021
# Belal A. Thabet

def artist(artistName):
	if artistName == "ghaba":
		print("Marwan Paplo")
	elif artistName == "Take Five":
		print("Dave Brubeck")
	elif artistName == "my love":
		print("lnez")
	elif artistName == "shape of you":
		print("Ed sheeran")
	elif artistName == "my future":
		print("Billie Eilish ")
	
def Genre(artistName):
 	if artistName == "ghaba":
 		print("pop")
 	elif artistName == "Take Five":
 		print("Jazz")
 	elif artistName == "my love":
 		print("Pop")
 	elif artistName == "shape of you":
 		print("Pop")
 	elif artistName == "my future":
 		print("Pop ")
	
def Year(artistName):
 	if artistName == "ghaba":
 		print("2021")
 	elif artistName == "Take Five":
 		print("1980")
 	elif artistName == "my love":
 		print("2019")
 	elif artistName == "shape of you":
 		print("2017")
 	elif artistName == "my future":
 		print("2020 ")
	
artist("ghaba")
Genre("ghaba")
Year("ghaba")
Genre("shape of you")
artist("shape of you")
Year("shape of you")

print("=========================")
# An additional feature to know all the information about a specific song...
def all(text): 
	x = str(input("write a song name  to see its info=>"))
	artist(x)
	Year(x)
	Genre(x)
text= 1
all(text)

print("Done !")
print("===========================")


def weight(s): # additinal Credit :)
	x = input("for inch 0 for fe 1")
	fe = 1/30.48*(s)
	inch = 1/2.45*(s)
	if x != 0:
		print(fe)
	else:
		print(inch)
weight(18)


# ghaba = {"name":"ghaba","Genre":"pop","year":2021,"artist":"marwan paplo"}
# control = {"name":"control","Genre":"rap","year":2010,"artist":"jaber soso"}
# habebe = {"name":"7abebe","Genre":"hiphop","year":2000,"artist":"ameeer"}
# myLove = {"name":"my love","Genre":"electric","year":1999,"artist":"7elme"}				