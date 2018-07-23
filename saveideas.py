#ignore the concrete aspects of the examples
#1
import pickle

player = Player(...)
level_state = Level(...)

# saving
with open('savefile.dat', 'wb') as f:
    pickle.dump([player, level_state], f, protocol=2)

# loading
with open('savefile.dat', 'rb') as f:
    player, level_state = pickle.load(f)
    
#2: make a dictionary to store all the stats
#pickle vs json: pickle can save more crazy python objects, while json can be read in other laguages
    
#3: another save method 
import json
 #save files below
def save_file():
 #to enter a name for your file
 #if you don't want to just make it a string
    save_name = input("savename: ")
    path = 'path_to_dir{0}.json'.format(save_name)
    data = {
         'name': save_name
     }
    with open(path, 'w+') as f:
        json.dump(data, f)
 
 
def load_file():
    load_name = save_name
    path_two = 'path_to_dir{0}.json'.format(load_name)
    with open(path_two, 'r') as f:
        j = json.load(f)
        name = str(j['name'])
         
#4: pickle
import pickle

fp = '/path/to/saved/file.pkl'
with open(fp, 'wb') as f:
    pickle.dump(board, f)

#5
#https://inventwithpython.com/blog/2012/05/03/implement-a-save-game-feature-in-python-with-the-shelve-module/

#6
#save
def askSave():
    ask = input("Do you want to save?\n--> ").upper()
    if ask == "Y" or ask == "YES":
        Save = Player(PlayerIG.name) #Saves the desired class AND a chosen attribute
        pickle.dump(Save, open("Save File", "wb")) #Creates the file and puts the data into the file
 #The file doesn't have an extension because it is a binary file and makes it easier to parse. 
    elif ask == "N" or ask == "NO":
        print("Okay, maybe next time!")
        return
    else:
        print("Sorry, that does not compute with me! Please try again!")
        askSave()

#loadimport json

import json
data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
def load():
    me = pickle.load(open("Save File","rb")) #Loads the file
    me.display(Player.display) #Prints the stats out to verify the load has successfully happened
    return dragonRunFight()

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)

#7
#https://www.quora.com/How-do-you-make-a-save-file-for-a-game-written-in-Python

#8
import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
    
#9
#https://inventwithpython.com/blog/2012/05/03/implement-a-save-game-feature-in-python-with-the-shelve-module/