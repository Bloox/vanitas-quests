import discord
import random

class Quest:
    
    color=["#33ff33","#ff3333"]
    def __init__(self,game_name,description:str,level:int,link=None,generator=None):
        self.name=game_name
        self.desc=description
        self.lvl=["łatwy","trudny"][level-1]
        self.level=level
        self.link=link
        self.gen=generator
    def generate(self):
        COLOR=discord.Color.from_str(self.color[self.level-1])
        content=f"Poziom: {self.lvl}\n\n"+(self.desc if self.gen==None else self.gen())
        return discord.Embed(color=COLOR,title=self.name,description=content,url=self.link)
    

def cuphead_random_eq(plane=False):
    ekwipunke = {
        'broń':(['peashooter','spread','chaser','lobber','charge','roundabout'] if plane==False else ['normalny','bomby']),
        'ulty':['I','II',"III"],
        'charmy':['HEART','coffe','smoke bomb','p. SUGAR','TWOM HEART','WHETSTONE']
    }
    text="Ekwipunek:\n"
    for i in ekwipunke:
        text+=f'\t{i}: {random.choice(ekwipunke[i])}'+"\n"
    return text
def cuphead_one_boss():
    
    bosses=[#0 for normal 1 for airplane
        ("The root pack",0),
        ("Goopy Le Grande",0),
        ("Hilda Berg",1),
        ("Cagney Carnation",0),
        ("Baroness Von Bon Bon",0),
        ("Beppi The Clown",0),
        ("Djimmi The Great",1),
        ("Grim Matchstick",0),
        ("Wally Warbles",0),
        ("Rumor Honeybottoms",0),
        ("Captain Brineybeard",0),
        ("Sally Stageplay",0),
        ("Werner Werman",0),
        ("Dr. Kahl's Robot",1),
        ("Cala Maria",1),
        ("Phantom Express",0),
        ("King Dice",0),
        ("The Devil",0)
    ]
    boss=random.choice(bosses)
    text=cuphead_random_eq(boss[1])
    if boss[0]=="King Dice":
        text+="\tBroń na samolot: "+random.choice(['normalny','bomby'])
    return f"Twoje zadanie to pokonać jednego bossa\nWalczysz z:{boss[0]}\n"+text
def cuphead_island():
    islands=["WORLD 1","WORLD 2","WORLD 3","FINALE"]
    island=random.choice(islands)
    text=cuphead_random_eq()
    text+="\tBroń na samolot: "+random.choice(['normalny','bomby'])
    return f"twoje zadanie to pokonać każdego bossa na {island}\n\n"+text
quests_e=[
    Quest("Cuphead",'none',1,generator=cuphead_one_boss),
    Quest("fortnite","wygraj solo!",1),
]
quests_h=[
    Quest("Cuphead",'none',2,generator=cuphead_island)
]