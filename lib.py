import discord
import random
version=0.3

class Quest:
    
    color=["#33ff33","#ff3333","#ffff33"]
    def __init__(self,game_name,description:str,level:int=2,link:str=None,generator=None):
        self.name=game_name
        self.desc=description
        self.lvl=["łatwy","trudny","trudny/kto pierwszy ten lepszy"][level-1]
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
        text+=f'> {i}: {random.choice(ekwipunke[i])}'+"\n"
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
        text+="> Broń na samolot: "+random.choice(['normalny','bomby'])
    return f"Twoje zadanie to pokonać jednego bossa\nWalczysz z:{boss[0]}\n"+text
def cuphead_island():
    islands=["WORLD 1","WORLD 2","WORLD 3","FINALE"]
    island=random.choice(islands)
    text=cuphead_random_eq()
    text+="> Broń na samolot: "+random.choice(['normalny','bomby'])
    return f"twoje zadanie to pokonać każdego bossa na {island}\n\n"+text

quests_e=[
    Quest("Cuphead",'none',1,generator=cuphead_one_boss), #index = 0 itp
    Quest("fortnite","wygraj solo!",1),
    Quest("Slay the Spire","none",1,generator=lambda: f"Pokonaj bossa aktu II postacią {random.choice(['Pancernik','Cień','Defekt'])}"),
    Quest("Brawhalla","wygranie dwóch rankedów",1),
    Quest("Celeste","Przejście gry do 5 chapteru",1),
    Quest("bloons td6","przejście dziennego trudnego wyzwania",1),#620
    Quest("portal 2", 'Przejście poziomu "portalowe działo" z użyciem jednego teleportu',1),
    Quest("Celeste","przejście pierwszego chapteru bez dashów",1),
    Quest("Cookie Clicker","kliknij w jedno złote ciastko",1,link="https://orteil.dashnet.org/cookieclicker/"),
    Quest("Wikispeedrun","none",1,generator=lambda: f"zaczynając od losowego artykuło dojdz do {random.choice(['Stalin','Hilter','Mussolini'])} w mniej niż 10 minut", link="https://wikispeedruns.com/"),
    Quest("portal 2","przejść pierwszą połowę gry",1),
    Quest("Dead Cells", "przejść do TRZECIEJ strefy na defultowym ekwipunku",1),
    Quest("Celeste","przejść drugi chapter na wszystkich assystach włączonych",1),
    Quest("Cookie Clicker","Zdobyć dwa mroczne achivmenty",1,link="https://orteil.dashnet.org/cookieclicker/"),
    Quest("bloons td6","Zrobić mapę na trybe HARD",1),
    Quest("IRL","Nauczyć się wybranego wiersza na pamięc",1,link="https://wolnelektury.pl/katalog/gatunek/wiersz/"),
    Quest("OSU", "przejdź dowolną 3 gwiazdkową mapę ma być “trudna”",1),
    Quest("Don't touch the spikes","zdobąć 50 punktów w jednej grze",1),
]
quests_h=[
    Quest("Brawlhalla","Zamiana klawiatura na pada lub na odwrót (wygranie trzech gier)",2),
    Quest("the Messenger","bez upgradów do ogrów",2),
    Quest("the Messenger","bez śmierci do ogrów",2),
    Quest("Celeste","1c i 2c i 7c bez śmierci PODRZĄD",2),
    Quest("bloons td6","Przejście wspólnie ustalonego wyzwania którego przeszło mniej niż 2\% graczy",2),
    Quest("Brawlhalla","wygranie jednej normalnej gry tylko łapkami",2),
    Quest("cookie clicker","50 babć",2,link="https://orteil.dashnet.org/cookieclicker/"),
    Quest("slay the spire","wyzwanie dzienne",2),
    Quest("IRL","dotknąć trawę i przesłać zdjęcie!",2,link="https://w1.pngwing.com/pngs/507/107/png-transparent-grass-sweet-grass-vetiver-commodity-wheatgrass-plant-stem-chrysopogon-grasses.png"),
    Quest("Cuphead",'none',2,generator=cuphead_island),
    Quest("IRL","none",2,generator=lambda:f"Wyrzucić 6 razy pod rząd {'⚀⚁⚂⚃⚄⚅'[random.randint(0,5)]} na kości k6"),
    Quest("Cuphead","Jagódka no hit",2,link="https://pl.wikipedia.org/wiki/Pokrzyk_wilcza_jagoda"),
    Quest("Technik Inforatyk","nauczyć się języka programowania(uzgadniamy jaki) i napisać:\n>obliczał objęcość i pole sześcianu o boku n\n>pętle liczącą do 100\n> i jak ktoś jest chętny to fizzbuzz",2,link="https://esolangs.org/wiki/FizzBuzz"),
    Quest("Duck Game","losowy automat na 2 medale!",2),
    Quest("Hollow Knight","na nowym koncie zabić pierwszego (prawdziwego) bossa (maksymalnie można dostać tylko raz)",2),
    Quest("Comic Sans","doprowadzić sansa do pierwszego potu (na stronie)",2,link="https://jcw87.github.io/c2-sans-fight/"),
    Quest("Vanitas",r"zrobić dzisiejsze trudne wyzwanie ¯\_(ツ)_/¯",2,link="https://www.youtube.com/watch?v=xm3YgoEiEDc&ab_channel=skisles"),
    Quest("IRL","Policz do tysiąca",2,link="https://scp-wiki.wikidot.com/scp-series"),
    Quest("Celeste","Nagrać i wrzucić film na wybrany temat(z tego questa można zrezygnować)",2),
    Quest("Fortnite","Wygrać wspólnie ustalonego deathrana",2,link="https://www.fortnitemaps.com/section/death_runs"),
    Quest("Celeste","1a,2a,3a bez śmierci na nowym save",2),
    Quest("Sudoku","ukończ poziom średni",link="https://sudoku.com/medium/"),
    Quest("Cuphead","tylko defyltowa broń (bez charmów, bez ultów, i bez bomb na samolotach)\n osoba która dokona tego szybciej (liczy się suma czasów bossów) dostaje punkty",3),
    Quest("Brawhalla","pokonać bota ustawionego na tryb chason",2),
    Quest("Celeste","przejść do 5a na padzie",2),
    Quest("Don't touch the spikes","zdobąć 70 punktów w jednej grze",1),
]
"""
A SPECTER is haunting Europe--the specter of comm
nism. All the powers of old Europe have entered into
holy alliance to exorcise this specter: Pope and Czar, M
ternich and Cuizot, 1 French Radicals2 and German poli
spies.
Wh r~ is the party in opposition that has not been d
cried as communistic by its opponents in power? Whe
the Opposition thnt has not hurled back the branding r
proach of communism, against the more advanced oppo
tion parties, as w<'ll as against its reactionary adversari
Two things result from this fact:
I. Communism is already acknowledged by all Europe
powers to be ils<'lf a power.
II. It is high lime that Communists should openly, ·
the face of the whole world, publish their views, th
aims, their tendencies, and meet this nursery tale of t
spect<'r of communism with a manifesto of the party itse
To this end, Communists of various nationalities ha
ao;;sembled in London, and sketched the followin~ rna
festo, to be published in the English, Fr


"""