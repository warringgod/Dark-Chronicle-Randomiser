# This is a randomizer file for the Simple Randomizer Maker.
# This file must be named randomizer.py in order to work.

from classes import *
import random

def value(name):
	for att in Attributes:
		if att.name == name:
			return att
	print("This attribute does not exist: "+name)
	return None

########################
# EDIT BELOW THIS LINE #
########################

Program_Name = "Dark Chronicle Randomiser"
Rom_Name = "DarkCloud2"
Rom_File_Format = "iso" # Rom file format (nes, gba, etc.)
About_Page_Text = ""
Timeout = 10
Slow_Mode = False

# Example below is addresses for the dark 0x2f4521cloud 2 USA rom, and how the statistics offsets are related to hp ( in hex)
"""
Count Balloon = 2F4521
HP = 2F4560
ABS = 2F4566
Gilda = 2F4568
Attacks to Break = 2F4570
ATK = 2F4576
DEF = 2F4578
Wrench Effectiveness % = 2F458C
Gun Effectiveness % = 2F458E
Beam Effectiveness % = 2F4590
Grenade Effectiveness % = 2F4592
Sword Effectiveness % = 2F4594
Armband Effectiveness % = 2F4596
Item 1 = 2F45B0
Item 2 = 2F45B2
Item 3 = 2F45B4

HP = HP + 0
ABS = HP + 06
Gilda = HP + 08
Attacks to Break = HP + 10
ATK = HP + 16
DEF = HP + 18
WRENCH % = HP +2C
GUN % = HP +2E
BEAM % = HP + 30
GRENADE = HP + 32
SWORD = HP + 34
ARMBAND = HP +36
ITEM 1 = HP + 50
ITEM 2 = HP + 52
ITEM 3 = HP + 54

I believe Item 1 is stolen item, item 2 is common, item 3 is rare maybe? test.

"""
#Variables , these are all %'s of base values, whole numbers only, applies to all monsters
# maybe if there is demand to make it based on dungeon i'd make that

Change_HP = True
Min_HP_Range = 100
Max_HP_Range = 100

Change_ABS = True
Min_ABS_Range = 100
Max_ABS_Range = 100

Change_GILDA = True
Min_GILDA_Range = 100
Max_GILDA_Range = 100

Change_ATK = True
Min_ATK_Range = 100
Max_ATK_Range = 100

Change_DEF = True
Min_DEF_Range = 100
Max_DEF_Range = 100

#Constants

tier1weaponsmax = [1, 2, 9, 15, 22, 23, 24, 90]
tier2weaponsmax = [10, 11, 18, 25, 28, 31]
tier3weaponsmax = [3, 12, 17, 26, 35]
tier4weaponsmax = [4, 6, 13, 29, 32, 36]
tier5weaponsmax = [5, 7, 14, 16, 27, 37]
tier6weaponsmax = [8, 19, 30, 33, 38]
tier7weaponsmax = [20, 21, 34, 39, 40]

tier1weaponsmonica = [41, 43, 44, 91]
tier2weaponsmonica = [42, 46, 48, 61, 73, 92, 93, 110]
tier3weaponsmonica = [45, 49, 54, 65, 67, 69, 74, 94, 104]
tier4weaponsmonica = [47, 52, 58, 62, 68, 70, 76, 82, 95, 103]
tier5weaponsmonica = [50, 51, 56, 64, 66, 71, 75, 85, 86, 97, 98, 100, 106]
tier6weaponsmonica = [55, 59, 63, 72, 77, 80, 84, 87, 96, 99, 105, 107]
tier7weaponsmonica = [57, 60, 78, 79, 81, 83, 88, 89, 101, 102, 108, 109]

tierclothes = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
			   132, 133, 134, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267]

tier1ridepod = [135, 136, 145, 146, 147, 151, 155, 156, 157, 158, 163, 165, 166]
tier2ridepod = [137, 138, 149, 159, 160, 161, 162, 167, 392, 393, 395, 398, 410]
tier3ridepod = [139, 140, 148, 150, 152, 153, 154, 168, 394, 396, 399, 401, 404, 411]
tier4ridepod = [141, 142, 169, 397, 400, 402, 405, 407, 412, 413, 416, 419]
tier5ridepod = [170, 403, 406, 408, 409, 414, 417, 420]
tier6ridepod = [415, 418, 421]

tierattachments = [175, 176, 177, 178, 179, 180, 181, 182, 183, 184]
tiergems = [186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197]
tierraregems = [198, 199]
tiercoins = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209]

tier1items = [210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 230, 231,
			  232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 253, 254, 255, 256, 257, 268, 269,
			  275, 276, 277, 278, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 298, 301,
			  312, 313, 314, 315, 316, 317, 318, 319, 352, 425]

tier2items = [225, 270, 271, 272, 274, 279, 299, 304, 307, 377, 378, 379, 380, 381, 383, 390]
tier3items = [273, 295, 296, 297, 376, 388, 389, 391]
tierfish = [310, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336]

# these are used for chest randomisation
tier1chests = [210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,227,245,268,294,298,352,281]
tier2chests = [228,229,230,231,232,233,234,235,236,275,276,237,238,239,240,241,242,243,244,226,280]
tier3chests = [277,278,287,288,289,290,291,175,176,177,178,179,180,181,182,183,184,269,225]
tier4chests = [310,312,313,314,315,316,317,318,319,299,300,253,254,255,256,257,301,292,270,274,279,282,283,284,285,293]
tier5chests = [286,381,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,272,297,304]
tier6chests = [377,378,379,380,271,336,307,390,273,391,383,200,201,202,203,204,205,206,207,208,209]
tier7chests = [111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,258,259,260,261,262,263,264,265,266,267]
tier8chests = [186,187,188,190,191,192,193,194,195,196,197,189,295,198,199,388,389,296,384]

"""
1,"Battle Wrench";
2,"Drill Wrench";
3,"Smash Wrench";
4,"Stinger Wrench";
5,"Poison Wrench";
6,"Cubic Hammer";
7,"Digi Hammer";
8,"Heavy Hammer";
9,"Handy Stick";
10,"Turkey";
11,"Swan";
12,"Flamingo";
13,"Falcon";
14,"Albatross";
15,"Turtle Shell Hammer";
16,"Big Bucks Hammer";
17,"Frozen Tuna";
18,"Kubera's Hand";
19,"Sigma Breaker";
20,"Grade Zero";
21,"LEGEND";
22,"Classic Gun";
23,"Dryer Gun";
24,"Trumpet Gun";
25,"Bell Trigger";
26,"Magic Gun";
27,"Soul Breaker";
28,"Grenade Launcher";
29,"Dark Viper";
30,"Twin Buster";
31,"Jurak Gun";
32,"Question Shooter";
33,"Steal Gun";
34,"Supernova";
35,"Star Breaker";
36,"Wild Cat";
37,"Sexy Panther";
38,"Desperado";
39,"Sigma Bazooka";
40,"Last Resort";
41,"Long Sword";
42,"Broad Sword";
43,"Baselard";
44,"Gladius";
45,"Wise Owl Sword";
46,"Cliff Knife";
47,"Antique Sword";
48,"Bastard Sword";
49,"Kitchen Knife";
50,"Tsukikage";
51,"Sun Sword";
52,"Serpent Slicer";
53,"Macho Sword";
54,"Shamshir";
55,"Ama no Murakumo";
56,"Lamb's Sword";
57,"Dark Cloud";
58,"Brave Ark";
59,"Big Bang";
60,"Atlamillia Sword";
61,"Mardan Sword";
62,"Garayan Sword";
63,"Mardan Garayan";
64,"Ruler's Sword";
65,"Evilcise";
66,"Small Sword";
67,"Sand Breaker";
68,"Drain Seeker";
69,"Chopper";
70,"Choora";
71,"Claymore";
72,"Maneater";
73,"Bone Rapier";
74,"Sax";
75,"7 Branch Sword";
76,"Dusack";
77,"Cross Heinder";
78,"7th Heaven";
79,"Sword of Zeus";
80,"Chronicle Sword";
81,"Chronicle 2";
82,"Holy Daedalus Blade";
83,"Muramasa";
84,"Dark Excalibur";
85,"Sargatanas";
86,"Halloween Blade";
87,"Shining Bravado";
88,"Island King";
89,"Griffon Fork";
90,"True Battle Wrench";
91,"Magic Brassard";
92,"Gold Brassard";
93,"Bandit Brassard";
94,"Crystal Brassard";
95,"Platinum Brassard";
96,"Goddess Brassard";
97,"Spirit Brassard";
98,"Destruction Brassard";
99,"Satan Brassard";
100,"Athena's Armlet";
101,"Mobius Bangle";
102,"Angel Shooter";
103,"Pocklekul";
104,"Thorn Armlet";
105,"Star Armlet";
106,"Moon Armlet";
107,"Sun Armlet";
108,"Five-Star Armlet";
109,"Love";
110,"Royal Sword";
111,"Hunting Cap";
112,"Fashionable Cap";
113,"Two-Tone Beret";
114,"Maintenance Cap";
115,"Explorer's Helmet";
116,"Clown Hat";
117,"Leather Shoes";
118,"Wing Shoes";
119,"Work Shoes";
120,"Dragon Shoes";
121,"Clown Shoes";
122,"Explorer's Shoes";
123,"Yellow Ribbon";
124,"Striped Ribbon";
125,"Zipangu Comb";
126,"Swallowtail";
127,"Princess Orb";
128,"Kitty Bell";
129,"Knight Boots";
130,"Metal Boots";
131,"Wing Boots";
132,"Spike Boots";
133,"Princess Boots";
134,"Panther Boots";
135,"Drum Can Body";
136,"Milk Can Body";
137,"Refrigerator Body";
138,"Wooden Box Body";
139,"Clown Body";
140,"Samurai Body";
141,"Super-Alloy Body";
142,"Sun and Moon Armor";
145,"Cannonball Arm";
146,"Barrel Cannon";
147,"Drill Arm";
148,"Missile Pod Arm";
149,"Hammer Arm";
150,"Machine Gun Arm";
151,"Clown Hand";
152,"Samurai Arm";
153,"Laser Arm";
154,"Nova Cannon";
155,"Iron Leg";
156,"Caterpillar";
157,"Bucket Leg";
158,"Roller Foot";
159,"Buggy";
160,"Propeller Leg";
161,"Multi Feet";
162,"Jet Hover";
163,"Clown Foot";
165,"Energy Pack";
166,"Energy Pack (Barrel)";
167,"Bucket Pack";
168,"Cleaner Pack";
169,"Energy Pack (Urn)";
170,"Triple-Urn Pack";
172,"Monster Notes";
173,"Dynamite";
174,"Seal-Breaking Scroll";
175,"Flame Crystal";
176,"Chill Crystal";
177,"Lightning Crystal";
178,"Hunter Crystal";
179,"Holy Crystal";
180,"Destruction Crystal";
181,"Wind Crystal";
182,"Sea Dragon Crystal";
183,"Power Crystal";
184,"Protector Crystal";
185,"[line1]";
186,"Garnet";
187,"Amethyst";
188,"Aquamarine";
189,"Diamond";
190,"Emerald";
191,"Pearl";
192,"Ruby";
193,"Peridot";
194,"Sapphire";
195,"Opal";
196,"Topaz";
197,"Turquoise";
198,"Sun Stone";
199,"Moon Stone";
200,"Wealth Coin";
201,"Dark Coin";
202,"Indestructible Coin";
203,"Poison Coin";
204,"Time Coin";
205,"Bandit Coin";
206,"Absorption Coin";
207,"Healing Coin";
208,"Bull's-Eye Coin";
209,"Experience Coin";
210,"Rolling Log";
211,"Sturdy Rock";
212,"Rough Rock";
213,"Bundle of Hay";
214,"Sturdy Cloth";
215,"Gunpowder";
216,"Glass Material";
217,"Unknown Bone";
218,"Sticky Clay";
219,"Flour";
220,"Sugar Cane";
221,"Super Hot Pepper";
222,"Poison";
223,"Forest Dew";
224,"Scrap of Metal";
225,"Gold Bar";
226,"Silver Ball";
227,"Hunk of Copper";
228,"Light Element";
229,"Holy Element";
230,"Earth Element";
231,"Water Element";
232,"Chill Element";
233,"Thunder Element";
234,"Wind Element";
235,"Fire Element";
236,"Life Element";
237,"Paint (Red)";
238,"Paint (Blue)";
239,"Paint (Black)";
240,"Paint (Green)";
241,"Paint (Orange)";
242,"Paint (Yellow)";
243,"Paint (Purple)";
244,"Paint (Pink)";
245,"Thick Hide";
246,"Core";
247,"Improved Core";
248,"Core II";
249,"Core III";
250,"Super Core";
251,"Hyper Core";
252,"Master Grade Core";
253,"Anti-Petrify Amulet";
254,"Non-Stop Amulet";
255,"Anti-Curse Amulet";
256,"Anti-Goo Amulet";
257,"Antidote Amulet";
258,"Green Overalls";
259,"Red Vest";
260,"Denim Overalls";
261,"Explorer's Outfit";
262,"Clown Suit";
263,"Pumpkin Shorts";
264,"Striped Dress";
265,"Star Leotard";
266,"Princess Dress";
267,"Panther Ensemble";
268,"Bread";
269,"Cheese";
270,"Premium Chicken";
271,"Double Pudding";
272,"Plum Rice Ball";
273,"Resurrection Powder";
274,"Stamina Drink";
275,"Antidote Drink";
276,"Holy Water";
277,"Soap";
278,"Medusa's Tear";
279,"Mighty Healing";
280,"Bomb";
281,"Stone";
282,"Flame Stone";
283,"Chill Stone";
284,"Lightning Stone";
285,"Wind Stone";
286,"Holy Stone";
287,"Heart-Throb Cherry";
288,"Stone Berry";
289,"Gooey Peach";
290,"Bomb Nut";
291,"Poison Apple";
292,"Mellow Banana";
293,"Escape Powder";
294,"Repair Powder";
295,"Level Up Powder";
296,"Fruit of Eden";
297,"Treasure Chest Key";
298,"Gun Repair Powder";
299,"Crunchy Bread";
300,"Crunchy Bread";
301,"Roasted Chestnut";
302,"Fishing Rod";
303,"Lure Rod";
304,"Gift Capsule";
305,"Map";
306,"Magic Crystal";
307,"Lightspeed";
308,"Badge Box";
309,"Aquarium";
310,"Priscleen";
311,"Medal Holder";
312,"Prickly";
313,"Mimi";
314,"Evy";
315,"Carrot";
316,"Potato Cake";
317,"Minon";
318,"Battan";
319,"Petite Fish";
320,"Bobo";
321,"Gobbler";
322,"Nonky";
323,"Kaji";
324,"Baku Baku";
325,"Mardan Garayan";
326,"Gummy";
327,"Niler";
328,"Umadakara";
329,"Tarton";
330,"Piccoly";
331,"Bon";
332,"Hama Hama";
333,"Negie";
334,"Den";
335,"Heela";
336,"Baron Garayan";
337,"Key Handle";
338,"Channel Key";
339,"Fairy Saw";
340,"Slash Branch";
341,"Giant Meat";
342,"Luna Stone";
343,"Luna Stone Piece";
344,"Magma Rock";
345,"Rope";
346,"Stone "T"";
347,"White Wind Vase";
348,"Queen's Watering Pot";
349,"Moon Clock Hand";
350,"Trolley Oil";
351,"Rusted Key";
352,"Armband Repair Powder";
353,"Circus Ticket";
354,"Fire Horn";
355,"Inside Scoop Memo";
356,"Sundrop";
357,"Photo Album";
358,"Cooking Stove";
359,"Help Receiver";
360,"Electric Worm";
361,"Lafrescia Seed";
362,"Star Key";
363,"White Windflower";
364,"Miracle Dumplings";
365,"Earth Gem";
366,"Water Gem";
367,"Wind Gem";
368,"Fire Gem";
369,"Camera";
370,"Grape Juice";
371,"Starglass";
372,"Time Bomb";
373,"Shell Talkie";
374,"Flower of the Sun";
375,"Secret Dragon Remedy";
376,"Gold Paint";
377,"Spinner";
378,"Frog";
379,"Minnow";
380,"Fork";
381,"Ridepod Fuel";
382,"Wrench";
383,"Monster Drop";
384,"Name-Change Ticket";
385,"Teal Envelope";
386,"Notebook";
387,"Wrench";
388,"Potato Pie";
389,"Witch Parfait";
390,"Improved Bomb";
391,"Final Bomb";
392,"Cannonball Arm II";
393,"Cannonball Arm III";
394,"Cannonball Arm IV";
395,"Barrel Cannon II";
396,"Barrel Cannon III";
397,"Barrel Cannon IV";
398,"Drill Arm II";
399,"Drill Arm III";
400,"Drill Arm IV";
401,"Missile Pod Arm II";
402,"Missile Pod Arm III";
403,"Missile Pod Arm IV";
404,"Hammer Arm II";
405,"Hammer Arm III";
406,"Hammer Arm IV";
407,"Machine Gun Arm II";
408,"Machine Gun Arm III";
409,"Machine Gun Arm IV";
410,"Clown Hand II";
411,"Clown Hand III";
412,"Clown Hand IV";
413,"Samurai Arm II";
414,"Samurai Arm III";
415,"Samurai Arm IV";
416,"Laser Arm II";
417,"Laser Arm III";
418,"Laser Arm IV";
419,"Nova Cannon II";
420,"Nova Cannon III";
421,"Nova Cannon IV";
422,"Voice Unit";
423,"Shield Kit";
424,"Himarra Badge";
425,"Tasty Water";
427,"Sun Badge";
428,"Moon Badge";

"""

"""
Some Key Addresses

Depending on the Chapter/Location I THINk , the shops can contain different things, so the shops have different entries depending on when they are?
In Theory if this is right, then we can potentially make things more/less expensive depending on the part of the game, but consistency is nice.

I believe even if you can't access the shop in the chapter, the shop is still there, not sure

https://darkcloud.fandom.com/wiki/Dark_Chronicle_shops seems to suggest that the these are different chapters, , but there is only 8 chapterS?
I think the shops change after the mid chapter event happens.

? Price and Shops Set 1 = 9B38800
? Price and Shops Set 2 = 9B3B000
? Price and Shops Set 3 = 9B3D800
? Price and Shops Set 4 = 9B40000
? Price and Shops Set 5 = 9B42800
? Price and Shops Set 6 = 9B45800
? Price and Shops Set 7 = 9B48800
? Price and Shops Set 8 = 9B4B800
? Price and Shops Set 9 = 9B4E800
? Price and Shops Set 10 = 9B51000
? Price and Shops Set 11 = 9B53800
? Price and Shops Set 12 = 9B56000
? Price and Shops Set 13 = 9B58800
? Price and Shops Set 14 = 9B5B000
? Price and Shops Set 15 = 9B5E000
? Price and Shops Set 16 = 9B61000


Chapter 1 Prices and Shops? = 9B4E800

Shop 00				9B3A79E	Milane			
Shop 01				9B3A7D0	Polly			
Shop 02				9B3A805	Dell			
Shop 03				9B3A826	Ferdinand		
Shop 04				9B3A84B	Morton			
Shop 05				9B3A894	Starlight Temple (Future) (Mandatory Starglass 371)
Shop 06				9B3A8F9	Donny			
Shop 07				9B3A92C	Borneo			
Shop 08				9B3A957	Gordon			
Shop 09				9B3A980	Parn			
Shop 10				9B3A9C1	Claire			
Shop 11				9B3A9E3	Stewart			
Shop 12 			9B3AA11	Adel			
Shop 13				9B3AA41	Erik			
Shop 14				9B3AA61	Gerald			
Shop 15				9B3AA86	Church			
Shop 16				9B3AAB6	Rufio			
Shop 17				9B3AB08	Flavin			
Shop 18				9B3AB46	Olive			
Shop 19				9B3AB78	Julia			
Shop 20				9B3AB97	Mena
Shop 21				9B3ABBF	Corinne
Shop 22				9B3ABF3	Rosa
Shop 23				9B3AC29	Cerdic
Shop 24				9B3AC53	Woody Tailor (Future) (Mandatory Himarra Badge 424)
Shop 25				9B3AC95	Jurak Arms (Future)
Shop 26				9B3ACC4	Mushroom Burger Eatery (Future)
Shop 27				9B3AD16	Starlight Weapons (Future)
Shop 28				9B3AD3B	G-Parts (Future)
Shop 29				9B3AD64	G-Tools (Future)
Shop 30				9B3AD8F	G-Weapons (Future)
Shop 31				9B3ADB7	Conda

"""

def Get_Address(HP_Address, attribute):
    Card_HP_Address = int(HP_Address)

    if attribute == "HP":
        offset = int(0x00)
    elif attribute == "ABS":
        offset = int(0x06)
    elif attribute == "GILDA":
        offset = int(0x08)
    elif attribute == "ATK":
        offset = int(0x16)
    elif attribute == "DEF":
        offset = int(0x18)
    elif attribute == "ITEM1":
        offset = int(0x50)
    elif attribute == "ITEM2":
        offset = int(0x52)
    elif attribute == "ITEM3":
        offset = int(0x54)

    SumInt = Card_HP_Address + offset
    SumHex = [hex(SumInt)]
    return SumHex

# I could make these into 1 min max function, but just in case we think of something later i'd rather modularise it
####################################################### Change_HP

def Min_HP_Multiplier(base_hp):

	if not Change_HP:
		return base_hp

	return round((base_hp * Min_HP_Range) / 100)

def Max_HP_Multiplier(base_hp):

	if not Change_HP:
		return base_hp

	return round((base_hp * Max_HP_Range) / 100)

####################################################### Change_HP

####################################################### Change_ABS

def Min_ABS_Multiplier(base_ABS):

	if not Change_ABS:
		return base_ABS

	return round((base_ABS * Min_ABS_Range) / 100)

def Max_ABS_Multiplier(base_ABS):

	if not Change_ABS:
		return base_ABS

	return round((base_ABS * Max_ABS_Range) / 100)

####################################################### Change_ABS

####################################################### Change_GILDA

def Min_GILDA_Multiplier(base_GILDA):

	if not Change_GILDA:
		return base_GILDA

	return round((base_GILDA * Min_GILDA_Range) / 100)

def Max_GILDA_Multiplier(base_GILDA):

	if not Change_GILDA:
		return base_GILDA

	return round((base_GILDA * Max_GILDA_Range) / 100)

####################################################### Change_GILDA

####################################################### Change_ATK

def Min_ATK_Multiplier(base_ATK):

	if not Change_ATK:
		return base_ATK

	return round((base_ATK * Min_ATK_Range) / 100)

def Max_ATK_Multiplier(base_ATK):

	if not Change_ATK:
		return base_ATK

	return round((base_ATK * Max_ATK_Range) / 100)

####################################################### Change_ATK

####################################################### Change_DEF

def Min_DEF_Multiplier(base_DEF):

	if not Change_DEF:
		return base_DEF

	return round((base_DEF * Min_DEF_Range) / 100)

def Max_DEF_Multiplier(base_DEF):

	if not Change_DEF:
		return base_DEF

	return round((base_DEF * Max_DEF_Range) / 100)

####################################################### Change_DEF

# BELOW ARE ALL DROPS FROM MONSTERS, THE MONSTER WILL ALWAYS HAVE THE SAME RANDOM DROP, NOT DIFF ONE EACH TIME

####################################################### ChooseSewerItems

def ChooseSewerDrops():

	x = random.randint(0, 100)

	if 0 <= x <= 39:
		item_number = 0
	elif 40 <= x <= 69:
		item_number = random.choice(tier1items)
	elif 70 <= x <= 89:
		item_number = random.choice(tierattachments)
	elif 90 <= x <= 97:
		item_number = random.choice(tier1weaponsmax + tier1weaponsmonica)
	elif 98 <= x <= 99:
		item_number = random.choice(tier2weaponsmax + tier2weaponsmonica + tiergems + tiercoins)
	elif x == 100:
		item_number = random.choice(tier2ridepod)
	return [item_number]

####################################################### ChooseSewerItems

####################################################### ChooseSindainItems

def ChooseSindainItems():

	x = random.randint(0, 100)

	if 0 <= x <= 19:
		item_number = 0
	elif 20 <= x <= 59:
		item_number = random.choice(tier1items)
	elif 60 <= x <= 84:
		item_number = random.choice(tierattachments)
	elif 84 <= x <= 89:
		item_number = random.choice(tier2items +tierfish)
	elif 90 <= x <= 94:
		item_number = random.choice(tier2weaponsmax + tier2weaponsmonica)
	elif 95 <= x <= 97:
		item_number = random.choice(tiergems + tiercoins)
	elif 98 <= x <= 99:
		item_number = random.choice(tier3weaponsmax + tier3weaponsmonica)
	elif x == 100:
		item_number = random.choice(tier3ridepod)
	return [item_number]

####################################################### ChooseSindainItems

####################################################### ChooseValleyItems

def ChooseValleyItems():

	x = random.randint(0, 100)

	if 0 <= x <= 39:
		item_number = random.choice(tier1items + tierclothes)
	elif 40 <= x <= 59:
		item_number = random.choice(tier2items + tierfish)
	elif 60 <= x <= 87:
		item_number = random.choice(tierattachments)
	elif 88 <= x <= 92:
		item_number = random.choice(tier2weaponsmax + tier2weaponsmonica)
	elif 93<= x <= 96:
		item_number = random.choice(tiergems + tiercoins)
	elif 97 <= x <= 99:
		item_number = random.choice(tier3weaponsmax + tier3weaponsmonica)
	elif x == 100:
		item_number = random.choice(tier4ridepod)
	return [item_number]

####################################################### ChooseValleyItems

####################################################### ChooseVeniccioItems

def ChooseVeniccioItems():

	x = random.randint(0, 100)

	if 0 <= x <= 29:
		item_number = random.choice(tier1items + tierclothes)
	elif 30 <= x <= 59:
		item_number = random.choice(tier2items )
	elif 60 <= x <= 87:
		item_number = random.choice(tierattachments)
	elif 88 <= x <= 92:
		item_number = random.choice(tier3weaponsmax + tier3weaponsmonica)
	elif 93<= x <= 97:
		item_number = random.choice(tiergems + tiercoins)
	elif 98 <= x <= 99:
		item_number = random.choice(tier4weaponsmax + tier4weaponsmonica)
	elif x == 100:
		item_number = random.choice(tier4ridepod)
	return [item_number]

####################################################### ChooseVeniccioItems

####################################################### ChooseHeimItems

def ChooseHeimItems():

	x = random.randint(0, 100)

	if 0 <= x <= 14:
		item_number = random.choice(tier1items)
	elif 15 <= x <= 49:
		item_number = random.choice(tier2items)
	elif 50 <= x <= 80:
		item_number = random.choice(tierattachments)
	elif 81 <= x <= 84:
		item_number = random.choice(tier3items)
	elif 85 <= x <= 89:
		item_number = random.choice(tier3weaponsmax + tier3weaponsmonica)
	elif 90<= x <= 94:
		item_number = random.choice(tiergems + tiercoins)
	elif 95 <= x <= 98:
		item_number = random.choice(tier4weaponsmax + tier4weaponsmonica)
	elif x == 99:
		item_number = random.choice(tierraregems)
	elif x == 100:
		item_number = random.choice(tier4ridepod)
	return [item_number]

####################################################### ChooseHeimItems


####################################################### ChooseMoonItems

def ChooseMoonItems():

	x = random.randint(0, 100)

	if 0 <= x <= 34:
		item_number = random.choice(tier2items)
	elif 35 <= x <= 69:
		item_number = random.choice(tierattachments)
	elif 70 <= x <= 74:
		item_number = random.choice(tier3items)
	elif 75 <= x <= 84:
		item_number = random.choice(tier4weaponsmax + tier4weaponsmonica)
	elif 85<= x <= 92:
		item_number = random.choice(tiergems)
	elif 93 <= x <= 94:
		item_number = random.choice(tiercoins)
	elif 95 <= x <= 98:
		item_number = random.choice(tier5weaponsmax + tier5weaponsmonica)
	elif x == 99:
		item_number = random.choice(tierraregems)
	elif x == 100:
		item_number = random.choice(tier5ridepod)
	return [item_number]

####################################################### ChooseMoonItems

####################################################### ChooseZelmiteItems

def ChooseZelmiteItems():

	x = random.randint(0, 100)

	if 0 <= x <= 34:
		item_number = random.choice(tier2items)
	if 35 <= x <= 44:
		item_number = random.choice(tier3items)
	elif 45 <= x <= 69:
		item_number = random.choice(tierattachments)
	elif 70 <= x <= 84:
		item_number = random.choice(tier5weaponsmax + tier5weaponsmonica)
	elif 85<= x <= 94:
		item_number = random.choice(tiergems)
	elif 95 <= x <= 97:
		item_number = random.choice(tier6weaponsmax + tier6weaponsmonica)
	elif x == 98:
		item_number = random.choice(tierraregems)
	elif x == 99:
		item_number = random.choice(tier7weaponsmax + tier7weaponsmonica)
	elif x == 100:
		item_number = random.choice(tier6ridepod)
	return [item_number]

####################################################### ChooseZelmiteItems

####################################################### ChooseItemDrops

def ChooseItemDrops(Dungeon):
	item = 0
	if Dungeon == "Sewer":
		item = ChooseSewerDrops()
	if Dungeon == "Sindain":
		item = ChooseSindainItems()
	if Dungeon == "Valley":
		item = ChooseValleyItems()
	if Dungeon == "Veniccio":
		item = ChooseVeniccioItems()
	if Dungeon == "Heim":
		item = ChooseHeimItems()
	if Dungeon == "Star":
		item = ChooseHeimItems()
	if Dungeon == "Moon":
		item = ChooseMoonItems()
	if Dungeon == "Zelmite":
		item = ChooseZelmiteItems()
	if Dungeon == "Depths":
		item = ChooseHeimItems()
	return item

####################################################### ChooseItemDrops

## SHOP FNS ##

def fdig(num, n):
	number = str(num)
	return int(number[n -1])

def concat(a,b,c):
	string = "0x" + str(a+30) + str(b+30) + str(c+30)
	string = int(string,16)
	return string

def ChooseShopItems(Shop):

	x = random.randint(0, 100)

	if 0 <= x <= 49:
		item_number = random.choice(tier1items)
	elif 50 <= x <= 59:
		item_number = random.choice(tierattachments)
	elif 60 <= x <= 64:
		item_number = random.choice(tierfish)
	elif 65 <= x <= 69:
		item_number = random.choice(tiergems)
	elif 70 <= x <= 79:
		item_number = random.choice(tier2items)
	elif 80 <= x <= 84:
		item_number = random.choice(tiercoins)
	elif 80 <= x <= 84:
		item_number = random.choice(tiergems)
	elif 85 <= x <= 89:
		item_number = random.choice(tierclothes)
	elif 90 <= x <= 92:
		item_number = random.choice(tier3items)
	elif 93 <= x <= 100:
		item_number = random.choice(tierraregems)
	elif x == 100:
		item_number = random.choice(tierraregems)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseSewerItems

def ChooseSewerChestDrops():

	x = random.randint(0, 100)

	if 0 <= x <= 54:
		item_number = random.choice(tier1chests)
	elif 55 <= x <= 79:
		item_number = random.choice(tier2chests)
	elif 80 <= x <= 94:
		item_number = random.choice(tier3chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier1ridepod)
	elif x == 100:
		item_number = random.choice(tier4chests + tier5chests + tier6chests + tier7chests + tier8chests + tier2ridepod)
	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseSewerChestDrops

####################################################### ChooseSindainChestDrops

def ChooseSindainChestDrops():

	x = random.randint(0, 100)

	if 0 <= x <= 39:
		item_number = random.choice(tier1chests)
	elif 40 <= x <= 59:
		item_number = random.choice(tier2chests)
	elif 60 <= x <= 84:
		item_number = random.choice(tier3chests)
	elif 85 <= x <= 94:
		item_number = random.choice(tier4chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier2ridepod)
	elif x == 100:
		item_number = random.choice(tier5chests + tier6chests + tier7chests + tier8chests + tier3ridepod)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseSindainChestDrops

####################################################### ChooseSindainChestDrops
##TODO, I DONT KNOW WHAT THIS SECTION IS SO FORCING THIS ITEM TO FIND OUT
def ChooseSection3ChestDrops():

	x = random.randint(0, 100)

	item_number = 189

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseSindainChestDrops

####################################################### ChooseValleyChestDrops

def ChooseValleyChestDrops():

	x = random.randint(0, 100)

	if 0 <= x <= 19:
		item_number = random.choice(tier1chests)
	elif 20 <= x <= 39:
		item_number = random.choice(tier2chests)
	elif 40 <= x <= 69:
		item_number = random.choice(tier3chests)
	elif 70 <= x <= 89:
		item_number = random.choice(tier4chests)
	elif 90 <= x <= 94:
		item_number = random.choice(tier5chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier3ridepod)
	elif x == 100:
		item_number = random.choice(tier6chests + tier7chests + tier8chests + tier4ridepod)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseValleyChestDrops

####################################################### ChooseVeniccioChestDrops

def ChooseVeniccioChestDrops():

	x = random.randint(0, 100)

	if  0 <= x <= 19:
		item_number = random.choice(tier2chests)
	elif 20 <= x <= 39:
		item_number = random.choice(tier3chests)
	elif 40 <= x <= 59:
		item_number = random.choice(tier4chests)
	elif 60 <= x <= 79:
		item_number = random.choice(tier5chests)
	elif 80 <= x <= 94:
		item_number = random.choice(tier6chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier4ridepod)
	elif x == 100:
		item_number = random.choice(tier7chests + tier8chests)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseVeniccioChestDrops

####################################################### ChooseHeimChestDrops

def ChooseHeimChestDrops():

	x = random.randint(0, 100)

	if  0 <= x <= 29:
		item_number = random.choice(tier3chests)
	elif 30 <= x <= 49:
		item_number = random.choice(tier4chests)
	elif 50 <= x <= 69:
		item_number = random.choice(tier5chests)
	elif 70 <= x <= 89:
		item_number = random.choice(tier6chests)
	elif 90 <= x <= 94:
		item_number = random.choice(tier7chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier5ridepod)
	elif x == 100:
		item_number = random.choice(tier8chests)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseHeimChestDrops

####################################################### ChooseMoonChestDrops

def ChooseMoonChestDrops():

	x = random.randint(0, 100)

	if  0 <= x <= 19:
		item_number = random.choice(tier3chests)
	elif 20 <= x <= 39:
		item_number = random.choice(tier4chests)
	elif 40 <= x <= 79:
		item_number = random.choice(tier5chests)
	elif 70 <= x <= 89:
		item_number = random.choice(tier6chests)
	elif 90 <= x <= 94:
		item_number = random.choice(tier7chests)
	elif 95 <= x <= 99:
		item_number = random.choice(tier6ridepod)
	elif x == 100:
		item_number = random.choice(tier8chests)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseMoonChestDrops

####################################################### ChooseZelmiteChestDrops

def ChooseZelmiteChestDrops():

	x = random.randint(0, 100)

	if  0 <= x <= 39:
		item_number = random.choice(tier5chests)
	elif 40 <= x <= 79:
		item_number = random.choice(tier6chests)
	elif 80 <= x <= 84:
		item_number = random.choice(tier6ridepod)
	elif x >= 85:
		item_number = random.choice(tier8chests)

	y =	concat(fdig(item_number,1),fdig(item_number,2),fdig(item_number,3))

	return [y]

####################################################### ChooseZelmiteChestDrops


# START RANDO
Attributes = [
#SEWER RAT 0x2F3264
	Attribute(
		name="SEWER RAT HP",
		addresses=[0x2F32B0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(25),
		max_value=Max_HP_Multiplier(25),
		is_little_endian=True,),
	Attribute(
		name="SEWER RAT ABS",
		addresses=[0x2F32B6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True,),
	Attribute(
		name="SEWER RAT GILDA",
		addresses=[0x2F32B8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(6),
		max_value=Max_GILDA_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ATK",
		addresses=[0x2F32C6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(7),
		max_value=Max_ATK_Multiplier(7),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT DEF",
		addresses=[0x2F32C8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ITEM1",
		addresses=[0x2F3300],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ITEM2",
		addresses=[0x2F3302],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ITEM3",
		addresses=[0x2F3304],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#BEACH RAT 0x2F331C
	Attribute(
		name="BEACH RAT HP",
		addresses=[0x2f3368],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(260),
		max_value=Max_HP_Multiplier(260),
		is_little_endian=True,),
	Attribute(
		name="BEACH RAT ABS",
		addresses=[0x2f336e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(52),
		max_value=Max_ABS_Multiplier(52),
		is_little_endian=True,),
	Attribute(
		name="BEACH RAT GILDA",
		addresses=[0x2f3370],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(27),
		max_value=Max_GILDA_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ATK",
		addresses=[0x2f337e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(40),
		max_value=Max_ATK_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT DEF",
		addresses=[0x2f3380],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(29),
		max_value=Max_DEF_Multiplier(29),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ITEM1",
		addresses=[0x2f33b8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ITEM2",
		addresses=[0x2f33ba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ITEM3",
		addresses=[0x2f33bc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#castle eater 0x2F33D4
	Attribute(
		name="CASTLE EATER HP",
		addresses=[0x2f3420],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(872),
		max_value=Max_HP_Multiplier(872),
		is_little_endian=True,),
	Attribute(
		name="CASTLE EATER ABS",
		addresses=[0x2f3426],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(174),
		max_value=Max_ABS_Multiplier(174),
		is_little_endian=True,),
	Attribute(
		name="CASTLE EATER GILDA",
		addresses=[0x2f3428],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="CASTLE EATER ATK",
		addresses=[0x2f3436],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(96),
		max_value=Max_ATK_Multiplier(96),
		is_little_endian=True, ),
	Attribute(
		name="CASTLE EATER DEF",
		addresses=[0x2f3438],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(64),
		max_value=Max_DEF_Multiplier(64),
		is_little_endian=True, ),
	Attribute(
		name="CASTLE EATER ITEM1",
		addresses=[0x2f3470],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CASTLE EATER ITEM2",
		addresses=[0x2f3472],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CASTLE EATER ITEM3",
		addresses=[0x2f3474],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#death mouse 0x2F348C
	Attribute(
		name="DEATH MOUSE HP",
		addresses=[0x2f34d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(5500),
		max_value=Max_HP_Multiplier(5500),
		is_little_endian=True,),
	Attribute(
		name="DEATH MOUSE ABS",
		addresses=[0x2f34de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True,),
	Attribute(
		name="DEATH MOUSE GILDA",
		addresses=[0x2f34e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="DEATH MOUSE ATK",
		addresses=[0x2f34ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="DEATH MOUSE DEF",
		addresses=[0x2f34f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="DEATH MOUSE ITEM1",
		addresses=[0x2f3528],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEATH MOUSE ITEM2",
		addresses=[0x2f352a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEATH MOUSE ITEM3",
		addresses=[0x2f352c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#vanguard 0x2F3544
	Attribute(
		name="VANGUARD HP",
		addresses=[0x2f3590],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(200),
		max_value=Max_HP_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD ABS",
		addresses=[0x2f3596],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(16),
		max_value=Max_ABS_Multiplier(16),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD GILDA",
		addresses=[0x2f3598],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(14),
		max_value=Max_GILDA_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD ATK",
		addresses=[0x2f35a6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(16),
		max_value=Max_ATK_Multiplier(16),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD DEF",
		addresses=[0x2f35a8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(5),
		max_value=Max_DEF_Multiplier(5),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD ITEM1",
		addresses=[0x2f35e0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD ITEM2",
		addresses=[0x2f35e2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD ITEM3",
		addresses=[0x2f35e4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#neo vanguard 0x2F35FC
	Attribute(
		name="NEO VANGUARD HP",
		addresses=[0x2f3648],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500),
		max_value=Max_HP_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD ABS",
		addresses=[0x2f364e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(72),
		max_value=Max_ABS_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD GILDA",
		addresses=[0x2f3650],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(81),
		max_value=Max_GILDA_Multiplier(81),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD ATK",
		addresses=[0x2f365e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(45),
		max_value=Max_ATK_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD DEF",
		addresses=[0x2f3660],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD ITEM1",
		addresses=[0x2f3698],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD ITEM2",
		addresses=[0x2f369a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="NEO VANGUARD ITEM3",
		addresses=[0x2f369c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#vanguard mk 2 0x2F36B4
	Attribute(
		name="VANGUARD MK 2 HP",
		addresses=[0x2f3700],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2000),
		max_value=Max_HP_Multiplier(2000),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 ABS",
		addresses=[0x2f3706],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 GILDA",
		addresses=[0x2f3708],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(135),
		max_value=Max_GILDA_Multiplier(135),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 ATK",
		addresses=[0x2f3716],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(110),
		max_value=Max_ATK_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 DEF",
		addresses=[0x2f3718],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 ITEM1",
		addresses=[0x2f3750],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 ITEM2",
		addresses=[0x2f3752],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="VANGUARD MK 2 ITEM3",
		addresses=[0x2f3754],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#nail burst (boss) 0x2F376C
	Attribute(
		name="NAIL BURST HP",
		addresses=[0x2f37b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(18000),
		max_value=Max_HP_Multiplier(18000),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST ABS",
		addresses=[0x2f37be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST GILDA",
		addresses=[0x2f37c0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(110),
		max_value=Max_GILDA_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST ATK",
		addresses=[0x2f37ce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(180),
		max_value=Max_ATK_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST DEF",
		addresses=[0x2f37d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST ITEM1",
		addresses=[0x2f3808],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST ITEM2",
		addresses=[0x2f380a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="NAIL BURST ITEM3",
		addresses=[0x2f380c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#froggy 0x2F3824
	Attribute(
		name="FROGGY HP",
		addresses=[0x2f3870],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(26),
		max_value=Max_HP_Multiplier(26),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY ABS",
		addresses=[0x2f3876],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY GILDA",
		addresses=[0x2f3878],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(6),
		max_value=Max_GILDA_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY ATK",
		addresses=[0x2f3886],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(6),
		max_value=Max_ATK_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY DEF",
		addresses=[0x2f3888],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY ITEM1",
		addresses=[0x2f38c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY ITEM2",
		addresses=[0x2f38c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="FROGGY ITEM3",
		addresses=[0x2f38c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#geron 0x2F38DC
	Attribute(
		name="GERON HP",
		addresses=[0x2f3928],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(235),
		max_value=Max_HP_Multiplier(235),
		is_little_endian=True, ),
	Attribute(
		name="GERON ABS",
		addresses=[0x2f392e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(46),
		max_value=Max_ABS_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="GERON GILDA",
		addresses=[0x2f3930],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(27),
		max_value=Max_GILDA_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="GERON ATK",
		addresses=[0x2f393e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(38),
		max_value=Max_ATK_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="GERON DEF",
		addresses=[0x2f3940],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(31),
		max_value=Max_DEF_Multiplier(31),
		is_little_endian=True, ),
	Attribute(
		name="GERON ITEM1",
		addresses=[0x2f3978],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="GERON ITEM2",
		addresses=[0x2f397a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="GERON ITEM3",
		addresses=[0x2f397c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#gamal 0x2F3994
	Attribute(
		name="GAMAL HP",
		addresses=[0x2f39e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1900),
		max_value=Max_HP_Multiplier(1900),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL ABS",
		addresses=[0x2f39e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL GILDA",
		addresses=[0x2f39e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL ATK",
		addresses=[0x2f39f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL DEF",
		addresses=[0x2f39f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(77),
		max_value=Max_DEF_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL ITEM1",
		addresses=[0x2f3a30],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL ITEM2",
		addresses=[0x2f3a32],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GAMAL ITEM3",
		addresses=[0x2f3a34],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#plutos 0x2F3A4C
	Attribute(
		name="PLUTOS HP",
		addresses=[0x2f3a98],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(5700),
		max_value=Max_HP_Multiplier(5700),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS ABS",
		addresses=[0x2f3a9e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS GILDA",
		addresses=[0x2f3aa0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS ATK",
		addresses=[0x2f3aae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS DEF",
		addresses=[0x2f3ab0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS ITEM1",
		addresses=[0x2f3ae8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS ITEM2",
		addresses=[0x2f3aea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="PLUTOS ITEM3",
		addresses=[0x2f3aec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#tore 0x2F3B04
	Attribute(
		name="TORE HP",
		addresses=[0x2f3b50],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(200),
		max_value=Max_HP_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="TORE ABS",
		addresses=[0x2f3b56],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(16),
		max_value=Max_ABS_Multiplier(16),
		is_little_endian=True, ),
	Attribute(
		name="TORE GILDA",
		addresses=[0x2f3b58],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(8),
		max_value=Max_GILDA_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="TORE ATK",
		addresses=[0x2f3b66],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(18),
		max_value=Max_ATK_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="TORE DEF",
		addresses=[0x2f3b68],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(8),
		max_value=Max_DEF_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="TORE ITEM1",
		addresses=[0x2f3ba0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TORE ITEM2",
		addresses=[0x2f3ba2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TORE ITEM3",
		addresses=[0x2f3ba4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#steam tore 0x2F3BBC
	Attribute(
		name="STEAM TORE HP",
		addresses=[0x2f3c08],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500),
		max_value=Max_HP_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE ABS",
		addresses=[0x2f3c0e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(100),
		max_value=Max_ABS_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE GILDA",
		addresses=[0x2f3c10],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(27),
		max_value=Max_GILDA_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE ATK",
		addresses=[0x2f3c1e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(50),
		max_value=Max_ATK_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE DEF",
		addresses=[0x2f3c20],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE ITEM1",
		addresses=[0x2f3c58],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE ITEM2",
		addresses=[0x2f3c5a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STEAM TORE ITEM3",
		addresses=[0x2f3c5c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#mad tore 0x2F3C74
	Attribute(
		name="MAD TORE HP",
		addresses=[0x2f3cc0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700),
		max_value=Max_HP_Multiplier(700),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE ABS",
		addresses=[0x2f3cc6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(140),
		max_value=Max_ABS_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE GILDA",
		addresses=[0x2f3cc8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(60),
		max_value=Max_GILDA_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE ATK",
		addresses=[0x2f3cd6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(77),
		max_value=Max_ATK_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE DEF",
		addresses=[0x2f3cd8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE ITEM1",
		addresses=[0x2f3d10],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE ITEM2",
		addresses=[0x2f3d12],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MAD TORE ITEM3",
		addresses=[0x2f3d14],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#great tree 0x2F3D2C
	Attribute(
		name="GREAT TREE HP",
		addresses=[0x2f3d78],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6600),
		max_value=Max_HP_Multiplier(6600),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE ABS",
		addresses=[0x2f3d7e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE GILDA",
		addresses=[0x2f3d80],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE ATK",
		addresses=[0x2f3d8e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE DEF",
		addresses=[0x2f3d90],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE ITEM1",
		addresses=[0x2f3dc8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE ITEM2",
		addresses=[0x2f3dca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GREAT TREE ITEM3",
		addresses=[0x2f3dcc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#kotore 0x2F3DE4
    Attribute(
        name="KOTORE HP",
        addresses=[0x2f3e30],
        number_of_bytes=2,
        min_value=Min_HP_Multiplier(10),
        max_value=Max_HP_Multiplier(10),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE ABS",
        addresses=[0x2f3e36],
        number_of_bytes=2,
        min_value=Min_ABS_Multiplier(0),
        max_value=Max_ABS_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE GILDA",
        addresses=[0x2f3e38],
        number_of_bytes=2,
        min_value=Min_GILDA_Multiplier(0),
        max_value=Max_GILDA_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE ATK",
        addresses=[0x2f3e46],
        number_of_bytes=2,
        min_value=Min_ATK_Multiplier(21),
        max_value=Max_ATK_Multiplier(21),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE DEF",
        addresses=[0x2f3e48],
        number_of_bytes=2,
        min_value=Min_DEF_Multiplier(0),
        max_value=Max_DEF_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE ITEM1",
        addresses=[0x2f3e80],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Sindain"),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE ITEM2",
        addresses=[0x2f3e82],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Sindain"),
        is_little_endian=True, ),
    Attribute(
        name="KOTORE ITEM3",
        addresses=[0x2f3e84],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Sindain"),
        is_little_endian=True, ),
#steam kotore 0x2F3E9C
    Attribute(
        name="STEAM KOTORE HP",
        addresses=[0x2f3ee8],
        number_of_bytes=2,
        min_value=Min_HP_Multiplier(108),
        max_value=Max_HP_Multiplier(108),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE ABS",
        addresses=[0x2f3eee],
        number_of_bytes=2,
        min_value=Min_ABS_Multiplier(0),
        max_value=Max_ABS_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE GILDA",
        addresses=[0x2f3ef0],
        number_of_bytes=2,
        min_value=Min_GILDA_Multiplier(0),
        max_value=Max_GILDA_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE ATK",
        addresses=[0x2f3efe],
        number_of_bytes=2,
        min_value=Min_ATK_Multiplier(45),
        max_value=Max_ATK_Multiplier(45),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE DEF",
        addresses=[0x2f3f00],
        number_of_bytes=2,
        min_value=Min_DEF_Multiplier(20),
        max_value=Max_DEF_Multiplier(20),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE ITEM1",
        addresses=[0x2f3f38],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Heim"),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE ITEM2",
        addresses=[0x2f3f3a],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Heim"),
        is_little_endian=True, ),
    Attribute(
        name="STEAM KOTORE ITEM3",
        addresses=[0x2f3f3c],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Heim"),
        is_little_endian=True, ),
#dorone 0x2F3F54
    Attribute(
        name="DORONE HP",
        addresses=[0x2f3fa0],
        number_of_bytes=2,
        min_value=Min_HP_Multiplier(200),
        max_value=Max_HP_Multiplier(200),
        is_little_endian=True, ),
    Attribute(
        name="DORONE ABS",
        addresses=[0x2f3fa6],
        number_of_bytes=2,
        min_value=Min_ABS_Multiplier(0),
        max_value=Max_ABS_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="DORONE GILDA",
        addresses=[0x2f3fa8],
        number_of_bytes=2,
        min_value=Min_GILDA_Multiplier(12),
        max_value=Max_GILDA_Multiplier(12),
        is_little_endian=True, ),
    Attribute(
        name="DORONE ATK",
        addresses=[0x2f3fb6],
        number_of_bytes=2,
        min_value=Min_ATK_Multiplier(68),
        max_value=Max_ATK_Multiplier(68),
        is_little_endian=True, ),
    Attribute(
        name="DORONE DEF",
        addresses=[0x2f3fb8],
        number_of_bytes=2,
        min_value=Min_DEF_Multiplier(10),
        max_value=Max_DEF_Multiplier(10),
        is_little_endian=True, ),
    Attribute(
        name="DORONE ITEM1",
        addresses=[0x2f3ff0],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Star"),
        is_little_endian=True, ),
    Attribute(
        name="DORONE ITEM2",
        addresses=[0x2f3ff2],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Star"),
        is_little_endian=True, ),
    Attribute(
        name="DORONE ITEM3",
        addresses=[0x2f3ff4],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Star"),
        is_little_endian=True, ),
#small tree 0x2F400C
    Attribute(
        name="SMALL TREE HP",
        addresses=[0x2f4058],
        number_of_bytes=2,
        min_value=Min_HP_Multiplier(5400),
        max_value=Max_HP_Multiplier(5400),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE ABS",
        addresses=[0x2f405e],
        number_of_bytes=2,
        min_value=Min_ABS_Multiplier(0),
        max_value=Max_ABS_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE GILDA",
        addresses=[0x2f4060],
        number_of_bytes=2,
        min_value=Min_GILDA_Multiplier(0),
        max_value=Max_GILDA_Multiplier(0),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE ATK",
        addresses=[0x2f406e],
        number_of_bytes=2,
        min_value=Min_ATK_Multiplier(142),
        max_value=Max_ATK_Multiplier(142),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE DEF",
        addresses=[0x2f4070],
        number_of_bytes=2,
        min_value=Min_DEF_Multiplier(92),
        max_value=Max_DEF_Multiplier(92),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE ITEM1",
        addresses=[0x2f40a8],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Zelmite"),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE ITEM2",
        addresses=[0x2f40aa],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Zelmite"),
        is_little_endian=True, ),
    Attribute(
        name="SMALL TREE ITEM3",
        addresses=[0x2f40ac],
        number_of_bytes=2,
        possible_values=ChooseItemDrops("Zelmite"),
        is_little_endian=True, ),
#hunter fox 0x2F40C4
	Attribute(
		name="HUNTER FOX HP",
		addresses=[0x2f4110],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(70),
		max_value=Max_HP_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX ABS",
		addresses=[0x2f4116],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(12),
		max_value=Max_ABS_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX GILDA",
		addresses=[0x2f4118],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(14),
		max_value=Max_GILDA_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX ATK",
		addresses=[0x2f4126],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(17),
		max_value=Max_ATK_Multiplier(17),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX DEF",
		addresses=[0x2f4128],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(11),
		max_value=Max_DEF_Multiplier(11),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX ITEM1",
		addresses=[0x2f4160],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX ITEM2",
		addresses=[0x2f4162],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="HUNTER FOX ITEM3",
		addresses=[0x2f4164],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#red fox 0x2F417C
	Attribute(
		name="RED FOX HP",
		addresses=[0x2f41c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550),
		max_value=Max_HP_Multiplier(550),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX ABS",
		addresses=[0x2f41ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX GILDA",
		addresses=[0x2f41d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX ATK",
		addresses=[0x2f41de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(71),
		max_value=Max_ATK_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX DEF",
		addresses=[0x2f41e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX ITEM1",
		addresses=[0x2f4218],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX ITEM2",
		addresses=[0x2f421a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="RED FOX ITEM3",
		addresses=[0x2f421c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#rifle wolf 0x2F4234
	Attribute(
		name="RIFLE WOLF HP",
		addresses=[0x2f4280],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(340),
		max_value=Max_HP_Multiplier(340),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF ABS",
		addresses=[0x2f4286],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(68),
		max_value=Max_ABS_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF GILDA",
		addresses=[0x2f4288],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(76),
		max_value=Max_GILDA_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF ATK",
		addresses=[0x2f4296],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF DEF",
		addresses=[0x2f4298],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(38),
		max_value=Max_DEF_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF ITEM1",
		addresses=[0x2f42d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF ITEM2",
		addresses=[0x2f42d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RIFLE WOLF ITEM3",
		addresses=[0x2f42d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#smiling wolf 0x2F42EC
	Attribute(
		name="SMILING WOLF HP",
		addresses=[0x2f4338],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8800),
		max_value=Max_HP_Multiplier(8800),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF ABS",
		addresses=[0x2f433e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF GILDA",
		addresses=[0x2f4340],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF ATK",
		addresses=[0x2f434e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF DEF",
		addresses=[0x2f4350],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF ITEM1",
		addresses=[0x2f4388],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF ITEM2",
		addresses=[0x2f438a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SMILING WOLF ITEM3",
		addresses=[0x2f438c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#baron balloon 0x2F43A4
	Attribute(
		name="BARON BALLOON HP",
		addresses=[0x2f43f0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(32),
		max_value=Max_HP_Multiplier(32),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON ABS",
		addresses=[0x2f43f6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(8),
		max_value=Max_ABS_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON GILDA",
		addresses=[0x2f43f8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(9),
		max_value=Max_GILDA_Multiplier(9),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON ATK",
		addresses=[0x2f4406],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(8),
		max_value=Max_ATK_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON DEF",
		addresses=[0x2f4408],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON ITEM1",
		addresses=[0x2f4440],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON ITEM2",
		addresses=[0x2f4442],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="BARON BALLOON ITEM3",
		addresses=[0x2f4444],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#flotsam balloon 0x2F445C
	Attribute(
		name="FLOTSAM BALLOON HP",
		addresses=[0x2f44a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(50),
		max_value=Max_HP_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON ABS",
		addresses=[0x2f44ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON GILDA",
		addresses=[0x2f44b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(14),
		max_value=Max_GILDA_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON ATK",
		addresses=[0x2f44be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(12),
		max_value=Max_ATK_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON DEF",
		addresses=[0x2f44c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(1),
		max_value=Max_DEF_Multiplier(1),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON ITEM1",
		addresses=[0x2f44f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON ITEM2",
		addresses=[0x2f44fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="FLOTSAM BALLOON ITEM3",
		addresses=[0x2f44fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#count balloon 0x2F4514
	Attribute(
		name="COUNT BALLOON HP",
		addresses=[0x2f4560],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(812),
		max_value=Max_HP_Multiplier(812),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON ABS",
		addresses=[0x2f4566],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(162),
		max_value=Max_ABS_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON GILDA",
		addresses=[0x2f4568],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON ATK",
		addresses=[0x2f4576],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(92),
		max_value=Max_ATK_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON DEF",
		addresses=[0x2f4578],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON ITEM1",
		addresses=[0x2f45b0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON ITEM2",
		addresses=[0x2f45b2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="COUNT BALLOON ITEM3",
		addresses=[0x2f45b4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#duke balloon 0x2F45CC
	Attribute(
		name="DUKE BALLOON HP",
		addresses=[0x2f4618],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(5600),
		max_value=Max_HP_Multiplier(5600),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON ABS",
		addresses=[0x2f461e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON GILDA",
		addresses=[0x2f4620],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON ATK",
		addresses=[0x2f462e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON DEF",
		addresses=[0x2f4630],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON ITEM1",
		addresses=[0x2f4668],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON ITEM2",
		addresses=[0x2f466a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DUKE BALLOON ITEM3",
		addresses=[0x2f466c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#tortoise 0x2F4684
	Attribute(
		name="TORTOISE HP",
		addresses=[0x2f46d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(100),
		max_value=Max_HP_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE ABS",
		addresses=[0x2f46d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(14),
		max_value=Max_ABS_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE GILDA",
		addresses=[0x2f46d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(15),
		max_value=Max_GILDA_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE ATK",
		addresses=[0x2f46e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(19),
		max_value=Max_ATK_Multiplier(19),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE DEF",
		addresses=[0x2f46e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(11),
		max_value=Max_DEF_Multiplier(11),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE ITEM1",
		addresses=[0x2f4720],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE ITEM2",
		addresses=[0x2f4722],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TORTOISE ITEM3",
		addresses=[0x2f4724],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#sea tortoise 0x2F473C
	Attribute(
		name="SEA TORTOISE HP",
		addresses=[0x2f4788],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(335),
		max_value=Max_HP_Multiplier(335),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE ABS",
		addresses=[0x2f478e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(66),
		max_value=Max_ABS_Multiplier(66),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE GILDA",
		addresses=[0x2f4790],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(36),
		max_value=Max_GILDA_Multiplier(36),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE ATK",
		addresses=[0x2f479e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(47),
		max_value=Max_ATK_Multiplier(47),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE DEF",
		addresses=[0x2f47a0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(37),
		max_value=Max_DEF_Multiplier(37),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE ITEM1",
		addresses=[0x2f47d8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE ITEM2",
		addresses=[0x2f47da],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA TORTOISE ITEM3",
		addresses=[0x2f47dc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#star tortoise 0x2F47F4
	Attribute(
		name="STAR TORTOISE HP",
		addresses=[0x2f4840],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(590),
		max_value=Max_HP_Multiplier(590),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE ABS",
		addresses=[0x2f4846],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(118),
		max_value=Max_ABS_Multiplier(118),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE GILDA",
		addresses=[0x2f4848],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE ATK",
		addresses=[0x2f4856],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(74),
		max_value=Max_ATK_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE DEF",
		addresses=[0x2f4858],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE ITEM1",
		addresses=[0x2f4890],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE ITEM2",
		addresses=[0x2f4892],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="STAR TORTOISE ITEM3",
		addresses=[0x2f4894],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#ebony tortoise 0x2F48AC
	Attribute(
		name="EBONY TORTOISE HP",
		addresses=[0x2f48f8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7800),
		max_value=Max_HP_Multiplier(7800),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE ABS",
		addresses=[0x2f48fe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE GILDA",
		addresses=[0x2f4900],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(145),
		max_value=Max_GILDA_Multiplier(145),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE ATK",
		addresses=[0x2f490e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE DEF",
		addresses=[0x2f4910],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE ITEM1",
		addresses=[0x2f4948],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE ITEM2",
		addresses=[0x2f494a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="EBONY TORTOISE ITEM3",
		addresses=[0x2f494c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#turtle 0x2F4964
	Attribute(
		name="TURTLE HP",
		addresses=[0x2f49b0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(50),
		max_value=Max_HP_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE ABS",
		addresses=[0x2f49b6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE GILDA",
		addresses=[0x2f49b8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(6),
		max_value=Max_GILDA_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE ATK",
		addresses=[0x2f49c6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(7),
		max_value=Max_ATK_Multiplier(7),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE DEF",
		addresses=[0x2f49c8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(2),
		max_value=Max_DEF_Multiplier(2),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE ITEM1",
		addresses=[0x2f4a00],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE ITEM2",
		addresses=[0x2f4a02],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="TURTLE ITEM3",
		addresses=[0x2f4a04],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#flintol 0x2F4A1C
	Attribute(
		name="FLINTOL HP",
		addresses=[0x2f4a68],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(220),
		max_value=Max_HP_Multiplier(220),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL ABS",
		addresses=[0x2f4a6e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(44),
		max_value=Max_ABS_Multiplier(44),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL GILDA",
		addresses=[0x2f4a70],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(42),
		max_value=Max_GILDA_Multiplier(42),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL ATK",
		addresses=[0x2f4a7e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(36),
		max_value=Max_ATK_Multiplier(36),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL DEF",
		addresses=[0x2f4a80],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(31),
		max_value=Max_DEF_Multiplier(31),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL ITEM1",
		addresses=[0x2f4ab8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL ITEM2",
		addresses=[0x2f4aba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="FLINTOL ITEM3",
		addresses=[0x2f4abc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#arkerath 0x2F4AD4
	Attribute(
		name="ARKERATH HP",
		addresses=[0x2f4b20],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550),
		max_value=Max_HP_Multiplier(550),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH ABS",
		addresses=[0x2f4b26],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH GILDA",
		addresses=[0x2f4b28],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH ATK",
		addresses=[0x2f4b36],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(71),
		max_value=Max_ATK_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH DEF",
		addresses=[0x2f4b38],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH ITEM1",
		addresses=[0x2f4b70],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH ITEM2",
		addresses=[0x2f4b72],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ARKERATH ITEM3",
		addresses=[0x2f4b74],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#bolter 0x2F4B8C
	Attribute(
		name="BOLTER HP",
		addresses=[0x2f4bd8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(5800),
		max_value=Max_HP_Multiplier(5800),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER ABS",
		addresses=[0x2f4bde],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER GILDA",
		addresses=[0x2f4be0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(85),
		max_value=Max_GILDA_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER ATK",
		addresses=[0x2f4bee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER DEF",
		addresses=[0x2f4bf0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER ITEM1",
		addresses=[0x2f4c28],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER ITEM2",
		addresses=[0x2f4c2a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BOLTER ITEM3",
		addresses=[0x2f4c2c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#clown 0x2F4C44
	Attribute(
		name="CLOWN HP",
		addresses=[0x2f4c90],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(30),
		max_value=Max_HP_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN ABS",
		addresses=[0x2f4c96],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN GILDA",
		addresses=[0x2f4c98],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(6),
		max_value=Max_GILDA_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN ATK",
		addresses=[0x2f4ca6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(7),
		max_value=Max_ATK_Multiplier(7),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN DEF",
		addresses=[0x2f4ca8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN ITEM1",
		addresses=[0x2f4ce0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN ITEM2",
		addresses=[0x2f4ce2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="CLOWN ITEM3",
		addresses=[0x2f4ce4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#griffon soldier  0x2F4CFC
	Attribute(
		name="GRIFFON SOLDIER HP",
		addresses=[0x2f4d48],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(420),
		max_value=Max_HP_Multiplier(420),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER ABS",
		addresses=[0x2f4d4e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(84),
		max_value=Max_ABS_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER GILDA",
		addresses=[0x2f4d50],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(33),
		max_value=Max_GILDA_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER ATK",
		addresses=[0x2f4d5e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(48),
		max_value=Max_ATK_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER DEF",
		addresses=[0x2f4d60],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(42),
		max_value=Max_DEF_Multiplier(42),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER ITEM1",
		addresses=[0x2f4d98],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER ITEM2",
		addresses=[0x2f4d9a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="GRIFFON SOLDIER ITEM3",
		addresses=[0x2f4d9c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#evil performer 0x2F4DB4
	Attribute(
		name="EVIL PERFORMER HP",
		addresses=[0x2f4e00],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(888),
		max_value=Max_HP_Multiplier(888),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER ABS",
		addresses=[0x2f4e06],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(176),
		max_value=Max_ABS_Multiplier(176),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER GILDA",
		addresses=[0x2f4e08],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(135),
		max_value=Max_GILDA_Multiplier(135),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER ATK",
		addresses=[0x2f4e16],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(98),
		max_value=Max_ATK_Multiplier(98),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER DEF",
		addresses=[0x2f4e18],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(64),
		max_value=Max_DEF_Multiplier(64),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER ITEM1",
		addresses=[0x2f4e50],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER ITEM2",
		addresses=[0x2f4e52],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL PERFORMER ITEM3",
		addresses=[0x2f4e54],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#dark alchemist 0x2F4E6C
	Attribute(
		name="DARK ALCHEMIST HP",
		addresses=[0x2f4eb8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8600),
		max_value=Max_HP_Multiplier(8600),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST ABS",
		addresses=[0x2f4ebe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST GILDA",
		addresses=[0x2f4ec0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST ATK",
		addresses=[0x2f4ece],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST DEF",
		addresses=[0x2f4ed0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST ITEM1",
		addresses=[0x2f4f08],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST ITEM2",
		addresses=[0x2f4f0a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK ALCHEMIST ITEM3",
		addresses=[0x2f4f0c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#tigriff 0x2F4F24
	Attribute(
		name="TIGRIFF HP",
		addresses=[0x2f4f70],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(140),
		max_value=Max_HP_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF ABS",
		addresses=[0x2f4f76],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF GILDA",
		addresses=[0x2f4f78],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(24),
		max_value=Max_GILDA_Multiplier(24),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF ATK",
		addresses=[0x2f4f86],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(21),
		max_value=Max_ATK_Multiplier(21),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF DEF",
		addresses=[0x2f4f88],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(13),
		max_value=Max_DEF_Multiplier(13),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF ITEM1",
		addresses=[0x2f4fc0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF ITEM2",
		addresses=[0x2f4fc2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="TIGRIFF ITEM3",
		addresses=[0x2f4fc4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#chimera 0x2F4FDC
	Attribute(
		name="CHIMERA HP",
		addresses=[0x2f5028],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(490),
		max_value=Max_HP_Multiplier(490),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA ABS",
		addresses=[0x2f502e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(96),
		max_value=Max_ABS_Multiplier(96),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA GILDA",
		addresses=[0x2f5030],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA ATK",
		addresses=[0x2f503e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(54),
		max_value=Max_ATK_Multiplier(54),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA DEF",
		addresses=[0x2f5040],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(45),
		max_value=Max_DEF_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA ITEM1",
		addresses=[0x2f5078],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA ITEM2",
		addresses=[0x2f507a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="CHIMERA ITEM3",
		addresses=[0x2f507c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#leogriff 0x2F5094
	Attribute(
		name="LEOGRIFF HP",
		addresses=[0x2f50e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2500),
		max_value=Max_HP_Multiplier(2500),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF ABS",
		addresses=[0x2f50e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(195),
		max_value=Max_ABS_Multiplier(195),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF GILDA",
		addresses=[0x2f50e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF ATK",
		addresses=[0x2f50f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(110),
		max_value=Max_ATK_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF DEF",
		addresses=[0x2f50f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF ITEM1",
		addresses=[0x2f5130],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF ITEM2",
		addresses=[0x2f5132],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LEOGRIFF ITEM3",
		addresses=[0x2f5134],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#sphinx (boss) 0x2F514C
	Attribute(
		name="SPHINX HP",
		addresses=[0x2f5198],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(20000),
		max_value=Max_HP_Multiplier(20000),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX ABS",
		addresses=[0x2f519e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX GILDA",
		addresses=[0x2f51a0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(80),
		max_value=Max_GILDA_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX ATK",
		addresses=[0x2f51ae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(190),
		max_value=Max_ATK_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX DEF",
		addresses=[0x2f51b0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX ITEM1",
		addresses=[0x2f51e8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX ITEM2",
		addresses=[0x2f51ea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPHINX ITEM3",
		addresses=[0x2f51ec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#pixie 0x2F5204
	Attribute(
		name="PIXIE HP",
		addresses=[0x2f5250],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(80),
		max_value=Max_HP_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE ABS",
		addresses=[0x2f5256],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(8),
		max_value=Max_ABS_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE GILDA",
		addresses=[0x2f5258],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(5),
		max_value=Max_GILDA_Multiplier(5),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE ATK",
		addresses=[0x2f5266],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(16),
		max_value=Max_ATK_Multiplier(16),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE DEF",
		addresses=[0x2f5268],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(5),
		max_value=Max_DEF_Multiplier(5),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE ITEM1",
		addresses=[0x2f52a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE ITEM2",
		addresses=[0x2f52a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="PIXIE ITEM3",
		addresses=[0x2f52a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#sylph 0x2F52BC
	Attribute(
		name="SYLPH HP",
		addresses=[0x2f5308],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH ABS",
		addresses=[0x2f530e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH GILDA",
		addresses=[0x2f5310],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH ATK",
		addresses=[0x2f531e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(73),
		max_value=Max_ATK_Multiplier(73),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH DEF",
		addresses=[0x2f5320],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(57),
		max_value=Max_DEF_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH ITEM1",
		addresses=[0x2f5358],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH ITEM2",
		addresses=[0x2f535a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SYLPH ITEM3",
		addresses=[0x2f535c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#faerie 0x2F5374
	Attribute(
		name="FAERIE HP",
		addresses=[0x2f53c0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4600),
		max_value=Max_HP_Multiplier(4600),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE ABS",
		addresses=[0x2f53c6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE GILDA",
		addresses=[0x2f53c8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE ATK",
		addresses=[0x2f53d6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE DEF",
		addresses=[0x2f53d8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(99),
		max_value=Max_DEF_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE ITEM1",
		addresses=[0x2f5410],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE ITEM2",
		addresses=[0x2f5412],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FAERIE ITEM3",
		addresses=[0x2f5414],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#imp 0x2F542C
	Attribute(
		name="IMP HP",
		addresses=[0x2f5478],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8900),
		max_value=Max_HP_Multiplier(8900),
		is_little_endian=True, ),
	Attribute(
		name="IMP ABS",
		addresses=[0x2f547e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="IMP GILDA",
		addresses=[0x2f5480],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="IMP ATK",
		addresses=[0x2f548e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(162),
		max_value=Max_ATK_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="IMP DEF",
		addresses=[0x2f5490],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="IMP ITEM1",
		addresses=[0x2f54c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IMP ITEM2",
		addresses=[0x2f54ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IMP ITEM3",
		addresses=[0x2f54cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#linda (boss) 0x2F54E4
	Attribute(
		name="LINDA HP",
		addresses=[0x2f5530],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(400),
		max_value=Max_HP_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="LINDA ABS",
		addresses=[0x2f5536],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="LINDA GILDA",
		addresses=[0x2f5538],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(0),
		max_value=Max_GILDA_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="LINDA ATK",
		addresses=[0x2f5546],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(13),
		max_value=Max_ATK_Multiplier(13),
		is_little_endian=True, ),
	Attribute(
		name="LINDA DEF",
		addresses=[0x2f5548],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="LINDA ITEM1",
		addresses=[0x2f5580],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="LINDA ITEM2",
		addresses=[0x2f5582],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="LINDA ITEM3",
		addresses=[0x2f5584],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#elfas 0x2F559C
	Attribute(
		name="ELFAS HP",
		addresses=[0x2f55e8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(360),
		max_value=Max_HP_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS ABS",
		addresses=[0x2f55ee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS GILDA",
		addresses=[0x2f55f0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS ATK",
		addresses=[0x2f55fe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(26),
		max_value=Max_ATK_Multiplier(26),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS DEF",
		addresses=[0x2f5600],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS ITEM1",
		addresses=[0x2f5638],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS ITEM2",
		addresses=[0x2f563a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="ELFAS ITEM3",
		addresses=[0x2f563c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#moonflowephant 0x2F5654
	Attribute(
		name="MOONFLOWER ELEPHANT HP",
		addresses=[0x2f56a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1500),
		max_value=Max_HP_Multiplier(1500),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT ABS",
		addresses=[0x2f56a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(196),
		max_value=Max_ABS_Multiplier(196),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT GILDA",
		addresses=[0x2f56a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT ATK",
		addresses=[0x2f56b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(105),
		max_value=Max_ATK_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT DEF",
		addresses=[0x2f56b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT ITEM1",
		addresses=[0x2f56f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT ITEM2",
		addresses=[0x2f56f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOONFLOWER ELEPHANT ITEM3",
		addresses=[0x2f56f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#behemoth 0x2F570C
	Attribute(
		name="BEHEMOTH HP",
		addresses=[0x2f5758],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6500),
		max_value=Max_HP_Multiplier(6500),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH ABS",
		addresses=[0x2f575e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH GILDA",
		addresses=[0x2f5760],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH ATK",
		addresses=[0x2f576e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH DEF",
		addresses=[0x2f5770],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH ITEM1",
		addresses=[0x2f57a8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH ITEM2",
		addresses=[0x2f57aa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BEHEMOTH ITEM3",
		addresses=[0x2f57ac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#himarra 0x2F57C4
	Attribute(
		name="HIMARRA HP",
		addresses=[0x2f5810],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(55),
		max_value=Max_HP_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA ABS",
		addresses=[0x2f5816],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA GILDA",
		addresses=[0x2f5818],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA ATK",
		addresses=[0x2f5826],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(14),
		max_value=Max_ATK_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA DEF",
		addresses=[0x2f5828],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(6),
		max_value=Max_DEF_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA ITEM1",
		addresses=[0x2f5860],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA ITEM2",
		addresses=[0x2f5862],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="HIMARRA ITEM3",
		addresses=[0x2f5864],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#balalla 0x2F587C
	Attribute(
		name="BALALLA HP",
		addresses=[0x2f58c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA ABS",
		addresses=[0x2f58ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA GILDA",
		addresses=[0x2f58d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA ATK",
		addresses=[0x2f58de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(74),
		max_value=Max_ATK_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA DEF",
		addresses=[0x2f58e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA ITEM1",
		addresses=[0x2f5918],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA ITEM2",
		addresses=[0x2f591a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BALALLA ITEM3",
		addresses=[0x2f591c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#stormflower 0x2F5934
	Attribute(
		name="STORMFLOWER HP",
		addresses=[0x2f5980],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2700),
		max_value=Max_HP_Multiplier(2700),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER ABS",
		addresses=[0x2f5986],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER GILDA",
		addresses=[0x2f5988],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(90),
		max_value=Max_GILDA_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER ATK",
		addresses=[0x2f5996],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER DEF",
		addresses=[0x2f5998],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(88),
		max_value=Max_DEF_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER ITEM1",
		addresses=[0x2f59d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER ITEM2",
		addresses=[0x2f59d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="STORMFLOWER ITEM3",
		addresses=[0x2f59d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mandora (boss) 0x2F59EC
	Attribute(
		name="MANDORA HP",
		addresses=[0x2f5a38],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10000),
		max_value=Max_HP_Multiplier(10000),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA ABS",
		addresses=[0x2f5a3e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA GILDA",
		addresses=[0x2f5a40],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA ATK",
		addresses=[0x2f5a4e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(170),
		max_value=Max_ATK_Multiplier(170),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA DEF",
		addresses=[0x2f5a50],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA ITEM1",
		addresses=[0x2f5a88],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA ITEM2",
		addresses=[0x2f5a8a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MANDORA ITEM3",
		addresses=[0x2f5a8c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#gyumo 0x2F5AA4
	Attribute(
		name="GYUMO HP",
		addresses=[0x2f5af0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(160),
		max_value=Max_HP_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO ABS",
		addresses=[0x2f5af6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(18),
		max_value=Max_ABS_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO GILDA",
		addresses=[0x2f5af8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(21),
		max_value=Max_GILDA_Multiplier(21),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO ATK",
		addresses=[0x2f5b06],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(19),
		max_value=Max_ATK_Multiplier(19),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO DEF",
		addresses=[0x2f5b08],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(10),
		max_value=Max_DEF_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO ITEM1",
		addresses=[0x2f5b40],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO ITEM2",
		addresses=[0x2f5b42],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="GYUMO ITEM3",
		addresses=[0x2f5b44],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#blumo 0x2F5B5C
	Attribute(
		name="BLUMO HP",
		addresses=[0x2f5ba8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(780),
		max_value=Max_HP_Multiplier(780),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO ABS",
		addresses=[0x2f5bae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(156),
		max_value=Max_ABS_Multiplier(156),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO GILDA",
		addresses=[0x2f5bb0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO ATK",
		addresses=[0x2f5bbe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(82),
		max_value=Max_ATK_Multiplier(82),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO DEF",
		addresses=[0x2f5bc0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO ITEM1",
		addresses=[0x2f5bf8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO ITEM2",
		addresses=[0x2f5bfa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BLUMO ITEM3",
		addresses=[0x2f5bfc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#cabuble 0x2F5C14
	Attribute(
		name="CABUBLE HP",
		addresses=[0x2f5c60],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2800),
		max_value=Max_HP_Multiplier(2800),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE ABS",
		addresses=[0x2f5c66],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE GILDA",
		addresses=[0x2f5c68],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE ATK",
		addresses=[0x2f5c76],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE DEF",
		addresses=[0x2f5c78],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(88),
		max_value=Max_DEF_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE ITEM1",
		addresses=[0x2f5cb0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE ITEM2",
		addresses=[0x2f5cb2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="CABUBLE ITEM3",
		addresses=[0x2f5cb4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#minotaurus 0x2F5CCC
	Attribute(
		name="MINOTAURUS HP",
		addresses=[0x2f5d18],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11300),
		max_value=Max_HP_Multiplier(11300),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS ABS",
		addresses=[0x2f5d1e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS GILDA",
		addresses=[0x2f5d20],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS ATK",
		addresses=[0x2f5d2e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS DEF",
		addresses=[0x2f5d30],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS ITEM1",
		addresses=[0x2f5d68],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS ITEM2",
		addresses=[0x2f5d6a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MINOTAURUS ITEM3",
		addresses=[0x2f5d6c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#nightstalker 0x2F5D84
	Attribute(
		name="NIGHTSTALKER HP",
		addresses=[0x2f5dd0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(43),
		max_value=Max_HP_Multiplier(43),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER ABS",
		addresses=[0x2f5dd6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(8),
		max_value=Max_ABS_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER GILDA",
		addresses=[0x2f5dd8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(9),
		max_value=Max_GILDA_Multiplier(9),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER ATK",
		addresses=[0x2f5de6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(9),
		max_value=Max_ATK_Multiplier(9),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER DEF",
		addresses=[0x2f5de8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER ITEM1",
		addresses=[0x2f5e20],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER ITEM2",
		addresses=[0x2f5e22],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="NIGHTSTALKER ITEM3",
		addresses=[0x2f5e24],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#ragstink 0x2F5E3C
	Attribute(
		name="RAGSTINK HP",
		addresses=[0x2f5e88],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(320),
		max_value=Max_HP_Multiplier(320),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK ABS",
		addresses=[0x2f5e8e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(64),
		max_value=Max_ABS_Multiplier(64),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK GILDA",
		addresses=[0x2f5e90],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(39),
		max_value=Max_GILDA_Multiplier(39),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK ATK",
		addresses=[0x2f5e9e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK DEF",
		addresses=[0x2f5ea0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(30),
		max_value=Max_DEF_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK ITEM1",
		addresses=[0x2f5ed8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK ITEM2",
		addresses=[0x2f5eda],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="RAGSTINK ITEM3",
		addresses=[0x2f5edc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#leech 0x2F5EF4
	Attribute(
		name="LEECH HP",
		addresses=[0x2f5f40],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1160),
		max_value=Max_HP_Multiplier(1160),
		is_little_endian=True, ),
	Attribute(
		name="LEECH ABS",
		addresses=[0x2f5f46],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="LEECH GILDA",
		addresses=[0x2f5f48],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="LEECH ATK",
		addresses=[0x2f5f56],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(115),
		max_value=Max_ATK_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="LEECH DEF",
		addresses=[0x2f5f58],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="LEECH ITEM1",
		addresses=[0x2f5f90],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LEECH ITEM2",
		addresses=[0x2f5f92],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LEECH ITEM3",
		addresses=[0x2f5f94],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#wraith 0x2F5FAC
	Attribute(
		name="WRAITH HP",
		addresses=[0x2f5ff8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10700),
		max_value=Max_HP_Multiplier(10700),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH ABS",
		addresses=[0x2f5ffe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH GILDA",
		addresses=[0x2f6000],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(101),
		max_value=Max_GILDA_Multiplier(101),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH ATK",
		addresses=[0x2f600e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH DEF",
		addresses=[0x2f6010],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH ITEM1",
		addresses=[0x2f6048],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH ITEM2",
		addresses=[0x2f604a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WRAITH ITEM3",
		addresses=[0x2f604c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#dragon 0x2F6064
	Attribute(
		name="DRAGON HP",
		addresses=[0x2f60b0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON ABS",
		addresses=[0x2f60b6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(50),
		max_value=Max_ABS_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON GILDA",
		addresses=[0x2f60b8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON ATK",
		addresses=[0x2f60c6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(33),
		max_value=Max_ATK_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON DEF",
		addresses=[0x2f60c8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(25),
		max_value=Max_DEF_Multiplier(25),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON ITEM1",
		addresses=[0x2f6100],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON ITEM2",
		addresses=[0x2f6102],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="DRAGON ITEM3",
		addresses=[0x2f6104],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#red dragon 0x2F611C
	Attribute(
		name="RED DRAGON HP",
		addresses=[0x2f6168],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900),
		max_value=Max_HP_Multiplier(900),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON ABS",
		addresses=[0x2f616e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(118),
		max_value=Max_ABS_Multiplier(118),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON GILDA",
		addresses=[0x2f6170],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(132),
		max_value=Max_GILDA_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON ATK",
		addresses=[0x2f617e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(60),
		max_value=Max_ATK_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON DEF",
		addresses=[0x2f6180],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(49),
		max_value=Max_DEF_Multiplier(49),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON ITEM1",
		addresses=[0x2f6180],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON ITEM2",
		addresses=[0x2f61ba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RED DRAGON ITEM3",
		addresses=[0x2f61bc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#earth dragon 0x2F61D4
	Attribute(
		name="EARTH DRAGON HP",
		addresses=[0x2f6220],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2500),
		max_value=Max_HP_Multiplier(2500),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON ABS",
		addresses=[0x2f6226],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON GILDA",
		addresses=[0x2f6228],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON ATK",
		addresses=[0x2f6236],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(120),
		max_value=Max_ATK_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON DEF",
		addresses=[0x2f6238],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(75),
		max_value=Max_DEF_Multiplier(75),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON ITEM1",
		addresses=[0x2f6270],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON ITEM2",
		addresses=[0x2f6272],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EARTH DRAGON ITEM3",
		addresses=[0x2f6274],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#tiamat 0x2F628C
	Attribute(
		name="TIAMAT HP",
		addresses=[0x2f62d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11400),
		max_value=Max_HP_Multiplier(11400),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT ABS",
		addresses=[0x2f62de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(600),
		max_value=Max_ABS_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT GILDA",
		addresses=[0x2f62e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(83),
		max_value=Max_GILDA_Multiplier(83),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT ATK",
		addresses=[0x2f62ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(117),
		max_value=Max_ATK_Multiplier(117),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT DEF",
		addresses=[0x2f62f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(83),
		max_value=Max_DEF_Multiplier(83),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT ITEM1",
		addresses=[0x2f6328],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT ITEM2",
		addresses=[0x2f632a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TIAMAT ITEM3",
		addresses=[0x2f632c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#memo eater (boss) 0x2F6344
	Attribute(
		name="MEMO EATER HP",
		addresses=[0x2f6390],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(450),
		max_value=Max_HP_Multiplier(450),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER ABS",
		addresses=[0x2f6396],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(0),
		max_value=Max_ABS_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER GILDA",
		addresses=[0x2f6398],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(0),
		max_value=Max_GILDA_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER ATK",
		addresses=[0x2f63a6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(37),
		max_value=Max_ATK_Multiplier(37),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER DEF",
		addresses=[0x2f63a8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(30),
		max_value=Max_DEF_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER ITEM1",
		addresses=[0x2f63e0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER ITEM2",
		addresses=[0x2f63e2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MEMO EATER ITEM3",
		addresses=[0x2f63e4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#burger 0x2F63FC
	Attribute(
		name="BURGER HP",
		addresses=[0x2f6448],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(450),
		max_value=Max_HP_Multiplier(450),
		is_little_endian=True, ),
	Attribute(
		name="BURGER ABS",
		addresses=[0x2f644e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(90),
		max_value=Max_ABS_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="BURGER GILDA",
		addresses=[0x2f6450],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="BURGER ATK",
		addresses=[0x2f645e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(52),
		max_value=Max_ATK_Multiplier(52),
		is_little_endian=True, ),
	Attribute(
		name="BURGER DEF",
		addresses=[0x2f6460],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="BURGER ITEM1",
		addresses=[0x2f6498],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BURGER ITEM2",
		addresses=[0x2f649a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BURGER ITEM3",
		addresses=[0x2f649c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#stormy 0x2F64B4
	Attribute(
		name="STORMY HP",
		addresses=[0x2f65b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1600),
		max_value=Max_HP_Multiplier(1600),
		is_little_endian=True, ),
	Attribute(
		name="STORMY ABS",
		addresses=[0x2f65be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(180),
		max_value=Max_ABS_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="STORMY GILDA",
		addresses=[0x2f65c0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="STORMY ATK",
		addresses=[0x2f65c0],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(105),
		max_value=Max_ATK_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="STORMY DEF",
		addresses=[0x2f65d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="STORMY ITEM1",
		addresses=[0x2f6608],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="STORMY ITEM2",
		addresses=[0x2f660a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="STORMY ITEM3",
		addresses=[0x2f660c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#ladha 0x2F656C
	Attribute(
		name="LADHA HP",
		addresses=[0x2f65b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7700),
		max_value=Max_HP_Multiplier(7700),
		is_little_endian=True, ),
	Attribute(
		name="LADHA ABS",
		addresses=[0x2f65be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="LADHA GILDA",
		addresses=[0x2f65be],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="LADHA ATK",
		addresses=[0x2f65ce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="LADHA DEF",
		addresses=[0x2f65d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="LADHA ITEM1",
		addresses=[0x2f6608],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="LADHA ITEM2",
		addresses=[0x2f660a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="LADHA ITEM3",
		addresses=[0x2f660c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#spider lady (RBW) 0x2F6624
	Attribute(
		name="SPIDER LADY RBW HP",
		addresses=[0x2f6670],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(95),
		max_value=Max_HP_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW ABS",
		addresses=[0x2f6676],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(14),
		max_value=Max_ABS_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW GILDA",
		addresses=[0x2f6678],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(15),
		max_value=Max_GILDA_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW ATK",
		addresses=[0x2f6686],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(15),
		max_value=Max_ATK_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW DEF",
		addresses=[0x2f6688],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(5),
		max_value=Max_DEF_Multiplier(5),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW ITEM1",
		addresses=[0x2f66c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW ITEM2",
		addresses=[0x2f66c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY RBW ITEM3",
		addresses=[0x2f66c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#shiva 0x2F66DC
	Attribute(
		name="SHIVA HP",
		addresses=[0x2f6728],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(250),
		max_value=Max_HP_Multiplier(250),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA ABS",
		addresses=[0x2f672e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(50),
		max_value=Max_ABS_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA GILDA",
		addresses=[0x2f6730],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA ATK",
		addresses=[0x2f673e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(43),
		max_value=Max_ATK_Multiplier(43),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA DEF",
		addresses=[0x2f6740],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(25),
		max_value=Max_DEF_Multiplier(25),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA ITEM1",
		addresses=[0x2f6778],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA ITEM2",
		addresses=[0x2f677a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SHIVA ITEM3",
		addresses=[0x2f677c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#spider lady (zmm) 0x2F6624
	Attribute(
		name="SPIDER LADY ZMM HP",
		addresses=[0x2f67e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4800),
		max_value=Max_HP_Multiplier(4800),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM ABS",
		addresses=[0x2f67e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM GILDA",
		addresses=[0x2f67e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM ATK",
		addresses=[0x2f67f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM DEF",
		addresses=[0x2f67f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM ITEM1",
		addresses=[0x2f6830],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM ITEM2",
		addresses=[0x2f6832],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPIDER LADY ZMM ITEM3",
		addresses=[0x2f6834],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#bambamchoo 0x2F684C
	Attribute(
		name="BAMBAMCHOO HP",
		addresses=[0x2f6898],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10100),
		max_value=Max_HP_Multiplier(10100),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO ABS",
		addresses=[0x2f689e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO GILDA",
		addresses=[0x2f68a0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO ATK",
		addresses=[0x2f68ae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO DEF",
		addresses=[0x2f68b0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO ITEM1",
		addresses=[0x2f68e8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO ITEM2",
		addresses=[0x2f68ea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BAMBAMCHOO ITEM3",
		addresses=[0x2f68ec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#fire element 0x2F6904
	Attribute(
		name="FIRE ELEMENT HP",
		addresses=[0x2f6950],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(85),
		max_value=Max_HP_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT ABS",
		addresses=[0x2f6956],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(14),
		max_value=Max_ABS_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT GILDA",
		addresses=[0x2f6958],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(15),
		max_value=Max_GILDA_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT ATK",
		addresses=[0x2f6966],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(18),
		max_value=Max_ATK_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT DEF",
		addresses=[0x2f6968],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(10),
		max_value=Max_DEF_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT ITEM1",
		addresses=[0x2f69a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT ITEM2",
		addresses=[0x2f69a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE ELEMENT ITEM3",
		addresses=[0x2f69a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#fire spirit 0x2F69BC
	Attribute(
		name="FIRE SPIRIT HP",
		addresses=[0x2f6a08],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT ABS",
		addresses=[0x2f6a0e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT GILDA",
		addresses=[0x2f6a10],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT ATK",
		addresses=[0x2f6a1e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(74),
		max_value=Max_ATK_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT DEF",
		addresses=[0x2f6a20],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT ITEM1",
		addresses=[0x2f6a58],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT ITEM2",
		addresses=[0x2f6a5a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE SPIRIT ITEM3",
		addresses=[0x2f6a5c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#fire ghost 0x2F6A74
	Attribute(
		name="FIRE GHOST HP",
		addresses=[0x2f6ac0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3100),
		max_value=Max_HP_Multiplier(3100),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST ABS",
		addresses=[0x2f6ac6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST GILDA",
		addresses=[0x2f6ac8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(80),
		max_value=Max_GILDA_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST ATK",
		addresses=[0x2f6ad6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST DEF",
		addresses=[0x2f6ad8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(89),
		max_value=Max_DEF_Multiplier(89),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST ITEM1",
		addresses=[0x2f6b10],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST ITEM2",
		addresses=[0x2f6b12],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GHOST ITEM3",
		addresses=[0x2f6b14],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#magma servant 0x2F6B2C
	Attribute(
		name="MAGMA SERVANT HP",
		addresses=[0x2f6b78],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9500),
		max_value=Max_HP_Multiplier(9500),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT ABS",
		addresses=[0x2f6b7e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT GILDA",
		addresses=[0x2f6b80],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT ATK",
		addresses=[0x2f6b8e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(167),
		max_value=Max_ATK_Multiplier(167),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT DEF",
		addresses=[0x2f6b90],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT ITEM1",
		addresses=[0x2f6bc8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT ITEM2",
		addresses=[0x2f6bca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MAGMA SERVANT ITEM3",
		addresses=[0x2f6bcc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#ice element 0x2F6BE4
	Attribute(
		name="ICE ELEMENT HP",
		addresses=[0x2f6c30],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(85),
		max_value=Max_HP_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT ABS",
		addresses=[0x2f6c36],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(14),
		max_value=Max_ABS_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT GILDA",
		addresses=[0x2f6c38],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(15),
		max_value=Max_GILDA_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT ATK",
		addresses=[0x2f6c46],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(18),
		max_value=Max_ATK_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT DEF",
		addresses=[0x2f6c48],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(10),
		max_value=Max_DEF_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT ITEM1",
		addresses=[0x2f6c80],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT ITEM2",
		addresses=[0x2f6c82],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="ICE ELEMENT ITEM3",
		addresses=[0x2f6c84],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#ice spirit 0x2F6C9C
	Attribute(
		name="ICE SPIRIT HP",
		addresses=[0x2f6ce8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT ABS",
		addresses=[0x2f6cee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT GILDA",
		addresses=[0x2f6cf0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT ATK",
		addresses=[0x2f6cfe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(74),
		max_value=Max_ATK_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT DEF",
		addresses=[0x2f6d00],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT ITEM1",
		addresses=[0x2f6d38],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT ITEM2",
		addresses=[0x2f6d3a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ICE SPIRIT ITEM3",
		addresses=[0x2f6d3c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#snow ghost 0x2F6D54
	Attribute(
		name="SNOW GHOST HP",
		addresses=[0x2f6da0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3000),
		max_value=Max_HP_Multiplier(3000),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST ABS",
		addresses=[0x2f6da6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST GILDA",
		addresses=[0x2f6da8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(80),
		max_value=Max_GILDA_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST ATK",
		addresses=[0x2f6db6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST DEF",
		addresses=[0x2f6db8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(88),
		max_value=Max_DEF_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST ITEM1",
		addresses=[0x2f6df0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST ITEM2",
		addresses=[0x2f6df2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SNOW GHOST ITEM3",
		addresses=[0x2f6df4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#snow servant 0x2F6E0C
	Attribute(
		name="SNOW SERVANT HP",
		addresses=[0x2f6e58],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9500),
		max_value=Max_HP_Multiplier(9500),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT ABS",
		addresses=[0x2f6e5e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT GILDA",
		addresses=[0x2f6e60],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT ATK",
		addresses=[0x2f6e6e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(167),
		max_value=Max_ATK_Multiplier(167),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT DEF",
		addresses=[0x2f6e70],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT ITEM1",
		addresses=[0x2f6ea8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT ITEM2",
		addresses=[0x2f6eaa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SNOW SERVANT ITEM3",
		addresses=[0x2f6eac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#zappy 0x2F6EC4
	Attribute(
		name="ZAPPY HP",
		addresses=[0x2f6f10],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY ABS",
		addresses=[0x2f6f16],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(70),
		max_value=Max_ABS_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY GILDA",
		addresses=[0x2f6f18],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(36),
		max_value=Max_GILDA_Multiplier(36),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY ATK",
		addresses=[0x2f6f26],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(45),
		max_value=Max_ATK_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY DEF",
		addresses=[0x2f6f28],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(33),
		max_value=Max_DEF_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY ITEM1",
		addresses=[0x2f6f60],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY ITEM2",
		addresses=[0x2f6f62],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="ZAPPY ITEM3",
		addresses=[0x2f6f64],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#thunder spirit 0x2F6F7C
	Attribute(
		name="THUNDER SPIRIT HP",
		addresses=[0x2f6fc8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(580),
		max_value=Max_HP_Multiplier(580),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT ABS",
		addresses=[0x2f6fce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(116),
		max_value=Max_ABS_Multiplier(116),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT GILDA",
		addresses=[0x2f6fd0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT ATK",
		addresses=[0x2f6fde],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(72),
		max_value=Max_ATK_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT DEF",
		addresses=[0x2f6fe0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT ITEM1",
		addresses=[0x2f7018],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT ITEM2",
		addresses=[0x2f701a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SPIRIT ITEM3",
		addresses=[0x2f701c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#thunder ghost 0x2F7034
	Attribute(
		name="THUNDER GHOST HP",
		addresses=[0x2f7080],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950),
		max_value=Max_HP_Multiplier(950),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST ABS",
		addresses=[0x2f7086],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST GILDA",
		addresses=[0x2f7088],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST ATK",
		addresses=[0x2f7096],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(108),
		max_value=Max_ATK_Multiplier(108),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST DEF",
		addresses=[0x2f7098],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST ITEM1",
		addresses=[0x2f70d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST ITEM2",
		addresses=[0x2f70d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GHOST ITEM3",
		addresses=[0x2f70d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#thunder servant 0x2F70EC
	Attribute(
		name="THUNDER SERVANT HP",
		addresses=[0x2f7138],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9700),
		max_value=Max_HP_Multiplier(9700),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT ABS",
		addresses=[0x2f713e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT GILDA",
		addresses=[0x2f7140],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT ATK",
		addresses=[0x2f714e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(167),
		max_value=Max_ATK_Multiplier(167),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT DEF",
		addresses=[0x2f7150],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT ITEM1",
		addresses=[0x2f7188],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT ITEM2",
		addresses=[0x2f718a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER SERVANT ITEM3",
		addresses=[0x2f718c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#aqua element 0x2F71A4
	Attribute(
		name="AQUA ELEMENT HP",
		addresses=[0x2f71f0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(295),
		max_value=Max_HP_Multiplier(295),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT ABS",
		addresses=[0x2f71f6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(58),
		max_value=Max_ABS_Multiplier(58),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT GILDA",
		addresses=[0x2f71f6],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT ATK",
		addresses=[0x2f7206],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(41),
		max_value=Max_ATK_Multiplier(41),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT DEF",
		addresses=[0x2f7208],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(30),
		max_value=Max_DEF_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT ITEM1",
		addresses=[0x2f7240],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT ITEM2",
		addresses=[0x2f7242],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="AQUA ELEMENT ITEM3",
		addresses=[0x2f7244],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#water spirit 0x2F725C
	Attribute(
		name="WATER SPIRIT HP",
		addresses=[0x2f72a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(590),
		max_value=Max_HP_Multiplier(590),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT ABS",
		addresses=[0x2f72ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(118),
		max_value=Max_ABS_Multiplier(118),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT GILDA",
		addresses=[0x2f72b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT ATK",
		addresses=[0x2f72be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(73),
		max_value=Max_ATK_Multiplier(73),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT DEF",
		addresses=[0x2f72c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT ITEM1",
		addresses=[0x2f72f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT ITEM2",
		addresses=[0x2f72fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="WATER SPIRIT ITEM3",
		addresses=[0x2f72fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#rain ghost 0x2F7314
	Attribute(
		name="RAIN GHOST HP",
		addresses=[0x2f7360],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950),
		max_value=Max_HP_Multiplier(950),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST ABS",
		addresses=[0x2f7366],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST GILDA",
		addresses=[0x2f7368],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST ATK",
		addresses=[0x2f7376],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(108),
		max_value=Max_ATK_Multiplier(108),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST DEF",
		addresses=[0x2f7378],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST ITEM1",
		addresses=[0x2f73b0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST ITEM2",
		addresses=[0x2f73b2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="RAIN GHOST ITEM3",
		addresses=[0x2f73b4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#tempest servant 0x2F73CC
	Attribute(
		name="TEMPEST SERVANT HP",
		addresses=[0x2f7418],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9900),
		max_value=Max_HP_Multiplier(9900),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT ABS",
		addresses=[0x2f741e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT GILDA",
		addresses=[0x2f7420],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT ATK",
		addresses=[0x2f742e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(167),
		max_value=Max_ATK_Multiplier(167),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT DEF",
		addresses=[0x2f7430],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT ITEM1",
		addresses=[0x2f7468],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT ITEM2",
		addresses=[0x2f746a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TEMPEST SERVANT ITEM3",
		addresses=[0x2f746c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#wind element 0x2F7484
	Attribute(
		name="WIND ELEMENT HP",
		addresses=[0x2f74d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(180),
		max_value=Max_HP_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT ABS",
		addresses=[0x2f74d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(28),
		max_value=Max_ABS_Multiplier(28),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT GILDA",
		addresses=[0x2f74d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT ATK",
		addresses=[0x2f74e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(32),
		max_value=Max_ATK_Multiplier(32),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT DEF",
		addresses=[0x2f74e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(24),
		max_value=Max_DEF_Multiplier(24),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT ITEM1",
		addresses=[0x2f7520],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT ITEM2",
		addresses=[0x2f7522],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="WIND ELEMENT ITEM3",
		addresses=[0x2f7524],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#spirit flyer 0x2F753C
	Attribute(
		name="SPIRIT FLYER HP",
		addresses=[0x2f7588],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(560),
		max_value=Max_HP_Multiplier(560),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER ABS",
		addresses=[0x2f758e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(112),
		max_value=Max_ABS_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER GILDA",
		addresses=[0x2f7590],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(114),
		max_value=Max_GILDA_Multiplier(114),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER ATK",
		addresses=[0x2f759e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(69),
		max_value=Max_ATK_Multiplier(69),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER DEF",
		addresses=[0x2f75a0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER ITEM1",
		addresses=[0x2f75d8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER ITEM2",
		addresses=[0x2f75da],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SPIRIT FLYER ITEM3",
		addresses=[0x2f75dc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#storm ghost 0x2F75F4
	Attribute(
		name="STORM GHOST HP",
		addresses=[0x2f7640],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950),
		max_value=Max_HP_Multiplier(950),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST ABS",
		addresses=[0x2f7646],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST GILDA",
		addresses=[0x2f7648],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST ATK",
		addresses=[0x2f7656],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(108),
		max_value=Max_ATK_Multiplier(108),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST DEF",
		addresses=[0x2f7658],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST ITEM1",
		addresses=[0x2f7690],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST ITEM2",
		addresses=[0x2f7692],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="STORM GHOST ITEM3",
		addresses=[0x2f7694],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#wind servant 0x2F76AC
	Attribute(
		name="WIND SERVANT HP",
		addresses=[0x2f76f8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9800),
		max_value=Max_HP_Multiplier(9800),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT ABS",
		addresses=[0x2f76fe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT GILDA",
		addresses=[0x2f7700],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT ATK",
		addresses=[0x2f770e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(167),
		max_value=Max_ATK_Multiplier(167),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT DEF",
		addresses=[0x2f7710],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT ITEM1",
		addresses=[0x2f7748],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT ITEM2",
		addresses=[0x2f774a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND SERVANT ITEM3",
		addresses=[0x2f774c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#masked tribesman 0x2F7764
	Attribute(
		name="MASKED TRIBESMAN HP",
		addresses=[0x2f77b0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(110),
		max_value=Max_HP_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN ABS",
		addresses=[0x2f77b6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(20),
		max_value=Max_ABS_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN GILDA",
		addresses=[0x2f77b8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN ATK",
		addresses=[0x2f77c6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(23),
		max_value=Max_ATK_Multiplier(23),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN DEF",
		addresses=[0x2f77c8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(11),
		max_value=Max_DEF_Multiplier(11),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN ITEM1",
		addresses=[0x2f7800],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN ITEM2",
		addresses=[0x2f7802],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MASKED TRIBESMAN ITEM3",
		addresses=[0x2f7804],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#lava runner 0x2F781C
	Attribute(
		name="LAVA RUNNER HP",
		addresses=[0x2f7868],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(495),
		max_value=Max_HP_Multiplier(495),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER ABS",
		addresses=[0x2f786e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(95),
		max_value=Max_ABS_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER GILDA",
		addresses=[0x2f7870],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER ATK",
		addresses=[0x2f787e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(51),
		max_value=Max_ATK_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER DEF",
		addresses=[0x2f7880],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(45),
		max_value=Max_DEF_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER ITEM1",
		addresses=[0x2f78b8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER ITEM2",
		addresses=[0x2f78ba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="LAVA RUNNER ITEM3",
		addresses=[0x2f78bc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#stone guard 0x2F78D4
	Attribute(
		name="STONE GUARD HP",
		addresses=[0x2f7920],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2600),
		max_value=Max_HP_Multiplier(2600),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD ABS",
		addresses=[0x2f7926],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD GILDA",
		addresses=[0x2f7928],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(110),
		max_value=Max_GILDA_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD ATK",
		addresses=[0x2f7936],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD DEF",
		addresses=[0x2f7938],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(85),
		max_value=Max_DEF_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD ITEM1",
		addresses=[0x2f7970],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD ITEM2",
		addresses=[0x2f7972],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="STONE GUARD ITEM3",
		addresses=[0x2f7974],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#last guardian 0x2F798C
	Attribute(
		name="LAST GUARDIAN HP",
		addresses=[0x2f79d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8500),
		max_value=Max_HP_Multiplier(8500),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN ABS",
		addresses=[0x2f79de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN GILDA",
		addresses=[0x2f79e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(122),
		max_value=Max_GILDA_Multiplier(122),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN ATK",
		addresses=[0x2f79ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN DEF",
		addresses=[0x2f79f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN ITEM1",
		addresses=[0x2f7a28],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN ITEM2",
		addresses=[0x2f7a2a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="LAST GUARDIAN ITEM3",
		addresses=[0x2f7a2c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#pumpkinhead 0x2F7A44
	Attribute(
		name="PUMPKIN HEAD HP",
		addresses=[0x2f7a90],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(50),
		max_value=Max_HP_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD ABS",
		addresses=[0x2f7a96],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD GILDA",
		addresses=[0x2f7a98],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD ATK",
		addresses=[0x2f7aa6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(14),
		max_value=Max_ATK_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD DEF",
		addresses=[0x2f7aa8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(6),
		max_value=Max_DEF_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD ITEM1",
		addresses=[0x2f7ae0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD ITEM2",
		addresses=[0x2f7ae2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="PUMPKIN HEAD ITEM3",
		addresses=[0x2f7ae4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#zucky 0x2F7AFC
	Attribute(
		name="ZUCKY HP",
		addresses=[0x2f7b48],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(580),
		max_value=Max_HP_Multiplier(580),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY ABS",
		addresses=[0x2f7b4e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(116),
		max_value=Max_ABS_Multiplier(116),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY GILDA",
		addresses=[0x2f7b50],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY ATK",
		addresses=[0x2f7b5e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(70),
		max_value=Max_ATK_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY DEF",
		addresses=[0x2f7b60],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(53),
		max_value=Max_DEF_Multiplier(53),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY ITEM1",
		addresses=[0x2f7b98],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY ITEM2",
		addresses=[0x2f7b9a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ZUCKY ITEM3",
		addresses=[0x2f7b9c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#mallone 0x2F7BB4
	Attribute(
		name="MALLONE HP",
		addresses=[0x2f7c00],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1800),
		max_value=Max_HP_Multiplier(1800),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE ABS",
		addresses=[0x2f7c06],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE GILDA",
		addresses=[0x2f7c08],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(101),
		max_value=Max_GILDA_Multiplier(101),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE ATK",
		addresses=[0x2f7c16],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE DEF",
		addresses=[0x2f7c18],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(77),
		max_value=Max_DEF_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE ITEM1",
		addresses=[0x2f7c50],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE ITEM2",
		addresses=[0x2f7c52],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MALLONE ITEM3",
		addresses=[0x2f7c54],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#scarecrow 0x2F7C6C
	Attribute(
		name="SCARECROW HP",
		addresses=[0x2f7cb8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(5900),
		max_value=Max_HP_Multiplier(5900),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW ABS",
		addresses=[0x2f7cbe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW GILDA",
		addresses=[0x2f7cc0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(101),
		max_value=Max_GILDA_Multiplier(101),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW ATK",
		addresses=[0x2f7cce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW DEF",
		addresses=[0x2f7cd0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW ITEM1",
		addresses=[0x2f7d08],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW ITEM2",
		addresses=[0x2f7d0a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SCARECROW ITEM3",
		addresses=[0x2f7d0c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mummy 0x2F7D24
	Attribute(
		name="MUMMY HP",
		addresses=[0x2f7d70],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(560),
		max_value=Max_HP_Multiplier(560),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY ABS",
		addresses=[0x2f7d76],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(112),
		max_value=Max_ABS_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY GILDA",
		addresses=[0x2f7d78],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(114),
		max_value=Max_GILDA_Multiplier(114),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY ATK",
		addresses=[0x2f7d86],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(71),
		max_value=Max_ATK_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY DEF",
		addresses=[0x2f7d88],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(57),
		max_value=Max_DEF_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY ITEM1",
		addresses=[0x2f7dc0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY ITEM2",
		addresses=[0x2f7dc2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MUMMY ITEM3",
		addresses=[0x2f7dc4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#bundy 0x2F7DDC
	Attribute(
		name="BUNDY HP",
		addresses=[0x2f7e28],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(820),
		max_value=Max_HP_Multiplier(820),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY ABS",
		addresses=[0x2f7e2e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(164),
		max_value=Max_ABS_Multiplier(164),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY GILDA",
		addresses=[0x2f7e30],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY ATK",
		addresses=[0x2f7e3e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(94),
		max_value=Max_ATK_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY DEF",
		addresses=[0x2f7e40],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY ITEM1",
		addresses=[0x2f7e78],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY ITEM2",
		addresses=[0x2f7e7a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="BUNDY ITEM3",
		addresses=[0x2f7e7c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#ghoul 0x2F7E94
	Attribute(
		name="GHOUL HP",
		addresses=[0x2f7ee0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3800),
		max_value=Max_HP_Multiplier(3800),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL ABS",
		addresses=[0x2f7ee6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL GILDA",
		addresses=[0x2f7ee8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL ATK",
		addresses=[0x2f7ef6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL DEF",
		addresses=[0x2f7ef8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(90),
		max_value=Max_DEF_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL ITEM1",
		addresses=[0x2f7f30],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL ITEM2",
		addresses=[0x2f7f32],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GHOUL ITEM3",
		addresses=[0x2f7f34],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#revenant 0x2F7F4C
	Attribute(
		name="REVENANT HP",
		addresses=[0x2f7f98],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8000),
		max_value=Max_HP_Multiplier(8000),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT ABS",
		addresses=[0x2f7f9e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT GILDA",
		addresses=[0x2f7fa0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(85),
		max_value=Max_GILDA_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT ATK",
		addresses=[0x2f7fae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT DEF",
		addresses=[0x2f7fb0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT ITEM1",
		addresses=[0x2f7fe8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT ITEM2",
		addresses=[0x2f7fe8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="REVENANT ITEM3",
		addresses=[0x2f7fec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#man eating grass 0x2F8004
	Attribute(
		name="MAN EATING GRASS HP",
		addresses=[0x2f8050],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(60),
		max_value=Max_HP_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS ABS",
		addresses=[0x2f8056],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS GILDA",
		addresses=[0x2f8058],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS ATK",
		addresses=[0x2f8066],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(13),
		max_value=Max_ATK_Multiplier(13),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS DEF",
		addresses=[0x2f8068],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(5),
		max_value=Max_DEF_Multiplier(5),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS ITEM1",
		addresses=[0x2f80a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS ITEM2",
		addresses=[0x2f80a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MAN EATING GRASS ITEM3",
		addresses=[0x2f80a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#cursed rose 0x2F80BC
	Attribute(
		name="CURSED ROSE HP",
		addresses=[0x2f8108],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(590),
		max_value=Max_HP_Multiplier(590),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE ABS",
		addresses=[0x2f810e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(118),
		max_value=Max_ABS_Multiplier(118),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE GILDA",
		addresses=[0x2f8110],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(54),
		max_value=Max_GILDA_Multiplier(54),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE ATK",
		addresses=[0x2f811e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(71),
		max_value=Max_ATK_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE DEF",
		addresses=[0x2f8120],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(54),
		max_value=Max_DEF_Multiplier(54),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE ITEM1",
		addresses=[0x2f8158],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE ITEM2",
		addresses=[0x2f815a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="CURSED ROSE ITEM3",
		addresses=[0x2f815c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#dark flower 0x2F8174
	Attribute(
		name="DARK FLOWER HP",
		addresses=[0x2f81c0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1700),
		max_value=Max_HP_Multiplier(1700),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER ABS",
		addresses=[0x2f81c6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER GILDA",
		addresses=[0x2f81c8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(85),
		max_value=Max_GILDA_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER ATK",
		addresses=[0x2f81d6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER DEF",
		addresses=[0x2f81d8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(77),
		max_value=Max_DEF_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER ITEM1",
		addresses=[0x2f8210],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER ITEM2",
		addresses=[0x2f8212],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK FLOWER ITEM3",
		addresses=[0x2f8214],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mystery plant 0x2F822C
	Attribute(
		name="MYSTERY PLANT HP",
		addresses=[0x2f8278],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6000),
		max_value=Max_HP_Multiplier(6000),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT ABS",
		addresses=[0x2f827e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT GILDA",
		addresses=[0x2f8280],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT ATK",
		addresses=[0x2f828e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT DEF",
		addresses=[0x2f8290],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT ITEM1",
		addresses=[0x2f82c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT ITEM2",
		addresses=[0x2f82ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MYSTERY PLANT ITEM3",
		addresses=[0x2f82cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#fire gemron 0x2F82E4
	Attribute(
		name="FIRE GEMRON HP",
		addresses=[0x2f8330],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(120),
		max_value=Max_HP_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON ABS",
		addresses=[0x2f8336],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON GILDA",
		addresses=[0x2f8338],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON ATK",
		addresses=[0x2f8346],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON DEF",
		addresses=[0x2f8348],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON ITEM1",
		addresses=[0x2f8380],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON ITEM2",
		addresses=[0x2f8382],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GEMRON ITEM3",
		addresses=[0x2f8384],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#fire gundron 0x2F839C
	Attribute(
		name="FIRE GUNDRON HP",
		addresses=[0x2f83e8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(505),
		max_value=Max_HP_Multiplier(505),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON ABS",
		addresses=[0x2f83ee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(100),
		max_value=Max_ABS_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON GILDA",
		addresses=[0x2f83f0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON ATK",
		addresses=[0x2f83fe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(57),
		max_value=Max_ATK_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON DEF",
		addresses=[0x2f8400],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON ITEM1",
		addresses=[0x2f8438],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON ITEM2",
		addresses=[0x2f843a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE GUNDRON ITEM3",
		addresses=[0x2f843c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#fire drake 0x2F8454
	Attribute(
		name="FIRE DRAKE HP",
		addresses=[0x2f84a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950),
		max_value=Max_HP_Multiplier(950),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE ABS",
		addresses=[0x2f84a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE GILDA",
		addresses=[0x2f84a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(148),
		max_value=Max_GILDA_Multiplier(148),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE ATK",
		addresses=[0x2f84b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(105),
		max_value=Max_ATK_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE DEF",
		addresses=[0x2f84b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(68),
		max_value=Max_DEF_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE ITEM1",
		addresses=[0x2f84f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE ITEM2",
		addresses=[0x2f84f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE DRAKE ITEM3",
		addresses=[0x2f84f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#fire wywrm 0x2F850C
	Attribute(
		name="FIRE WYRM HP",
		addresses=[0x2f8558],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6800),
		max_value=Max_HP_Multiplier(6800),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM ABS",
		addresses=[0x2f855e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM GILDA",
		addresses=[0x2f8560],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM ATK",
		addresses=[0x2f856e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM DEF",
		addresses=[0x2f8570],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM ITEM1",
		addresses=[0x2f85a8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM ITEM2",
		addresses=[0x2f85aa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FIRE WYRM ITEM3",
		addresses=[0x2f85ac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#ice gemron 0x2F85C4
	Attribute(
		name="ICE GEMRON HP",
		addresses=[0x2f8610],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(120),
		max_value=Max_HP_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON ABS",
		addresses=[0x2f8616],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON GILDA",
		addresses=[0x2f8618],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON ATK",
		addresses=[0x2f8626],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON DEF",
		addresses=[0x2f8628],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON ITEM1",
		addresses=[0x2f8660],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON ITEM2",
		addresses=[0x2f8662],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="ICE GEMRON ITEM3",
		addresses=[0x2f8664],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#ice gundron 0x2F867C
	Attribute(
		name="ICE GUNDRON HP",
		addresses=[0x2f86c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON ABS",
		addresses=[0x2f86ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(70),
		max_value=Max_ABS_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON GILDA",
		addresses=[0x2f86d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON ATK",
		addresses=[0x2f86de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON DEF",
		addresses=[0x2f86e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON ITEM1",
		addresses=[0x2f8718],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON ITEM2",
		addresses=[0x2f871a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ICE GUNDRON ITEM3",
		addresses=[0x2f871c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#ice drake 0x2F8734
	Attribute(
		name="ICE DRAKE HP",
		addresses=[0x2f8780],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950),
		max_value=Max_HP_Multiplier(950),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE ABS",
		addresses=[0x2f8786],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE GILDA",
		addresses=[0x2f8788],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(148),
		max_value=Max_GILDA_Multiplier(148),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE ATK",
		addresses=[0x2f8796],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(105),
		max_value=Max_ATK_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE DEF",
		addresses=[0x2f8798],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(68),
		max_value=Max_DEF_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE ITEM1",
		addresses=[0x2f87d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE ITEM2",
		addresses=[0x2f87d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="ICE DRAKE ITEM3",
		addresses=[0x2f87d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#ice wyrm 0x2F87EC
	Attribute(
		name="ICE WYRM HP",
		addresses=[0x2f8838],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6900),
		max_value=Max_HP_Multiplier(6900),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM ABS",
		addresses=[0x2f883e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM GILDA",
		addresses=[0x2f8840],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM ATK",
		addresses=[0x2f884e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM DEF",
		addresses=[0x2f8850],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM ITEM1",
		addresses=[0x2f8888],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM ITEM2",
		addresses=[0x2f888a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ICE WYRM ITEM3",
		addresses=[0x2f888c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#thunder gemron 0x2F88A4
	Attribute(
		name="THUNDER GEMRON HP",
		addresses=[0x2f88f0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(120),
		max_value=Max_HP_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON ABS",
		addresses=[0x2f88f6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON GILDA",
		addresses=[0x2f88f8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON ATK",
		addresses=[0x2f8906],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON DEF",
		addresses=[0x2f8908],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON ITEM1",
		addresses=[0x2f8940],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON ITEM2",
		addresses=[0x2f8942],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GEMRON ITEM3",
		addresses=[0x2f8944],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#thunder gundron 0x2F895C
	Attribute(
		name="THUNDER GUNDRON HP",
		addresses=[0x2f89a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON ABS",
		addresses=[0x2f89ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(70),
		max_value=Max_ABS_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON GILDA",
		addresses=[0x2f89b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON ATK",
		addresses=[0x2f89be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON DEF",
		addresses=[0x2f89c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON ITEM1",
		addresses=[0x2f89f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON ITEM2",
		addresses=[0x2f89fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER GUNDRON ITEM3",
		addresses=[0x2f89fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#thunder drake 0x2F8A14
	Attribute(
		name="THUNDER DRAKE HP",
		addresses=[0x2f8a60],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2200),
		max_value=Max_HP_Multiplier(2200),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE ABS",
		addresses=[0x2f8a66],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE GILDA",
		addresses=[0x2f8a68],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(111),
		max_value=Max_GILDA_Multiplier(111),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE ATK",
		addresses=[0x2f8a76],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE DEF",
		addresses=[0x2f8a78],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(81),
		max_value=Max_DEF_Multiplier(81),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE ITEM1",
		addresses=[0x2f8ab0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE ITEM2",
		addresses=[0x2f8ab2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER DRAKE ITEM3",
		addresses=[0x2f8ab4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#thunder wyrm 0x2F8ACC
	Attribute(
		name="THUNDER WYRM HP",
		addresses=[0x2f8b18],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7100),
		max_value=Max_HP_Multiplier(7100),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM ABS",
		addresses=[0x2f8b1e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM GILDA",
		addresses=[0x2f8b20],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM ATK",
		addresses=[0x2f8b2e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM DEF",
		addresses=[0x2f8b30],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM ITEM1",
		addresses=[0x2f8b68],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM ITEM2",
		addresses=[0x2f8b6a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="THUNDER WYRM ITEM3",
		addresses=[0x2f8b6c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#wind gemron 0x2F8B84
	Attribute(
		name="WIND GEMRON HP",
		addresses=[0x2f8bd0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(120),
		max_value=Max_HP_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON ABS",
		addresses=[0x2f8bd6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON GILDA",
		addresses=[0x2f8bd8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON ATK",
		addresses=[0x2f8be6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON DEF",
		addresses=[0x2f8be8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON ITEM1",
		addresses=[0x2f8c20],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON ITEM2",
		addresses=[0x2f8c22],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="WIND GEMRON ITEM3",
		addresses=[0x2f8c24],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#wind gundron 0x2F8C3C
	Attribute(
		name="WIND GUNDRON HP",
		addresses=[0x2f8c88],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON ABS",
		addresses=[0x2f8c8e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(70),
		max_value=Max_ABS_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON GILDA",
		addresses=[0x2f8c90],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON ATK",
		addresses=[0x2f8c9e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON DEF",
		addresses=[0x2f8ca0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON ITEM1",
		addresses=[0x2f8cd8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON ITEM2",
		addresses=[0x2f8cda],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="WIND GUNDRON ITEM3",
		addresses=[0x2f8cdc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#wind drake 0x2F8CF4
	Attribute(
		name="WIND DRAKE HP",
		addresses=[0x2f8d40],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2300),
		max_value=Max_HP_Multiplier(2300),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE ABS",
		addresses=[0x2f8d46],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE GILDA",
		addresses=[0x2f8d48],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE ATK",
		addresses=[0x2f8d56],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE DEF",
		addresses=[0x2f8d58],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(82),
		max_value=Max_DEF_Multiplier(82),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE ITEM1",
		addresses=[0x2f8d90],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE ITEM2",
		addresses=[0x2f8d92],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND DRAKE ITEM3",
		addresses=[0x2f8d94],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#wind wyrm 0x2F8DAC
	Attribute(
		name="WIND WYRM HP",
		addresses=[0x2f8df8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7000),
		max_value=Max_HP_Multiplier(7000),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM ABS",
		addresses=[0x2f8dfe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM GILDA",
		addresses=[0x2f8e00],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM ATK",
		addresses=[0x2f8e0e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM DEF",
		addresses=[0x2f8e10],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM ITEM1",
		addresses=[0x2f8e48],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM ITEM2",
		addresses=[0x2f8e4a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WIND WYRM ITEM3",
		addresses=[0x2f8e4c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#holy gemron 0x2F8E64
	Attribute(
		name="HOLY GEMRON HP",
		addresses=[0x2f8eb0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(160),
		max_value=Max_HP_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON ABS",
		addresses=[0x2f8eb6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(38),
		max_value=Max_ABS_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON GILDA",
		addresses=[0x2f8eb8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON ATK",
		addresses=[0x2f8ec6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON DEF",
		addresses=[0x2f8ec8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON ITEM1",
		addresses=[0x2f8f00],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON ITEM2",
		addresses=[0x2f8f02],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GEMRON ITEM3",
		addresses=[0x2f8f04],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#holy gundron 0x2F8F1C
	Attribute(
		name="HOLY GUNDRON HP",
		addresses=[0x2f8f68],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON ABS",
		addresses=[0x2f8f6e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(70),
		max_value=Max_ABS_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON GILDA",
		addresses=[0x2f8f70],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON ATK",
		addresses=[0x2f8f7e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON DEF",
		addresses=[0x2f8f80],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON ITEM1",
		addresses=[0x2f8fb8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON ITEM2",
		addresses=[0x2f8fba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY GUNDRON ITEM3",
		addresses=[0x2f8fbc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#holy drake 0x2F8FD4
	Attribute(
		name="HOLY DRAKE HP",
		addresses=[0x2f9020],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2400),
		max_value=Max_HP_Multiplier(2400),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE ABS",
		addresses=[0x2f9026],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE GILDA",
		addresses=[0x2f9028],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE ATK",
		addresses=[0x2f9036],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE DEF",
		addresses=[0x2f9038],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(83),
		max_value=Max_DEF_Multiplier(83),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE ITEM1",
		addresses=[0x2f9070],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE ITEM2",
		addresses=[0x2f9072],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY DRAKE ITEM3",
		addresses=[0x2f9074],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#holy wyrm 0x2F908C
	Attribute(
		name="HOLY WYRM HP",
		addresses=[0x2f90d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7200),
		max_value=Max_HP_Multiplier(7200),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM ABS",
		addresses=[0x2f90de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM GILDA",
		addresses=[0x2f90e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM ATK",
		addresses=[0x2f90ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM DEF",
		addresses=[0x2f90f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM ITEM1",
		addresses=[0x2f9128],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM ITEM2",
		addresses=[0x2f912a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HOLY WYRM ITEM3",
		addresses=[0x2f912c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#nikapous 0x2F9144
	Attribute(
		name="NIKAPOUS HP",
		addresses=[0x2f9190],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(155),
		max_value=Max_HP_Multiplier(155),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS ABS",
		addresses=[0x2f9196],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS GILDA",
		addresses=[0x2f9198],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS ATK",
		addresses=[0x2f91a6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(26),
		max_value=Max_ATK_Multiplier(26),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS DEF",
		addresses=[0x2f91a8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(18),
		max_value=Max_DEF_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS ITEM1",
		addresses=[0x2f91e0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS ITEM2",
		addresses=[0x2f91e2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="NIKAPOUS ITEM3",
		addresses=[0x2f91e4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#iron mask 0x2F91FC
	Attribute(
		name="IRON MASK HP",
		addresses=[0x2f9248],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700),
		max_value=Max_HP_Multiplier(700),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK ABS",
		addresses=[0x2f924e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(140),
		max_value=Max_ABS_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK GILDA",
		addresses=[0x2f9250],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK ATK",
		addresses=[0x2f925e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(76),
		max_value=Max_ATK_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK DEF",
		addresses=[0x2f9260],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(64),
		max_value=Max_DEF_Multiplier(64),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK ITEM1",
		addresses=[0x2f9298],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK ITEM2",
		addresses=[0x2f929a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="IRON MASK ITEM3",
		addresses=[0x2f929c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#ummagumma 0x2F92B4
	Attribute(
		name="UMAGUMMA HP",
		addresses=[0x2f9300],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3900),
		max_value=Max_HP_Multiplier(3900),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA ABS",
		addresses=[0x2f9306],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA GILDA",
		addresses=[0x2f9308],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(145),
		max_value=Max_GILDA_Multiplier(145),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA ATK",
		addresses=[0x2f9316],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA DEF",
		addresses=[0x2f9318],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA ITEM1",
		addresses=[0x2f9350],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA ITEM2",
		addresses=[0x2f9352],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="UMAGUMMA ITEM3",
		addresses=[0x2f9354],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#incuder 0x2F936C
	Attribute(
		name="INCUDER HP",
		addresses=[0x2f93b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9200),
		max_value=Max_HP_Multiplier(9200),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER ABS",
		addresses=[0x2f93be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER GILDA",
		addresses=[0x2f93c0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(110),
		max_value=Max_GILDA_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER ATK",
		addresses=[0x2f93ce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(162),
		max_value=Max_ATK_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER DEF",
		addresses=[0x2f93d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER ITEM1",
		addresses=[0x2f9408],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER ITEM2",
		addresses=[0x2f940a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="INCUDER ITEM3",
		addresses=[0x2f940c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#ram 0x2F9424
	Attribute(
		name="RAM HP",
		addresses=[0x2f9470],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(150),
		max_value=Max_HP_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="RAM ABS",
		addresses=[0x2f9476],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(22),
		max_value=Max_ABS_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="RAM GILDA",
		addresses=[0x2f9478],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="RAM ATK",
		addresses=[0x2f9486],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(24),
		max_value=Max_ATK_Multiplier(24),
		is_little_endian=True, ),
	Attribute(
		name="RAM DEF",
		addresses=[0x2f9488],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(13),
		max_value=Max_DEF_Multiplier(13),
		is_little_endian=True, ),
	Attribute(
		name="RAM ITEM1",
		addresses=[0x2f94c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="RAM ITEM2",
		addresses=[0x2f94c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="RAM ITEM3",
		addresses=[0x2f94c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#savage ram 0x2F94DC
	Attribute(
		name="SAVAGE RAM HP",
		addresses=[0x2f9528],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650),
		max_value=Max_HP_Multiplier(650),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM ABS",
		addresses=[0x2f952e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(84),
		max_value=Max_ABS_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM GILDA",
		addresses=[0x2f9530],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(36),
		max_value=Max_GILDA_Multiplier(36),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM ATK",
		addresses=[0x2f953e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(48),
		max_value=Max_ATK_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM DEF",
		addresses=[0x2f9540],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(38),
		max_value=Max_DEF_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM ITEM1",
		addresses=[0x2f9578],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM ITEM2",
		addresses=[0x2f957a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="SAVAGE RAM ITEM3",
		addresses=[0x2f957c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#ram z 0x2F9594
	Attribute(
		name="RAM Z HP",
		addresses=[0x2f95e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3700),
		max_value=Max_HP_Multiplier(3700),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z ABS",
		addresses=[0x2f95e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z GILDA",
		addresses=[0x2f95e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z ATK",
		addresses=[0x2f95f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z DEF",
		addresses=[0x2f95f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(94),
		max_value=Max_DEF_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z ITEM1",
		addresses=[0x2f9630],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z ITEM2",
		addresses=[0x2f9632],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RAM Z ITEM3",
		addresses=[0x2f9634],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#bandou 0x2F964C
	Attribute(
		name="BANDOU HP",
		addresses=[0x2f9698],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7400),
		max_value=Max_HP_Multiplier(7400),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU ABS",
		addresses=[0x2f969e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU GILDA",
		addresses=[0x2f969e],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(140),
		max_value=Max_GILDA_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU ATK",
		addresses=[0x2f96ae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU DEF",
		addresses=[0x2f96b0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU ITEM1",
		addresses=[0x2f96e8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU ITEM2",
		addresses=[0x2f96ea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BANDOU ITEM3",
		addresses=[0x2f96ec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#moler 0x2F9704
	Attribute(
		name="MOLER HP",
		addresses=[0x2f9750],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(55),
		max_value=Max_HP_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="MOLER ABS",
		addresses=[0x2f9756],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="MOLER GILDA",
		addresses=[0x2f9758],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(13),
		max_value=Max_GILDA_Multiplier(13),
		is_little_endian=True, ),
	Attribute(
		name="MOLER ATK",
		addresses=[0x2f9766],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(17),
		max_value=Max_ATK_Multiplier(17),
		is_little_endian=True, ),
	Attribute(
		name="MOLER DEF",
		addresses=[0x2f9768],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(6),
		max_value=Max_DEF_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="MOLER ITEM1",
		addresses=[0x2f97a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MOLER ITEM2",
		addresses=[0x2f97a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MOLER ITEM3",
		addresses=[0x2f97a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#sand moler 0x2F97BC
	Attribute(
		name="SAND MOLER HP",
		addresses=[0x2f9808],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(250),
		max_value=Max_HP_Multiplier(250),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER ABS",
		addresses=[0x2f980e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(50),
		max_value=Max_ABS_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER GILDA",
		addresses=[0x2f9810],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER ATK",
		addresses=[0x2f981e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER DEF",
		addresses=[0x2f9820],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(25),
		max_value=Max_DEF_Multiplier(25),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER ITEM1",
		addresses=[0x2f9858],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER ITEM2",
		addresses=[0x2f985a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SAND MOLER ITEM3",
		addresses=[0x2f985c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#mine moler 0x2F9874
	Attribute(
		name="MINE MOLER HP",
		addresses=[0x2f98c0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2000),
		max_value=Max_HP_Multiplier(2000),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER ABS",
		addresses=[0x2f98c6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER GILDA",
		addresses=[0x2f98c8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER ATK",
		addresses=[0x2f98d6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER DEF",
		addresses=[0x2f98d8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(79),
		max_value=Max_DEF_Multiplier(79),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER ITEM1",
		addresses=[0x2f9910],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER ITEM2",
		addresses=[0x2f9912],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MINE MOLER ITEM3",
		addresses=[0x2f9914],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#busy moler 0x2F992C
	Attribute(
		name="BUSY MOLER HP",
		addresses=[0x2f9978],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9300),
		max_value=Max_HP_Multiplier(9300),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER ABS",
		addresses=[0x2f997e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER GILDA",
		addresses=[0x2f9980],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(90),
		max_value=Max_GILDA_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER ATK",
		addresses=[0x2f998e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(162),
		max_value=Max_ATK_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER DEF",
		addresses=[0x2f9990],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER ITEM1",
		addresses=[0x2f99c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER ITEM2",
		addresses=[0x2f99ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BUSY MOLER ITEM3",
		addresses=[0x2f99cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#killer snake 0x2F99E4
	Attribute(
		name="KILLER SNAKE HP",
		addresses=[0x2f9a30],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(150),
		max_value=Max_HP_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE ABS",
		addresses=[0x2f9a36],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(20),
		max_value=Max_ABS_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE GILDA",
		addresses=[0x2f9a38],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE ATK",
		addresses=[0x2f9a46],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(19),
		max_value=Max_ATK_Multiplier(19),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE DEF",
		addresses=[0x2f9a48],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE ITEM1",
		addresses=[0x2f9a80],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE ITEM2",
		addresses=[0x2f9a82],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="KILLER SNAKE ITEM3",
		addresses=[0x2f9a84],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#sea serpent 0x2F9A9C
	Attribute(
		name="SEA SERPENT HP",
		addresses=[0x2f9ae8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(390),
		max_value=Max_HP_Multiplier(390),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT ABS",
		addresses=[0x2f9aee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(78),
		max_value=Max_ABS_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT GILDA",
		addresses=[0x2f9af0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(30),
		max_value=Max_GILDA_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT ATK",
		addresses=[0x2f9afe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(51),
		max_value=Max_ATK_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT DEF",
		addresses=[0x2f9b00],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(38),
		max_value=Max_DEF_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT ITEM1",
		addresses=[0x2f9b38],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT ITEM2",
		addresses=[0x2f9b3a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA SERPENT ITEM3",
		addresses=[0x2f9b3c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#sand dragon 0x2F9B54
	Attribute(
		name="SAND DRAGON HP",
		addresses=[0x2f9ba0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6500),
		max_value=Max_HP_Multiplier(6500),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON ABS",
		addresses=[0x2f9ba6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON GILDA",
		addresses=[0x2f9ba8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON ATK",
		addresses=[0x2f9bb6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON DEF",
		addresses=[0x2f9bb8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON ITEM1",
		addresses=[0x2f9bf0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON ITEM2",
		addresses=[0x2f9bf2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SAND DRAGON ITEM3",
		addresses=[0x2f9bf4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#dead rope 0x2F9C0C
	Attribute(
		name="DEAD ROPE HP",
		addresses=[0x2f9c58],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9400),
		max_value=Max_HP_Multiplier(9400),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE ABS",
		addresses=[0x2f9c5e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE GILDA",
		addresses=[0x2f9c60],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE ATK",
		addresses=[0x2f9c6e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(162),
		max_value=Max_ATK_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE DEF",
		addresses=[0x2f9c70],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE ITEM1",
		addresses=[0x2f9ca8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE ITEM2",
		addresses=[0x2f9caa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEAD ROPE ITEM3",
		addresses=[0x2f9cac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#goyone 0x2F9CC4
	Attribute(
		name="GOYONE HP",
		addresses=[0x2f9d10],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(240),
		max_value=Max_HP_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE ABS",
		addresses=[0x2f9d16],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(48),
		max_value=Max_ABS_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE GILDA",
		addresses=[0x2f9d18],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(54),
		max_value=Max_GILDA_Multiplier(54),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE ATK",
		addresses=[0x2f9d26],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(37),
		max_value=Max_ATK_Multiplier(37),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE DEF",
		addresses=[0x2f9d28],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(30),
		max_value=Max_DEF_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE ITEM1",
		addresses=[0x2f9d60],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE ITEM2",
		addresses=[0x2f9d62],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="GOYONE ITEM3",
		addresses=[0x2f9d64],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#steam goyone 0x2F9D7C
	Attribute(
		name="STEAM GOYONE HP",
		addresses=[0x2f9dc8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(420),
		max_value=Max_HP_Multiplier(420),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE ABS",
		addresses=[0x2f9dce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(84),
		max_value=Max_ABS_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE GILDA",
		addresses=[0x2f9dd0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(94),
		max_value=Max_GILDA_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE ATK",
		addresses=[0x2f9dde],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(47),
		max_value=Max_ATK_Multiplier(47),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE DEF",
		addresses=[0x2f9de0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(42),
		max_value=Max_DEF_Multiplier(42),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE ITEM1",
		addresses=[0x2f9e18],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE ITEM2",
		addresses=[0x2f9e1a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STEAM GOYONE ITEM3",
		addresses=[0x2f9e1c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#moon goyone 0x2F9E34
	Attribute(
		name="MOON GOYONE HP",
		addresses=[0x2f9e80],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900),
		max_value=Max_HP_Multiplier(900),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE ABS",
		addresses=[0x2f9e86],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(160),
		max_value=Max_ABS_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE GILDA",
		addresses=[0x2f9e88],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(135),
		max_value=Max_GILDA_Multiplier(135),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE ATK",
		addresses=[0x2f9e96],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(100),
		max_value=Max_ATK_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE DEF",
		addresses=[0x2f9e98],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(66),
		max_value=Max_DEF_Multiplier(66),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE ITEM1",
		addresses=[0x2f9ed0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE ITEM2",
		addresses=[0x2f9ed2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOON GOYONE ITEM3",
		addresses=[0x2f9ed4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#mariner 0x2F9EEC
	Attribute(
		name="MARINER HP",
		addresses=[0x2f9f38],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8200),
		max_value=Max_HP_Multiplier(8200),
		is_little_endian=True, ),
	Attribute(
		name="MARINER ABS",
		addresses=[0x2f9f3e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="MARINER GILDA",
		addresses=[0x2f9f40],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="MARINER ATK",
		addresses=[0x2f9f4e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="MARINER DEF",
		addresses=[0x2f9f50],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="MARINER ITEM1",
		addresses=[0x2f9f88],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MARINER ITEM2",
		addresses=[0x2f9f8a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MARINER ITEM3",
		addresses=[0x2f9f8c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#auntie medusa 0x2F9FA4
	Attribute(
		name="AUNTIE MEDUSA HP",
		addresses=[0x2f9ff0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(330),
		max_value=Max_HP_Multiplier(330),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA ABS",
		addresses=[0x2f9ff6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(66),
		max_value=Max_ABS_Multiplier(66),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA GILDA",
		addresses=[0x2f9ff8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(75),
		max_value=Max_GILDA_Multiplier(75),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA ATK",
		addresses=[0x2fa006],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(43),
		max_value=Max_ATK_Multiplier(43),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA DEF",
		addresses=[0x2fa008],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(32),
		max_value=Max_DEF_Multiplier(32),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA ITEM1",
		addresses=[0x2fa040],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA ITEM2",
		addresses=[0x2fa042],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="AUNTIE MEDUSA ITEM3",
		addresses=[0x2fa044],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#fat naga 0x2FA05C
	Attribute(
		name="FAT NAGA HP",
		addresses=[0x2fa0a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700),
		max_value=Max_HP_Multiplier(700),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA ABS",
		addresses=[0x2fa0ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(140),
		max_value=Max_ABS_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA GILDA",
		addresses=[0x2fa0b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA ATK",
		addresses=[0x2fa0be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(79),
		max_value=Max_ATK_Multiplier(79),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA DEF",
		addresses=[0x2fa0c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(59),
		max_value=Max_DEF_Multiplier(59),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA ITEM1",
		addresses=[0x2fa0f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA ITEM2",
		addresses=[0x2fa0fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FAT NAGA ITEM3",
		addresses=[0x2fa0fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#miss gourgon 0x2FA114
	Attribute(
		name="MISS GOURGON HP",
		addresses=[0x2fa160],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(965),
		max_value=Max_HP_Multiplier(965),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON ABS",
		addresses=[0x2fa166],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(192),
		max_value=Max_ABS_Multiplier(192),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON GILDA",
		addresses=[0x2fa168],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON ATK",
		addresses=[0x2fa176],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(104),
		max_value=Max_ATK_Multiplier(104),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON DEF",
		addresses=[0x2fa178],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(68),
		max_value=Max_DEF_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON ITEM1",
		addresses=[0x2fa1b0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON ITEM2",
		addresses=[0x2fa1b2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MISS GOURGON ITEM3",
		addresses=[0x2fa1b4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#mrs gourgon 0x2FA1CC
	Attribute(
		name="MRS GOURGON HP",
		addresses=[0x2fa218],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10000),
		max_value=Max_HP_Multiplier(10000),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON ABS",
		addresses=[0x2fa21e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(172),
		max_value=Max_ABS_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON GILDA",
		addresses=[0x2fa220],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(160),
		max_value=Max_GILDA_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON ATK",
		addresses=[0x2fa22e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON DEF",
		addresses=[0x2fa230],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON ITEM1",
		addresses=[0x2fa268],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON ITEM2",
		addresses=[0x2fa26a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MRS GOURGON ITEM3",
		addresses=[0x2fa26c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#dog statue 0x2FA284
	Attribute(
		name="DOG STATUE HP",
		addresses=[0x2fa2d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(100),
		max_value=Max_HP_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE ABS",
		addresses=[0x2fa2d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(20),
		max_value=Max_ABS_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE GILDA",
		addresses=[0x2fa2d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE ATK",
		addresses=[0x2fa2e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(25),
		max_value=Max_ATK_Multiplier(25),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE DEF",
		addresses=[0x2fa2e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(17),
		max_value=Max_DEF_Multiplier(17),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE ITEM1",
		addresses=[0x2fa320],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE ITEM2",
		addresses=[0x2fa322],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="DOG STATUE ITEM3",
		addresses=[0x2fa324],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#coral dog 0x2FA33C
	Attribute(
		name="CORAL DOG HP",
		addresses=[0x2fa388],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG ABS",
		addresses=[0x2fa38e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG GILDA",
		addresses=[0x2fa390],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG ATK",
		addresses=[0x2fa39e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(75),
		max_value=Max_ATK_Multiplier(75),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG DEF",
		addresses=[0x2fa3a0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG ITEM1",
		addresses=[0x2fa3d8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG ITEM2",
		addresses=[0x2fa3da],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="CORAL DOG ITEM3",
		addresses=[0x2fa3dc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#toy rock 0x2FA3F4
	Attribute(
		name="TOY ROCK HP",
		addresses=[0x2fa440],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1065),
		max_value=Max_HP_Multiplier(1065),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK ABS",
		addresses=[0x2fa446],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(198),
		max_value=Max_ABS_Multiplier(198),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK GILDA",
		addresses=[0x2fa448],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK ATK",
		addresses=[0x2fa456],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(107),
		max_value=Max_ATK_Multiplier(107),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK DEF",
		addresses=[0x2fa458],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK ITEM1",
		addresses=[0x2fa490],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK ITEM2",
		addresses=[0x2fa492],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="TOY ROCK ITEM3",
		addresses=[0x2fa494],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#cerberus 0x2FA4AC
	Attribute(
		name="CERBERUS HP",
		addresses=[0x2fa4f8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8300),
		max_value=Max_HP_Multiplier(8300),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS ABS",
		addresses=[0x2fa4fe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS GILDA",
		addresses=[0x2fa500],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS ATK",
		addresses=[0x2fa50e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS DEF",
		addresses=[0x2fa510],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS ITEM1",
		addresses=[0x2fa548],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS ITEM2",
		addresses=[0x2fa54a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="CERBERUS ITEM3",
		addresses=[0x2fa54c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#ivanoff 0x2FA564
	Attribute(
		name="IVANOFF HP",
		addresses=[0x2fa5b0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(180),
		max_value=Max_HP_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF ABS",
		addresses=[0x2fa5b6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(34),
		max_value=Max_ABS_Multiplier(34),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF GILDA",
		addresses=[0x2fa5b8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF ATK",
		addresses=[0x2fa5c6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF DEF",
		addresses=[0x2fa5c8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(20),
		max_value=Max_DEF_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF ITEM1",
		addresses=[0x2fa600],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF ITEM2",
		addresses=[0x2fa602],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="IVANOFF ITEM3",
		addresses=[0x2fa604],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#magmanoff 0x2FA61C
	Attribute(
		name="MAGMANOFF HP",
		addresses=[0x2fa668],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(450),
		max_value=Max_HP_Multiplier(450),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF ABS",
		addresses=[0x2fa66e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(90),
		max_value=Max_ABS_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF GILDA",
		addresses=[0x2fa670],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(33),
		max_value=Max_GILDA_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF ATK",
		addresses=[0x2fa67e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(48),
		max_value=Max_ATK_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF DEF",
		addresses=[0x2fa680],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(45),
		max_value=Max_DEF_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF ITEM1",
		addresses=[0x2fa6b8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF ITEM2",
		addresses=[0x2fa6ba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="MAGMANOFF ITEM3",
		addresses=[0x2fa6bc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#rock face 0x2FA6D4
	Attribute(
		name="ROCK FACE HP",
		addresses=[0x2fa720],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6000),
		max_value=Max_HP_Multiplier(6000),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE ABS",
		addresses=[0x2fa726],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE GILDA",
		addresses=[0x2fa728],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(60),
		max_value=Max_GILDA_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE ATK",
		addresses=[0x2fa736],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE DEF",
		addresses=[0x2fa738],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE ITEM1",
		addresses=[0x2fa770],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE ITEM2",
		addresses=[0x2fa772],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ROCK FACE ITEM3",
		addresses=[0x2fa774],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#iwanosuke 0x2FA78C
	Attribute(
		name="IWANOSUKE HP",
		addresses=[0x2fa7d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10200),
		max_value=Max_HP_Multiplier(10200),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE ABS",
		addresses=[0x2fa7de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE GILDA",
		addresses=[0x2fa7e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE ATK",
		addresses=[0x2fa7ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE DEF",
		addresses=[0x2fa7f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE ITEM1",
		addresses=[0x2fa828],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE ITEM2",
		addresses=[0x2fa82a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IWANOSUKE ITEM3",
		addresses=[0x2fa82c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#statue 0x2FA844
	Attribute(
		name="STATUE HP",
		addresses=[0x2fa890],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="STATUE ABS",
		addresses=[0x2fa896],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(50),
		max_value=Max_ABS_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="STATUE GILDA",
		addresses=[0x2fa898],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="STATUE ATK",
		addresses=[0x2fa8a6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(40),
		max_value=Max_ATK_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="STATUE DEF",
		addresses=[0x2fa8a8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(32),
		max_value=Max_DEF_Multiplier(32),
		is_little_endian=True, ),
	Attribute(
		name="STATUE ITEM1",
		addresses=[0x2fa8e0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="STATUE ITEM2",
		addresses=[0x2fa8e2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="STATUE ITEM3",
		addresses=[0x2fa8e4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#living armour 0x2FA8FC
	Attribute(
		name="LIVING ARMOUR HP",
		addresses=[0x2fa948],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(560),
		max_value=Max_HP_Multiplier(560),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR ABS",
		addresses=[0x2fa94e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(112),
		max_value=Max_ABS_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR GILDA",
		addresses=[0x2fa950],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(114),
		max_value=Max_GILDA_Multiplier(114),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR ATK",
		addresses=[0x2fa95e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(71),
		max_value=Max_ATK_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR DEF",
		addresses=[0x2fa960],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(52),
		max_value=Max_DEF_Multiplier(52),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR ITEM1",
		addresses=[0x2fa998],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR ITEM2",
		addresses=[0x2fa99a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="LIVING ARMOUR ITEM3",
		addresses=[0x2fa99c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#guardia 0x2FA9B4
	Attribute(
		name="GUARDIA HP",
		addresses=[0x2faa00],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(920),
		max_value=Max_HP_Multiplier(920),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA ABS",
		addresses=[0x2faa06],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(184),
		max_value=Max_ABS_Multiplier(184),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA GILDA",
		addresses=[0x2faa08],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(82),
		max_value=Max_GILDA_Multiplier(82),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA ATK",
		addresses=[0x2faa16],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(102),
		max_value=Max_ATK_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA DEF",
		addresses=[0x2faa18],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA ITEM1",
		addresses=[0x2faa50],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA ITEM2",
		addresses=[0x2faa52],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="GUARDIA ITEM3",
		addresses=[0x2faa54],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#dark keeper 0x2FAA6C
	Attribute(
		name="DARK KEEPER HP",
		addresses=[0x2faab8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8100),
		max_value=Max_HP_Multiplier(8100),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER ABS",
		addresses=[0x2faabe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER GILDA",
		addresses=[0x2faac0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(101),
		max_value=Max_GILDA_Multiplier(101),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER ATK",
		addresses=[0x2faace],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(157),
		max_value=Max_ATK_Multiplier(157),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER DEF",
		addresses=[0x2faad0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER ITEM1",
		addresses=[0x2fab08],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER ITEM2",
		addresses=[0x2fab0a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARK KEEPER ITEM3",
		addresses=[0x2fab0c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#golem 0x2FAB24
	Attribute(
		name="GOLEM HP",
		addresses=[0x2fab70],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(450),
		max_value=Max_HP_Multiplier(450),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM ABS",
		addresses=[0x2fab76],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM GILDA",
		addresses=[0x2fab78],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM ATK",
		addresses=[0x2fab86],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(26),
		max_value=Max_ATK_Multiplier(26),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM DEF",
		addresses=[0x2fab88],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(18),
		max_value=Max_DEF_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM ITEM1",
		addresses=[0x2fabc0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM ITEM2",
		addresses=[0x2fabc2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="GOLEM ITEM3",
		addresses=[0x2fabc4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#rave golem (lava golem) 0x2FABDC
	Attribute(
		name="RAVE GOLEM HP",
		addresses=[0x2fac28],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850),
		max_value=Max_HP_Multiplier(850),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM ABS",
		addresses=[0x2fac2e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(104),
		max_value=Max_ABS_Multiplier(104),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM GILDA",
		addresses=[0x2fac30],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM ATK",
		addresses=[0x2fac3e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(55),
		max_value=Max_ATK_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM DEF",
		addresses=[0x2fac40],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(49),
		max_value=Max_DEF_Multiplier(49),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM ITEM1",
		addresses=[0x2fac78],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM ITEM2",
		addresses=[0x2fac7a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="RAVE GOLEM ITEM3",
		addresses=[0x2fac7c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#rock taster 0x2FAC94
	Attribute(
		name="ROCK TASTER HP",
		addresses=[0x2face0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(980),
		max_value=Max_HP_Multiplier(980),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER ABS",
		addresses=[0x2face6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER GILDA",
		addresses=[0x2face8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER ATK",
		addresses=[0x2facf6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(105),
		max_value=Max_ATK_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER DEF",
		addresses=[0x2facf8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(72),
		max_value=Max_DEF_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER ITEM1",
		addresses=[0x2fad30],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER ITEM2",
		addresses=[0x2fad32],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="ROCK TASTER ITEM3",
		addresses=[0x2fad34],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#titan 0x2FAD4C
	Attribute(
		name="TITAN HP",
		addresses=[0x2fad98],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(8500),
		max_value=Max_HP_Multiplier(8500),
		is_little_endian=True, ),
	Attribute(
		name="TITAN ABS",
		addresses=[0x2fad9e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="TITAN GILDA",
		addresses=[0x2fada0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(150),
		max_value=Max_GILDA_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="TITAN ATK",
		addresses=[0x2fadae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(150),
		max_value=Max_ATK_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="TITAN DEF",
		addresses=[0x2fadb0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="TITAN ITEM1",
		addresses=[0x2fade8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TITAN ITEM2",
		addresses=[0x2fadea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="TITAN ITEM3",
		addresses=[0x2fadec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#bone lord 0x2FAE04
	Attribute(
		name="BONE LORD HP",
		addresses=[0x2fae50],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850),
		max_value=Max_HP_Multiplier(850),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD ABS",
		addresses=[0x2fae56],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD GILDA",
		addresses=[0x2fae58],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD ATK",
		addresses=[0x2fae66],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(59),
		max_value=Max_ATK_Multiplier(59),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD DEF",
		addresses=[0x2fae68],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(45),
		max_value=Max_DEF_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD ITEM1",
		addresses=[0x2faea0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD ITEM2",
		addresses=[0x2faea2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BONE LORD ITEM3",
		addresses=[0x2faea4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#flaming nail 0x2FAEBC
	Attribute(
		name="FLAMING NAIL HP",
		addresses=[0x2faf08],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700),
		max_value=Max_HP_Multiplier(700),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL ABS",
		addresses=[0x2faf0e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(140),
		max_value=Max_ABS_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL GILDA",
		addresses=[0x2faf10],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL ATK",
		addresses=[0x2faf1e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(79),
		max_value=Max_ATK_Multiplier(79),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL DEF",
		addresses=[0x2faf20],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL ITEM1",
		addresses=[0x2faf58],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL ITEM2",
		addresses=[0x2faf5a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="FLAMING NAIL ITEM3",
		addresses=[0x2faf5c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#evil nail 0x2FAF74
	Attribute(
		name="EVIL NAIL HP",
		addresses=[0x2fafc0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1500),
		max_value=Max_HP_Multiplier(1500),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL ABS",
		addresses=[0x2fafc6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL GILDA",
		addresses=[0x2fafc8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(147),
		max_value=Max_GILDA_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL ATK",
		addresses=[0x2fafd6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(116),
		max_value=Max_ATK_Multiplier(116),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL DEF",
		addresses=[0x2fafd8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(72),
		max_value=Max_DEF_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL ITEM1",
		addresses=[0x2fb010],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL ITEM2",
		addresses=[0x2fb012],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL NAIL ITEM3",
		addresses=[0x2fb014],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#bone king 0x2FB02C
	Attribute(
		name="BONE KING HP",
		addresses=[0x2fb078],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11500),
		max_value=Max_HP_Multiplier(11500),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING ABS",
		addresses=[0x2fb07e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(600),
		max_value=Max_ABS_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING GILDA",
		addresses=[0x2fb080],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(110),
		max_value=Max_GILDA_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING ATK",
		addresses=[0x2fb08e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(182),
		max_value=Max_ATK_Multiplier(182),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING DEF",
		addresses=[0x2fb090],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(130),
		max_value=Max_DEF_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING ITEM1",
		addresses=[0x2fb0c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING ITEM2",
		addresses=[0x2fb0ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="BONE KING ITEM3",
		addresses=[0x2fb0cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#skeleton soldier 0x2FB0E4
	Attribute(
		name="SKELETON SOLDIER HP",
		addresses=[0x2fb130],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(70),
		max_value=Max_HP_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER ABS",
		addresses=[0x2fb136],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(14),
		max_value=Max_ABS_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER GILDA",
		addresses=[0x2fb138],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(14),
		max_value=Max_GILDA_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER ATK",
		addresses=[0x2fb146],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(14),
		max_value=Max_ATK_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER DEF",
		addresses=[0x2fb148],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(6),
		max_value=Max_DEF_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER ITEM1",
		addresses=[0x2fb180],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER ITEM2",
		addresses=[0x2fb182],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SKELETON SOLDIER ITEM3",
		addresses=[0x2fb184],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#horn head 0x2FB19C
	Attribute(
		name="HORN HEAD HP",
		addresses=[0x2fb1e8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(345),
		max_value=Max_HP_Multiplier(345),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD ABS",
		addresses=[0x2fb1ee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(68),
		max_value=Max_ABS_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD GILDA",
		addresses=[0x2fb1f0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(33),
		max_value=Max_GILDA_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD ATK",
		addresses=[0x2fb1fe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(45),
		max_value=Max_ATK_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD DEF",
		addresses=[0x2fb200],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(34),
		max_value=Max_DEF_Multiplier(34),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD ITEM1",
		addresses=[0x2fb238],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD ITEM2",
		addresses=[0x2fb23a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="HORN HEAD ITEM3",
		addresses=[0x2fb23c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#silver gear 0x2FB254
	Attribute(
		name="SILVER GEAR HP",
		addresses=[0x2fb2a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(880),
		max_value=Max_HP_Multiplier(880),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR ABS",
		addresses=[0x2fb2a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(177),
		max_value=Max_ABS_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR GILDA",
		addresses=[0x2fb2a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(123),
		max_value=Max_GILDA_Multiplier(123),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR ATK",
		addresses=[0x2fb2b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(97),
		max_value=Max_ATK_Multiplier(97),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR DEF",
		addresses=[0x2fb2b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(64),
		max_value=Max_DEF_Multiplier(64),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR ITEM1",
		addresses=[0x2fb2f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR ITEM2",
		addresses=[0x2fb2f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SILVER GEAR ITEM3",
		addresses=[0x2fb2f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#platinum gear 0x2FB30C
	Attribute(
		name="PLATINUM GEAR HP",
		addresses=[0x2fb358],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6200),
		max_value=Max_HP_Multiplier(6200),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR ABS",
		addresses=[0x2fb35e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR GILDA",
		addresses=[0x2fb360],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(122),
		max_value=Max_GILDA_Multiplier(122),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR ATK",
		addresses=[0x2fb36e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR DEF",
		addresses=[0x2fb370],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR ITEM1",
		addresses=[0x2fb3a8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR ITEM2",
		addresses=[0x2fb3aa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="PLATINUM GEAR ITEM3",
		addresses=[0x2fb3ac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#master jacket 0x2FB3C4
	Attribute(
		name="MASTER JACKET HP",
		addresses=[0x2fb410],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(395),
		max_value=Max_HP_Multiplier(395),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET ABS",
		addresses=[0x2fb416],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(76),
		max_value=Max_ABS_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET GILDA",
		addresses=[0x2fb418],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(87),
		max_value=Max_GILDA_Multiplier(87),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET ATK",
		addresses=[0x2fb426],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(49),
		max_value=Max_ATK_Multiplier(49),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET DEF",
		addresses=[0x2fb428],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET ITEM1",
		addresses=[0x2fb460],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET ITEM2",
		addresses=[0x2fb462],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="MASTER JACKET ITEM3",
		addresses=[0x2fb464],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#heat wear 0x2FB47C
	Attribute(
		name="HEAT WEAR HP",
		addresses=[0x2fb4c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(580),
		max_value=Max_HP_Multiplier(580),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR ABS",
		addresses=[0x2fb4ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(116),
		max_value=Max_ABS_Multiplier(116),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR GILDA",
		addresses=[0x2fb4d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR ATK",
		addresses=[0x2fb4de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(72),
		max_value=Max_ATK_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR DEF",
		addresses=[0x2fb4e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR ITEM1",
		addresses=[0x2fb518],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR ITEM2",
		addresses=[0x2fb51a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="HEAT WEAR ITEM3",
		addresses=[0x2fb51c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#skull chief 0x2FB534
	Attribute(
		name="SKULL CHIEF HP",
		addresses=[0x2fb580],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(999),
		max_value=Max_HP_Multiplier(999),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF ABS",
		addresses=[0x2fb586],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(198),
		max_value=Max_ABS_Multiplier(198),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF GILDA",
		addresses=[0x2fb588],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(135),
		max_value=Max_GILDA_Multiplier(135),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF ATK",
		addresses=[0x2fb596],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(106),
		max_value=Max_ATK_Multiplier(106),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF DEF",
		addresses=[0x2fb598],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(71),
		max_value=Max_DEF_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF ITEM1",
		addresses=[0x2fb5d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF ITEM2",
		addresses=[0x2fb5d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SKULL CHIEF ITEM3",
		addresses=[0x2fb5d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#rare jacket (boss)  0x2FB5EC
	Attribute(
		name="RARE JACKET HP",
		addresses=[0x2fb638],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(15000),
		max_value=Max_HP_Multiplier(15000),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET ABS",
		addresses=[0x2fb63e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET GILDA",
		addresses=[0x2fb640],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(80),
		max_value=Max_GILDA_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET ATK",
		addresses=[0x2fb64e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(180),
		max_value=Max_ATK_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET DEF",
		addresses=[0x2fb650],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(115),
		max_value=Max_DEF_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET ITEM1",
		addresses=[0x2fb688],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET ITEM2",
		addresses=[0x2fb68a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RARE JACKET ITEM3",
		addresses=[0x2fb68c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#captain 0x2FB6A4
	Attribute(
		name="CAPTAIN HP",
		addresses=[0x2fb6f0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(310),
		max_value=Max_HP_Multiplier(310),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN ABS",
		addresses=[0x2fb6f6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(62),
		max_value=Max_ABS_Multiplier(62),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN GILDA",
		addresses=[0x2fb6f8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(33),
		max_value=Max_GILDA_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN ATK",
		addresses=[0x2fb706],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(44),
		max_value=Max_ATK_Multiplier(44),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN DEF",
		addresses=[0x2fb708],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN ITEM1",
		addresses=[0x2fb740],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN ITEM2",
		addresses=[0x2fb742],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="CAPTAIN ITEM3",
		addresses=[0x2fb744],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#blackbeard 0x2FB75C
	Attribute(
		name="BLACKBEARD HP",
		addresses=[0x2fb7a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(580),
		max_value=Max_HP_Multiplier(580),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD ABS",
		addresses=[0x2fb7ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(116),
		max_value=Max_ABS_Multiplier(116),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD GILDA",
		addresses=[0x2fb7b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD ATK",
		addresses=[0x2fb7be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(73),
		max_value=Max_ATK_Multiplier(73),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD DEF",
		addresses=[0x2fb7c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD ITEM1",
		addresses=[0x2fb7f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD ITEM2",
		addresses=[0x2fb7fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="BLACKBEARD ITEM3",
		addresses=[0x2fb7fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#whitebeard 0x2FB814
	Attribute(
		name="WHITEBEARD HP",
		addresses=[0x2fb860],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2100),
		max_value=Max_HP_Multiplier(2100),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD ABS",
		addresses=[0x2fb866],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD GILDA",
		addresses=[0x2fb868],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(122),
		max_value=Max_GILDA_Multiplier(122),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD ATK",
		addresses=[0x2fb876],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD DEF",
		addresses=[0x2fb878],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(80),
		max_value=Max_DEF_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD ITEM1",
		addresses=[0x2fb8b0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD ITEM2",
		addresses=[0x2fb8b2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="WHITEBEARD ITEM3",
		addresses=[0x2fb8b4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#oyakata 0x2FB8CC
	Attribute(
		name="OYAKATA HP",
		addresses=[0x2fb918],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7300),
		max_value=Max_HP_Multiplier(7300),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA ABS",
		addresses=[0x2fb91e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA GILDA",
		addresses=[0x2fb920],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA ATK",
		addresses=[0x2fb92e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA DEF",
		addresses=[0x2fb930],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA ITEM1",
		addresses=[0x2fb968],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA ITEM2",
		addresses=[0x2fb96a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="OYAKATA ITEM3",
		addresses=[0x2fb96c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#corsair 0x2FB984
	Attribute(
		name="CORSAIR HP",
		addresses=[0x2fb9d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(230),
		max_value=Max_HP_Multiplier(230),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR ABS",
		addresses=[0x2fb9d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(46),
		max_value=Max_ABS_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR GILDA",
		addresses=[0x2fb9d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(24),
		max_value=Max_GILDA_Multiplier(24),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR ATK",
		addresses=[0x2fb9e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(37),
		max_value=Max_ATK_Multiplier(37),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR DEF",
		addresses=[0x2fb9e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(28),
		max_value=Max_DEF_Multiplier(28),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR ITEM1",
		addresses=[0x2fba20],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR ITEM2",
		addresses=[0x2fba22],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="CORSAIR ITEM3",
		addresses=[0x2fba24],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#zombie pirate 0x2FBA3C
	Attribute(
		name="ZOMBIE PIRATE HP",
		addresses=[0x2fba88],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(560),
		max_value=Max_HP_Multiplier(560),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE ABS",
		addresses=[0x2fba8e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(112),
		max_value=Max_ABS_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE GILDA",
		addresses=[0x2fba90],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(114),
		max_value=Max_GILDA_Multiplier(114),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE ATK",
		addresses=[0x2fba9e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(72),
		max_value=Max_ATK_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE DEF",
		addresses=[0x2fbaa0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(52),
		max_value=Max_DEF_Multiplier(52),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE ITEM1",
		addresses=[0x2fbad8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE ITEM2",
		addresses=[0x2fbada],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ZOMBIE PIRATE ITEM3",
		addresses=[0x2fbadc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#ore robber 0x2FBAF4
	Attribute(
		name="ORE ROBBER HP",
		addresses=[0x2fbb40],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1500),
		max_value=Max_HP_Multiplier(1500),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER ABS",
		addresses=[0x2fbb46],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER GILDA",
		addresses=[0x2fbb48],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER ATK",
		addresses=[0x2fbb56],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER DEF",
		addresses=[0x2fbb58],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(77),
		max_value=Max_DEF_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER ITEM1",
		addresses=[0x2fbb90],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER ITEM2",
		addresses=[0x2fbb92],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ORE ROBBER ITEM3",
		addresses=[0x2fbb94],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#elite corsair 0x2FBBAC
	Attribute(
		name="ELITE CORSAIR HP",
		addresses=[0x2fbbf8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6300),
		max_value=Max_HP_Multiplier(6300),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR ABS",
		addresses=[0x2fbbfe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR GILDA",
		addresses=[0x2fbc00],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(111),
		max_value=Max_GILDA_Multiplier(111),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR ATK",
		addresses=[0x2fbc0e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR DEF",
		addresses=[0x2fbc10],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR ITEM1",
		addresses=[0x2fbc48],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR ITEM2",
		addresses=[0x2fbc4a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ELITE CORSAIR ITEM3",
		addresses=[0x2fbc4c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#face of prajna 0x2FBC64
	Attribute(
		name="FACE OF PRAJNA HP",
		addresses=[0x2fbcb0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(66),
		max_value=Max_HP_Multiplier(66),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA ABS",
		addresses=[0x2fbcb6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(12),
		max_value=Max_ABS_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA GILDA",
		addresses=[0x2fbcb8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(14),
		max_value=Max_GILDA_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA ATK",
		addresses=[0x2fbcc6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(18),
		max_value=Max_ATK_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA DEF",
		addresses=[0x2fbcc8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(8),
		max_value=Max_DEF_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA ITEM1",
		addresses=[0x2fbd00],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA ITEM2",
		addresses=[0x2fbd02],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF PRAJNA ITEM3",
		addresses=[0x2fbd04],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#alexander 0x2FBD1C
	Attribute(
		name="ALEXANDER HP",
		addresses=[0x2fbd68],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(530),
		max_value=Max_HP_Multiplier(530),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER ABS",
		addresses=[0x2fbd6e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(106),
		max_value=Max_ABS_Multiplier(106),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER GILDA",
		addresses=[0x2fbd70],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(58),
		max_value=Max_GILDA_Multiplier(58),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER ATK",
		addresses=[0x2fbd7e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(58),
		max_value=Max_ATK_Multiplier(58),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER DEF",
		addresses=[0x2fbd80],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(48),
		max_value=Max_DEF_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER ITEM1",
		addresses=[0x2fbdb8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER ITEM2",
		addresses=[0x2fbdba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ALEXANDER ITEM3",
		addresses=[0x2fbdbc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#face of yaska 0x2FBDD4
	Attribute(
		name="FACE OF YASKA HP",
		addresses=[0x2fbe20],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3200),
		max_value=Max_HP_Multiplier(3200),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA ABS",
		addresses=[0x2fbe26],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA GILDA",
		addresses=[0x2fbe28],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA ATK",
		addresses=[0x2fbe36],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA DEF",
		addresses=[0x2fbe38],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(90),
		max_value=Max_DEF_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA ITEM1",
		addresses=[0x2fbe70],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA ITEM2",
		addresses=[0x2fbe72],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FACE OF YASKA ITEM3",
		addresses=[0x2fbe74],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#demon puppet 0x2FBE8C
	Attribute(
		name="DEMON PUPPET HP",
		addresses=[0x2fbed8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6700),
		max_value=Max_HP_Multiplier(6700),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET ABS",
		addresses=[0x2fbede],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET GILDA",
		addresses=[0x2fbee0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(110),
		max_value=Max_GILDA_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET ATK",
		addresses=[0x2fbeee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET DEF",
		addresses=[0x2fbef0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(100),
		max_value=Max_DEF_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET ITEM1",
		addresses=[0x2fbf28],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET ITEM2",
		addresses=[0x2fbf2a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DEMON PUPPET ITEM3",
		addresses=[0x2fbf2c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#smiling fairy 0x2FBF44
	Attribute(
		name="SMILING FAIRY HP",
		addresses=[0x2fbf90],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(99),
		max_value=Max_HP_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY ABS",
		addresses=[0x2fbf96],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(18),
		max_value=Max_ABS_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY GILDA",
		addresses=[0x2fbf98],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY ATK",
		addresses=[0x2fbfa6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(22),
		max_value=Max_ATK_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY DEF",
		addresses=[0x2fbfa8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(10),
		max_value=Max_DEF_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY ITEM1",
		addresses=[0x2fbfe0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY ITEM2",
		addresses=[0x2fbfe2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="SMILING FAIRY ITEM3",
		addresses=[0x2fbfe4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#heat fairy 0x2FBFFC
	Attribute(
		name="HEAT FAIRY HP",
		addresses=[0x2fc048],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550),
		max_value=Max_HP_Multiplier(550),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY ABS",
		addresses=[0x2fc04e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY GILDA",
		addresses=[0x2fc050],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY ATK",
		addresses=[0x2fc05e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(70),
		max_value=Max_ATK_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY DEF",
		addresses=[0x2fc060],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY ITEM1",
		addresses=[0x2fc098],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY ITEM2",
		addresses=[0x2fc09a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="HEAT FAIRY ITEM3",
		addresses=[0x2fc09c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#fairy helper 0x2FC0B4
	Attribute(
		name="FAIRY HELPER HP",
		addresses=[0x2fc100],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1600),
		max_value=Max_HP_Multiplier(1600),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER ABS",
		addresses=[0x2fc106],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER GILDA",
		addresses=[0x2fc108],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER ATK",
		addresses=[0x2fc116],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(124),
		max_value=Max_ATK_Multiplier(124),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER DEF",
		addresses=[0x2fc118],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(77),
		max_value=Max_DEF_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER ITEM1",
		addresses=[0x2fc150],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER ITEM2",
		addresses=[0x2fc152],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FAIRY HELPER ITEM3",
		addresses=[0x2fc154],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#hell fairy 0x2FC16C
	Attribute(
		name="HELL FAIRY HP",
		addresses=[0x2fc1b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6100),
		max_value=Max_HP_Multiplier(6100),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY ABS",
		addresses=[0x2fc1be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY GILDA",
		addresses=[0x2fc1c0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY ATK",
		addresses=[0x2fc1ce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY DEF",
		addresses=[0x2fc1d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY ITEM1",
		addresses=[0x2fc208],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY ITEM2",
		addresses=[0x2fc20a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="HELL FAIRY ITEM3",
		addresses=[0x2fc20c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#crecent baron 0x2FC224
	Attribute(
		name="CRECENT BARON HP",
		addresses=[0x2fc270],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(200),
		max_value=Max_HP_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON ABS",
		addresses=[0x2fc276],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(40),
		max_value=Max_ABS_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON GILDA",
		addresses=[0x2fc278],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON ATK",
		addresses=[0x2fc286],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(30),
		max_value=Max_ATK_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON DEF",
		addresses=[0x2fc288],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON ITEM1",
		addresses=[0x2fc2c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON ITEM2",
		addresses=[0x2fc2c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="CRECENT BARON ITEM3",
		addresses=[0x2fc2c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#stick joe 0x2FC2DC
	Attribute(
		name="STICK JOE HP",
		addresses=[0x2fc328],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(370),
		max_value=Max_HP_Multiplier(370),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE ABS",
		addresses=[0x2fc32e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(74),
		max_value=Max_ABS_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE GILDA",
		addresses=[0x2fc330],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(57),
		max_value=Max_GILDA_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE ATK",
		addresses=[0x2fc33e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(49),
		max_value=Max_ATK_Multiplier(49),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE DEF",
		addresses=[0x2fc340],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE ITEM1",
		addresses=[0x2fc378],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE ITEM2",
		addresses=[0x2fc37a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="STICK JOE ITEM3",
		addresses=[0x2fc37c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#moon joe 0x2FC394
	Attribute(
		name="MOON JOE HP",
		addresses=[0x2fc3e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1036),
		max_value=Max_HP_Multiplier(1036),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE ABS",
		addresses=[0x2fc3e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(198),
		max_value=Max_ABS_Multiplier(198),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE GILDA",
		addresses=[0x2fc3e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE ATK",
		addresses=[0x2fc3f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(111),
		max_value=Max_ATK_Multiplier(111),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE DEF",
		addresses=[0x2fc3f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(69),
		max_value=Max_DEF_Multiplier(69),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE ITEM1",
		addresses=[0x2fc430],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE ITEM2",
		addresses=[0x2fc432],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MOON JOE ITEM3",
		addresses=[0x2fc434],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#moonlight hulk 0x2FC44C
	Attribute(
		name="MOONLIGHT HULK HP",
		addresses=[0x2fc498],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7600),
		max_value=Max_HP_Multiplier(7600),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK ABS",
		addresses=[0x2fc49e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK GILDA",
		addresses=[0x2fc4a0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK ATK",
		addresses=[0x2fc4ae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK DEF",
		addresses=[0x2fc4b0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK ITEM1",
		addresses=[0x2fc4e8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK ITEM2",
		addresses=[0x2fc4ea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MOONLIGHT HULK ITEM3",
		addresses=[0x2fc4ec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#darkness 0x2FC504
	Attribute(
		name="DARKNESS HP",
		addresses=[0x2fc550],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(55),
		max_value=Max_HP_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS ABS",
		addresses=[0x2fc556],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS GILDA",
		addresses=[0x2fc558],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS ATK",
		addresses=[0x2fc566],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(11),
		max_value=Max_ATK_Multiplier(11),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS DEF",
		addresses=[0x2fc568],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(3),
		max_value=Max_DEF_Multiplier(3),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS ITEM1",
		addresses=[0x2fc5a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS ITEM2",
		addresses=[0x2fc5a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="DARKNESS ITEM3",
		addresses=[0x2fc5a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#sooty 0x2FC5BC
	Attribute(
		name="SOOTY HP",
		addresses=[0x2fc608],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(340),
		max_value=Max_HP_Multiplier(340),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY ABS",
		addresses=[0x2fc60e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(68),
		max_value=Max_ABS_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY GILDA",
		addresses=[0x2fc610],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(76),
		max_value=Max_GILDA_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY ATK",
		addresses=[0x2fc61e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(46),
		max_value=Max_ATK_Multiplier(46),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY DEF",
		addresses=[0x2fc620],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(33),
		max_value=Max_DEF_Multiplier(33),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY ITEM1",
		addresses=[0x2fc658],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY ITEM2",
		addresses=[0x2fc65a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SOOTY ITEM3",
		addresses=[0x2fc65c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#darker 0x2FC674
	Attribute(
		name="DARKER HP",
		addresses=[0x2fc6c0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2500),
		max_value=Max_HP_Multiplier(2500),
		is_little_endian=True, ),
	Attribute(
		name="DARKER ABS",
		addresses=[0x2fc6c6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="DARKER GILDA",
		addresses=[0x2fc6c8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="DARKER ATK",
		addresses=[0x2fc6d6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="DARKER DEF",
		addresses=[0x2fc6d8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(84),
		max_value=Max_DEF_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="DARKER ITEM1",
		addresses=[0x2fc710],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARKER ITEM2",
		addresses=[0x2fc712],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DARKER ITEM3",
		addresses=[0x2fc714],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#shadow 0x2FC72C
	Attribute(
		name="SHADOW HP",
		addresses=[0x2fc778],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(6400),
		max_value=Max_HP_Multiplier(6400),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW ABS",
		addresses=[0x2fc77e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW GILDA",
		addresses=[0x2fc780],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(1100),
		max_value=Max_GILDA_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW ATK",
		addresses=[0x2fc78e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(147),
		max_value=Max_ATK_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW DEF",
		addresses=[0x2fc790],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW ITEM1",
		addresses=[0x2fc7c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW ITEM2",
		addresses=[0x2fc7ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SHADOW ITEM3",
		addresses=[0x2fc7cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#priest of rama 0x2FC7E4
	Attribute(
		name="PRIEST OF RAMA HP",
		addresses=[0x2fc830],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(150),
		max_value=Max_HP_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA ABS",
		addresses=[0x2fc836],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA GILDA",
		addresses=[0x2fc838],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA ATK",
		addresses=[0x2fc846],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(27),
		max_value=Max_ATK_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA DEF",
		addresses=[0x2fc848],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA ITEM1",
		addresses=[0x2fc880],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA ITEM2",
		addresses=[0x2fc882],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="PRIEST OF RAMA ITEM3",
		addresses=[0x2fc884],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#sleeber 0x2FC89C
	Attribute(
		name="SLEEBER HP",
		addresses=[0x2fc8e8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730),
		max_value=Max_HP_Multiplier(730),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER ABS",
		addresses=[0x2fc8ee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(80),
		max_value=Max_ABS_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER GILDA",
		addresses=[0x2fc8f0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(147),
		max_value=Max_GILDA_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER ATK",
		addresses=[0x2fc8fe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(80),
		max_value=Max_ATK_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER DEF",
		addresses=[0x2fc900],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER ITEM1",
		addresses=[0x2fc938],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER ITEM2",
		addresses=[0x2fc93a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="SLEEBER ITEM3",
		addresses=[0x2fc93c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#crow priest 0x2FC954
	Attribute(
		name="CROW PRIEST HP",
		addresses=[0x2fc9a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(895),
		max_value=Max_HP_Multiplier(895),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST ABS",
		addresses=[0x2fc9a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(178),
		max_value=Max_ABS_Multiplier(178),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST GILDA",
		addresses=[0x2fc9a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(135),
		max_value=Max_GILDA_Multiplier(135),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST ATK",
		addresses=[0x2fc9b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(99),
		max_value=Max_ATK_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST DEF",
		addresses=[0x2fc9b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST ITEM1",
		addresses=[0x2fc9f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST ITEM2",
		addresses=[0x2fc9f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CROW PRIEST ITEM3",
		addresses=[0x2fc9f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#garuda 0x2FCA0C
	Attribute(
		name="GARUDA HP",
		addresses=[0x2fca58],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10500),
		max_value=Max_HP_Multiplier(10500),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA ABS",
		addresses=[0x2fca5e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA GILDA",
		addresses=[0x2fca60],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA ATK",
		addresses=[0x2fca6e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA DEF",
		addresses=[0x2fca70],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA ITEM1",
		addresses=[0x2fcaa8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA ITEM2",
		addresses=[0x2fcaaa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="GARUDA ITEM3",
		addresses=[0x2fcaac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#arthur 0x2FCAC4
	Attribute(
		name="ARTHUR HP",
		addresses=[0x2fcb10],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(780),
		max_value=Max_HP_Multiplier(780),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR ABS",
		addresses=[0x2fcb16],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(156),
		max_value=Max_ABS_Multiplier(156),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR GILDA",
		addresses=[0x2fcb18],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR ATK",
		addresses=[0x2fcb26],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(82),
		max_value=Max_ATK_Multiplier(82),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR DEF",
		addresses=[0x2fcb28],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR ITEM1",
		addresses=[0x2fcb60],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR ITEM2",
		addresses=[0x2fcb62],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ARTHUR ITEM3",
		addresses=[0x2fcb64],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#lancer 0x2FCB7C
	Attribute(
		name="LANCER HP",
		addresses=[0x2fcbc8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1900),
		max_value=Max_HP_Multiplier(1900),
		is_little_endian=True, ),
	Attribute(
		name="LANCER ABS",
		addresses=[0x2fcbce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="LANCER GILDA",
		addresses=[0x2fcbd0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(147),
		max_value=Max_GILDA_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="LANCER ATK",
		addresses=[0x2fcbde],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(115),
		max_value=Max_ATK_Multiplier(115),
		is_little_endian=True, ),
	Attribute(
		name="LANCER DEF",
		addresses=[0x2fcbe0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(71),
		max_value=Max_DEF_Multiplier(71),
		is_little_endian=True, ),
	Attribute(
		name="LANCER ITEM1",
		addresses=[0x2fcc18],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LANCER ITEM2",
		addresses=[0x2fcc1a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="LANCER ITEM3",
		addresses=[0x2fcc1c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#iron spear 0x2FCC34
	Attribute(
		name="IRON SPEAR HP",
		addresses=[0x2fcc80],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10000),
		max_value=Max_HP_Multiplier(10000),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR ABS",
		addresses=[0x2fcc86],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR GILDA",
		addresses=[0x2fcc88],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(160),
		max_value=Max_GILDA_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR ATK",
		addresses=[0x2fcc96],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR DEF",
		addresses=[0x2fcc98],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR ITEM1",
		addresses=[0x2fccd0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR ITEM2",
		addresses=[0x2fccd2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IRON SPEAR ITEM3",
		addresses=[0x2fccd4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#flying steel 0x2FCCEC
	Attribute(
		name="FLYING STEEL HP",
		addresses=[0x2fcd38],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11800),
		max_value=Max_HP_Multiplier(11800),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL ABS",
		addresses=[0x2fcd3e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(600),
		max_value=Max_ABS_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL GILDA",
		addresses=[0x2fcd40],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL ATK",
		addresses=[0x2fcd4e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(198),
		max_value=Max_ATK_Multiplier(198),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL DEF",
		addresses=[0x2fcd50],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(130),
		max_value=Max_DEF_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL ITEM1",
		addresses=[0x2fcd88],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL ITEM2",
		addresses=[0x2fcd8a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="FLYING STEEL ITEM3",
		addresses=[0x2fcd8c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#pirate tank 0x2FCDA4
	Attribute(
		name="PIRATE TANK HP",
		addresses=[0x2fcdf0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(400),
		max_value=Max_HP_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK ABS",
		addresses=[0x2fcdf6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(66),
		max_value=Max_ABS_Multiplier(66),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK GILDA",
		addresses=[0x2fcdf8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(75),
		max_value=Max_GILDA_Multiplier(75),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK ATK",
		addresses=[0x2fce06],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(45),
		max_value=Max_ATK_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK DEF",
		addresses=[0x2fce08],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(34),
		max_value=Max_DEF_Multiplier(34),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK ITEM1",
		addresses=[0x2fce40],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK ITEM2",
		addresses=[0x2fce42],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE TANK ITEM3",
		addresses=[0x2fce44],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#pirate eye 0x2FCE5C
	Attribute(
		name="PIRATE EYE HP",
		addresses=[0x2fcea8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730),
		max_value=Max_HP_Multiplier(730),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE ABS",
		addresses=[0x2fceae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(146),
		max_value=Max_ABS_Multiplier(146),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE GILDA",
		addresses=[0x2fceb0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(147),
		max_value=Max_GILDA_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE ATK",
		addresses=[0x2fcebe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(79),
		max_value=Max_ATK_Multiplier(79),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE DEF",
		addresses=[0x2fcec0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE ITEM1",
		addresses=[0x2fcef8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE ITEM2",
		addresses=[0x2fcefa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="PIRATE EYE ITEM3",
		addresses=[0x2fcefc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#angry canon 0x2FCF14
	Attribute(
		name="ANGRY CANON HP",
		addresses=[0x2fcf60],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3500),
		max_value=Max_HP_Multiplier(3500),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON ABS",
		addresses=[0x2fcf66],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON GILDA",
		addresses=[0x2fcf68],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(140),
		max_value=Max_GILDA_Multiplier(140),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON ATK",
		addresses=[0x2fcf76],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON DEF",
		addresses=[0x2fcf78],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(91),
		max_value=Max_DEF_Multiplier(91),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON ITEM1",
		addresses=[0x2fcfb0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON ITEM2",
		addresses=[0x2fcfb2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="ANGRY CANON ITEM3",
		addresses=[0x2fcfb4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#iron ghost 0x2FCFCC
	Attribute(
		name="IRON GHOST HP",
		addresses=[0x2fd018],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10600),
		max_value=Max_HP_Multiplier(10600),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST ABS",
		addresses=[0x2fd01e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST GILDA",
		addresses=[0x2fd020],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(85),
		max_value=Max_GILDA_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST ATK",
		addresses=[0x2fd02e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST DEF",
		addresses=[0x2fd030],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST ITEM1",
		addresses=[0x2fd068],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST ITEM2",
		addresses=[0x2fd06a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="IRON GHOST ITEM3",
		addresses=[0x2fd06c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#bomber head 0x2FD084
	Attribute(
		name="BOMBER HEAD HP",
		addresses=[0x2fd0d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(444),
		max_value=Max_HP_Multiplier(444),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD ABS",
		addresses=[0x2fd0d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD GILDA",
		addresses=[0x2fd0d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(22),
		max_value=Max_GILDA_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD ATK",
		addresses=[0x2fd0e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(51),
		max_value=Max_ATK_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD DEF",
		addresses=[0x2fd0e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(38),
		max_value=Max_DEF_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD ITEM1",
		addresses=[0x2fd120],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD ITEM2",
		addresses=[0x2fd122],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="BOMBER HEAD ITEM3",
		addresses=[0x2fd124],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#triple cracker 0x2FD13C
	Attribute(
		name="TRIPLE CRACKER HP",
		addresses=[0x2fd188],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(555),
		max_value=Max_HP_Multiplier(555),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER ABS",
		addresses=[0x2fd18e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(110),
		max_value=Max_ABS_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER GILDA",
		addresses=[0x2fd190],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER ATK",
		addresses=[0x2fd19e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(72),
		max_value=Max_ATK_Multiplier(72),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER DEF",
		addresses=[0x2fd1a0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER ITEM1",
		addresses=[0x2fd1d8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER ITEM2",
		addresses=[0x2fd1da],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="TRIPLE CRACKER ITEM3",
		addresses=[0x2fd1dc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#danger bomb 0x2FD1F4
	Attribute(
		name="DANGER BOMB HP",
		addresses=[0x2fd240],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2900),
		max_value=Max_HP_Multiplier(2900),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB ABS",
		addresses=[0x2fd246],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB GILDA",
		addresses=[0x2fd248],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(130),
		max_value=Max_GILDA_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB ATK",
		addresses=[0x2fd256],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(127),
		max_value=Max_ATK_Multiplier(127),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB DEF",
		addresses=[0x2fd258],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(87),
		max_value=Max_DEF_Multiplier(87),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB ITEM1",
		addresses=[0x2fd290],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB ITEM2",
		addresses=[0x2fd292],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="DANGER BOMB ITEM3",
		addresses=[0x2fd294],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#sweet dynamite 0x2FD2AC
	Attribute(
		name="SWEET DYNAMITE HP",
		addresses=[0x2fd2f8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10400),
		max_value=Max_HP_Multiplier(10400),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE ABS",
		addresses=[0x2fd2fe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE GILDA",
		addresses=[0x2fd300],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(145),
		max_value=Max_GILDA_Multiplier(145),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE ATK",
		addresses=[0x2fd30e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(172),
		max_value=Max_ATK_Multiplier(172),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE DEF",
		addresses=[0x2fd310],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE ITEM1",
		addresses=[0x2fd348],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE ITEM2",
		addresses=[0x2fd34a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SWEET DYNAMITE ITEM3",
		addresses=[0x2fd34c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#club 0x2FD364
	Attribute(
		name="CLUB HP",
		addresses=[0x2fd3b0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(833),
		max_value=Max_HP_Multiplier(833),
		is_little_endian=True, ),
	Attribute(
		name="CLUB ABS",
		addresses=[0x2fd3b6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(166),
		max_value=Max_ABS_Multiplier(166),
		is_little_endian=True, ),
	Attribute(
		name="CLUB GILDA",
		addresses=[0x2fd3b8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="CLUB ATK",
		addresses=[0x2fd3c6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(94),
		max_value=Max_ATK_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="CLUB DEF",
		addresses=[0x2fd3c8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="CLUB ITEM1",
		addresses=[0x2fd400],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CLUB ITEM2",
		addresses=[0x2fd402],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CLUB ITEM3",
		addresses=[0x2fd404],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#s club 0x2FD41C
	Attribute(
		name="S CLUB HP",
		addresses=[0x2fd468],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100),
		max_value=Max_HP_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB ABS",
		addresses=[0x2fd46e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB GILDA",
		addresses=[0x2fd470],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(102),
		max_value=Max_GILDA_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB ATK",
		addresses=[0x2fd47e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(112),
		max_value=Max_ATK_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB DEF",
		addresses=[0x2fd480],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB ITEM1",
		addresses=[0x2fd4b8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB ITEM2",
		addresses=[0x2fd4ba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S CLUB ITEM3",
		addresses=[0x2fd4bc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#r club 0x2FD4D4
	Attribute(
		name="R CLUB HP",
		addresses=[0x2fd520],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4200),
		max_value=Max_HP_Multiplier(4200),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB ABS",
		addresses=[0x2fd526],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB GILDA",
		addresses=[0x2fd528],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB ATK",
		addresses=[0x2fd536],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB DEF",
		addresses=[0x2fd538],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(95),
		max_value=Max_DEF_Multiplier(95),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB ITEM1",
		addresses=[0x2fd570],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB ITEM2",
		addresses=[0x2fd572],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R CLUB ITEM3",
		addresses=[0x2fd574],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#rsf club 0x2FD58C
	Attribute(
		name="RSF CLUB HP",
		addresses=[0x2fd5d8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(10800),
		max_value=Max_HP_Multiplier(10800),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB ABS",
		addresses=[0x2fd5de],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB GILDA",
		addresses=[0x2fd5e0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(100),
		max_value=Max_GILDA_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB ATK",
		addresses=[0x2fd5ee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB DEF",
		addresses=[0x2fd5f0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB ITEM1",
		addresses=[0x2fd628],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB ITEM2",
		addresses=[0x2fd62a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF CLUB ITEM3",
		addresses=[0x2fd62c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#heart 0x2FD644
	Attribute(
		name="HEART HP",
		addresses=[0x2fd690],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(842),
		max_value=Max_HP_Multiplier(842),
		is_little_endian=True, ),
	Attribute(
		name="HEART ABS",
		addresses=[0x2fd696],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(166),
		max_value=Max_ABS_Multiplier(166),
		is_little_endian=True, ),
	Attribute(
		name="HEART GILDA",
		addresses=[0x2fd698],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="HEART ATK",
		addresses=[0x2fd6a6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(94),
		max_value=Max_ATK_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="HEART DEF",
		addresses=[0x2fd6a8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="HEART ITEM1",
		addresses=[0x2fd6e0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="HEART ITEM2",
		addresses=[0x2fd6e2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="HEART ITEM3",
		addresses=[0x2fd6e4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#s heart 0x2FD6FC
	Attribute(
		name="S HEART HP",
		addresses=[0x2fd748],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100),
		max_value=Max_HP_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="S HEART ABS",
		addresses=[0x2fd74e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="S HEART GILDA",
		addresses=[0x2fd750],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(102),
		max_value=Max_GILDA_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="S HEART ATK",
		addresses=[0x2fd75e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(112),
		max_value=Max_ATK_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="S HEART DEF",
		addresses=[0x2fd760],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="S HEART ITEM1",
		addresses=[0x2fd798],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S HEART ITEM2",
		addresses=[0x2fd79a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S HEART ITEM3",
		addresses=[0x2fd79c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#r heart 0x2FD7B4
	Attribute(
		name="R HEART HP",
		addresses=[0x2fd800],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4300),
		max_value=Max_HP_Multiplier(4300),
		is_little_endian=True, ),
	Attribute(
		name="R HEART ABS",
		addresses=[0x2fd806],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="R HEART GILDA",
		addresses=[0x2fd808],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="R HEART ATK",
		addresses=[0x2fd816],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="R HEART DEF",
		addresses=[0x2fd818],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(96),
		max_value=Max_DEF_Multiplier(96),
		is_little_endian=True, ),
	Attribute(
		name="R HEART ITEM1",
		addresses=[0x2fd850],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R HEART ITEM2",
		addresses=[0x2fd852],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R HEART ITEM3",
		addresses=[0x2fd854],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#rsf heart 0x2FD86C
	Attribute(
		name="RSF HEART HP",
		addresses=[0x2fd8b8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11200),
		max_value=Max_HP_Multiplier(11200),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART ABS",
		addresses=[0x2fd8be],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART GILDA",
		addresses=[0x2fd8c0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART ATK",
		addresses=[0x2fd8ce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART DEF",
		addresses=[0x2fd8d0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART ITEM1",
		addresses=[0x2fd908],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART ITEM2",
		addresses=[0x2fd90a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF HEART ITEM3",
		addresses=[0x2fd90c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#spade 0x2FD924
	Attribute(
		name="SPADE HP",
		addresses=[0x2fd970],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850),
		max_value=Max_HP_Multiplier(850),
		is_little_endian=True, ),
	Attribute(
		name="SPADE ABS",
		addresses=[0x2fd976],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(166),
		max_value=Max_ABS_Multiplier(166),
		is_little_endian=True, ),
	Attribute(
		name="SPADE GILDA",
		addresses=[0x2fd978],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="SPADE ATK",
		addresses=[0x2fd986],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(94),
		max_value=Max_ATK_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="SPADE DEF",
		addresses=[0x2fd988],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(68),
		max_value=Max_DEF_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="SPADE ITEM1",
		addresses=[0x2fd9c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SPADE ITEM2",
		addresses=[0x2fd9c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="SPADE ITEM3",
		addresses=[0x2fd9c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#s spade 0x2FD9DC
	Attribute(
		name="S SPADE HP",
		addresses=[0x2fda28],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100),
		max_value=Max_HP_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE ABS",
		addresses=[0x2fda2e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE GILDA",
		addresses=[0x2fda30],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(102),
		max_value=Max_GILDA_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE ATK",
		addresses=[0x2fda3e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(112),
		max_value=Max_ATK_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE DEF",
		addresses=[0x2fda40],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE ITEM1",
		addresses=[0x2fda78],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE ITEM2",
		addresses=[0x2fda7a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S SPADE ITEM3",
		addresses=[0x2fda7c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#r spade 0x2FDA94
	Attribute(
		name="R SPADE HP",
		addresses=[0x2fdae0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4400),
		max_value=Max_HP_Multiplier(4400),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE ABS",
		addresses=[0x2fdae6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE GILDA",
		addresses=[0x2fdae8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE ATK",
		addresses=[0x2fdaf6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE DEF",
		addresses=[0x2fdaf8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(97),
		max_value=Max_DEF_Multiplier(97),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE ITEM1",
		addresses=[0x2fdb30],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE ITEM2",
		addresses=[0x2fdb32],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R SPADE ITEM3",
		addresses=[0x2fdb34],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#rsf spade 0x2FDB4C
	Attribute(
		name="RSF SPADE HP",
		addresses=[0x2fdb98],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11000),
		max_value=Max_HP_Multiplier(11000),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE ABS",
		addresses=[0x2fdb9e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE GILDA",
		addresses=[0x2fdba0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE ATK",
		addresses=[0x2fdbae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE DEF",
		addresses=[0x2fdbb0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE ITEM1",
		addresses=[0x2fdbe8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE ITEM2",
		addresses=[0x2fdbea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF SPADE ITEM3",
		addresses=[0x2fdbec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#diamond 0x2FDC04
	Attribute(
		name="DIAMOND HP",
		addresses=[0x2fdc50],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(865),
		max_value=Max_HP_Multiplier(865),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND ABS",
		addresses=[0x2fdc56],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(166),
		max_value=Max_ABS_Multiplier(166),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND GILDA",
		addresses=[0x2fdc58],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND ATK",
		addresses=[0x2fdc66],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(94),
		max_value=Max_ATK_Multiplier(94),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND DEF",
		addresses=[0x2fdc68],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND ITEM1",
		addresses=[0x2fdca0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND ITEM2",
		addresses=[0x2fdca2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="DIAMOND ITEM3",
		addresses=[0x2fdca4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#s diamond 0x2FDCBC
	Attribute(
		name="S DIAMOND HP",
		addresses=[0x2fdd08],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100),
		max_value=Max_HP_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND ABS",
		addresses=[0x2fdd0e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND GILDA",
		addresses=[0x2fdd10],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(102),
		max_value=Max_GILDA_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND ATK",
		addresses=[0x2fdd1e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(112),
		max_value=Max_ATK_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND DEF",
		addresses=[0x2fdd20],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND ITEM1",
		addresses=[0x2fdd58],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND ITEM2",
		addresses=[0x2fdd5a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S DIAMOND ITEM3",
		addresses=[0x2fdd5c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#r diamond 0x2FDD74
	Attribute(
		name="R DIAMOND HP",
		addresses=[0x2fddc0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4500),
		max_value=Max_HP_Multiplier(4500),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND ABS",
		addresses=[0x2fddc6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND GILDA",
		addresses=[0x2fddc8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND ATK",
		addresses=[0x2fddd6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND DEF",
		addresses=[0x2fddd8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(98),
		max_value=Max_DEF_Multiplier(98),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND ITEM1",
		addresses=[0x2fde10],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND ITEM2",
		addresses=[0x2fde12],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R DIAMOND ITEM3",
		addresses=[0x2fde14],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#rsf diamond 0x2FDE2C
	Attribute(
		name="RSF DIAMOND HP",
		addresses=[0x2fde78],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11100),
		max_value=Max_HP_Multiplier(11100),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND ABS",
		addresses=[0x2fde7e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND GILDA",
		addresses=[0x2fde80],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(111),
		max_value=Max_GILDA_Multiplier(111),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND ATK",
		addresses=[0x2fde8e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND DEF",
		addresses=[0x2fde90],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND ITEM1",
		addresses=[0x2fdec8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND ITEM2",
		addresses=[0x2fdeca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF DIAMOND ITEM3",
		addresses=[0x2fdecc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#joker 0x2FDEE4
	Attribute(
		name="JOKER HP",
		addresses=[0x2fdf30],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(910),
		max_value=Max_HP_Multiplier(910),
		is_little_endian=True, ),
	Attribute(
		name="JOKER ABS",
		addresses=[0x2fdf36],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(182),
		max_value=Max_ABS_Multiplier(182),
		is_little_endian=True, ),
	Attribute(
		name="JOKER GILDA",
		addresses=[0x2fdf38],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="JOKER ATK",
		addresses=[0x2fdf46],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(101),
		max_value=Max_ATK_Multiplier(101),
		is_little_endian=True, ),
	Attribute(
		name="JOKER DEF",
		addresses=[0x2fdf48],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(67),
		max_value=Max_DEF_Multiplier(67),
		is_little_endian=True, ),
	Attribute(
		name="JOKER ITEM1",
		addresses=[0x2fdf80],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="JOKER ITEM2",
		addresses=[0x2fdf82],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="JOKER ITEM3",
		addresses=[0x2fdf84],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#s joker 0x2FDF9C
	Attribute(
		name="S JOKER HP",
		addresses=[0x2fdfe8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100),
		max_value=Max_HP_Multiplier(1100),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER ABS",
		addresses=[0x2fdfee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(190),
		max_value=Max_ABS_Multiplier(190),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER GILDA",
		addresses=[0x2fdff0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(102),
		max_value=Max_GILDA_Multiplier(102),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER ATK",
		addresses=[0x2fdffe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(133),
		max_value=Max_ATK_Multiplier(133),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER DEF",
		addresses=[0x2fe000],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER ITEM1",
		addresses=[0x2fe038],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER ITEM2",
		addresses=[0x2fe03a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="S JOKER ITEM3",
		addresses=[0x2fe03c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#r joker 0x2FE054
	Attribute(
		name="R JOKER HP",
		addresses=[0x2fe0a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(4900),
		max_value=Max_HP_Multiplier(4900),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER ABS",
		addresses=[0x2fe0a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER GILDA",
		addresses=[0x2fe0a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER ATK",
		addresses=[0x2fe0b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(137),
		max_value=Max_ATK_Multiplier(137),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER DEF",
		addresses=[0x2fe0b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER ITEM1",
		addresses=[0x2fe0f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER ITEM2",
		addresses=[0x2fe0f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="R JOKER ITEM3",
		addresses=[0x2fe0f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#rsf joker 0x2FE10C
	Attribute(
		name="RSF JOKER HP",
		addresses=[0x2fe158],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11200),
		max_value=Max_HP_Multiplier(11200),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER ABS",
		addresses=[0x2fe15e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(500),
		max_value=Max_ABS_Multiplier(500),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER GILDA",
		addresses=[0x2fe160],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(120),
		max_value=Max_GILDA_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER ATK",
		addresses=[0x2fe16e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(177),
		max_value=Max_ATK_Multiplier(177),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER DEF",
		addresses=[0x2fe170],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(120),
		max_value=Max_DEF_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER ITEM1",
		addresses=[0x2fe1a8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER ITEM2",
		addresses=[0x2fe1aa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="RSF JOKER ITEM3",
		addresses=[0x2fe1ac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mimic (uwc) 0x2FE1C4
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fe210],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(80),
		max_value=Max_HP_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe216],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(8),
		max_value=Max_ABS_Multiplier(8),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe218],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(9),
		max_value=Max_GILDA_Multiplier(9),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe226],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(9),
		max_value=Max_ATK_Multiplier(9),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe228],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(2),
		max_value=Max_DEF_Multiplier(2),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe260],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe262],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe264],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#king mimic (uwc) 0x2FE27C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe2c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(150),
		max_value=Max_HP_Multiplier(150),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe2ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe2d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(12),
		max_value=Max_GILDA_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fe2de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(14),
		max_value=Max_ATK_Multiplier(14),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fe2e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(7),
		max_value=Max_DEF_Multiplier(7),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fe318],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fe31a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fe31c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#mimic (rbw) 0x2FE334
		Attribute(
		name="MIMIC HP",
		addresses=[0x2fe380],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(120),
		max_value=Max_HP_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe386],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(10),
		max_value=Max_ABS_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe388],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe396],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(19),
		max_value=Max_ATK_Multiplier(19),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe398],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(10),
		max_value=Max_DEF_Multiplier(10),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe3d0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe3d2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe3d4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#king mimic (rbw) 0x2FE3EC
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe438],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(250),
		max_value=Max_HP_Multiplier(250),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe43e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(16),
		max_value=Max_ABS_Multiplier(16),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe440],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(18),
		max_value=Max_GILDA_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fe44e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(21),
		max_value=Max_ATK_Multiplier(21),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fe450],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(15),
		max_value=Max_DEF_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fe488],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fe48a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fe48c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#mimic (slc) 0x2FE4A4
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fe4f0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(300),
		max_value=Max_HP_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe4f6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(20),
		max_value=Max_ABS_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe4f8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(27),
		max_value=Max_GILDA_Multiplier(27),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe506],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(28),
		max_value=Max_ATK_Multiplier(28),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe508],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(18),
		max_value=Max_DEF_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe540],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe542],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe544],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#king mimic (slc) 0x2FE55C
		Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe5a8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(400),
		max_value=Max_HP_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe5ae],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(38),
		max_value=Max_ABS_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe5b0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(20),
		max_value=Max_GILDA_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fe5be],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(38),
		max_value=Max_ATK_Multiplier(38),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fe5c0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(20),
		max_value=Max_DEF_Multiplier(20),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fe5f8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fe5fa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fe5fc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#mimic (orc) 0x2FE614
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fe660],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(350),
		max_value=Max_HP_Multiplier(350),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe666],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe668],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(40),
		max_value=Max_GILDA_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe676],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(45),
		max_value=Max_ATK_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe678],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe6b0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe6b2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe6b4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#king mimic (orc) 0x2FE6CC
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe718],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600),
		max_value=Max_HP_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe71e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(40),
		max_value=Max_ABS_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe720],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(40),
		max_value=Max_GILDA_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fe72e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(51),
		max_value=Max_ATK_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fe730],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(40),
		max_value=Max_DEF_Multiplier(40),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fe768],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fe76a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fe76c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#mimic (mgd) 0x2FE784
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fe7d0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(460),
		max_value=Max_HP_Multiplier(460),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe7d6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(92),
		max_value=Max_ABS_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe7d8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(51),
		max_value=Max_GILDA_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe7e6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(51),
		max_value=Max_ATK_Multiplier(51),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe7e8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(45),
		max_value=Max_DEF_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe820],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe822],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe824],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#king mimic (mgd) 0x2FE83C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe888],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750),
		max_value=Max_HP_Multiplier(750),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe88e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(120),
		max_value=Max_ABS_Multiplier(120),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe890],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fe89e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(61),
		max_value=Max_ATK_Multiplier(61),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fe8a0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(50),
		max_value=Max_DEF_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fe8d8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fe8da],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fe8dc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#mimic (rbw) (star) 0x2FE8F4
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fe940],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650),
		max_value=Max_HP_Multiplier(650),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fe946],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(130),
		max_value=Max_ABS_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fe948],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fe956],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(74),
		max_value=Max_ATK_Multiplier(74),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fe958],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(58),
		max_value=Max_DEF_Multiplier(58),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fe990],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fe992],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fe994],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#king mimic (rbw) (star) 0x2FE9AC
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fe9f8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730),
		max_value=Max_HP_Multiplier(730),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fe9fe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(146),
		max_value=Max_ABS_Multiplier(146),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fe9fe],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fea00],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(77),
		max_value=Max_ATK_Multiplier(77),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fea0e],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(57),
		max_value=Max_DEF_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fea10],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fea48],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fea4c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#mimic (slc) (star) 0x2FEA64
	Attribute(
		name="MIMIC HP",
		addresses=[0x2feab0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650),
		max_value=Max_HP_Multiplier(650),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2feab6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(130),
		max_value=Max_ABS_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2feab8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2feac6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(76),
		max_value=Max_ATK_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2feac8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(62),
		max_value=Max_DEF_Multiplier(62),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2feb00],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2feb02],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2feb04],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#king mimic (slc) (star) 0x2FEB1C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2feb68],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800),
		max_value=Max_HP_Multiplier(800),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2feb6e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(160),
		max_value=Max_ABS_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2feb70],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2feb7e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(84),
		max_value=Max_ATK_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2feb80],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2febb8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2febba],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2febbc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#mimic (orc) (star) 0x2FEBD4
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fec20],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800),
		max_value=Max_HP_Multiplier(800),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fec26],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(130),
		max_value=Max_ABS_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fec28],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fec36],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(76),
		max_value=Max_ATK_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fec38],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(57),
		max_value=Max_DEF_Multiplier(57),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fec70],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fec72],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fec74],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#king mimic (orc) (star) 0x2FEC8C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fecd8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800),
		max_value=Max_HP_Multiplier(800),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fecde],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(160),
		max_value=Max_ABS_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fece0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fecee],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(85),
		max_value=Max_ATK_Multiplier(85),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fecf0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fed28],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fed2a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fed2c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#mimic (mfp) 0x2FED44
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fed90],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1350),
		max_value=Max_HP_Multiplier(1350),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fed96],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(100),
		max_value=Max_ABS_Multiplier(100),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fed98],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2feda6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(107),
		max_value=Max_ATK_Multiplier(107),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2feda8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(73),
		max_value=Max_DEF_Multiplier(73),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fede0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fede2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fede4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#king mimic (mfp) 0x2FEDFC
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fee48],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1300),
		max_value=Max_HP_Multiplier(1300),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fee4e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fee50],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(112),
		max_value=Max_GILDA_Multiplier(112),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fee5e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(117),
		max_value=Max_ATK_Multiplier(117),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fee60],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(80),
		max_value=Max_DEF_Multiplier(80),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2fee98],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2fee9a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2fee9c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#mimic (zmm) 0x2FEEB4
	Attribute(
		name="MIMIC HP",
		addresses=[0x2fef00],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(3600),
		max_value=Max_HP_Multiplier(3600),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2fef06],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(240),
		max_value=Max_ABS_Multiplier(240),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2fef08],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(50),
		max_value=Max_GILDA_Multiplier(50),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2fef16],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(132),
		max_value=Max_ATK_Multiplier(132),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2fef18],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(93),
		max_value=Max_DEF_Multiplier(93),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2fef50],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2fef52],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2fef54],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#king mimic (zmm) 0x2FEF6C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2fefb8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7000),
		max_value=Max_HP_Multiplier(7000),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2fefbe],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(300),
		max_value=Max_ABS_Multiplier(300),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2fefc0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(90),
		max_value=Max_GILDA_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2fefce],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(142),
		max_value=Max_ATK_Multiplier(142),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2fefd0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(92),
		max_value=Max_DEF_Multiplier(92),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2ff008],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2ff00a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2ff00c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mimic (zmm) (depths) 0x2FF024
	Attribute(
		name="MIMIC HP",
		addresses=[0x2ff070],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(7900),
		max_value=Max_HP_Multiplier(7900),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2ff076],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(360),
		max_value=Max_ABS_Multiplier(360),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2ff078],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(99),
		max_value=Max_GILDA_Multiplier(99),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2ff086],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(152),
		max_value=Max_ATK_Multiplier(152),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2ff088],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(105),
		max_value=Max_DEF_Multiplier(105),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2ff0c0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2ff0c2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2ff0c4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#king mimic (zmm) (depths) 0x2FF0DC
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2ff128],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11700),
		max_value=Max_HP_Multiplier(11700),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2ff12e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(600),
		max_value=Max_ABS_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2ff130],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2ff13e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(182),
		max_value=Max_ATK_Multiplier(182),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2ff140],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(130),
		max_value=Max_DEF_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2ff178],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2ff17a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2ff17c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#mimic (mgd) (star) 0x2FF194
	Attribute(
		name="MIMIC HP",
		addresses=[0x2ff1e0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650),
		max_value=Max_HP_Multiplier(650),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ABS",
		addresses=[0x2ff1e6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(130),
		max_value=Max_ABS_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC GILDA",
		addresses=[0x2ff1e8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ATK",
		addresses=[0x2ff1f6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(76),
		max_value=Max_ATK_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC DEF",
		addresses=[0x2ff1f8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(58),
		max_value=Max_DEF_Multiplier(58),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM1",
		addresses=[0x2ff230],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM2",
		addresses=[0x2ff232],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="MIMIC ITEM3",
		addresses=[0x2ff234],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#king mimic (mgd) star) 0x2FF24C
	Attribute(
		name="KING MIMIC HP",
		addresses=[0x2ff298],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800),
		max_value=Max_HP_Multiplier(800),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ABS",
		addresses=[0x2ff29e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(160),
		max_value=Max_ABS_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC GILDA",
		addresses=[0x2ff2a0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(78),
		max_value=Max_GILDA_Multiplier(78),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ATK",
		addresses=[0x2ff2ae],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(84),
		max_value=Max_ATK_Multiplier(84),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC DEF",
		addresses=[0x2ff2b0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(65),
		max_value=Max_DEF_Multiplier(65),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM1",
		addresses=[0x2ff2e8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM2",
		addresses=[0x2ff2ea],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="KING MIMIC ITEM3",
		addresses=[0x2ff2ec],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#sonic bomber 0x2FF304
	Attribute(
		name="SONIC BOMBER HP",
		addresses=[0x2ff350],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(210),
		max_value=Max_HP_Multiplier(210),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER ABS",
		addresses=[0x2ff356],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(18),
		max_value=Max_ABS_Multiplier(18),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER GILDA",
		addresses=[0x2ff358],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(21),
		max_value=Max_GILDA_Multiplier(21),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER ATK",
		addresses=[0x2ff366],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(19),
		max_value=Max_ATK_Multiplier(19),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER DEF",
		addresses=[0x2ff368],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(12),
		max_value=Max_DEF_Multiplier(12),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER ITEM1",
		addresses=[0x2ff3a0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER ITEM2",
		addresses=[0x2ff3a2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
	Attribute(
		name="SONIC BOMBER ITEM3",
		addresses=[0x2ff3a4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sindain"),
		is_little_endian=True, ),
#ultrasonic bomb 0x2FF3BC
	Attribute(
		name="ULTRASONIC BOMB HP",
		addresses=[0x2ff408],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(540),
		max_value=Max_HP_Multiplier(540),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB ABS",
		addresses=[0x2ff40e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(108),
		max_value=Max_ABS_Multiplier(108),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB GILDA",
		addresses=[0x2ff410],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB ATK",
		addresses=[0x2ff41e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(56),
		max_value=Max_ATK_Multiplier(56),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB DEF",
		addresses=[0x2ff420],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(48),
		max_value=Max_DEF_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB ITEM1",
		addresses=[0x2ff458],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB ITEM2",
		addresses=[0x2ff45a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="ULTRASONIC BOMB ITEM3",
		addresses=[0x2ff45c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#metal bomber 0x2FF474
	Attribute(
		name="METAL BOMBER HP",
		addresses=[0x2ff4c0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850),
		max_value=Max_HP_Multiplier(850),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER ABS",
		addresses=[0x2ff4c6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(156),
		max_value=Max_ABS_Multiplier(156),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER GILDA",
		addresses=[0x2ff4c8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(68),
		max_value=Max_GILDA_Multiplier(68),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER ATK",
		addresses=[0x2ff4d6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(83),
		max_value=Max_ATK_Multiplier(83),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER DEF",
		addresses=[0x2ff4d8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(60),
		max_value=Max_DEF_Multiplier(60),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER ITEM1",
		addresses=[0x2ff510],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER ITEM2",
		addresses=[0x2ff512],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="METAL BOMBER ITEM3",
		addresses=[0x2ff514],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#krau mauness 0x2FF52C
	Attribute(
		name="KRAU MAUNESS HP",
		addresses=[0x2ff578],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(9100),
		max_value=Max_HP_Multiplier(9100),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS ABS",
		addresses=[0x2ff57e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(400),
		max_value=Max_ABS_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS GILDA",
		addresses=[0x2ff580],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS ATK",
		addresses=[0x2ff58e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(162),
		max_value=Max_ATK_Multiplier(162),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS DEF",
		addresses=[0x2ff590],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(110),
		max_value=Max_DEF_Multiplier(110),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS ITEM1",
		addresses=[0x2ff5c8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS ITEM2",
		addresses=[0x2ff5ca],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="KRAU MAUNESS ITEM3",
		addresses=[0x2ff5cc],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#yoyo barrel 0x2FF5E4
	Attribute(
		name="YOYO BARREL HP",
		addresses=[0x2ff630],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(160),
		max_value=Max_HP_Multiplier(160),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL ABS",
		addresses=[0x2ff636],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL GILDA",
		addresses=[0x2ff638],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(45),
		max_value=Max_GILDA_Multiplier(45),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL ATK",
		addresses=[0x2ff646],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(28),
		max_value=Max_ATK_Multiplier(28),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL DEF",
		addresses=[0x2ff648],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(30),
		max_value=Max_DEF_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL ITEM1",
		addresses=[0x2ff680],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL ITEM2",
		addresses=[0x2ff682],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
	Attribute(
		name="YOYO BARREL ITEM3",
		addresses=[0x2ff684],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Valley"),
		is_little_endian=True, ),
#rolling rocks 0x2FF69C
	Attribute(
		name="ROLLING ROCKS HP",
		addresses=[0x2ff6e8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730),
		max_value=Max_HP_Multiplier(730),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS ABS",
		addresses=[0x2ff6ee],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(146),
		max_value=Max_ABS_Multiplier(146),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS GILDA",
		addresses=[0x2ff6f0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(147),
		max_value=Max_GILDA_Multiplier(147),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS ATK",
		addresses=[0x2ff6fe],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(76),
		max_value=Max_ATK_Multiplier(76),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS DEF",
		addresses=[0x2ff700],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(55),
		max_value=Max_DEF_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS ITEM1",
		addresses=[0x2ff738],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS ITEM2",
		addresses=[0x2ff73a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
	Attribute(
		name="ROLLING ROCKS ITEM3",
		addresses=[0x2ff73c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Star"),
		is_little_endian=True, ),
#clock knight 0x2FF754
	Attribute(
		name="CLOCK KNIGHT HP",
		addresses=[0x2ff7a0],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2300),
		max_value=Max_HP_Multiplier(2300),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT ABS",
		addresses=[0x2ff7a6],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(200),
		max_value=Max_ABS_Multiplier(200),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT GILDA",
		addresses=[0x2ff7a8],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(148),
		max_value=Max_GILDA_Multiplier(148),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT ATK",
		addresses=[0x2ff7b6],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(114),
		max_value=Max_ATK_Multiplier(114),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT DEF",
		addresses=[0x2ff7b8],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT ITEM1",
		addresses=[0x2ff7f0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT ITEM2",
		addresses=[0x2ff7f2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
	Attribute(
		name="CLOCK KNIGHT ITEM3",
		addresses=[0x2ff7f4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Moon"),
		is_little_endian=True, ),
#spinning saucer 0x2FF80C
	Attribute(
		name="SPINNING SAUCER HP",
		addresses=[0x2ff858],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(11600),
		max_value=Max_HP_Multiplier(11600),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER ABS",
		addresses=[0x2ff85e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(600),
		max_value=Max_ABS_Multiplier(600),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER GILDA",
		addresses=[0x2ff860],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(90),
		max_value=Max_GILDA_Multiplier(90),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER ATK",
		addresses=[0x2ff86e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(182),
		max_value=Max_ATK_Multiplier(182),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER DEF",
		addresses=[0x2ff870],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(130),
		max_value=Max_DEF_Multiplier(130),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER ITEM1",
		addresses=[0x2ff8a8],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER ITEM2",
		addresses=[0x2ff8aa],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="SPINNING SAUCER ITEM3",
		addresses=[0x2ff8ac],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
#bat 0x2FF8C4
	Attribute(
		name="BAT HP",
		addresses=[0x2ff910],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(22),
		max_value=Max_HP_Multiplier(22),
		is_little_endian=True, ),
	Attribute(
		name="BAT ABS",
		addresses=[0x2ff916],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="BAT GILDA",
		addresses=[0x2ff918],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(6),
		max_value=Max_GILDA_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="BAT ATK",
		addresses=[0x2ff926],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(6),
		max_value=Max_ATK_Multiplier(6),
		is_little_endian=True, ),
	Attribute(
		name="BAT DEF",
		addresses=[0x2ff928],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(0),
		max_value=Max_DEF_Multiplier(0),
		is_little_endian=True, ),
	Attribute(
		name="BAT ITEM1",
		addresses=[0x2ff960],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="BAT ITEM2",
		addresses=[0x2ff962],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
	Attribute(
		name="BAT ITEM3",
		addresses=[0x2ff964],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Sewer"),
		is_little_endian=True, ),
#sea bat 0x2FF97C
	Attribute(
		name="SEA BAT HP",
		addresses=[0x2ff9c8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(250),
		max_value=Max_HP_Multiplier(250),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT ABS",
		addresses=[0x2ff9ce],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(30),
		max_value=Max_ABS_Multiplier(30),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT GILDA",
		addresses=[0x2ff9d0],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(15),
		max_value=Max_GILDA_Multiplier(15),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT ATK",
		addresses=[0x2ff9de],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(37),
		max_value=Max_ATK_Multiplier(37),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT DEF",
		addresses=[0x2ff9e0],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(25),
		max_value=Max_DEF_Multiplier(25),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT ITEM1",
		addresses=[0x2ffa18],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT ITEM2",
		addresses=[0x2ffa1a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
	Attribute(
		name="SEA BAT ITEM3",
		addresses=[0x2ffa1c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Veniccio"),
		is_little_endian=True, ),
#lava bat 0x2FFA34
	Attribute(
		name="LAVA BAT HP",
		addresses=[0x2ffa80],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(400),
		max_value=Max_HP_Multiplier(400),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT ABS",
		addresses=[0x2ffa86],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(55),
		max_value=Max_ABS_Multiplier(55),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT GILDA",
		addresses=[0x2ffa88],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(32),
		max_value=Max_GILDA_Multiplier(32),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT ATK",
		addresses=[0x2ffa96],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(48),
		max_value=Max_ATK_Multiplier(48),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT DEF",
		addresses=[0x2ffa98],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(35),
		max_value=Max_DEF_Multiplier(35),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT ITEM1",
		addresses=[0x2ffad0],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT ITEM2",
		addresses=[0x2ffad2],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
	Attribute(
		name="LAVA BAT ITEM3",
		addresses=[0x2ffad4],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Heim"),
		is_little_endian=True, ),
#evil bat 0x2FFAEC
	Attribute(
		name="EVIL BAT HP",
		addresses=[0x2ffb38],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1000),
		max_value=Max_HP_Multiplier(1000),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT ABS",
		addresses=[0x2ffb3e],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(180),
		max_value=Max_ABS_Multiplier(180),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT GILDA",
		addresses=[0x2ffb40],
		number_of_bytes=2,
		min_value=Min_GILDA_Multiplier(88),
		max_value=Max_GILDA_Multiplier(88),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT ATK",
		addresses=[0x2ffb4e],
		number_of_bytes=2,
		min_value=Min_ATK_Multiplier(122),
		max_value=Max_ATK_Multiplier(122),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT DEF",
		addresses=[0x2ffb50],
		number_of_bytes=2,
		min_value=Min_DEF_Multiplier(70),
		max_value=Max_DEF_Multiplier(70),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT ITEM1",
		addresses=[0x2ffb88],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT ITEM2",
		addresses=[0x2ffb8a],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
	Attribute(
		name="EVIL BAT ITEM3",
		addresses=[0x2ffb8c],
		number_of_bytes=2,
		possible_values=ChooseItemDrops("Zelmite"),
		is_little_endian=True, ),
# END OF MONSTERS
	# START OF SHOPS

	# 01 POLLY SHOP
	# POLLY ITEM POOL [219,220,221,268,425]
	Attribute(
		name="POLLY ITEM 1",
		addresses=[0x9b3a7d7, 0x9b3cfe0, 0x9b3f7e7, 0x9b42010, 0x9b447f0, 0x9b477f0, 0x9b4a7f0, 0x9b4d7fc, 0x9b507d7,
				   0x9b52fe0, 0x9b557e7, 0x9b57ff0, 0x9b5a7f0, 0x9b5cff0, 0x9b5fff0, 0x9b62ffc],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 2",
		addresses=[0x9b3a7db, 0x9b3cfe4, 0x9b3f7eb, 0x9b42014, 0x9b447f4, 0x9b477f4, 0x9b4a7f4, 0x9b4d800, 0x9b507db,
				   0x9b52fe4, 0x9b557eb, 0x9b57ff4, 0x9b5a7f4, 0x9b5cff4, 0x9b5fff4, 0x9b63000],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 3",
		addresses=[0x9b3a7df, 0x9b3cfe8, 0x9b3f7ef, 0x9b42018, 0x9b447f8, 0x9b477f8, 0x9b4a7f8, 0x9b4d804, 0x9b507df,
				   0x9b52fe8, 0x9b557ef, 0x9b57ff8, 0x9b5a7f8, 0x9b5cff8, 0x9b5fff8, 0x9b63004],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 4",
		addresses=[0x9b3a7e3, 0x9b3cfec, 0x9b3f7f3, 0x9b4201c, 0x9b447fc, 0x9b477fc, 0x9b4a7fc, 0x9b4d808, 0x9b507e3,
				   0x9b52fec, 0x9b557f3, 0x9b57ffc, 0x9b5a7fc, 0x9b5cffc, 0x9b5fffc, 0x9b63008],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 5",
		addresses=[0x9b3a7e7, 0x9b3cff0, 0x9b3f7f7, 0x9b42020, 0x9b44800, 0x9b47800, 0x9b4a800, 0x9b4d80c, 0x9b507e7,
				   0x9b52ff0, 0x9b557f7, 0x9b58000, 0x9b5a800, 0x9b5d000, 0x9b60000, 0x9b6300c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),

	# 02 DELL SHOP
	# DELL ITEM POOL [279]
	Attribute(
		name="DELL ITEM 1",
		addresses=[0x9b3a80c, 0x9b3d015, 0x9b3f81c, 0x9b42025, 0x9b44825, 0x9b47825, 0x9b4a825, 0x9b4d831, 0x9b5080c,
				   0x9b53015, 0x9b5581c, 0x9b58025, 0x9b5a825, 0x9b5d025, 0x9b60025, 0x9b63031],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DELL"),
		is_little_endian=False, ),

	# 03 FERDINAND SHOP
	# FERDINAND ITEM POOL [270]
	Attribute(
		name="FERDINAND ITEM 1",
		addresses=[0x9b3a82d, 0x9b3d036, 0x9b3f83d, 0x9b42046, 0x9b44846, 0x9b47846, 0x9b4a846, 0x9b4d852, 0x9b5082d,
				   0x9b53036, 0x9b5583d, 0x9b58046, 0x9b5a846, 0x9b5d046, 0x9b60046, 0x9b63052],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FERDINAND"),
		is_little_endian=False, ),

	# 04 MORTONS SHOP
	# MORTON ITEM POOL [186,187,188,189,190,191,192,193,194,195
	# 			   ,196,197,200,201,202,203,204,205,206,207
	# 			   ,208,209,215,224,227,245,275,280,390,391
	# 			   ,294,298,381,172,355,358,174,376]
	Attribute(
		name="MORTON ITEM 1",
		addresses=[0x9b50852, 0x9b5305b, 0x9b55862, 0x9b3a852, 0x9b3d05b, 0x9b5806b, 0x9b3f862, 0x9b5a86b, 0x9b4206b,
				   0x9b5d06b, 0x9b6006b, 0x9b4486b, 0x9b4786b, 0x9b4a86b, 0x9b63077, 0x9b4d877],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 2",
		addresses=[0x9b50856, 0x9b5305f, 0x9b55866, 0x9b3a856, 0x9b3d05f, 0x9b5806f, 0x9b3f866, 0x9b5a86f, 0x9b4206f,
				   0x9b5d06f, 0x9b6006f, 0x9b4486f, 0x9b4786f, 0x9b4a86f, 0x9b6307b, 0x9b4d87b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 3",
		addresses=[0x9b5085a, 0x9b53063, 0x9b5586a, 0x9b3a85a, 0x9b3d063, 0x9b58073, 0x9b3f86a, 0x9b5a873, 0x9b42073,
				   0x9b5d073, 0x9b60073, 0x9b44873, 0x9b47873, 0x9b4a873, 0x9b6307f, 0x9b4d87f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 4",
		addresses=[0x9b5085e, 0x9b53067, 0x9b5586e, 0x9b3a85e, 0x9b3d067, 0x9b58077, 0x9b3f86e, 0x9b5a877, 0x9b42077,
				   0x9b5d077, 0x9b60077, 0x9b44877, 0x9b47877, 0x9b4a877, 0x9b63083, 0x9b4d883],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 5",
		addresses=[0x9b50862, 0x9b5306b, 0x9b55872, 0x9b3a862, 0x9b3d06b, 0x9b5807b, 0x9b3f872, 0x9b5a87b, 0x9b4207b,
				   0x9b5d07b, 0x9b6007b, 0x9b4487b, 0x9b4787b, 0x9b4a87b, 0x9b63087, 0x9b4d887],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 6",
		addresses=[0x9b50866, 0x9b5306f, 0x9b55876, 0x9b3a866, 0x9b3d06f, 0x9b5807f, 0x9b3f876, 0x9b5a87f, 0x9b4207f,
				   0x9b5d07f, 0x9b6007f, 0x9b4487f, 0x9b4787f, 0x9b4a87f, 0x9b6308b, 0x9b4d88b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 7",
		addresses=[0x9b5086a, 0x9b53073, 0x9b5587a, 0x9b3a86a, 0x9b3d073, 0x9b58083, 0x9b3f87a, 0x9b5a883, 0x9b42083,
				   0x9b5d083, 0x9b60083, 0x9b44883, 0x9b47883, 0x9b4a883, 0x9b6308f, 0x9b4d88f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 8",
		addresses=[0x9b5086e, 0x9b53077, 0x9b5587e, 0x9b3a86e, 0x9b3d077, 0x9b58087, 0x9b3f87e, 0x9b5a887, 0x9b42087,
				   0x9b5d087, 0x9b60087, 0x9b44887, 0x9b47887, 0x9b4a887, 0x9b63093, 0x9b4d893],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 9",
		addresses=[0x9b50872, 0x9b5307b, 0x9b55882, 0x9b3a872, 0x9b3d07b, 0x9b5808b, 0x9b3f882, 0x9b5a88b, 0x9b4208b,
				   0x9b5d08b, 0x9b6008b, 0x9b4488b, 0x9b4788b, 0x9b4a88b, 0x9b63097, 0x9b4d897],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 10",
		addresses=[0x9b50876, 0x9b5307f, 0x9b55886, 0x9b3a876, 0x9b3d07f, 0x9b5808f, 0x9b3f886, 0x9b5a88f, 0x9b4208f,
				   0x9b5d08f, 0x9b6008f, 0x9b4488f, 0x9b4788f, 0x9b4a88f, 0x9b6309b, 0x9b4d89b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 11",
		addresses=[0x9b5588a, 0x9b3a87a, 0x9b3d083, 0x9b58093, 0x9b3f88a, 0x9b5a893, 0x9b42093, 0x9b5d093, 0x9b60093,
				   0x9b44893, 0x9b47893, 0x9b4a893, 0x9b6309f, 0x9b4d89f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 12",
		addresses=[0x9b58097, 0x9b3f88e, 0x9b5a897, 0x9b42097, 0x9b5d097, 0x9b60097, 0x9b44897, 0x9b47897, 0x9b4a897,
				   0x9b630a3, 0x9b4d8a3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 13",
		addresses=[0x9b5a89b, 0x9b4209b, 0x9b5d09b, 0x9b6009b, 0x9b4489b, 0x9b4789b, 0x9b4a89b, 0x9b630a7, 0x9b4d8a7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 14",
		addresses=[0x9b5d09f, 0x9b6009f, 0x9b4489f, 0x9b4789f, 0x9b4a89f, 0x9b630ab, 0x9b4d8ab],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 15",
		addresses=[0x9b478a3, 0x9b4a8a3, 0x9b630af, 0x9b4d8af],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),

	Attribute(
		name="MORTON ITEM 16",
		addresses=[0x9b630b3, 0x9b4d8b3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 17",
		addresses=[0x9b630b7, 0x9b4d8b7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 18",
		addresses=[0x9b630bb, 0x9b4d8bb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 19",
		addresses=[0x9b630bf, 0x9b4d8bf],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 20",
		addresses=[0x9b630c3, 0x9b4d8c3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 21",
		addresses=[0x9b630c7, 0x9b4d8c7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 22",
		addresses=[0x9b630cb, 0x9b4d8cb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 23",
		addresses=[0x9b630cf, 0x9b4d8cf],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 24",
		addresses=[0x9b630d3, 0x9b4d8d3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 25",
		addresses=[0x9b630d7, 0x9b4d8d7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 26",
		addresses=[0x9b630db, 0x9b4d8db],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 27",
		addresses=[0x9b630df, 0x9b4d8df],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 28",
		addresses=[0x9b630e3, 0x9b4d8e3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 29",
		addresses=[0x9b630e7, 0x9b4d8e7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 30",
		addresses=[0x9b630eb, 0x9b4d8eb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 31",
		addresses=[0x9b630ef, 0x9b4d8ef],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 32",
		addresses=[0x9b630f3, 0x9b4d8f3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 33",
		addresses=[0x9b630f7, 0x9b4d8f7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 34",
		addresses=[0x9b630fb, 0x9b4d8fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 35",
		addresses=[0x9b630ff, 0x9b4d8ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 36",
		addresses=[0x9b63103, 0x9b4d903],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 36",
		addresses=[0x9b63107, 0x9b4d907],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 37",
		addresses=[0x9b4d90b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),

	# 05 STARLIGHT TEMPLE SHOP
	# STARLIGHT TEMPLE ITEM POOL [265,175,176,177,178,179,180,181,182,183
	#						 ,184,269,275,279,425,294,371]
	Attribute(
		name="STARLIGHT TEMPLE ITEM 1",
		addresses=[0x9b3a89b, 0x9b3d0a4, 0x9b3f8af, 0x9b420bc, 0x9b448c0, 0x9b478c4, 0x9b4a8c4, 0x9b4d92c, 0x9b50897,
				   0x9b530a0, 0x9b558ab, 0x9b580b8, 0x9b5a8bc, 0x9b5d0c0, 0x9b600c0, 0x9b63128],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 2",
		addresses=[0x9b3a89f, 0x9b3d0a8, 0x9b3f8b3, 0x9b420c0, 0x9b448c4, 0x9b478c8, 0x9b4a8c8, 0x9b4d930, 0x9b5089b,
				   0x9b530a4, 0x9b558af, 0x9b580bc, 0x9b5a8c0, 0x9b5d0c4, 0x9b600c4, 0x9b6312c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 3",
		addresses=[0x9b3a8a3, 0x9b3d0ac, 0x9b3f8b7, 0x9b420c4, 0x9b448c8, 0x9b478cc, 0x9b4a8cc, 0x9b4d934, 0x9b5089f,
				   0x9b530a8, 0x9b558b3, 0x9b580c0, 0x9b5a8c4, 0x9b5d0c8, 0x9b600c8, 0x9b63130],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 4",
		addresses=[0x9b3a8a7, 0x9b3d0b0, 0x9b3f8bb, 0x9b420c8, 0x9b448cc, 0x9b478d0, 0x9b4a8d0, 0x9b4d938, 0x9b508a3,
				   0x9b530ac, 0x9b558b7, 0x9b580c4, 0x9b5a8c8, 0x9b5d0cc, 0x9b600cc, 0x9b63134],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 5",
		addresses=[0x9b3a8ab, 0x9b3d0b4, 0x9b3f8bf, 0x9b420cc, 0x9b448d0, 0x9b478d4, 0x9b4a8d4, 0x9b4d93c, 0x9b508a7,
				   0x9b530b0, 0x9b558bb, 0x9b580c8, 0x9b5a8cc, 0x9b5d0d0, 0x9b600d0, 0x9b63138],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 6",
		addresses=[0x9b3a8af, 0x9b3d0b8, 0x9b3f8c3, 0x9b420d0, 0x9b448d4, 0x9b478d8, 0x9b4a8d8, 0x9b4d940, 0x9b508ab,
				   0x9b530b4, 0x9b558bf, 0x9b580cc, 0x9b5a8d0, 0x9b5d0d4, 0x9b600d4, 0x9b6313c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 7",
		addresses=[0x9b3a8b3, 0x9b3d0bc, 0x9b3f8c7, 0x9b420d4, 0x9b448d8, 0x9b478dc, 0x9b4a8dc, 0x9b4d944, 0x9b508af,
				   0x9b530b8, 0x9b558c3, 0x9b580d0, 0x9b5a8d4, 0x9b5d0d8, 0x9b600d8, 0x9b63140],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 8",
		addresses=[0x9b3a8b7, 0x9b3d0c0, 0x9b3f8cb, 0x9b420d8, 0x9b448dc, 0x9b478e0, 0x9b4a8e0, 0x9b4d948, 0x9b508b3,
				   0x9b530bc, 0x9b558c7, 0x9b580d4, 0x9b5a8d8, 0x9b5d0dc, 0x9b600dc, 0x9b63144],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 9",
		addresses=[0x9b3a8bb, 0x9b3d0c4, 0x9b3f8cf, 0x9b420dc, 0x9b448e0, 0x9b478e4, 0x9b4a8e4, 0x9b4d94c, 0x9b508b7,
				   0x9b530c0, 0x9b558cb, 0x9b580d8, 0x9b5a8dc, 0x9b5d0e0, 0x9b600e0, 0x9b63148],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 10",
		addresses=[0x9b3a8bf, 0x9b3d0c8, 0x9b3f8d3, 0x9b420e0, 0x9b448e4, 0x9b478e8, 0x9b4a8e8, 0x9b4d950, 0x9b508bb,
				   0x9b530c4, 0x9b558cf, 0x9b580dc, 0x9b5a8e0, 0x9b5d0e4, 0x9b600e4, 0x9b6314c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 11",
		addresses=[0x9b3a8c3, 0x9b3d0cc, 0x9b3f8d7, 0x9b420e4, 0x9b448e8, 0x9b478ec, 0x9b4a8ec, 0x9b4d954, 0x9b508bf,
				   0x9b530c8, 0x9b558d3, 0x9b580e0, 0x9b5a8e4, 0x9b5d0e8, 0x9b600e8, 0x9b63150],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 12",
		addresses=[0x9b3a8c7, 0x9b3d0d0, 0x9b3f8db, 0x9b420e8, 0x9b448ec, 0x9b478f0, 0x9b4a8f0, 0x9b4d958, 0x9b508c3,
				   0x9b530cc, 0x9b558d7, 0x9b580e4, 0x9b5a8e8, 0x9b5d0ec, 0x9b600ec, 0x9b63154],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 13",
		addresses=[0x9b3a8cb, 0x9b3d0d4, 0x9b3f8df, 0x9b420ec, 0x9b448f0, 0x9b478f4, 0x9b4a8f4, 0x9b4d95c, 0x9b508c7,
				   0x9b530d0, 0x9b558db, 0x9b580e8, 0x9b5a8ec, 0x9b5d0f0, 0x9b600f0, 0x9b63158],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 14",
		addresses=[0x9b3a8cf, 0x9b3d0d8, 0x9b3f8e3, 0x9b420f0, 0x9b448f4, 0x9b478f8, 0x9b4a8f8, 0x9b4d960, 0x9b508cb,
				   0x9b530d4, 0x9b558df, 0x9b580ec, 0x9b5a8f0, 0x9b5d0f4, 0x9b600f4, 0x9b6315c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 15",
		addresses=[0x9b3a8d3, 0x9b3d0dc, 0x9b3f8e7, 0x9b420f4, 0x9b448f8, 0x9b478fc, 0x9b4a8fc, 0x9b4d964, 0x9b508cf,
				   0x9b530d8, 0x9b558e3, 0x9b580f0, 0x9b5a8f4, 0x9b5d0f8, 0x9b600f8, 0x9b63160],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 16",
		addresses=[0x9b3a8d7, 0x9b3d0e0, 0x9b3f8eb, 0x9b420f8, 0x9b448fc, 0x9b47900, 0x9b4a900, 0x9b4d968, 0x9b508d3,
				   0x9b530dc, 0x9b558e7, 0x9b580f4, 0x9b5a8f8, 0x9b5d0fc, 0x9b600fc, 0x9b63164],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 17",
		addresses=[0x9b3a8db, 0x9b3d0e4, 0x9b3f8ef, 0x9b420fc, 0x9b44900, 0x9b47904, 0x9b4a904, 0x9b4d96c, 0x9b508d7,
				   0x9b530e0, 0x9b558eb, 0x9b580f8, 0x9b5a8fc, 0x9b5d100, 0x9b60100, 0x9b63168],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),

	# 06 DONNY SHOP
	# DONNY ITEM POOL [260,111,112,113,114,268,275,294,298,297
	#			  ,355]
	Attribute(
		name="DONNY ITEM 1",
		addresses=[0x9b508fc, 0x9b53105, 0x9b3a900, 0x9b3d109, 0x9b55910, 0x9b5811d, 0x9b3f914, 0x9b42121, 0x9b5a921,
				   0x9b44925, 0x9b5d125, 0x9b60125, 0x9b6318d, 0x9b47929, 0x9b4a929, 0x9b4d991],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 2",
		addresses=[0x9b50900, 0x9b53109, 0x9b3a904, 0x9b3d10d, 0x9b55914, 0x9b58121, 0x9b3f918, 0x9b42125, 0x9b5a925,
				   0x9b44929, 0x9b5d129, 0x9b60129, 0x9b63191, 0x9b4792d, 0x9b4a92d, 0x9b4d995],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 3",
		addresses=[0x9b50904, 0x9b5310d, 0x9b3a908, 0x9b3d111, 0x9b55918, 0x9b58125, 0x9b3f91c, 0x9b42129, 0x9b5a929,
				   0x9b4492d, 0x9b5d12d, 0x9b6012d, 0x9b63195, 0x9b47931, 0x9b4a931, 0x9b4d999],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 4",
		addresses=[0x9b50908, 0x9b53111, 0x9b3a90c, 0x9b3d115, 0x9b5591c, 0x9b58129, 0x9b3f920, 0x9b4212d, 0x9b5a92d,
				   0x9b44931, 0x9b5d131, 0x9b60131, 0x9b63199, 0x9b47935, 0x9b4a935, 0x9b4d99d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 5",
		addresses=[0x9b5090c, 0x9b53115, 0x9b3a910, 0x9b3d119, 0x9b55920, 0x9b5812d, 0x9b3f924, 0x9b42131, 0x9b5a931,
				   0x9b44935, 0x9b5d135, 0x9b60135, 0x9b6319d, 0x9b47939, 0x9b4a939, 0x9b4d9a1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 6",
		addresses=[0x9b3a914, 0x9b3d11d, 0x9b55924, 0x9b58131, 0x9b3f928, 0x9b42135, 0x9b5a935, 0x9b44939, 0x9b5d139,
				   0x9b60139, 0x9b631a1, 0x9b4793d, 0x9b4a93d, 0x9b4d9a5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 7",
		addresses=[0x9b58135, 0x9b3f92c, 0x9b42139, 0x9b5a939, 0x9b4493d, 0x9b5d13d, 0x9b6013d, 0x9b631a5, 0x9b47941,
				   0x9b4a941, 0x9b4d9a9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 8",
		addresses=[0x9b4213d, 0x9b5a93d, 0x9b44941, 0x9b5d141, 0x9b60141, 0x9b631a9, 0x9b47945, 0x9b4a945, 0x9b4d9ad],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 9",
		addresses=[0x9b44945, 0x9b5d145, 0x9b60145, 0x9b631ad, 0x9b47949, 0x9b4a949, 0x9b4d9b1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 10",
		addresses=[0x9b60149, 0x9b631b1, 0x9b4794d, 0x9b4a94d, 0x9b4d9b5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 11",
		addresses=[0x9b4a951, 0x9b4d9b9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),

	# 07 BORNEO SHOP
	# BORNEO ITEM POOL [212,225,226,227]
	Attribute(
		name="BORNEO ITEM 1",
		addresses=[0x9b3a933, 0x9b3d13c, 0x9b3f94b, 0x9b4215c, 0x9b44964, 0x9b4796c, 0x9b4a970, 0x9b4d9d8, 0x9b5092b,
				   0x9b53134, 0x9b55943, 0x9b58154, 0x9b5a95c, 0x9b5d164, 0x9b60168, 0x9b631d0],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 2",
		addresses=[0x9b3a937, 0x9b3d140, 0x9b3f94f, 0x9b42160, 0x9b44968, 0x9b47970, 0x9b4a974, 0x9b4d9dc, 0x9b5092f,
				   0x9b53138, 0x9b55947, 0x9b58158, 0x9b5a960, 0x9b5d168, 0x9b6016c, 0x9b631d4],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 3",
		addresses=[0x9b3a93b, 0x9b3d144, 0x9b3f953, 0x9b42164, 0x9b4496c, 0x9b47974, 0x9b4a978, 0x9b4d9e0, 0x9b50933,
				   0x9b5313c, 0x9b5594b, 0x9b5815c, 0x9b5a964, 0x9b5d16c, 0x9b60170, 0x9b631d8],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 4",
		addresses=[0x9b3a93f, 0x9b3d148, 0x9b3f957, 0x9b42168, 0x9b44970, 0x9b47978, 0x9b4a97c, 0x9b4d9e4, 0x9b50937,
				   0x9b53140, 0x9b5594f, 0x9b58160, 0x9b5a968, 0x9b5d170, 0x9b60174, 0x9b631dc],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),

	# 08 GORDON SHOP
	# GORDON ITEM POOL [210,211,223,272]
	Attribute(
		name="GORDON ITEM 1",
		addresses=[0x9b3a95e, 0x9b3d167, 0x9b3f976, 0x9b42187, 0x9b50956, 0x9b5315f, 0x9b5596e, 0x9b5817f, 0x9b4498f,
				   0x9b47997, 0x9b4a99b, 0x9b4da03, 0x9b5a987, 0x9b5d18f, 0x9b60193, 0x9b631fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 2",
		addresses=[0x9b3a962, 0x9b3d16b, 0x9b3f97a, 0x9b4218b, 0x9b5095a, 0x9b53163, 0x9b55972, 0x9b58183, 0x9b44993,
				   0x9b4799b, 0x9b4a99f, 0x9b4da07, 0x9b5a98b, 0x9b5d193, 0x9b60197, 0x9b631ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 3",
		addresses=[0x9b3a966, 0x9b3d16f, 0x9b3f97e, 0x9b4218f, 0x9b5095e, 0x9b53167, 0x9b55976, 0x9b58187, 0x9b44997,
				   0x9b4799f, 0x9b4a9a3, 0x9b4da0b, 0x9b5a98f, 0x9b5d197, 0x9b6019b, 0x9b63203],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 4",
		addresses=[0x9b4499b, 0x9b479a3, 0x9b4a9a7, 0x9b4da0f, 0x9b5a993, 0x9b5d19b, 0x9b6019f, 0x9b63207],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),

	# 09 PARN SHOP
	# PARN ITEM POOL [237,238,239,240,241,242,243,244]
	Attribute(
		name="PARN ITEM 1",
		addresses=[0x9b3a987, 0x9b3d190, 0x9b3f99f, 0x9b421b0, 0x9b449bc, 0x9b479c4, 0x9b4a9c8, 0x9b4da30, 0x9b5097f,
				   0x9b53188, 0x9b55997, 0x9b581a8, 0x9b5a9b4, 0x9b5d1bc, 0x9b601c0, 0x9b63228],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 2",
		addresses=[0x9b3a98b, 0x9b3d194, 0x9b3f9a3, 0x9b421b4, 0x9b449c0, 0x9b479c8, 0x9b4a9cc, 0x9b4da34, 0x9b50983,
				   0x9b5318c, 0x9b5599b, 0x9b581ac, 0x9b5a9b8, 0x9b5d1c0, 0x9b601c4, 0x9b6322c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 3",
		addresses=[0x9b3a98f, 0x9b3d198, 0x9b3f9a7, 0x9b421b8, 0x9b449c4, 0x9b479cc, 0x9b4a9d0, 0x9b4da38, 0x9b50987,
				   0x9b53190, 0x9b5599f, 0x9b581b0, 0x9b5a9bc, 0x9b5d1c4, 0x9b601c8, 0x9b63230],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 4",
		addresses=[0x9b3a993, 0x9b3d19c, 0x9b3f9ab, 0x9b421bc, 0x9b449c8, 0x9b479d0, 0x9b4a9d4, 0x9b4da3c, 0x9b5098b,
				   0x9b53194, 0x9b559a3, 0x9b581b4, 0x9b5a9c0, 0x9b5d1c8, 0x9b601cc, 0x9b63234],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 5",
		addresses=[0x9b3a997, 0x9b3d1a0, 0x9b3f9af, 0x9b421c0, 0x9b449cc, 0x9b479d4, 0x9b4a9d8, 0x9b4da40, 0x9b5098f,
				   0x9b53198, 0x9b559a7, 0x9b581b8, 0x9b5a9c4, 0x9b5d1cc, 0x9b601d0, 0x9b63238],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 6",
		addresses=[0x9b3a99b, 0x9b3d1a4, 0x9b3f9b3, 0x9b421c4, 0x9b449d0, 0x9b479d8, 0x9b4a9dc, 0x9b4da44, 0x9b50993,
				   0x9b5319c, 0x9b559ab, 0x9b581bc, 0x9b5a9c8, 0x9b5d1d0, 0x9b601d4, 0x9b6323c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 7",
		addresses=[0x9b3a99f, 0x9b3d1a8, 0x9b3f9b7, 0x9b421c8, 0x9b449d4, 0x9b479dc, 0x9b4a9e0, 0x9b4da48, 0x9b50997,
				   0x9b531a0, 0x9b559af, 0x9b581c0, 0x9b5a9cc, 0x9b5d1d4, 0x9b601d8, 0x9b63240],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 8",
		addresses=[0x9b3a9a3, 0x9b3d1ac, 0x9b3f9bb, 0x9b421cc, 0x9b449d8, 0x9b479e0, 0x9b4a9e4, 0x9b4da4c, 0x9b5099b,
				   0x9b531a4, 0x9b559b3, 0x9b581c4, 0x9b5a9d0, 0x9b5d1d8, 0x9b601dc, 0x9b63244],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),

	# 10 CLAIRE SHOP
	# CLAIRE ITEM POOL [304]
	Attribute(
		name="CLAIRE ITEM 1",
		addresses=[0x9b3a9c9, 0x9b3d1d2, 0x9b3f9e1, 0x9b421f2, 0x9b449fe, 0x9b47a06, 0x9b4aa0a, 0x9b4da72, 0x9b509c1,
				   0x9b531ca, 0x9b559d9, 0x9b581ea, 0x9b5a9f6, 0x9b5d1fe, 0x9b60202, 0x9b6326a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CLAIRE"),
		is_little_endian=False, ),

	# 11 STEWART SHOP
	# STEWART ITEM POOL [117,118,119,120]
	Attribute(
		name="STEWART ITEM 1",
		addresses=[0x9b3a9eb, 0x9b3d1f4, 0x9b3fa03, 0x9b42214, 0x9b44a20, 0x9b47a28, 0x9b4aa2c, 0x9b4da94, 0x9b509e3,
				   0x9b531ec, 0x9b559fb, 0x9b5820c, 0x9b5aa18, 0x9b5d220, 0x9b60224, 0x9b6328c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 2",
		addresses=[0x9b3a9ef, 0x9b3d1f8, 0x9b3fa07, 0x9b42218, 0x9b44a24, 0x9b47a2c, 0x9b4aa30, 0x9b4da98, 0x9b509e7,
				   0x9b531f0, 0x9b559ff, 0x9b58210, 0x9b5aa1c, 0x9b5d224, 0x9b60228, 0x9b63290],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 3",
		addresses=[0x9b3a9f3, 0x9b3d1fc, 0x9b3fa0b, 0x9b4221c, 0x9b44a28, 0x9b47a30, 0x9b4aa34, 0x9b4da9c, 0x9b509eb,
				   0x9b531f4, 0x9b55a03, 0x9b58214, 0x9b5aa20, 0x9b5d228, 0x9b6022c, 0x9b63294],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 4",
		addresses=[0x9b3a9f7, 0x9b3d200, 0x9b3fa0f, 0x9b42220, 0x9b44a2c, 0x9b47a34, 0x9b4aa38, 0x9b4daa0, 0x9b509ef,
				   0x9b531f8, 0x9b55a07, 0x9b58218, 0x9b5aa24, 0x9b5d22c, 0x9b60230, 0x9b63298],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),

	# 12 ADEL SHOP
	# ADEL ITEM POOL [425,287,288,289,291,292]
	Attribute(
		name="ADEL ITEM 1",
		addresses=[0x9b3aa19, 0x9b3d222, 0x9b3fa31, 0x9b42242, 0x9b44a4e, 0x9b47a56, 0x9b4aa5a, 0x9b4dac2, 0x9b50a11,
				   0x9b5321a, 0x9b55a29, 0x9b5823a, 0x9b5aa46, 0x9b5d24e, 0x9b60252, 0x9b632ba],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 2",
		addresses=[0x9b3aa1d, 0x9b3d226, 0x9b3fa35, 0x9b42246, 0x9b44a52, 0x9b47a5a, 0x9b4aa5e, 0x9b4dac6, 0x9b50a15,
				   0x9b5321e, 0x9b55a2d, 0x9b5823e, 0x9b5aa4a, 0x9b5d252, 0x9b60256, 0x9b632be],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 3",
		addresses=[0x9b3aa21, 0x9b3d22a, 0x9b3fa39, 0x9b4224a, 0x9b44a56, 0x9b47a5e, 0x9b4aa62, 0x9b4daca, 0x9b50a19,
				   0x9b53222, 0x9b55a31, 0x9b58242, 0x9b5aa4e, 0x9b5d256, 0x9b6025a, 0x9b632c2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 4",
		addresses=[0x9b3aa25, 0x9b3d22e, 0x9b3fa3d, 0x9b4224e, 0x9b44a5a, 0x9b47a62, 0x9b4aa66, 0x9b4dace, 0x9b50a1d,
				   0x9b53226, 0x9b55a35, 0x9b58246, 0x9b5aa52, 0x9b5d25a, 0x9b6025e, 0x9b632c6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 5",
		addresses=[0x9b3aa29, 0x9b3d232, 0x9b3fa41, 0x9b42252, 0x9b44a5e, 0x9b47a66, 0x9b4aa6a, 0x9b4dad2, 0x9b50a21,
				   0x9b5322a, 0x9b55a39, 0x9b5824a, 0x9b5aa56, 0x9b5d25e, 0x9b60262, 0x9b632ca],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 6",
		addresses=[0x9b3aa2d, 0x9b3d236, 0x9b3fa45, 0x9b42256, 0x9b44a62, 0x9b47a6a, 0x9b4aa6e, 0x9b4dad6, 0x9b50a25,
				   0x9b5322e, 0x9b55a3d, 0x9b5824e, 0x9b5aa5a, 0x9b5d262, 0x9b60266, 0x9b632ce],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),

	# 13 ERIK SHOP
	# ERIK ITEM POOL [215]
	Attribute(
		name="ERIK ITEM 1",
		addresses=[0x9b3aa49, 0x9b3d252, 0x9b3fa61, 0x9b42272, 0x9b44a7e, 0x9b47a86, 0x9b4aa8a, 0x9b4daf2, 0x9b50a41,
				   0x9b5324a, 0x9b55a59, 0x9b5826a, 0x9b5aa76, 0x9b5d27e, 0x9b60282, 0x9b632ea],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ERIK"),
		is_little_endian=False, ),

	# 14 GERALD SHOP
	# GERALD ITEM POOL [10,24,26,28,36]

	# 15 BRUNO SHOP
	# BRUNO ITEM POOL [275,276,277,278]
	Attribute(
		name="BRUNO ITEM 1",
		addresses=[0x9b3aa8e, 0x9b3d297, 0x9b3faa9, 0x9b422c0, 0x9b44acf, 0x9b47ad7, 0x9b4aadb, 0x9b4db43, 0x9b50a86,
				   0x9b5328f, 0x9b55aa1, 0x9b582b8, 0x9b5aac7, 0x9b5d2cf, 0x9b602d3, 0x9b6333b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 2",
		addresses=[0x9b3aa92, 0x9b3d29b, 0x9b3faad, 0x9b422c4, 0x9b44ad3, 0x9b47adb, 0x9b4aadf, 0x9b4db47, 0x9b50a8a,
				   0x9b53293, 0x9b55aa5, 0x9b582bc, 0x9b5aacb, 0x9b5d2d3, 0x9b602d7, 0x9b6333f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 3",
		addresses=[0x9b3aa96, 0x9b3d29f, 0x9b3fab1, 0x9b422c8, 0x9b44ad7, 0x9b47adf, 0x9b4aae3, 0x9b4db4b, 0x9b50a8e,
				   0x9b53297, 0x9b55aa9, 0x9b582c0, 0x9b5aacf, 0x9b5d2d7, 0x9b602db, 0x9b63343],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 4",
		addresses=[0x9b3aa9a, 0x9b3d2a3, 0x9b3fab5, 0x9b422cc, 0x9b44adb, 0x9b47ae3, 0x9b4aae7, 0x9b4db4f, 0x9b50a92,
				   0x9b5329b, 0x9b55aad, 0x9b582c4, 0x9b5aad3, 0x9b5d2db, 0x9b602df, 0x9b63347],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),

	# 16 RUFIO SHOP
	# RUFIO ITEM POOL [175,176,177,178,179,180,181,182,183,184,228,229,230,231,232,233,234,235,236]
	Attribute(
		name="RUFIO ITEM 1",
		addresses=[0x9b3aabe, 0x9b3d2c7, 0x9b3fad9, 0x9b422f0, 0x9b44aff, 0x9b47b07, 0x9b4ab0b, 0x9b50ab6, 0x9b532bf,
				   0x9b55ad1, 0x9b582e8, 0x9b5aaf7, 0x9b5d2ff, 0x9b60303, 0x9b4db73, 0x9b6336b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 2",
		addresses=[0x9b3aac2, 0x9b3d2cb, 0x9b3fadd, 0x9b422f4, 0x9b44b03, 0x9b47b0b, 0x9b4ab0f, 0x9b50aba, 0x9b532c3,
				   0x9b55ad5, 0x9b582ec, 0x9b5aafb, 0x9b5d303, 0x9b60307, 0x9b4db77, 0x9b6336f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 3",
		addresses=[0x9b3aac6, 0x9b3d2cf, 0x9b3fae1, 0x9b422f8, 0x9b44b07, 0x9b47b0f, 0x9b4ab13, 0x9b50abe, 0x9b532c7,
				   0x9b55ad9, 0x9b582f0, 0x9b5aaff, 0x9b5d307, 0x9b6030b, 0x9b4db7b, 0x9b63373],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 4",
		addresses=[0x9b3aaca, 0x9b3d2d3, 0x9b3fae5, 0x9b422fc, 0x9b44b0b, 0x9b47b13, 0x9b4ab17, 0x9b50ac2, 0x9b532cb,
				   0x9b55add, 0x9b582f4, 0x9b5ab03, 0x9b5d30b, 0x9b6030f, 0x9b4db7f, 0x9b63377],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 5",
		addresses=[0x9b3aace, 0x9b3d2d7, 0x9b3fae9, 0x9b42300, 0x9b44b0f, 0x9b47b17, 0x9b4ab1b, 0x9b50ac6, 0x9b532cf,
				   0x9b55ae1, 0x9b582f8, 0x9b5ab07, 0x9b5d30f, 0x9b60313, 0x9b4db83, 0x9b6337b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 6",
		addresses=[0x9b3aad2, 0x9b3d2db, 0x9b3faed, 0x9b42304, 0x9b44b13, 0x9b47b1b, 0x9b4ab1f, 0x9b50aca, 0x9b532d3,
				   0x9b55ae5, 0x9b582fc, 0x9b5ab0b, 0x9b5d313, 0x9b60317, 0x9b4db87, 0x9b6337f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 7",
		addresses=[0x9b3aad6, 0x9b3d2df, 0x9b3faf1, 0x9b42308, 0x9b44b17, 0x9b47b1f, 0x9b4ab23, 0x9b50ace, 0x9b532d7,
				   0x9b55ae9, 0x9b58300, 0x9b5ab0f, 0x9b5d317, 0x9b6031b, 0x9b4db8b, 0x9b63383],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 8",
		addresses=[0x9b3aada, 0x9b3d2e3, 0x9b3faf5, 0x9b4230c, 0x9b44b1b, 0x9b47b23, 0x9b4ab27, 0x9b50ad2, 0x9b532db,
				   0x9b55aed, 0x9b58304, 0x9b5ab13, 0x9b5d31b, 0x9b6031f, 0x9b4db8f, 0x9b63387],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 9",
		addresses=[0x9b3aade, 0x9b3d2e7, 0x9b3faf9, 0x9b42310, 0x9b44b1f, 0x9b47b27, 0x9b4ab2b, 0x9b50ad6, 0x9b532df,
				   0x9b55af1, 0x9b58308, 0x9b5ab17, 0x9b5d31f, 0x9b60323, 0x9b4db93, 0x9b6338b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 10",
		addresses=[0x9b3aae2, 0x9b3d2eb, 0x9b3fafd, 0x9b42314, 0x9b44b23, 0x9b47b2b, 0x9b4ab2f, 0x9b50ada, 0x9b532e3,
				   0x9b55af5, 0x9b5830c, 0x9b5ab1b, 0x9b5d323, 0x9b60327, 0x9b4db97, 0x9b6338f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 11",
		addresses=[0x9b3aae6, 0x9b3d2ef, 0x9b3fb01, 0x9b42318, 0x9b44b27, 0x9b47b2f, 0x9b4ab33, 0x9b50ade, 0x9b532e7,
				   0x9b55af9, 0x9b58310, 0x9b5ab1f, 0x9b5d327, 0x9b6032b, 0x9b4db9b, 0x9b63393],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 12",
		addresses=[0x9b3aaea, 0x9b3d2f3, 0x9b3fb05, 0x9b4231c, 0x9b44b2b, 0x9b47b33, 0x9b4ab37, 0x9b50ae2, 0x9b532eb,
				   0x9b55afd, 0x9b58314, 0x9b5ab23, 0x9b5d32b, 0x9b6032f, 0x9b4db9f, 0x9b63397],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 13",
		addresses=[0x9b3aaee, 0x9b3d2f7, 0x9b3fb09, 0x9b42320, 0x9b44b2f, 0x9b47b37, 0x9b4ab3b, 0x9b50ae6, 0x9b532ef,
				   0x9b55b01, 0x9b58318, 0x9b5ab27, 0x9b5d32f, 0x9b60333, 0x9b4dba3, 0x9b6339b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 14",
		addresses=[0x9b4dba7, 0x9b6339f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 15",
		addresses=[0x9b4dbab, 0x9b633a3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 16",
		addresses=[0x9b4dbaf, 0x9b633a7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 17",
		addresses=[0x9b4dbb3, 0x9b633ab],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 18",
		addresses=[0x9b4dbb7, 0x9b633af],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 19",
		addresses=[0x9b4dbbb, 0x9b633b3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),

	# 17 FLAVIN SHOP
	# FLAVIN ITEM POOL [312,313,314,315,316,317,318,319]
	Attribute(
		name="FLAVIN ITEM 1",
		addresses=[0x9b3ab10, 0x9b3d319, 0x9b3fb2b, 0x9b42342, 0x9b44b51, 0x9b47b59, 0x9b4ab5d, 0x9b4dbdd, 0x9b50b08,
				   0x9b53311, 0x9b55b23, 0x9b5833a, 0x9b5ab49, 0x9b5d351, 0x9b60355, 0x9b633d5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 2",
		addresses=[0x9b3ab14, 0x9b3d31d, 0x9b3fb2f, 0x9b42346, 0x9b44b55, 0x9b47b5d, 0x9b4ab61, 0x9b4dbe1, 0x9b50b0c,
				   0x9b53315, 0x9b55b27, 0x9b5833e, 0x9b5ab4d, 0x9b5d355, 0x9b60359, 0x9b633d9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 3",
		addresses=[0x9b3ab18, 0x9b3d321, 0x9b3fb33, 0x9b4234a, 0x9b44b59, 0x9b47b61, 0x9b4ab65, 0x9b4dbe5, 0x9b50b10,
				   0x9b53319, 0x9b55b2b, 0x9b58342, 0x9b5ab51, 0x9b5d359, 0x9b6035d, 0x9b633dd],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 4",
		addresses=[0x9b3ab1c, 0x9b3d325, 0x9b3fb37, 0x9b4234e, 0x9b44b5d, 0x9b47b65, 0x9b4ab69, 0x9b4dbe9, 0x9b50b14,
				   0x9b5331d, 0x9b55b2f, 0x9b58346, 0x9b5ab55, 0x9b5d35d, 0x9b60361, 0x9b633e1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 5",
		addresses=[0x9b3ab20, 0x9b3d329, 0x9b3fb3b, 0x9b42352, 0x9b44b61, 0x9b47b69, 0x9b4ab6d, 0x9b4dbed, 0x9b50b18,
				   0x9b53321, 0x9b55b33, 0x9b5834a, 0x9b5ab59, 0x9b5d361, 0x9b60365, 0x9b633e5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 6",
		addresses=[0x9b3ab24, 0x9b3d32d, 0x9b3fb3f, 0x9b42356, 0x9b44b65, 0x9b47b6d, 0x9b4ab71, 0x9b4dbf1, 0x9b50b1c,
				   0x9b53325, 0x9b55b37, 0x9b5834e, 0x9b5ab5d, 0x9b5d365, 0x9b60369, 0x9b633e9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 7",
		addresses=[0x9b3ab28, 0x9b3d331, 0x9b3fb43, 0x9b4235a, 0x9b44b69, 0x9b47b71, 0x9b4ab75, 0x9b4dbf5, 0x9b50b20,
				   0x9b53329, 0x9b55b3b, 0x9b58352, 0x9b5ab61, 0x9b5d369, 0x9b6036d, 0x9b633ed],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 8",
		addresses=[0x9b3ab2c, 0x9b3d335, 0x9b3fb47, 0x9b4235e, 0x9b44b6d, 0x9b47b75, 0x9b4ab79, 0x9b4dbf9, 0x9b50b24,
				   0x9b5332d, 0x9b55b3f, 0x9b58356, 0x9b5ab65, 0x9b5d36d, 0x9b60371, 0x9b633f1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),

	# 18 OLIVE SHOP
	# OLIVE ITEM POOL [303,377,378,379,380]
	Attribute(
		name="OLIVE ITEM 1",
		addresses=[0x9b3ab4e, 0x9b3d357, 0x9b3fb69, 0x9b42380, 0x9b44b8f, 0x9b47b97, 0x9b4ab9b, 0x9b4dc1b, 0x9b50b46,
				   0x9b5334f, 0x9b55b61, 0x9b58378, 0x9b5ab87, 0x9b5d38f, 0x9b60393, 0x9b63413],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 2",
		addresses=[0x9b3ab52, 0x9b3d35b, 0x9b3fb6d, 0x9b42384, 0x9b44b93, 0x9b47b9b, 0x9b4ab9f, 0x9b4dc1f, 0x9b50b4a,
				   0x9b53353, 0x9b55b65, 0x9b5837c, 0x9b5ab8b, 0x9b5d393, 0x9b60397, 0x9b63417],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 3",
		addresses=[0x9b3ab56, 0x9b3d35f, 0x9b3fb71, 0x9b42388, 0x9b44b97, 0x9b47b9f, 0x9b4aba3, 0x9b4dc23, 0x9b50b4e,
				   0x9b53357, 0x9b55b69, 0x9b58380, 0x9b5ab8f, 0x9b5d397, 0x9b6039b, 0x9b6341b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 4",
		addresses=[0x9b3ab5a, 0x9b3d363, 0x9b3fb75, 0x9b4238c, 0x9b44b9b, 0x9b47ba3, 0x9b4aba7, 0x9b4dc27, 0x9b50b52,
				   0x9b5335b, 0x9b55b6d, 0x9b58384, 0x9b5ab93, 0x9b5d39b, 0x9b6039f, 0x9b6341f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 5",
		addresses=[0x9b3ab5e, 0x9b3d367, 0x9b3fb79, 0x9b42390, 0x9b44b9f, 0x9b47ba7, 0x9b4abab, 0x9b4dc2b, 0x9b50b56,
				   0x9b5335f, 0x9b55b71, 0x9b58388, 0x9b5ab97, 0x9b5d39f, 0x9b603a3, 0x9b63423],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),

	# 19 JULIA
	# JULIA ITEM POOL [91,92,94,103]

	# 20 MENA SHOP
	# MENA ITEM POOL [263,264,265,129,130,131,132]
	Attribute(
		name="MENA ITEM 1",
		addresses=[0x9b3ab9f, 0x9b3d3ac, 0x9b3fbc1, 0x9b50b97, 0x9b533a4, 0x9b55bb9, 0x9b583d3, 0x9b423db, 0x9b44bea,
				   0x9b5abe2, 0x9b5d3ea, 0x9b603ee, 0x9b47bf2, 0x9b4abf6, 0x9b4dc76, 0x9b6346e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 2",
		addresses=[0x9b3aba3, 0x9b3d3b0, 0x9b3fbc5, 0x9b50b9b, 0x9b533a8, 0x9b55bbd, 0x9b583d7, 0x9b423df, 0x9b44bee,
				   0x9b5abe6, 0x9b5d3ee, 0x9b603f2, 0x9b47bf6, 0x9b4abfa, 0x9b4dc7a, 0x9b63472],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 3",
		addresses=[0x9b3aba7, 0x9b3d3b4, 0x9b3fbc9, 0x9b50b9f, 0x9b533ac, 0x9b55bc1, 0x9b583db, 0x9b423e3, 0x9b44bf2,
				   0x9b5abea, 0x9b5d3f2, 0x9b603f6, 0x9b47bfa, 0x9b4abfe, 0x9b4dc7e, 0x9b63476],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 4",
		addresses=[0x9b583df, 0x9b423e7, 0x9b44bf6, 0x9b5abee, 0x9b5d3f6, 0x9b603fa, 0x9b47bfe, 0x9b4ac02, 0x9b4dc82,
				   0x9b6347a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 5",
		addresses=[0x9b44bfa, 0x9b5abf2, 0x9b5d3fa, 0x9b603fe, 0x9b47c02, 0x9b4ac06, 0x9b4dc86, 0x9b6347e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 6",
		addresses=[0x9b5d3fe, 0x9b60402, 0x9b47c06, 0x9b4ac0a, 0x9b4dc8a, 0x9b63482],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 7",
		addresses=[0x9b4dc8e, 0x9b63486],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),

	# 21 CORINNE SHOP
	# CORINNE ITEM POOL [123,124,125,126]
	Attribute(
		name="CORINNE ITEM 1",
		addresses=[0x9b3abc7, 0x9b3d3d4, 0x9b3fbe9, 0x9b42407, 0x9b44c1a, 0x9b47c26, 0x9b4ac2a, 0x9b4dcae, 0x9b50bbf,
				   0x9b533cc, 0x9b55be1, 0x9b583ff, 0x9b5ac12, 0x9b5d41e, 0x9b60422, 0x9b634a6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 2",
		addresses=[0x9b3abcb, 0x9b3d3d8, 0x9b3fbed, 0x9b4240b, 0x9b44c1e, 0x9b47c2a, 0x9b4ac2e, 0x9b4dcb2, 0x9b50bc3,
				   0x9b533d0, 0x9b55be5, 0x9b58403, 0x9b5ac16, 0x9b5d422, 0x9b60426, 0x9b634aa],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 3",
		addresses=[0x9b3abcf, 0x9b3d3dc, 0x9b3fbf1, 0x9b4240f, 0x9b44c22, 0x9b47c2e, 0x9b4ac32, 0x9b4dcb6, 0x9b50bc7,
				   0x9b533d4, 0x9b55be9, 0x9b58407, 0x9b5ac1a, 0x9b5d426, 0x9b6042a, 0x9b634ae],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 4",
		addresses=[0x9b3abd3, 0x9b3d3e0, 0x9b3fbf5, 0x9b42413, 0x9b44c26, 0x9b47c32, 0x9b4ac36, 0x9b4dcba, 0x9b50bcb,
				   0x9b533d8, 0x9b55bed, 0x9b5840b, 0x9b5ac1e, 0x9b5d42a, 0x9b6042e, 0x9b634b2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),

	# 22 ROSA SHOP
	# ROSA ITEM POOL [253,254,255,256,257]
	Attribute(
		name="ROSA ITEM 1",
		addresses=[0x9b3abfb, 0x9b3d408, 0x9b3fc1d, 0x9b4243b, 0x9b44c4e, 0x9b47c5a, 0x9b4ac5e, 0x9b4dce2, 0x9b50bf3,
				   0x9b53400, 0x9b55c15, 0x9b58433, 0x9b5ac46, 0x9b5d452, 0x9b60456, 0x9b634da],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 2",
		addresses=[0x9b3abff, 0x9b3d40c, 0x9b3fc21, 0x9b4243f, 0x9b44c52, 0x9b47c5e, 0x9b4ac62, 0x9b4dce6, 0x9b50bf7,
				   0x9b53404, 0x9b55c19, 0x9b58437, 0x9b5ac4a, 0x9b5d456, 0x9b6045a, 0x9b634de],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 3",
		addresses=[0x9b3ac03, 0x9b3d410, 0x9b3fc25, 0x9b42443, 0x9b44c56, 0x9b47c62, 0x9b4ac66, 0x9b4dcea, 0x9b50bfb,
				   0x9b53408, 0x9b55c1d, 0x9b5843b, 0x9b5ac4e, 0x9b5d45a, 0x9b6045e, 0x9b634e2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 4",
		addresses=[0x9b3ac07, 0x9b3d414, 0x9b3fc29, 0x9b42447, 0x9b44c5a, 0x9b47c66, 0x9b4ac6a, 0x9b4dcee, 0x9b50bff,
				   0x9b5340c, 0x9b55c21, 0x9b5843f, 0x9b5ac52, 0x9b5d45e, 0x9b60462, 0x9b634e6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 5",
		addresses=[0x9b3ac0b, 0x9b3d418, 0x9b3fc2d, 0x9b4244b, 0x9b44c5e, 0x9b47c6a, 0x9b4ac6e, 0x9b4dcf2, 0x9b50c03,
				   0x9b53410, 0x9b55c25, 0x9b58443, 0x9b5ac56, 0x9b5d462, 0x9b60466, 0x9b634ea],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),

	# 24 WOODY TAILORS SHOP
	# WOODY TAILORS ITEM POOL [258,259,260,263,201,202,424,304,376]
	Attribute(
		name="WOODY TAILORS ITEM 1",
		addresses=[0x9b3ac5b, 0x9b3d470, 0x9b3fc89, 0x9b424af, 0x9b44cc6, 0x9b47cda, 0x9b4ace6, 0x9b4dd6a, 0x9b50c53,
				   0x9b53468, 0x9b55c81, 0x9b584a7, 0x9b5acbe, 0x9b5d4d2, 0x9b604de, 0x9b63562],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 2",
		addresses=[0x9b3ac5f, 0x9b3d474, 0x9b3fc8d, 0x9b424b3, 0x9b44cca, 0x9b47cde, 0x9b4acea, 0x9b4dd6e, 0x9b50c57,
				   0x9b5346c, 0x9b55c85, 0x9b584ab, 0x9b5acc2, 0x9b5d4d6, 0x9b604e2, 0x9b63566],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 3",
		addresses=[0x9b3ac63, 0x9b3d478, 0x9b3fc91, 0x9b424b7, 0x9b44cce, 0x9b47ce2, 0x9b4acee, 0x9b4dd72, 0x9b50c5b,
				   0x9b53470, 0x9b55c89, 0x9b584af, 0x9b5acc6, 0x9b5d4da, 0x9b604e6, 0x9b6356a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 4",
		addresses=[0x9b3ac67, 0x9b3d47c, 0x9b3fc95, 0x9b424bb, 0x9b44cd2, 0x9b47ce6, 0x9b4acf2, 0x9b4dd76, 0x9b50c5f,
				   0x9b53474, 0x9b55c8d, 0x9b584b3, 0x9b5acca, 0x9b5d4de, 0x9b604ea, 0x9b6356e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 5",
		addresses=[0x9b3ac6b, 0x9b3d480, 0x9b3fc99, 0x9b424bf, 0x9b44cd6, 0x9b47cea, 0x9b4acf6, 0x9b4dd7a, 0x9b50c63,
				   0x9b53478, 0x9b55c91, 0x9b584b7, 0x9b5acce, 0x9b5d4e2, 0x9b604ee, 0x9b63572],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 6",
		addresses=[0x9b3ac6f, 0x9b3d484, 0x9b3fc9d, 0x9b424c3, 0x9b44cda, 0x9b47cee, 0x9b4acfa, 0x9b4dd7e, 0x9b50c67,
				   0x9b5347c, 0x9b55c95, 0x9b584bb, 0x9b5acd2, 0x9b5d4e6, 0x9b604f2, 0x9b63576],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 7",
		addresses=[0x9b3ac73, 0x9b3d488, 0x9b3fca1, 0x9b424c7, 0x9b44cde, 0x9b47cf2, 0x9b4acfe, 0x9b4dd82, 0x9b50c6b,
				   0x9b53480, 0x9b55c99, 0x9b584bf, 0x9b5acd6, 0x9b5d4ea, 0x9b604f6, 0x9b6357a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 8",
		addresses=[0x9b3ac77, 0x9b3d48c, 0x9b3fca5, 0x9b424cb, 0x9b44ce2, 0x9b47cf6, 0x9b4ad02, 0x9b4dd86, 0x9b50c6f,
				   0x9b53484, 0x9b55c9d, 0x9b584c3, 0x9b5acda, 0x9b5d4ee, 0x9b604fa, 0x9b6357e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),

	# 25 JURAK ARMS SHOP
	# JURAK ARMS ITEM POOL [17,23,25,41,47,49,73,201,294,298,352] (201 IS REPLACED WITH 47 IN CHAPTER 5 ONWARDS)

	# 26 MUSHROOM BURGER EATERY SHOP
	# MUSHROOM BURGER EATERY ITEM POOL [219,220,268,301,425,287,289,290,291,292,313,315,316,318]
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 1",
		addresses=[0x9b3accc, 0x9b3d4e9, 0x9b3fd05, 0x9b42531, 0x9b44d47, 0x9b47d5b, 0x9b4ad67, 0x9b4ddeb, 0x9b50cc4,
				   0x9b534e1, 0x9b55cfd, 0x9b58529, 0x9b5ad3f, 0x9b5d553, 0x9b6055f, 0x9b635e3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 2",
		addresses=[0x9b3acd0, 0x9b3d4ed, 0x9b3fd09, 0x9b42535, 0x9b44d4b, 0x9b47d5f, 0x9b4ad6b, 0x9b4ddef, 0x9b50cc8,
				   0x9b534e5, 0x9b55d01, 0x9b5852d, 0x9b5ad43, 0x9b5d557, 0x9b60563, 0x9b635e7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 3",
		addresses=[0x9b3acd4, 0x9b3d4f1, 0x9b3fd0d, 0x9b42539, 0x9b44d4f, 0x9b47d63, 0x9b4ad6f, 0x9b4ddf3, 0x9b50ccc,
				   0x9b534e9, 0x9b55d05, 0x9b58531, 0x9b5ad47, 0x9b5d55b, 0x9b60567, 0x9b635eb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 4",
		addresses=[0x9b3acd8, 0x9b3d4f5, 0x9b3fd11, 0x9b4253d, 0x9b44d53, 0x9b47d67, 0x9b4ad73, 0x9b4ddf7, 0x9b50cd0,
				   0x9b534ed, 0x9b55d09, 0x9b58535, 0x9b5ad4b, 0x9b5d55f, 0x9b6056b, 0x9b635ef],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 5",
		addresses=[0x9b3acdc, 0x9b3d4f9, 0x9b3fd15, 0x9b42541, 0x9b44d57, 0x9b47d6b, 0x9b4ad77, 0x9b4ddfb, 0x9b50cd4,
				   0x9b534f1, 0x9b55d0d, 0x9b58539, 0x9b5ad4f, 0x9b5d563, 0x9b6056f, 0x9b635f3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 6",
		addresses=[0x9b3ace0, 0x9b3d4fd, 0x9b3fd19, 0x9b42545, 0x9b44d5b, 0x9b47d6f, 0x9b4ad7b, 0x9b4ddff, 0x9b50cd8,
				   0x9b534f5, 0x9b55d11, 0x9b5853d, 0x9b5ad53, 0x9b5d567, 0x9b60573, 0x9b635f7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 7",
		addresses=[0x9b3ace4, 0x9b3d501, 0x9b3fd1d, 0x9b42549, 0x9b44d5f, 0x9b47d73, 0x9b4ad7f, 0x9b4de03, 0x9b50cdc,
				   0x9b534f9, 0x9b55d15, 0x9b58541, 0x9b5ad57, 0x9b5d56b, 0x9b60577, 0x9b635fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 8",
		addresses=[0x9b3ace8, 0x9b3d505, 0x9b3fd21, 0x9b4254d, 0x9b44d63, 0x9b47d77, 0x9b4ad83, 0x9b4de07, 0x9b50ce0,
				   0x9b534fd, 0x9b55d19, 0x9b58545, 0x9b5ad5b, 0x9b5d56f, 0x9b6057b, 0x9b635ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 9",
		addresses=[0x9b3acec, 0x9b3d509, 0x9b3fd25, 0x9b42551, 0x9b44d67, 0x9b47d7b, 0x9b4ad87, 0x9b4de0b, 0x9b50ce4,
				   0x9b53501, 0x9b55d1d, 0x9b58549, 0x9b5ad5f, 0x9b5d573, 0x9b6057f, 0x9b63603],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 10",
		addresses=[0x9b3acf0, 0x9b3d50d, 0x9b3fd29, 0x9b42555, 0x9b44d6b, 0x9b47d7f, 0x9b4ad8b, 0x9b4de0f, 0x9b50ce8,
				   0x9b53505, 0x9b55d21, 0x9b5854d, 0x9b5ad63, 0x9b5d577, 0x9b60583, 0x9b63607],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 11",
		addresses=[0x9b3acf4, 0x9b3d511, 0x9b3fd2d, 0x9b42559, 0x9b44d6f, 0x9b47d83, 0x9b4ad8f, 0x9b4de13, 0x9b50cec,
				   0x9b53509, 0x9b55d25, 0x9b58551, 0x9b5ad67, 0x9b5d57b, 0x9b60587, 0x9b6360b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 12",
		addresses=[0x9b3acf8, 0x9b3d515, 0x9b3fd31, 0x9b4255d, 0x9b44d73, 0x9b47d87, 0x9b4ad93, 0x9b4de17, 0x9b50cf0,
				   0x9b5350d, 0x9b55d29, 0x9b58555, 0x9b5ad6b, 0x9b5d57f, 0x9b6058b, 0x9b6360f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 13",
		addresses=[0x9b3acfc, 0x9b3d519, 0x9b3fd35, 0x9b42561, 0x9b44d77, 0x9b47d8b, 0x9b4ad97, 0x9b4de1b, 0x9b50cf4,
				   0x9b53511, 0x9b55d2d, 0x9b58559, 0x9b5ad6f, 0x9b5d583, 0x9b6058f, 0x9b63613],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 14",
		addresses=[0x9b3ad00, 0x9b3d51d, 0x9b3fd39, 0x9b42565, 0x9b44d7b, 0x9b47d8f, 0x9b4ad9b, 0x9b4de1f, 0x9b50cf8,
				   0x9b53515, 0x9b55d31, 0x9b5855d, 0x9b5ad73, 0x9b5d587, 0x9b60593, 0x9b63617],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),

	# 27 STARLIGHT WEAPONS SHOP
	# STARLIGHT WEAPONS ITEM POOL [11,45,67,92,93,95,106,352]

	# 28 G PARTS SHOP
	# G PARTS ITEM POOL [137,150,160,166,381]
	Attribute(
		name="G PARTS ITEM 1",
		addresses=[0x9b3ad43, 0x9b3d560, 0x9b3fd7c, 0x9b425ab, 0x9b44dc4, 0x9b47ddc, 0x9b4ade8, 0x9b4de6c, 0x9b50d3b,
				   0x9b53558, 0x9b55d74, 0x9b585a3, 0x9b5adbc, 0x9b5d5d4, 0x9b605e0, 0x9b63664],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 2",
		addresses=[0x9b3ad47, 0x9b3d564, 0x9b3fd80, 0x9b425af, 0x9b44dc8, 0x9b47de0, 0x9b4adec, 0x9b4de70, 0x9b50d3f,
				   0x9b5355c, 0x9b55d78, 0x9b585a7, 0x9b5adc0, 0x9b5d5d8, 0x9b605e4, 0x9b63668],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 3",
		addresses=[0x9b3ad4b, 0x9b3d568, 0x9b3fd84, 0x9b425b3, 0x9b44dcc, 0x9b47de4, 0x9b4adf0, 0x9b4de74, 0x9b50d43,
				   0x9b53560, 0x9b55d7c, 0x9b585ab, 0x9b5adc4, 0x9b5d5dc, 0x9b605e8, 0x9b6366c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 4",
		addresses=[0x9b3ad4f, 0x9b3d56c, 0x9b3fd88, 0x9b425b7, 0x9b44dd0, 0x9b47de8, 0x9b4adf4, 0x9b4de78, 0x9b50d47,
				   0x9b53564, 0x9b55d80, 0x9b585af, 0x9b5adc8, 0x9b5d5e0, 0x9b605ec, 0x9b63670],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 5",
		addresses=[0x9b3ad53, 0x9b3d570, 0x9b3fd8c, 0x9b425bb, 0x9b44dd4, 0x9b47dec, 0x9b4adf8, 0x9b4de7c, 0x9b50d4b,
				   0x9b53568, 0x9b55d84, 0x9b585b3, 0x9b5adcc, 0x9b5d5e4, 0x9b605f0, 0x9b63674],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),

	# 29 G TOOLS SHOP
	# G TOOLS ITEM POOL [269,425,294,298,352]
	Attribute(
		name="G TOOLS ITEM 1",
		addresses=[0x9b3ad6c, 0x9b3d589, 0x9b3fda5, 0x9b425d4, 0x9b44ded, 0x9b47e05, 0x9b4ae11, 0x9b4de95, 0x9b50d64,
				   0x9b53581, 0x9b55d9d, 0x9b585cc, 0x9b5ade5, 0x9b5d5fd, 0x9b60609, 0x9b6368d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 2",
		addresses=[0x9b3ad70, 0x9b3d58d, 0x9b3fda9, 0x9b425d8, 0x9b44df1, 0x9b47e09, 0x9b4ae15, 0x9b4de99, 0x9b50d68,
				   0x9b53585, 0x9b55da1, 0x9b585d0, 0x9b5ade9, 0x9b5d601, 0x9b6060d, 0x9b63691],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 3",
		addresses=[0x9b3ad74, 0x9b3d591, 0x9b3fdad, 0x9b425dc, 0x9b44df5, 0x9b47e0d, 0x9b4ae19, 0x9b4de9d, 0x9b50d6c,
				   0x9b53589, 0x9b55da5, 0x9b585d4, 0x9b5aded, 0x9b5d605, 0x9b60611, 0x9b63695],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 4",
		addresses=[0x9b3ad78, 0x9b3d595, 0x9b3fdb1, 0x9b425e0, 0x9b44df9, 0x9b47e11, 0x9b4ae1d, 0x9b4dea1, 0x9b50d70,
				   0x9b5358d, 0x9b55da9, 0x9b585d8, 0x9b5adf1, 0x9b5d609, 0x9b60615, 0x9b63699],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 5",
		addresses=[0x9b3ad7c, 0x9b3d599, 0x9b3fdb5, 0x9b425e4, 0x9b44dfd, 0x9b47e15, 0x9b4ae21, 0x9b4dea5, 0x9b50d74,
				   0x9b53591, 0x9b55dad, 0x9b585dc, 0x9b5adf5, 0x9b5d60d, 0x9b60619, 0x9b6369d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),

	# 30 G WEAPONS SHOP
	# G WEAPONS ITEM POOL [6,7,13,32,70,71,76,95,294,298,352]

	# 31 CONDA SHOP
	# CONDA ITEM POOL [210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236]
	Attribute(
		name="CONDA ITEM 1",
		addresses=[0x9b3adbf, 0x9b3d5dc, 0x9b3fdf8, 0x9b42627, 0x9b44e51, 0x9b47e6e, 0x9b4ae7a, 0x9b4defe, 0x9b50db7,
				   0x9b535d4, 0x9b55df0, 0x9b5861f, 0x9b5ae49, 0x9b5d666, 0x9b60672, 0x9b636f6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 2",
		addresses=[0x9b3adc3, 0x9b3d5e0, 0x9b3fdfc, 0x9b4262b, 0x9b44e55, 0x9b47e72, 0x9b4ae7e, 0x9b4df02, 0x9b50dbb,
				   0x9b535d8, 0x9b55df4, 0x9b58623, 0x9b5ae4d, 0x9b5d66a, 0x9b60676, 0x9b636fa],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 3",
		addresses=[0x9b3adc7, 0x9b3d5e4, 0x9b3fe00, 0x9b4262f, 0x9b44e59, 0x9b47e76, 0x9b4ae82, 0x9b4df06, 0x9b50dbf,
				   0x9b535dc, 0x9b55df8, 0x9b58627, 0x9b5ae51, 0x9b5d66e, 0x9b6067a, 0x9b636fe],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 4",
		addresses=[0x9b3adcb, 0x9b3d5e8, 0x9b3fe04, 0x9b42633, 0x9b44e5d, 0x9b47e7a, 0x9b4ae86, 0x9b4df0a, 0x9b50dc3,
				   0x9b535e0, 0x9b55dfc, 0x9b5862b, 0x9b5ae55, 0x9b5d672, 0x9b6067e, 0x9b63702],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 5",
		addresses=[0x9b3adcf, 0x9b3d5ec, 0x9b3fe08, 0x9b42637, 0x9b44e61, 0x9b47e7e, 0x9b4ae8a, 0x9b4df0e, 0x9b50dc7,
				   0x9b535e4, 0x9b55e00, 0x9b5862f, 0x9b5ae59, 0x9b5d676, 0x9b60682, 0x9b63706],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 6",
		addresses=[0x9b3add3, 0x9b3d5f0, 0x9b3fe0c, 0x9b4263b, 0x9b44e65, 0x9b47e82, 0x9b4ae8e, 0x9b4df12, 0x9b50dcb,
				   0x9b535e8, 0x9b55e04, 0x9b58633, 0x9b5ae5d, 0x9b5d67a, 0x9b60686, 0x9b6370a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 7",
		addresses=[0x9b3add7, 0x9b3d5f4, 0x9b3fe10, 0x9b4263f, 0x9b44e69, 0x9b47e86, 0x9b4ae92, 0x9b4df16, 0x9b50dcf,
				   0x9b535ec, 0x9b55e08, 0x9b58637, 0x9b5ae61, 0x9b5d67e, 0x9b6068a, 0x9b6370e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 8",
		addresses=[0x9b3addb, 0x9b3d5f8, 0x9b3fe14, 0x9b42643, 0x9b44e6d, 0x9b47e8a, 0x9b4ae96, 0x9b4df1a, 0x9b50dd3,
				   0x9b535f0, 0x9b55e0c, 0x9b5863b, 0x9b5ae65, 0x9b5d682, 0x9b6068e, 0x9b63712],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 9",
		addresses=[0x9b3addf, 0x9b3d5fc, 0x9b3fe18, 0x9b42647, 0x9b44e71, 0x9b47e8e, 0x9b4ae9a, 0x9b4df1e, 0x9b50dd7,
				   0x9b535f4, 0x9b55e10, 0x9b5863f, 0x9b5ae69, 0x9b5d686, 0x9b60692, 0x9b63716],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 10",
		addresses=[0x9b3ade3, 0x9b3d600, 0x9b3fe1c, 0x9b4264b, 0x9b44e75, 0x9b47e92, 0x9b4ae9e, 0x9b4df22, 0x9b50ddb,
				   0x9b535f8, 0x9b55e14, 0x9b58643, 0x9b5ae6d, 0x9b5d68a, 0x9b60696, 0x9b6371a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 11",
		addresses=[0x9b3ade7, 0x9b3d604, 0x9b3fe20, 0x9b4264f, 0x9b44e79, 0x9b47e96, 0x9b4aea2, 0x9b4df26, 0x9b50ddf,
				   0x9b535fc, 0x9b55e18, 0x9b58647, 0x9b5ae71, 0x9b5d68e, 0x9b6069a, 0x9b6371e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 12",
		addresses=[0x9b3adeb, 0x9b3d608, 0x9b3fe24, 0x9b42653, 0x9b44e7d, 0x9b47e9a, 0x9b4aea6, 0x9b4df2a, 0x9b50de3,
				   0x9b53600, 0x9b55e1c, 0x9b5864b, 0x9b5ae75, 0x9b5d692, 0x9b6069e, 0x9b63722],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 13",
		addresses=[0x9b3adef, 0x9b3d60c, 0x9b3fe28, 0x9b42657, 0x9b44e81, 0x9b47e9e, 0x9b4aeaa, 0x9b4df2e, 0x9b50de7,
				   0x9b53604, 0x9b55e20, 0x9b5864f, 0x9b5ae79, 0x9b5d696, 0x9b606a2, 0x9b63726],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 14",
		addresses=[0x9b3adf3, 0x9b3d610, 0x9b3fe2c, 0x9b4265b, 0x9b44e85, 0x9b47ea2, 0x9b4aeae, 0x9b4df32, 0x9b50deb,
				   0x9b53608, 0x9b55e24, 0x9b58653, 0x9b5ae7d, 0x9b5d69a, 0x9b606a6, 0x9b6372a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 15",
		addresses=[0x9b3adf7, 0x9b3d614, 0x9b3fe30, 0x9b4265f, 0x9b44e89, 0x9b47ea6, 0x9b4aeb2, 0x9b4df36, 0x9b50def,
				   0x9b5360c, 0x9b55e28, 0x9b58657, 0x9b5ae81, 0x9b5d69e, 0x9b606aa, 0x9b6372e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 16",
		addresses=[0x9b3adfb, 0x9b3d618, 0x9b3fe34, 0x9b42663, 0x9b44e8d, 0x9b47eaa, 0x9b4aeb6, 0x9b4df3a, 0x9b50df3,
				   0x9b53610, 0x9b55e2c, 0x9b5865b, 0x9b5ae85, 0x9b5d6a2, 0x9b606ae, 0x9b63732],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 17",
		addresses=[0x9b3adff, 0x9b3d61c, 0x9b3fe38, 0x9b42667, 0x9b44e91, 0x9b47eae, 0x9b4aeba, 0x9b4df3e, 0x9b50df7,
				   0x9b53614, 0x9b55e30, 0x9b5865f, 0x9b5ae89, 0x9b5d6a6, 0x9b606b2, 0x9b63736],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 18",
		addresses=[0x9b3ae03, 0x9b3d620, 0x9b3fe3c, 0x9b4266b, 0x9b44e95, 0x9b47eb2, 0x9b4aebe, 0x9b4df42, 0x9b50dfb,
				   0x9b53618, 0x9b55e34, 0x9b58663, 0x9b5ae8d, 0x9b5d6aa, 0x9b606b6, 0x9b6373a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 19",
		addresses=[0x9b3ae07, 0x9b3d624, 0x9b3fe40, 0x9b4266f, 0x9b44e99, 0x9b47eb6, 0x9b4aec2, 0x9b4df46, 0x9b50dff,
				   0x9b5361c, 0x9b55e38, 0x9b58667, 0x9b5ae91, 0x9b5d6ae, 0x9b606ba, 0x9b6373e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 20",
		addresses=[0x9b3ae0b, 0x9b3d628, 0x9b3fe44, 0x9b42673, 0x9b44e9d, 0x9b47eba, 0x9b4aec6, 0x9b4df4a, 0x9b50e03,
				   0x9b53620, 0x9b55e3c, 0x9b5866b, 0x9b5ae95, 0x9b5d6b2, 0x9b606be, 0x9b63742],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 21",
		addresses=[0x9b3ae0f, 0x9b3d62c, 0x9b3fe48, 0x9b42677, 0x9b44ea1, 0x9b47ebe, 0x9b4aeca, 0x9b4df4e, 0x9b50e07,
				   0x9b53624, 0x9b55e40, 0x9b5866f, 0x9b5ae99, 0x9b5d6b6, 0x9b606c2, 0x9b63746],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 22",
		addresses=[0x9b3ae13, 0x9b3d630, 0x9b3fe4c, 0x9b4267b, 0x9b44ea5, 0x9b47ec2, 0x9b4aece, 0x9b4df52, 0x9b50e0b,
				   0x9b53628, 0x9b55e44, 0x9b58673, 0x9b5ae9d, 0x9b5d6ba, 0x9b606c6, 0x9b6374a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 23",
		addresses=[0x9b3ae17, 0x9b3d634, 0x9b3fe50, 0x9b4267f, 0x9b44ea9, 0x9b47ec6, 0x9b4aed2, 0x9b4df56, 0x9b50e0f,
				   0x9b5362c, 0x9b55e48, 0x9b58677, 0x9b5aea1, 0x9b5d6be, 0x9b606ca, 0x9b6374e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 24",
		addresses=[0x9b3ae1b, 0x9b3d638, 0x9b3fe54, 0x9b42683, 0x9b44ead, 0x9b47eca, 0x9b4aed6, 0x9b4df5a, 0x9b50e13,
				   0x9b53630, 0x9b55e4c, 0x9b5867b, 0x9b5aea5, 0x9b5d6c2, 0x9b606ce, 0x9b63752],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 25",
		addresses=[0x9b3ae1f, 0x9b3d63c, 0x9b3fe58, 0x9b42687, 0x9b44eb1, 0x9b47ece, 0x9b4aeda, 0x9b4df5e, 0x9b50e17,
				   0x9b53634, 0x9b55e50, 0x9b5867f, 0x9b5aea9, 0x9b5d6c6, 0x9b606d2, 0x9b63756],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 26",
		addresses=[0x9b3ae23, 0x9b3d640, 0x9b3fe5c, 0x9b4268b, 0x9b44eb5, 0x9b47ed2, 0x9b4aede, 0x9b4df62, 0x9b50e1b,
				   0x9b53638, 0x9b55e54, 0x9b58683, 0x9b5aead, 0x9b5d6ca, 0x9b606d6, 0x9b6375a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 27",
		addresses=[0x9b3ae27, 0x9b3d644, 0x9b3fe60, 0x9b4268f, 0x9b44eb9, 0x9b47ed6, 0x9b4aee2, 0x9b4df66, 0x9b50e1f,
				   0x9b5363c, 0x9b55e58, 0x9b58687, 0x9b5aeb1, 0x9b5d6ce, 0x9b606da, 0x9b6375e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),# START OF SHOPS

# 01 POLLY SHOP
# POLLY ITEM POOL [219,220,221,268,425]
	Attribute(
		name="POLLY ITEM 1",
		addresses=[0x9b3a7d7,0x9b3cfe0,0x9b3f7e7,0x9b42010,0x9b447f0,0x9b477f0,0x9b4a7f0,0x9b4d7fc,0x9b507d7,0x9b52fe0,0x9b557e7,0x9b57ff0,0x9b5a7f0,0x9b5cff0,0x9b5fff0,0x9b62ffc],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 2",
		addresses=[0x9b3a7db,0x9b3cfe4,0x9b3f7eb,0x9b42014,0x9b447f4,0x9b477f4,0x9b4a7f4,0x9b4d800,0x9b507db,0x9b52fe4,0x9b557eb,0x9b57ff4,0x9b5a7f4,0x9b5cff4,0x9b5fff4,0x9b63000],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 3",
		addresses=[0x9b3a7df,0x9b3cfe8,0x9b3f7ef,0x9b42018,0x9b447f8,0x9b477f8,0x9b4a7f8,0x9b4d804,0x9b507df,0x9b52fe8,0x9b557ef,0x9b57ff8,0x9b5a7f8,0x9b5cff8,0x9b5fff8,0x9b63004],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 4",
		addresses=[0x9b3a7e3,0x9b3cfec,0x9b3f7f3,0x9b4201c,0x9b447fc,0x9b477fc,0x9b4a7fc,0x9b4d808,0x9b507e3,0x9b52fec,0x9b557f3,0x9b57ffc,0x9b5a7fc,0x9b5cffc,0x9b5fffc,0x9b63008],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),
	Attribute(
		name="POLLY ITEM 5",
		addresses=[0x9b3a7e7,0x9b3cff0,0x9b3f7f7,0x9b42020,0x9b44800,0x9b47800,0x9b4a800,0x9b4d80c,0x9b507e7,0x9b52ff0,0x9b557f7,0x9b58000,0x9b5a800,0x9b5d000,0x9b60000,0x9b6300c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("POLLY"),
		is_little_endian=False, ),

# 02 DELL SHOP
# DELL ITEM POOL [279]
	Attribute(
		name="DELL ITEM 1",
		addresses=[0x9b3a80c,0x9b3d015,0x9b3f81c,0x9b42025,0x9b44825,0x9b47825,0x9b4a825,0x9b4d831,0x9b5080c,0x9b53015,0x9b5581c,0x9b58025,0x9b5a825,0x9b5d025,0x9b60025,0x9b63031],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DELL"),
		is_little_endian=False, ),

# 03 FERDINAND SHOP
# FERDINAND ITEM POOL [270]
	Attribute(
		name="FERDINAND ITEM 1",
		addresses=[0x9b3a82d,0x9b3d036,0x9b3f83d,0x9b42046,0x9b44846,0x9b47846,0x9b4a846,0x9b4d852,0x9b5082d,0x9b53036,0x9b5583d,0x9b58046,0x9b5a846,0x9b5d046,0x9b60046,0x9b63052],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FERDINAND"),
		is_little_endian=False, ),

# 04 MORTONS SHOP
# MORTON ITEM POOL [186,187,188,189,190,191,192,193,194,195
	# 			   ,196,197,200,201,202,203,204,205,206,207
	# 			   ,208,209,215,224,227,245,275,280,390,391
	# 			   ,294,298,381,172,355,358,174,376]
	Attribute(
		name="MORTON ITEM 1",
		addresses=[0x9b50852,0x9b5305b,0x9b55862,0x9b3a852,0x9b3d05b,0x9b5806b,0x9b3f862,0x9b5a86b,0x9b4206b,0x9b5d06b,0x9b6006b,0x9b4486b,0x9b4786b,0x9b4a86b,0x9b63077,0x9b4d877],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 2",
		addresses=[0x9b50856,0x9b5305f,0x9b55866,0x9b3a856,0x9b3d05f,0x9b5806f,0x9b3f866,0x9b5a86f,0x9b4206f,0x9b5d06f,0x9b6006f,0x9b4486f,0x9b4786f,0x9b4a86f,0x9b6307b,0x9b4d87b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 3",
		addresses=[0x9b5085a,0x9b53063,0x9b5586a,0x9b3a85a,0x9b3d063,0x9b58073,0x9b3f86a,0x9b5a873,0x9b42073,0x9b5d073,0x9b60073,0x9b44873,0x9b47873,0x9b4a873,0x9b6307f,0x9b4d87f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 4",
		addresses=[0x9b5085e,0x9b53067,0x9b5586e,0x9b3a85e,0x9b3d067,0x9b58077,0x9b3f86e,0x9b5a877,0x9b42077,0x9b5d077,0x9b60077,0x9b44877,0x9b47877,0x9b4a877,0x9b63083,0x9b4d883],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 5",
		addresses=[0x9b50862,0x9b5306b,0x9b55872,0x9b3a862,0x9b3d06b,0x9b5807b,0x9b3f872,0x9b5a87b,0x9b4207b,0x9b5d07b,0x9b6007b,0x9b4487b,0x9b4787b,0x9b4a87b,0x9b63087,0x9b4d887],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 6",
		addresses=[0x9b50866,0x9b5306f,0x9b55876,0x9b3a866,0x9b3d06f,0x9b5807f,0x9b3f876,0x9b5a87f,0x9b4207f,0x9b5d07f,0x9b6007f,0x9b4487f,0x9b4787f,0x9b4a87f,0x9b6308b,0x9b4d88b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 7",
		addresses=[0x9b5086a,0x9b53073,0x9b5587a,0x9b3a86a,0x9b3d073,0x9b58083,0x9b3f87a,0x9b5a883,0x9b42083,0x9b5d083,0x9b60083,0x9b44883,0x9b47883,0x9b4a883,0x9b6308f,0x9b4d88f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 8",
		addresses=[0x9b5086e,0x9b53077,0x9b5587e,0x9b3a86e,0x9b3d077,0x9b58087,0x9b3f87e,0x9b5a887,0x9b42087,0x9b5d087,0x9b60087,0x9b44887,0x9b47887,0x9b4a887,0x9b63093,0x9b4d893],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 9",
		addresses=[0x9b50872,0x9b5307b,0x9b55882,0x9b3a872,0x9b3d07b,0x9b5808b,0x9b3f882,0x9b5a88b,0x9b4208b,0x9b5d08b,0x9b6008b,0x9b4488b,0x9b4788b,0x9b4a88b,0x9b63097,0x9b4d897],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 10",
		addresses=[0x9b50876,0x9b5307f,0x9b55886,0x9b3a876,0x9b3d07f,0x9b5808f,0x9b3f886,0x9b5a88f,0x9b4208f,0x9b5d08f,0x9b6008f,0x9b4488f,0x9b4788f,0x9b4a88f,0x9b6309b,0x9b4d89b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 11",
		addresses=[0x9b5588a,0x9b3a87a,0x9b3d083,0x9b58093,0x9b3f88a,0x9b5a893,0x9b42093,0x9b5d093,0x9b60093,0x9b44893,0x9b47893,0x9b4a893,0x9b6309f,0x9b4d89f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 12",
		addresses=[0x9b58097,0x9b3f88e,0x9b5a897,0x9b42097,0x9b5d097,0x9b60097,0x9b44897,0x9b47897,0x9b4a897,0x9b630a3,0x9b4d8a3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 13",
		addresses=[0x9b5a89b,0x9b4209b,0x9b5d09b,0x9b6009b,0x9b4489b,0x9b4789b,0x9b4a89b,0x9b630a7,0x9b4d8a7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 14",
		addresses=[0x9b5d09f,0x9b6009f,0x9b4489f,0x9b4789f,0x9b4a89f,0x9b630ab,0x9b4d8ab],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 15",
		addresses=[0x9b478a3,0x9b4a8a3,0x9b630af,0x9b4d8af],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),

	Attribute(
		name="MORTON ITEM 16",
		addresses=[0x9b630b3,0x9b4d8b3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 17",
		addresses=[0x9b630b7,0x9b4d8b7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 18",
		addresses=[0x9b630bb,0x9b4d8bb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 19",
		addresses=[0x9b630bf,0x9b4d8bf],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 20",
		addresses=[0x9b630c3,0x9b4d8c3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 21",
		addresses=[0x9b630c7,0x9b4d8c7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 22",
		addresses=[0x9b630cb,0x9b4d8cb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 23",
		addresses=[0x9b630cf,0x9b4d8cf],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 24",
		addresses=[0x9b630d3,0x9b4d8d3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 25",
		addresses=[0x9b630d7,0x9b4d8d7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 26",
		addresses=[0x9b630db,0x9b4d8db],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 27",
		addresses=[0x9b630df,0x9b4d8df],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 28",
		addresses=[0x9b630e3,0x9b4d8e3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 29",
		addresses=[0x9b630e7,0x9b4d8e7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 30",
		addresses=[0x9b630eb,0x9b4d8eb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 31",
		addresses=[0x9b630ef,0x9b4d8ef],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 32",
		addresses=[0x9b630f3,0x9b4d8f3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 33",
		addresses=[0x9b630f7,0x9b4d8f7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 34",
		addresses=[0x9b630fb,0x9b4d8fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 35",
		addresses=[0x9b630ff,0x9b4d8ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 36",
		addresses=[0x9b63103,0x9b4d903],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 36",
		addresses=[0x9b63107,0x9b4d907],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),
	Attribute(
		name="MORTON ITEM 37",
		addresses=[0x9b4d90b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MORTON"),
		is_little_endian=False, ),

# 05 STARLIGHT TEMPLE SHOP
# STARLIGHT TEMPLE ITEM POOL [265,175,176,177,178,179,180,181,182,183
	#						 ,184,269,275,279,425,294,371]
	Attribute(
		name="STARLIGHT TEMPLE ITEM 1",
		addresses=[0x9b3a89b,0x9b3d0a4,0x9b3f8af,0x9b420bc,0x9b448c0,0x9b478c4,0x9b4a8c4,0x9b4d92c,0x9b50897,0x9b530a0,0x9b558ab,0x9b580b8,0x9b5a8bc,0x9b5d0c0,0x9b600c0,0x9b63128],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 2",
		addresses=[0x9b3a89f,0x9b3d0a8,0x9b3f8b3,0x9b420c0,0x9b448c4,0x9b478c8,0x9b4a8c8,0x9b4d930,0x9b5089b,0x9b530a4,0x9b558af,0x9b580bc,0x9b5a8c0,0x9b5d0c4,0x9b600c4,0x9b6312c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 3",
		addresses=[0x9b3a8a3,0x9b3d0ac,0x9b3f8b7,0x9b420c4,0x9b448c8,0x9b478cc,0x9b4a8cc,0x9b4d934,0x9b5089f,0x9b530a8,0x9b558b3,0x9b580c0,0x9b5a8c4,0x9b5d0c8,0x9b600c8,0x9b63130],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 4",
		addresses=[0x9b3a8a7,0x9b3d0b0,0x9b3f8bb,0x9b420c8,0x9b448cc,0x9b478d0,0x9b4a8d0,0x9b4d938,0x9b508a3,0x9b530ac,0x9b558b7,0x9b580c4,0x9b5a8c8,0x9b5d0cc,0x9b600cc,0x9b63134],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 5",
		addresses=[0x9b3a8ab,0x9b3d0b4,0x9b3f8bf,0x9b420cc,0x9b448d0,0x9b478d4,0x9b4a8d4,0x9b4d93c,0x9b508a7,0x9b530b0,0x9b558bb,0x9b580c8,0x9b5a8cc,0x9b5d0d0,0x9b600d0,0x9b63138],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 6",
		addresses=[0x9b3a8af,0x9b3d0b8,0x9b3f8c3,0x9b420d0,0x9b448d4,0x9b478d8,0x9b4a8d8,0x9b4d940,0x9b508ab,0x9b530b4,0x9b558bf,0x9b580cc,0x9b5a8d0,0x9b5d0d4,0x9b600d4,0x9b6313c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 7",
		addresses=[0x9b3a8b3,0x9b3d0bc,0x9b3f8c7,0x9b420d4,0x9b448d8,0x9b478dc,0x9b4a8dc,0x9b4d944,0x9b508af,0x9b530b8,0x9b558c3,0x9b580d0,0x9b5a8d4,0x9b5d0d8,0x9b600d8,0x9b63140],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 8",
		addresses=[0x9b3a8b7,0x9b3d0c0,0x9b3f8cb,0x9b420d8,0x9b448dc,0x9b478e0,0x9b4a8e0,0x9b4d948,0x9b508b3,0x9b530bc,0x9b558c7,0x9b580d4,0x9b5a8d8,0x9b5d0dc,0x9b600dc,0x9b63144],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 9",
		addresses=[0x9b3a8bb,0x9b3d0c4,0x9b3f8cf,0x9b420dc,0x9b448e0,0x9b478e4,0x9b4a8e4,0x9b4d94c,0x9b508b7,0x9b530c0,0x9b558cb,0x9b580d8,0x9b5a8dc,0x9b5d0e0,0x9b600e0,0x9b63148],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 10",
		addresses=[0x9b3a8bf,0x9b3d0c8,0x9b3f8d3,0x9b420e0,0x9b448e4,0x9b478e8,0x9b4a8e8,0x9b4d950,0x9b508bb,0x9b530c4,0x9b558cf,0x9b580dc,0x9b5a8e0,0x9b5d0e4,0x9b600e4,0x9b6314c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 11",
		addresses=[0x9b3a8c3,0x9b3d0cc,0x9b3f8d7,0x9b420e4,0x9b448e8,0x9b478ec,0x9b4a8ec,0x9b4d954,0x9b508bf,0x9b530c8,0x9b558d3,0x9b580e0,0x9b5a8e4,0x9b5d0e8,0x9b600e8,0x9b63150],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 12",
		addresses=[0x9b3a8c7,0x9b3d0d0,0x9b3f8db,0x9b420e8,0x9b448ec,0x9b478f0,0x9b4a8f0,0x9b4d958,0x9b508c3,0x9b530cc,0x9b558d7,0x9b580e4,0x9b5a8e8,0x9b5d0ec,0x9b600ec,0x9b63154],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 13",
		addresses=[0x9b3a8cb,0x9b3d0d4,0x9b3f8df,0x9b420ec,0x9b448f0,0x9b478f4,0x9b4a8f4,0x9b4d95c,0x9b508c7,0x9b530d0,0x9b558db,0x9b580e8,0x9b5a8ec,0x9b5d0f0,0x9b600f0,0x9b63158],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 14",
		addresses=[0x9b3a8cf,0x9b3d0d8,0x9b3f8e3,0x9b420f0,0x9b448f4,0x9b478f8,0x9b4a8f8,0x9b4d960,0x9b508cb,0x9b530d4,0x9b558df,0x9b580ec,0x9b5a8f0,0x9b5d0f4,0x9b600f4,0x9b6315c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 15",
		addresses=[0x9b3a8d3,0x9b3d0dc,0x9b3f8e7,0x9b420f4,0x9b448f8,0x9b478fc,0x9b4a8fc,0x9b4d964,0x9b508cf,0x9b530d8,0x9b558e3,0x9b580f0,0x9b5a8f4,0x9b5d0f8,0x9b600f8,0x9b63160],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 16",
		addresses=[0x9b3a8d7,0x9b3d0e0,0x9b3f8eb,0x9b420f8,0x9b448fc,0x9b47900,0x9b4a900,0x9b4d968,0x9b508d3,0x9b530dc,0x9b558e7,0x9b580f4,0x9b5a8f8,0x9b5d0fc,0x9b600fc,0x9b63164],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),
	Attribute(
		name="STARLIGHT TEMPLE ITEM 17",
		addresses=[0x9b3a8db,0x9b3d0e4,0x9b3f8ef,0x9b420fc,0x9b44900,0x9b47904,0x9b4a904,0x9b4d96c,0x9b508d7,0x9b530e0,0x9b558eb,0x9b580f8,0x9b5a8fc,0x9b5d100,0x9b60100,0x9b63168],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STARLIGHT TEMPLE"),
		is_little_endian=False, ),

# 06 DONNY SHOP
# DONNY ITEM POOL [260,111,112,113,114,268,275,294,298,297
	#			  ,355]
	Attribute(
		name="DONNY ITEM 1",
		addresses=[0x9b508fc,0x9b53105,0x9b3a900,0x9b3d109,0x9b55910,0x9b5811d,0x9b3f914,0x9b42121,0x9b5a921,0x9b44925,0x9b5d125,0x9b60125,0x9b6318d,0x9b47929,0x9b4a929,0x9b4d991],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 2",
		addresses=[0x9b50900,0x9b53109,0x9b3a904,0x9b3d10d,0x9b55914,0x9b58121,0x9b3f918,0x9b42125,0x9b5a925,0x9b44929,0x9b5d129,0x9b60129,0x9b63191,0x9b4792d,0x9b4a92d,0x9b4d995],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 3",
		addresses=[0x9b50904,0x9b5310d,0x9b3a908,0x9b3d111,0x9b55918,0x9b58125,0x9b3f91c,0x9b42129,0x9b5a929,0x9b4492d,0x9b5d12d,0x9b6012d,0x9b63195,0x9b47931,0x9b4a931,0x9b4d999],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 4",
		addresses=[0x9b50908,0x9b53111,0x9b3a90c,0x9b3d115,0x9b5591c,0x9b58129,0x9b3f920,0x9b4212d,0x9b5a92d,0x9b44931,0x9b5d131,0x9b60131,0x9b63199,0x9b47935,0x9b4a935,0x9b4d99d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 5",
		addresses=[0x9b5090c,0x9b53115,0x9b3a910,0x9b3d119,0x9b55920,0x9b5812d,0x9b3f924,0x9b42131,0x9b5a931,0x9b44935,0x9b5d135,0x9b60135,0x9b6319d,0x9b47939,0x9b4a939,0x9b4d9a1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 6",
		addresses=[0x9b3a914,0x9b3d11d,0x9b55924,0x9b58131,0x9b3f928,0x9b42135,0x9b5a935,0x9b44939,0x9b5d139,0x9b60139,0x9b631a1,0x9b4793d,0x9b4a93d,0x9b4d9a5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 7",
		addresses=[0x9b58135,0x9b3f92c,0x9b42139,0x9b5a939,0x9b4493d,0x9b5d13d,0x9b6013d,0x9b631a5,0x9b47941,0x9b4a941,0x9b4d9a9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 8",
		addresses=[0x9b4213d,0x9b5a93d,0x9b44941,0x9b5d141,0x9b60141,0x9b631a9,0x9b47945,0x9b4a945,0x9b4d9ad],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 9",
		addresses=[0x9b44945,0x9b5d145,0x9b60145,0x9b631ad,0x9b47949,0x9b4a949,0x9b4d9b1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 10",
		addresses=[0x9b60149,0x9b631b1,0x9b4794d,0x9b4a94d,0x9b4d9b5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),
	Attribute(
		name="DONNY ITEM 11",
		addresses=[0x9b4a951,0x9b4d9b9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("DONNY"),
		is_little_endian=False, ),

# 07 BORNEO SHOP
# BORNEO ITEM POOL [212,225,226,227]
	Attribute(
		name="BORNEO ITEM 1",
		addresses=[0x9b3a933,0x9b3d13c,0x9b3f94b,0x9b4215c,0x9b44964,0x9b4796c,0x9b4a970,0x9b4d9d8,0x9b5092b,0x9b53134,0x9b55943,0x9b58154,0x9b5a95c,0x9b5d164,0x9b60168,0x9b631d0],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 2",
		addresses=[0x9b3a937,0x9b3d140,0x9b3f94f,0x9b42160,0x9b44968,0x9b47970,0x9b4a974,0x9b4d9dc,0x9b5092f,0x9b53138,0x9b55947,0x9b58158,0x9b5a960,0x9b5d168,0x9b6016c,0x9b631d4],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 3",
		addresses=[0x9b3a93b,0x9b3d144,0x9b3f953,0x9b42164,0x9b4496c,0x9b47974,0x9b4a978,0x9b4d9e0,0x9b50933,0x9b5313c,0x9b5594b,0x9b5815c,0x9b5a964,0x9b5d16c,0x9b60170,0x9b631d8],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),
	Attribute(
		name="BORNEO ITEM 4",
		addresses=[0x9b3a93f,0x9b3d148,0x9b3f957,0x9b42168,0x9b44970,0x9b47978,0x9b4a97c,0x9b4d9e4,0x9b50937,0x9b53140,0x9b5594f,0x9b58160,0x9b5a968,0x9b5d170,0x9b60174,0x9b631dc],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BORNEO"),
		is_little_endian=False, ),

# 08 GORDON SHOP
# GORDON ITEM POOL [210,211,223,272]
	Attribute(
		name="GORDON ITEM 1",
		addresses=[0x9b3a95e,0x9b3d167,0x9b3f976,0x9b42187,0x9b50956,0x9b5315f,0x9b5596e,0x9b5817f,0x9b4498f,0x9b47997,0x9b4a99b,0x9b4da03,0x9b5a987,0x9b5d18f,0x9b60193,0x9b631fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 2",
		addresses=[0x9b3a962,0x9b3d16b,0x9b3f97a,0x9b4218b,0x9b5095a,0x9b53163,0x9b55972,0x9b58183,0x9b44993,0x9b4799b,0x9b4a99f,0x9b4da07,0x9b5a98b,0x9b5d193,0x9b60197,0x9b631ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 3",
		addresses=[0x9b3a966,0x9b3d16f,0x9b3f97e,0x9b4218f,0x9b5095e,0x9b53167,0x9b55976,0x9b58187,0x9b44997,0x9b4799f,0x9b4a9a3,0x9b4da0b,0x9b5a98f,0x9b5d197,0x9b6019b,0x9b63203],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),
	Attribute(
		name="GORDON ITEM 4",
		addresses=[0x9b4499b,0x9b479a3,0x9b4a9a7,0x9b4da0f,0x9b5a993,0x9b5d19b,0x9b6019f,0x9b63207],
		number_of_bytes=3,
		possible_values=ChooseShopItems("GORDON"),
		is_little_endian=False, ),

# 09 PARN SHOP
# PARN ITEM POOL [237,238,239,240,241,242,243,244]
	Attribute(
		name="PARN ITEM 1",
		addresses=[0x9b3a987,0x9b3d190,0x9b3f99f,0x9b421b0,0x9b449bc,0x9b479c4,0x9b4a9c8,0x9b4da30,0x9b5097f,0x9b53188,0x9b55997,0x9b581a8,0x9b5a9b4,0x9b5d1bc,0x9b601c0,0x9b63228],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 2",
		addresses=[0x9b3a98b,0x9b3d194,0x9b3f9a3,0x9b421b4,0x9b449c0,0x9b479c8,0x9b4a9cc,0x9b4da34,0x9b50983,0x9b5318c,0x9b5599b,0x9b581ac,0x9b5a9b8,0x9b5d1c0,0x9b601c4,0x9b6322c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 3",
		addresses=[0x9b3a98f,0x9b3d198,0x9b3f9a7,0x9b421b8,0x9b449c4,0x9b479cc,0x9b4a9d0,0x9b4da38,0x9b50987,0x9b53190,0x9b5599f,0x9b581b0,0x9b5a9bc,0x9b5d1c4,0x9b601c8,0x9b63230],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 4",
		addresses=[0x9b3a993,0x9b3d19c,0x9b3f9ab,0x9b421bc,0x9b449c8,0x9b479d0,0x9b4a9d4,0x9b4da3c,0x9b5098b,0x9b53194,0x9b559a3,0x9b581b4,0x9b5a9c0,0x9b5d1c8,0x9b601cc,0x9b63234],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 5",
		addresses=[0x9b3a997,0x9b3d1a0,0x9b3f9af,0x9b421c0,0x9b449cc,0x9b479d4,0x9b4a9d8,0x9b4da40,0x9b5098f,0x9b53198,0x9b559a7,0x9b581b8,0x9b5a9c4,0x9b5d1cc,0x9b601d0,0x9b63238],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 6",
		addresses=[0x9b3a99b,0x9b3d1a4,0x9b3f9b3,0x9b421c4,0x9b449d0,0x9b479d8,0x9b4a9dc,0x9b4da44,0x9b50993,0x9b5319c,0x9b559ab,0x9b581bc,0x9b5a9c8,0x9b5d1d0,0x9b601d4,0x9b6323c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 7",
		addresses=[0x9b3a99f,0x9b3d1a8,0x9b3f9b7,0x9b421c8,0x9b449d4,0x9b479dc,0x9b4a9e0,0x9b4da48,0x9b50997,0x9b531a0,0x9b559af,0x9b581c0,0x9b5a9cc,0x9b5d1d4,0x9b601d8,0x9b63240],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),
	Attribute(
		name="PARN ITEM 8",
		addresses=[0x9b3a9a3,0x9b3d1ac,0x9b3f9bb,0x9b421cc,0x9b449d8,0x9b479e0,0x9b4a9e4,0x9b4da4c,0x9b5099b,0x9b531a4,0x9b559b3,0x9b581c4,0x9b5a9d0,0x9b5d1d8,0x9b601dc,0x9b63244],
		number_of_bytes=3,
		possible_values=ChooseShopItems("PARN"),
		is_little_endian=False, ),

# 10 CLAIRE SHOP
# CLAIRE ITEM POOL [304]
	Attribute(
		name="CLAIRE ITEM 1",
		addresses=[0x9b3a9c9,0x9b3d1d2,0x9b3f9e1,0x9b421f2,0x9b449fe,0x9b47a06,0x9b4aa0a,0x9b4da72,0x9b509c1,0x9b531ca,0x9b559d9,0x9b581ea,0x9b5a9f6,0x9b5d1fe,0x9b60202,0x9b6326a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CLAIRE"),
		is_little_endian=False, ),

# 11 STEWART SHOP
# STEWART ITEM POOL [117,118,119,120]
	Attribute(
		name="STEWART ITEM 1",
		addresses=[0x9b3a9eb,0x9b3d1f4,0x9b3fa03,0x9b42214,0x9b44a20,0x9b47a28,0x9b4aa2c,0x9b4da94,0x9b509e3,0x9b531ec,0x9b559fb,0x9b5820c,0x9b5aa18,0x9b5d220,0x9b60224,0x9b6328c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 2",
		addresses=[0x9b3a9ef,0x9b3d1f8,0x9b3fa07,0x9b42218,0x9b44a24,0x9b47a2c,0x9b4aa30,0x9b4da98,0x9b509e7,0x9b531f0,0x9b559ff,0x9b58210,0x9b5aa1c,0x9b5d224,0x9b60228,0x9b63290],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 3",
		addresses=[0x9b3a9f3,0x9b3d1fc,0x9b3fa0b,0x9b4221c,0x9b44a28,0x9b47a30,0x9b4aa34,0x9b4da9c,0x9b509eb,0x9b531f4,0x9b55a03,0x9b58214,0x9b5aa20,0x9b5d228,0x9b6022c,0x9b63294],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),
	Attribute(
		name="STEWART ITEM 4",
		addresses=[0x9b3a9f7,0x9b3d200,0x9b3fa0f,0x9b42220,0x9b44a2c,0x9b47a34,0x9b4aa38,0x9b4daa0,0x9b509ef,0x9b531f8,0x9b55a07,0x9b58218,0x9b5aa24,0x9b5d22c,0x9b60230,0x9b63298],
		number_of_bytes=3,
		possible_values=ChooseShopItems("STEWART"),
		is_little_endian=False, ),

# 12 ADEL SHOP
# ADEL ITEM POOL [425,287,288,289,291,292]
	Attribute(
		name="ADEL ITEM 1",
		addresses=[0x9b3aa19,0x9b3d222,0x9b3fa31,0x9b42242,0x9b44a4e,0x9b47a56,0x9b4aa5a,0x9b4dac2,0x9b50a11,0x9b5321a,0x9b55a29,0x9b5823a,0x9b5aa46,0x9b5d24e,0x9b60252,0x9b632ba],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 2",
		addresses=[0x9b3aa1d,0x9b3d226,0x9b3fa35,0x9b42246,0x9b44a52,0x9b47a5a,0x9b4aa5e,0x9b4dac6,0x9b50a15,0x9b5321e,0x9b55a2d,0x9b5823e,0x9b5aa4a,0x9b5d252,0x9b60256,0x9b632be],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 3",
		addresses=[0x9b3aa21,0x9b3d22a,0x9b3fa39,0x9b4224a,0x9b44a56,0x9b47a5e,0x9b4aa62,0x9b4daca,0x9b50a19,0x9b53222,0x9b55a31,0x9b58242,0x9b5aa4e,0x9b5d256,0x9b6025a,0x9b632c2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 4",
		addresses=[0x9b3aa25,0x9b3d22e,0x9b3fa3d,0x9b4224e,0x9b44a5a,0x9b47a62,0x9b4aa66,0x9b4dace,0x9b50a1d,0x9b53226,0x9b55a35,0x9b58246,0x9b5aa52,0x9b5d25a,0x9b6025e,0x9b632c6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 5",
		addresses=[0x9b3aa29,0x9b3d232,0x9b3fa41,0x9b42252,0x9b44a5e,0x9b47a66,0x9b4aa6a,0x9b4dad2,0x9b50a21,0x9b5322a,0x9b55a39,0x9b5824a,0x9b5aa56,0x9b5d25e,0x9b60262,0x9b632ca],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),
	Attribute(
		name="ADEL ITEM 6",
		addresses=[0x9b3aa2d,0x9b3d236,0x9b3fa45,0x9b42256,0x9b44a62,0x9b47a6a,0x9b4aa6e,0x9b4dad6,0x9b50a25,0x9b5322e,0x9b55a3d,0x9b5824e,0x9b5aa5a,0x9b5d262,0x9b60266,0x9b632ce],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ADEL"),
		is_little_endian=False, ),

# 13 ERIK SHOP
# ERIK ITEM POOL [215]
	Attribute(
		name="ERIK ITEM 1",
		addresses=[0x9b3aa49,0x9b3d252,0x9b3fa61,0x9b42272,0x9b44a7e,0x9b47a86,0x9b4aa8a,0x9b4daf2,0x9b50a41,0x9b5324a,0x9b55a59,0x9b5826a,0x9b5aa76,0x9b5d27e,0x9b60282,0x9b632ea],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ERIK"),
		is_little_endian=False, ),

# 14 GERALD SHOP
# GERALD ITEM POOL [10,24,26,28,36]

# 15 BRUNO SHOP
# BRUNO ITEM POOL [275,276,277,278]
	Attribute(
		name="BRUNO ITEM 1",
		addresses=[0x9b3aa8e,0x9b3d297,0x9b3faa9,0x9b422c0,0x9b44acf,0x9b47ad7,0x9b4aadb,0x9b4db43,0x9b50a86,0x9b5328f,0x9b55aa1,0x9b582b8,0x9b5aac7,0x9b5d2cf,0x9b602d3,0x9b6333b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 2",
		addresses=[0x9b3aa92,0x9b3d29b,0x9b3faad,0x9b422c4,0x9b44ad3,0x9b47adb,0x9b4aadf,0x9b4db47,0x9b50a8a,0x9b53293,0x9b55aa5,0x9b582bc,0x9b5aacb,0x9b5d2d3,0x9b602d7,0x9b6333f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 3",
		addresses=[0x9b3aa96,0x9b3d29f,0x9b3fab1,0x9b422c8,0x9b44ad7,0x9b47adf,0x9b4aae3,0x9b4db4b,0x9b50a8e,0x9b53297,0x9b55aa9,0x9b582c0,0x9b5aacf,0x9b5d2d7,0x9b602db,0x9b63343],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),
	Attribute(
		name="BRUNO ITEM 4",
		addresses=[0x9b3aa9a,0x9b3d2a3,0x9b3fab5,0x9b422cc,0x9b44adb,0x9b47ae3,0x9b4aae7,0x9b4db4f,0x9b50a92,0x9b5329b,0x9b55aad,0x9b582c4,0x9b5aad3,0x9b5d2db,0x9b602df,0x9b63347],
		number_of_bytes=3,
		possible_values=ChooseShopItems("BRUNO"),
		is_little_endian=False, ),

# 16 RUFIO SHOP
# RUFIO ITEM POOL [175,176,177,178,179,180,181,182,183,184,228,229,230,231,232,233,234,235,236]
	Attribute(
		name="RUFIO ITEM 1",
		addresses=[0x9b3aabe,0x9b3d2c7,0x9b3fad9,0x9b422f0,0x9b44aff,0x9b47b07,0x9b4ab0b,0x9b50ab6,0x9b532bf,0x9b55ad1,0x9b582e8,0x9b5aaf7,0x9b5d2ff,0x9b60303,0x9b4db73,0x9b6336b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 2",
		addresses=[0x9b3aac2,0x9b3d2cb,0x9b3fadd,0x9b422f4,0x9b44b03,0x9b47b0b,0x9b4ab0f,0x9b50aba,0x9b532c3,0x9b55ad5,0x9b582ec,0x9b5aafb,0x9b5d303,0x9b60307,0x9b4db77,0x9b6336f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 3",
		addresses=[0x9b3aac6,0x9b3d2cf,0x9b3fae1,0x9b422f8,0x9b44b07,0x9b47b0f,0x9b4ab13,0x9b50abe,0x9b532c7,0x9b55ad9,0x9b582f0,0x9b5aaff,0x9b5d307,0x9b6030b,0x9b4db7b,0x9b63373],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 4",
		addresses=[0x9b3aaca,0x9b3d2d3,0x9b3fae5,0x9b422fc,0x9b44b0b,0x9b47b13,0x9b4ab17,0x9b50ac2,0x9b532cb,0x9b55add,0x9b582f4,0x9b5ab03,0x9b5d30b,0x9b6030f,0x9b4db7f,0x9b63377],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 5",
		addresses=[0x9b3aace,0x9b3d2d7,0x9b3fae9,0x9b42300,0x9b44b0f,0x9b47b17,0x9b4ab1b,0x9b50ac6,0x9b532cf,0x9b55ae1,0x9b582f8,0x9b5ab07,0x9b5d30f,0x9b60313,0x9b4db83,0x9b6337b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 6",
		addresses=[0x9b3aad2,0x9b3d2db,0x9b3faed,0x9b42304,0x9b44b13,0x9b47b1b,0x9b4ab1f,0x9b50aca,0x9b532d3,0x9b55ae5,0x9b582fc,0x9b5ab0b,0x9b5d313,0x9b60317,0x9b4db87,0x9b6337f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 7",
		addresses=[0x9b3aad6,0x9b3d2df,0x9b3faf1,0x9b42308,0x9b44b17,0x9b47b1f,0x9b4ab23,0x9b50ace,0x9b532d7,0x9b55ae9,0x9b58300,0x9b5ab0f,0x9b5d317,0x9b6031b,0x9b4db8b,0x9b63383],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 8",
		addresses=[0x9b3aada,0x9b3d2e3,0x9b3faf5,0x9b4230c,0x9b44b1b,0x9b47b23,0x9b4ab27,0x9b50ad2,0x9b532db,0x9b55aed,0x9b58304,0x9b5ab13,0x9b5d31b,0x9b6031f,0x9b4db8f,0x9b63387],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 9",
		addresses=[0x9b3aade,0x9b3d2e7,0x9b3faf9,0x9b42310,0x9b44b1f,0x9b47b27,0x9b4ab2b,0x9b50ad6,0x9b532df,0x9b55af1,0x9b58308,0x9b5ab17,0x9b5d31f,0x9b60323,0x9b4db93,0x9b6338b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 10",
		addresses=[0x9b3aae2,0x9b3d2eb,0x9b3fafd,0x9b42314,0x9b44b23,0x9b47b2b,0x9b4ab2f,0x9b50ada,0x9b532e3,0x9b55af5,0x9b5830c,0x9b5ab1b,0x9b5d323,0x9b60327,0x9b4db97,0x9b6338f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 11",
		addresses=[0x9b3aae6,0x9b3d2ef,0x9b3fb01,0x9b42318,0x9b44b27,0x9b47b2f,0x9b4ab33,0x9b50ade,0x9b532e7,0x9b55af9,0x9b58310,0x9b5ab1f,0x9b5d327,0x9b6032b,0x9b4db9b,0x9b63393],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 12",
		addresses=[0x9b3aaea,0x9b3d2f3,0x9b3fb05,0x9b4231c,0x9b44b2b,0x9b47b33,0x9b4ab37,0x9b50ae2,0x9b532eb,0x9b55afd,0x9b58314,0x9b5ab23,0x9b5d32b,0x9b6032f,0x9b4db9f,0x9b63397],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 13",
		addresses=[0x9b3aaee,0x9b3d2f7,0x9b3fb09,0x9b42320,0x9b44b2f,0x9b47b37,0x9b4ab3b,0x9b50ae6,0x9b532ef,0x9b55b01,0x9b58318,0x9b5ab27,0x9b5d32f,0x9b60333,0x9b4dba3,0x9b6339b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 14",
		addresses=[0x9b4dba7,0x9b6339f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 15",
		addresses=[0x9b4dbab,0x9b633a3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 16",
		addresses=[0x9b4dbaf,0x9b633a7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 17",
		addresses=[0x9b4dbb3,0x9b633ab],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 18",
		addresses=[0x9b4dbb7,0x9b633af],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),
	Attribute(
		name="RUFIO ITEM 19",
		addresses=[0x9b4dbbb,0x9b633b3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("RUFIO"),
		is_little_endian=False, ),

# 17 FLAVIN SHOP
# FLAVIN ITEM POOL [312,313,314,315,316,317,318,319]
	Attribute(
		name="FLAVIN ITEM 1",
		addresses=[0x9b3ab10,0x9b3d319,0x9b3fb2b,0x9b42342,0x9b44b51,0x9b47b59,0x9b4ab5d,0x9b4dbdd,0x9b50b08,0x9b53311,0x9b55b23,0x9b5833a,0x9b5ab49,0x9b5d351,0x9b60355,0x9b633d5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 2",
		addresses=[0x9b3ab14,0x9b3d31d,0x9b3fb2f,0x9b42346,0x9b44b55,0x9b47b5d,0x9b4ab61,0x9b4dbe1,0x9b50b0c,0x9b53315,0x9b55b27,0x9b5833e,0x9b5ab4d,0x9b5d355,0x9b60359,0x9b633d9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 3",
		addresses=[0x9b3ab18,0x9b3d321,0x9b3fb33,0x9b4234a,0x9b44b59,0x9b47b61,0x9b4ab65,0x9b4dbe5,0x9b50b10,0x9b53319,0x9b55b2b,0x9b58342,0x9b5ab51,0x9b5d359,0x9b6035d,0x9b633dd],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 4",
		addresses=[0x9b3ab1c,0x9b3d325,0x9b3fb37,0x9b4234e,0x9b44b5d,0x9b47b65,0x9b4ab69,0x9b4dbe9,0x9b50b14,0x9b5331d,0x9b55b2f,0x9b58346,0x9b5ab55,0x9b5d35d,0x9b60361,0x9b633e1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 5",
		addresses=[0x9b3ab20,0x9b3d329,0x9b3fb3b,0x9b42352,0x9b44b61,0x9b47b69,0x9b4ab6d,0x9b4dbed,0x9b50b18,0x9b53321,0x9b55b33,0x9b5834a,0x9b5ab59,0x9b5d361,0x9b60365,0x9b633e5],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 6",
		addresses=[0x9b3ab24,0x9b3d32d,0x9b3fb3f,0x9b42356,0x9b44b65,0x9b47b6d,0x9b4ab71,0x9b4dbf1,0x9b50b1c,0x9b53325,0x9b55b37,0x9b5834e,0x9b5ab5d,0x9b5d365,0x9b60369,0x9b633e9],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 7",
		addresses=[0x9b3ab28,0x9b3d331,0x9b3fb43,0x9b4235a,0x9b44b69,0x9b47b71,0x9b4ab75,0x9b4dbf5,0x9b50b20,0x9b53329,0x9b55b3b,0x9b58352,0x9b5ab61,0x9b5d369,0x9b6036d,0x9b633ed],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),
	Attribute(
		name="FLAVIN ITEM 8",
		addresses=[0x9b3ab2c,0x9b3d335,0x9b3fb47,0x9b4235e,0x9b44b6d,0x9b47b75,0x9b4ab79,0x9b4dbf9,0x9b50b24,0x9b5332d,0x9b55b3f,0x9b58356,0x9b5ab65,0x9b5d36d,0x9b60371,0x9b633f1],
		number_of_bytes=3,
		possible_values=ChooseShopItems("FLAVIN"),
		is_little_endian=False, ),

# 18 OLIVE SHOP
# OLIVE ITEM POOL [303,377,378,379,380]
	Attribute(
		name="OLIVE ITEM 1",
		addresses=[0x9b3ab4e,0x9b3d357,0x9b3fb69,0x9b42380,0x9b44b8f,0x9b47b97,0x9b4ab9b,0x9b4dc1b,0x9b50b46,0x9b5334f,0x9b55b61,0x9b58378,0x9b5ab87,0x9b5d38f,0x9b60393,0x9b63413],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 2",
		addresses=[0x9b3ab52,0x9b3d35b,0x9b3fb6d,0x9b42384,0x9b44b93,0x9b47b9b,0x9b4ab9f,0x9b4dc1f,0x9b50b4a,0x9b53353,0x9b55b65,0x9b5837c,0x9b5ab8b,0x9b5d393,0x9b60397,0x9b63417],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 3",
		addresses=[0x9b3ab56,0x9b3d35f,0x9b3fb71,0x9b42388,0x9b44b97,0x9b47b9f,0x9b4aba3,0x9b4dc23,0x9b50b4e,0x9b53357,0x9b55b69,0x9b58380,0x9b5ab8f,0x9b5d397,0x9b6039b,0x9b6341b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 4",
		addresses=[0x9b3ab5a,0x9b3d363,0x9b3fb75,0x9b4238c,0x9b44b9b,0x9b47ba3,0x9b4aba7,0x9b4dc27,0x9b50b52,0x9b5335b,0x9b55b6d,0x9b58384,0x9b5ab93,0x9b5d39b,0x9b6039f,0x9b6341f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),
	Attribute(
		name="OLIVE ITEM 5",
		addresses=[0x9b3ab5e,0x9b3d367,0x9b3fb79,0x9b42390,0x9b44b9f,0x9b47ba7,0x9b4abab,0x9b4dc2b,0x9b50b56,0x9b5335f,0x9b55b71,0x9b58388,0x9b5ab97,0x9b5d39f,0x9b603a3,0x9b63423],
		number_of_bytes=3,
		possible_values=ChooseShopItems("OLIVE"),
		is_little_endian=False, ),

# 19 JULIA
# JULIA ITEM POOL [91,92,94,103]

# 20 MENA SHOP
# MENA ITEM POOL [263,264,265,129,130,131,132]
	Attribute(
		name="MENA ITEM 1",
		addresses=[0x9b3ab9f,0x9b3d3ac,0x9b3fbc1,0x9b50b97,0x9b533a4,0x9b55bb9,0x9b583d3,0x9b423db,0x9b44bea,0x9b5abe2,0x9b5d3ea,0x9b603ee,0x9b47bf2,0x9b4abf6,0x9b4dc76,0x9b6346e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 2",
		addresses=[0x9b3aba3,0x9b3d3b0,0x9b3fbc5,0x9b50b9b,0x9b533a8,0x9b55bbd,0x9b583d7,0x9b423df,0x9b44bee,0x9b5abe6,0x9b5d3ee,0x9b603f2,0x9b47bf6,0x9b4abfa,0x9b4dc7a,0x9b63472],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 3",
		addresses=[0x9b3aba7,0x9b3d3b4,0x9b3fbc9,0x9b50b9f,0x9b533ac,0x9b55bc1,0x9b583db,0x9b423e3,0x9b44bf2,0x9b5abea,0x9b5d3f2,0x9b603f6,0x9b47bfa,0x9b4abfe,0x9b4dc7e,0x9b63476],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 4",
		addresses=[0x9b583df,0x9b423e7,0x9b44bf6,0x9b5abee,0x9b5d3f6,0x9b603fa,0x9b47bfe,0x9b4ac02,0x9b4dc82,0x9b6347a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 5",
		addresses=[0x9b44bfa,0x9b5abf2,0x9b5d3fa,0x9b603fe,0x9b47c02,0x9b4ac06,0x9b4dc86,0x9b6347e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 6",
		addresses=[0x9b5d3fe,0x9b60402,0x9b47c06,0x9b4ac0a,0x9b4dc8a,0x9b63482],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),
	Attribute(
		name="MENA ITEM 7",
		addresses=[0x9b4dc8e,0x9b63486],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MENA"),
		is_little_endian=False, ),

# 21 CORINNE SHOP
# CORINNE ITEM POOL [123,124,125,126]
	Attribute(
		name="CORINNE ITEM 1",
		addresses=[0x9b3abc7,0x9b3d3d4,0x9b3fbe9,0x9b42407,0x9b44c1a,0x9b47c26,0x9b4ac2a,0x9b4dcae,0x9b50bbf,0x9b533cc,0x9b55be1,0x9b583ff,0x9b5ac12,0x9b5d41e,0x9b60422,0x9b634a6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 2",
		addresses=[0x9b3abcb,0x9b3d3d8,0x9b3fbed,0x9b4240b,0x9b44c1e,0x9b47c2a,0x9b4ac2e,0x9b4dcb2,0x9b50bc3,0x9b533d0,0x9b55be5,0x9b58403,0x9b5ac16,0x9b5d422,0x9b60426,0x9b634aa],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 3",
		addresses=[0x9b3abcf,0x9b3d3dc,0x9b3fbf1,0x9b4240f,0x9b44c22,0x9b47c2e,0x9b4ac32,0x9b4dcb6,0x9b50bc7,0x9b533d4,0x9b55be9,0x9b58407,0x9b5ac1a,0x9b5d426,0x9b6042a,0x9b634ae],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),
	Attribute(
		name="CORINNE ITEM 4",
		addresses=[0x9b3abd3,0x9b3d3e0,0x9b3fbf5,0x9b42413,0x9b44c26,0x9b47c32,0x9b4ac36,0x9b4dcba,0x9b50bcb,0x9b533d8,0x9b55bed,0x9b5840b,0x9b5ac1e,0x9b5d42a,0x9b6042e,0x9b634b2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CORINNE"),
		is_little_endian=False, ),

# 22 ROSA SHOP
# ROSA ITEM POOL [253,254,255,256,257]
	Attribute(
		name="ROSA ITEM 1",
		addresses=[0x9b3abfb,0x9b3d408,0x9b3fc1d,0x9b4243b,0x9b44c4e,0x9b47c5a,0x9b4ac5e,0x9b4dce2,0x9b50bf3,0x9b53400,0x9b55c15,0x9b58433,0x9b5ac46,0x9b5d452,0x9b60456,0x9b634da],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 2",
		addresses=[0x9b3abff,0x9b3d40c,0x9b3fc21,0x9b4243f,0x9b44c52,0x9b47c5e,0x9b4ac62,0x9b4dce6,0x9b50bf7,0x9b53404,0x9b55c19,0x9b58437,0x9b5ac4a,0x9b5d456,0x9b6045a,0x9b634de],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 3",
		addresses=[0x9b3ac03,0x9b3d410,0x9b3fc25,0x9b42443,0x9b44c56,0x9b47c62,0x9b4ac66,0x9b4dcea,0x9b50bfb,0x9b53408,0x9b55c1d,0x9b5843b,0x9b5ac4e,0x9b5d45a,0x9b6045e,0x9b634e2],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 4",
		addresses=[0x9b3ac07,0x9b3d414,0x9b3fc29,0x9b42447,0x9b44c5a,0x9b47c66,0x9b4ac6a,0x9b4dcee,0x9b50bff,0x9b5340c,0x9b55c21,0x9b5843f,0x9b5ac52,0x9b5d45e,0x9b60462,0x9b634e6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),
	Attribute(
		name="ROSA ITEM 5",
		addresses=[0x9b3ac0b,0x9b3d418,0x9b3fc2d,0x9b4244b,0x9b44c5e,0x9b47c6a,0x9b4ac6e,0x9b4dcf2,0x9b50c03,0x9b53410,0x9b55c25,0x9b58443,0x9b5ac56,0x9b5d462,0x9b60466,0x9b634ea],
		number_of_bytes=3,
		possible_values=ChooseShopItems("ROSA"),
		is_little_endian=False, ),

# 23 CEDRIC SHOP
# CEDRIC ITEM POOL [246,137,138,141,146,149,152,156,158,159,166,422,423]
	Attribute(
		name="CEDRIC ITEM 1",
		addresses=[0x9b3ac31,0x9b50c29,0x9b53436,0x9b3d43e,0x9b3fc53,0x9b55c4b,0x9b58469,0x9b42471,0x9b44c84,0x9b5ac7c,0x9b5d488,0x9b47c90,0x9b4ac94,0x9b4dd18,0x9b6048c,0x9b63510],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 2",
		addresses=[0x9b3ac35,0x9b50c2d,0x9b5343a,0x9b3d442,0x9b3fc57,0x9b55c4f,0x9b5846d,0x9b42475,0x9b44c88,0x9b5ac80,0x9b5d48c,0x9b47c94,0x9b4ac98,0x9b4dd1c,0x9b60490,0x9b63514],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 3",
		addresses=[0x9b3ac39,0x9b50c31,0x9b5343e,0x9b3d446,0x9b3fc5b,0x9b55c53,0x9b58471,0x9b42479,0x9b44c8c,0x9b5ac84,0x9b5d490,0x9b47c98,0x9b4ac9c,0x9b4dd20,0x9b60494,0x9b63518],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 4",
		addresses=[0x9b53442,0x9b3d44a,0x9b3fc5f,0x9b55c57,0x9b58475,0x9b4247d,0x9b44c90,0x9b5ac88,0x9b5d494,0x9b47c9c,0x9b4aca0,0x9b4dd24,0x9b60498,0x9b6351c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 5",
		addresses=[0x9b53446,0x9b3d44e,0x9b3fc63,0x9b55c5b,0x9b58479,0x9b42481,0x9b44c94,0x9b5ac8c,0x9b5d498,0x9b47ca0,0x9b4aca4,0x9b4dd28,0x9b6049c,0x9b63520],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 6",
		addresses=[0x9b3fc67,0x9b55c5f,0x9b5847d,0x9b42485,0x9b44c98,0x9b5ac90,0x9b5d49c,0x9b47ca4,0x9b4aca8,0x9b4dd2c,0x9b604a0,0x9b63524],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 7",
		addresses=[0x9b58481,0x9b42489,0x9b44c9c,0x9b5ac94,0x9b5d4a0,0x9b47ca8,0x9b4acac,0x9b4dd30,0x9b604a4,0x9b63528],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 8",
		addresses=[0x9b58485,0x9b4248d,0x9b44ca0,0x9b5ac98,0x9b5d4a4,0x9b47cac,0x9b4acb0,0x9b4dd34,0x9b604a8,0x9b6352c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 9",
		addresses=[0x9b44ca4,0x9b5ac9c,0x9b5d4a8,0x9b47cb0,0x9b4acb4,0x9b4dd38,0x9b604ac,0x9b63530],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 10",
		addresses=[0x9b5d4ac,0x9b47cb4,0x9b4acb8,0x9b4dd3c,0x9b604b0,0x9b6353],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 11",
		addresses=[0x9b5d4b0,0x9b47cb8,0x9b4acbc,0x9b4dd40,0x9b604b4,0x9b63538],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 12",
		addresses=[0x9b4acc0,0x9b4dd44,0x9b604b8,0x9b6353c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),
	Attribute(
		name="CEDRIC ITEM 13",
		addresses=[0x9b4acc4,0x9b4dd48,0x9b604bc,0x9b63540],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CEDRIC"),
		is_little_endian=False, ),

# 24 WOODY TAILORS SHOP
# WOODY TAILORS ITEM POOL [258,259,260,263,201,202,424,304,376]
	Attribute(
		name="WOODY TAILORS ITEM 1",
		addresses=[0x9b3ac5b,0x9b3d470,0x9b3fc89,0x9b424af,0x9b44cc6,0x9b47cda,0x9b4ace6,0x9b4dd6a,0x9b50c53,0x9b53468,0x9b55c81,0x9b584a7,0x9b5acbe,0x9b5d4d2,0x9b604de,0x9b63562],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 2",
		addresses=[0x9b3ac5f,0x9b3d474,0x9b3fc8d,0x9b424b3,0x9b44cca,0x9b47cde,0x9b4acea,0x9b4dd6e,0x9b50c57,0x9b5346c,0x9b55c85,0x9b584ab,0x9b5acc2,0x9b5d4d6,0x9b604e2,0x9b63566],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 3",
		addresses=[0x9b3ac63,0x9b3d478,0x9b3fc91,0x9b424b7,0x9b44cce,0x9b47ce2,0x9b4acee,0x9b4dd72,0x9b50c5b,0x9b53470,0x9b55c89,0x9b584af,0x9b5acc6,0x9b5d4da,0x9b604e6,0x9b6356a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 4",
		addresses=[0x9b3ac67,0x9b3d47c,0x9b3fc95,0x9b424bb,0x9b44cd2,0x9b47ce6,0x9b4acf2,0x9b4dd76,0x9b50c5f,0x9b53474,0x9b55c8d,0x9b584b3,0x9b5acca,0x9b5d4de,0x9b604ea,0x9b6356e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 5",
		addresses=[0x9b3ac6b,0x9b3d480,0x9b3fc99,0x9b424bf,0x9b44cd6,0x9b47cea,0x9b4acf6,0x9b4dd7a,0x9b50c63,0x9b53478,0x9b55c91,0x9b584b7,0x9b5acce,0x9b5d4e2,0x9b604ee,0x9b63572],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 6",
		addresses=[0x9b3ac6f,0x9b3d484,0x9b3fc9d,0x9b424c3,0x9b44cda,0x9b47cee,0x9b4acfa,0x9b4dd7e,0x9b50c67,0x9b5347c,0x9b55c95,0x9b584bb,0x9b5acd2,0x9b5d4e6,0x9b604f2,0x9b63576],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 7",
		addresses=[0x9b3ac73,0x9b3d488,0x9b3fca1,0x9b424c7,0x9b44cde,0x9b47cf2,0x9b4acfe,0x9b4dd82,0x9b50c6b,0x9b53480,0x9b55c99,0x9b584bf,0x9b5acd6,0x9b5d4ea,0x9b604f6,0x9b6357a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),
	Attribute(
		name="WOODY TAILORS ITEM 8",
		addresses=[0x9b3ac77,0x9b3d48c,0x9b3fca5,0x9b424cb,0x9b44ce2,0x9b47cf6,0x9b4ad02,0x9b4dd86,0x9b50c6f,0x9b53484,0x9b55c9d,0x9b584c3,0x9b5acda,0x9b5d4ee,0x9b604fa,0x9b6357e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("WOODY TAILORS"),
		is_little_endian=False, ),

# 25 JURAK ARMS SHOP
# JURAK ARMS ITEM POOL [17,23,25,41,47,49,73,201,294,298,352] (201 IS REPLACED WITH 47 IN CHAPTER 5 ONWARDS)

# 26 MUSHROOM BURGER EATERY SHOP
# MUSHROOM BURGER EATERY ITEM POOL [219,220,268,301,425,287,289,290,291,292,313,315,316,318]
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 1",
		addresses=[0x9b3accc,0x9b3d4e9,0x9b3fd05,0x9b42531,0x9b44d47,0x9b47d5b,0x9b4ad67,0x9b4ddeb,0x9b50cc4,0x9b534e1,0x9b55cfd,0x9b58529,0x9b5ad3f,0x9b5d553,0x9b6055f,0x9b635e3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 2",
		addresses=[0x9b3acd0,0x9b3d4ed,0x9b3fd09,0x9b42535,0x9b44d4b,0x9b47d5f,0x9b4ad6b,0x9b4ddef,0x9b50cc8,0x9b534e5,0x9b55d01,0x9b5852d,0x9b5ad43,0x9b5d557,0x9b60563,0x9b635e7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 3",
		addresses=[0x9b3acd4,0x9b3d4f1,0x9b3fd0d,0x9b42539,0x9b44d4f,0x9b47d63,0x9b4ad6f,0x9b4ddf3,0x9b50ccc,0x9b534e9,0x9b55d05,0x9b58531,0x9b5ad47,0x9b5d55b,0x9b60567,0x9b635eb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 4",
		addresses=[0x9b3acd8,0x9b3d4f5,0x9b3fd11,0x9b4253d,0x9b44d53,0x9b47d67,0x9b4ad73,0x9b4ddf7,0x9b50cd0,0x9b534ed,0x9b55d09,0x9b58535,0x9b5ad4b,0x9b5d55f,0x9b6056b,0x9b635ef],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 5",
		addresses=[0x9b3acdc,0x9b3d4f9,0x9b3fd15,0x9b42541,0x9b44d57,0x9b47d6b,0x9b4ad77,0x9b4ddfb,0x9b50cd4,0x9b534f1,0x9b55d0d,0x9b58539,0x9b5ad4f,0x9b5d563,0x9b6056f,0x9b635f3],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 6",
		addresses=[0x9b3ace0,0x9b3d4fd,0x9b3fd19,0x9b42545,0x9b44d5b,0x9b47d6f,0x9b4ad7b,0x9b4ddff,0x9b50cd8,0x9b534f5,0x9b55d11,0x9b5853d,0x9b5ad53,0x9b5d567,0x9b60573,0x9b635f7],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 7",
		addresses=[0x9b3ace4,0x9b3d501,0x9b3fd1d,0x9b42549,0x9b44d5f,0x9b47d73,0x9b4ad7f,0x9b4de03,0x9b50cdc,0x9b534f9,0x9b55d15,0x9b58541,0x9b5ad57,0x9b5d56b,0x9b60577,0x9b635fb],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 8",
		addresses=[0x9b3ace8,0x9b3d505,0x9b3fd21,0x9b4254d,0x9b44d63,0x9b47d77,0x9b4ad83,0x9b4de07,0x9b50ce0,0x9b534fd,0x9b55d19,0x9b58545,0x9b5ad5b,0x9b5d56f,0x9b6057b,0x9b635ff],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 9",
		addresses=[0x9b3acec,0x9b3d509,0x9b3fd25,0x9b42551,0x9b44d67,0x9b47d7b,0x9b4ad87,0x9b4de0b,0x9b50ce4,0x9b53501,0x9b55d1d,0x9b58549,0x9b5ad5f,0x9b5d573,0x9b6057f,0x9b63603],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 10",
		addresses=[0x9b3acf0,0x9b3d50d,0x9b3fd29,0x9b42555,0x9b44d6b,0x9b47d7f,0x9b4ad8b,0x9b4de0f,0x9b50ce8,0x9b53505,0x9b55d21,0x9b5854d,0x9b5ad63,0x9b5d577,0x9b60583,0x9b63607],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 11",
		addresses=[0x9b3acf4,0x9b3d511,0x9b3fd2d,0x9b42559,0x9b44d6f,0x9b47d83,0x9b4ad8f,0x9b4de13,0x9b50cec,0x9b53509,0x9b55d25,0x9b58551,0x9b5ad67,0x9b5d57b,0x9b60587,0x9b6360b],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 12",
		addresses=[0x9b3acf8,0x9b3d515,0x9b3fd31,0x9b4255d,0x9b44d73,0x9b47d87,0x9b4ad93,0x9b4de17,0x9b50cf0,0x9b5350d,0x9b55d29,0x9b58555,0x9b5ad6b,0x9b5d57f,0x9b6058b,0x9b6360f],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 13",
		addresses=[0x9b3acfc,0x9b3d519,0x9b3fd35,0x9b42561,0x9b44d77,0x9b47d8b,0x9b4ad97,0x9b4de1b,0x9b50cf4,0x9b53511,0x9b55d2d,0x9b58559,0x9b5ad6f,0x9b5d583,0x9b6058f,0x9b63613],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),
	Attribute(
		name="MUSHROOM BURGER EATERY ITEM 14",
		addresses=[0x9b3ad00,0x9b3d51d,0x9b3fd39,0x9b42565,0x9b44d7b,0x9b47d8f,0x9b4ad9b,0x9b4de1f,0x9b50cf8,0x9b53515,0x9b55d31,0x9b5855d,0x9b5ad73,0x9b5d587,0x9b60593,0x9b63617],
		number_of_bytes=3,
		possible_values=ChooseShopItems("MUSHROOM BURGER EATERY"),
		is_little_endian=False, ),

# 27 STARLIGHT WEAPONS SHOP
# STARLIGHT WEAPONS ITEM POOL [11,45,67,92,93,95,106,352]

# 28 G PARTS SHOP
# G PARTS ITEM POOL [137,150,160,166,381]
	Attribute(
		name="G PARTS ITEM 1",
		addresses=[0x9b3ad43,0x9b3d560,0x9b3fd7c,0x9b425ab,0x9b44dc4,0x9b47ddc,0x9b4ade8,0x9b4de6c,0x9b50d3b,0x9b53558,0x9b55d74,0x9b585a3,0x9b5adbc,0x9b5d5d4,0x9b605e0,0x9b63664],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 2",
		addresses=[0x9b3ad47,0x9b3d564,0x9b3fd80,0x9b425af,0x9b44dc8,0x9b47de0,0x9b4adec,0x9b4de70,0x9b50d3f,0x9b5355c,0x9b55d78,0x9b585a7,0x9b5adc0,0x9b5d5d8,0x9b605e4,0x9b63668],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 3",
		addresses=[0x9b3ad4b,0x9b3d568,0x9b3fd84,0x9b425b3,0x9b44dcc,0x9b47de4,0x9b4adf0,0x9b4de74,0x9b50d43,0x9b53560,0x9b55d7c,0x9b585ab,0x9b5adc4,0x9b5d5dc,0x9b605e8,0x9b6366c],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 4",
		addresses=[0x9b3ad4f,0x9b3d56c,0x9b3fd88,0x9b425b7,0x9b44dd0,0x9b47de8,0x9b4adf4,0x9b4de78,0x9b50d47,0x9b53564,0x9b55d80,0x9b585af,0x9b5adc8,0x9b5d5e0,0x9b605ec,0x9b63670],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),
	Attribute(
		name="G PARTS ITEM 5",
		addresses=[0x9b3ad53,0x9b3d570,0x9b3fd8c,0x9b425bb,0x9b44dd4,0x9b47dec,0x9b4adf8,0x9b4de7c,0x9b50d4b,0x9b53568,0x9b55d84,0x9b585b3,0x9b5adcc,0x9b5d5e4,0x9b605f0,0x9b63674],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G PARTS"),
		is_little_endian=False, ),

# 29 G TOOLS SHOP
# G TOOLS ITEM POOL [269,425,294,298,352]
	Attribute(
		name="G TOOLS ITEM 1",
		addresses=[0x9b3ad6c,0x9b3d589,0x9b3fda5,0x9b425d4,0x9b44ded,0x9b47e05,0x9b4ae11,0x9b4de95,0x9b50d64,0x9b53581,0x9b55d9d,0x9b585cc,0x9b5ade5,0x9b5d5fd,0x9b60609,0x9b6368d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 2",
		addresses=[0x9b3ad70,0x9b3d58d,0x9b3fda9,0x9b425d8,0x9b44df1,0x9b47e09,0x9b4ae15,0x9b4de99,0x9b50d68,0x9b53585,0x9b55da1,0x9b585d0,0x9b5ade9,0x9b5d601,0x9b6060d,0x9b63691],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 3",
		addresses=[0x9b3ad74,0x9b3d591,0x9b3fdad,0x9b425dc,0x9b44df5,0x9b47e0d,0x9b4ae19,0x9b4de9d,0x9b50d6c,0x9b53589,0x9b55da5,0x9b585d4,0x9b5aded,0x9b5d605,0x9b60611,0x9b63695],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 4",
		addresses=[0x9b3ad78,0x9b3d595,0x9b3fdb1,0x9b425e0,0x9b44df9,0x9b47e11,0x9b4ae1d,0x9b4dea1,0x9b50d70,0x9b5358d,0x9b55da9,0x9b585d8,0x9b5adf1,0x9b5d609,0x9b60615,0x9b63699],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),
	Attribute(
		name="G TOOLS ITEM 5",
		addresses=[0x9b3ad7c,0x9b3d599,0x9b3fdb5,0x9b425e4,0x9b44dfd,0x9b47e15,0x9b4ae21,0x9b4dea5,0x9b50d74,0x9b53591,0x9b55dad,0x9b585dc,0x9b5adf5,0x9b5d60d,0x9b60619,0x9b6369d],
		number_of_bytes=3,
		possible_values=ChooseShopItems("G TOOLS"),
		is_little_endian=False, ),

# 30 G WEAPONS SHOP
# G WEAPONS ITEM POOL [6,7,13,32,70,71,76,95,294,298,352]

# 31 CONDA SHOP
# CONDA ITEM POOL [210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236]
	Attribute(
		name="CONDA ITEM 1",
		addresses=[0x9b3adbf,0x9b3d5dc,0x9b3fdf8,0x9b42627,0x9b44e51,0x9b47e6e,0x9b4ae7a,0x9b4defe,0x9b50db7,0x9b535d4,0x9b55df0,0x9b5861f,0x9b5ae49,0x9b5d666,0x9b60672,0x9b636f6],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 2",
		addresses=[0x9b3adc3,0x9b3d5e0,0x9b3fdfc,0x9b4262b,0x9b44e55,0x9b47e72,0x9b4ae7e,0x9b4df02,0x9b50dbb,0x9b535d8,0x9b55df4,0x9b58623,0x9b5ae4d,0x9b5d66a,0x9b60676,0x9b636fa],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 3",
		addresses=[0x9b3adc7,0x9b3d5e4,0x9b3fe00,0x9b4262f,0x9b44e59,0x9b47e76,0x9b4ae82,0x9b4df06,0x9b50dbf,0x9b535dc,0x9b55df8,0x9b58627,0x9b5ae51,0x9b5d66e,0x9b6067a,0x9b636fe],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 4",
		addresses=[0x9b3adcb,0x9b3d5e8,0x9b3fe04,0x9b42633,0x9b44e5d,0x9b47e7a,0x9b4ae86,0x9b4df0a,0x9b50dc3,0x9b535e0,0x9b55dfc,0x9b5862b,0x9b5ae55,0x9b5d672,0x9b6067e,0x9b63702],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 5",
		addresses=[0x9b3adcf,0x9b3d5ec,0x9b3fe08,0x9b42637,0x9b44e61,0x9b47e7e,0x9b4ae8a,0x9b4df0e,0x9b50dc7,0x9b535e4,0x9b55e00,0x9b5862f,0x9b5ae59,0x9b5d676,0x9b60682,0x9b63706],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 6",
		addresses=[0x9b3add3,0x9b3d5f0,0x9b3fe0c,0x9b4263b,0x9b44e65,0x9b47e82,0x9b4ae8e,0x9b4df12,0x9b50dcb,0x9b535e8,0x9b55e04,0x9b58633,0x9b5ae5d,0x9b5d67a,0x9b60686,0x9b6370a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 7",
		addresses=[0x9b3add7,0x9b3d5f4,0x9b3fe10,0x9b4263f,0x9b44e69,0x9b47e86,0x9b4ae92,0x9b4df16,0x9b50dcf,0x9b535ec,0x9b55e08,0x9b58637,0x9b5ae61,0x9b5d67e,0x9b6068a,0x9b6370e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 8",
		addresses=[0x9b3addb,0x9b3d5f8,0x9b3fe14,0x9b42643,0x9b44e6d,0x9b47e8a,0x9b4ae96,0x9b4df1a,0x9b50dd3,0x9b535f0,0x9b55e0c,0x9b5863b,0x9b5ae65,0x9b5d682,0x9b6068e,0x9b63712],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 9",
		addresses=[0x9b3addf,0x9b3d5fc,0x9b3fe18,0x9b42647,0x9b44e71,0x9b47e8e,0x9b4ae9a,0x9b4df1e,0x9b50dd7,0x9b535f4,0x9b55e10,0x9b5863f,0x9b5ae69,0x9b5d686,0x9b60692,0x9b63716],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 10",
		addresses=[0x9b3ade3,0x9b3d600,0x9b3fe1c,0x9b4264b,0x9b44e75,0x9b47e92,0x9b4ae9e,0x9b4df22,0x9b50ddb,0x9b535f8,0x9b55e14,0x9b58643,0x9b5ae6d,0x9b5d68a,0x9b60696,0x9b6371a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 11",
		addresses=[0x9b3ade7,0x9b3d604,0x9b3fe20,0x9b4264f,0x9b44e79,0x9b47e96,0x9b4aea2,0x9b4df26,0x9b50ddf,0x9b535fc,0x9b55e18,0x9b58647,0x9b5ae71,0x9b5d68e,0x9b6069a,0x9b6371e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 12",
		addresses=[0x9b3adeb,0x9b3d608,0x9b3fe24,0x9b42653,0x9b44e7d,0x9b47e9a,0x9b4aea6,0x9b4df2a,0x9b50de3,0x9b53600,0x9b55e1c,0x9b5864b,0x9b5ae75,0x9b5d692,0x9b6069e,0x9b63722],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 13",
		addresses=[0x9b3adef,0x9b3d60c,0x9b3fe28,0x9b42657,0x9b44e81,0x9b47e9e,0x9b4aeaa,0x9b4df2e,0x9b50de7,0x9b53604,0x9b55e20,0x9b5864f,0x9b5ae79,0x9b5d696,0x9b606a2,0x9b63726],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 14",
		addresses=[0x9b3adf3,0x9b3d610,0x9b3fe2c,0x9b4265b,0x9b44e85,0x9b47ea2,0x9b4aeae,0x9b4df32,0x9b50deb,0x9b53608,0x9b55e24,0x9b58653,0x9b5ae7d,0x9b5d69a,0x9b606a6,0x9b6372a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 15",
		addresses=[0x9b3adf7,0x9b3d614,0x9b3fe30,0x9b4265f,0x9b44e89,0x9b47ea6,0x9b4aeb2,0x9b4df36,0x9b50def,0x9b5360c,0x9b55e28,0x9b58657,0x9b5ae81,0x9b5d69e,0x9b606aa,0x9b6372e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 16",
		addresses=[0x9b3adfb,0x9b3d618,0x9b3fe34,0x9b42663,0x9b44e8d,0x9b47eaa,0x9b4aeb6,0x9b4df3a,0x9b50df3,0x9b53610,0x9b55e2c,0x9b5865b,0x9b5ae85,0x9b5d6a2,0x9b606ae,0x9b63732],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 17",
		addresses=[0x9b3adff,0x9b3d61c,0x9b3fe38,0x9b42667,0x9b44e91,0x9b47eae,0x9b4aeba,0x9b4df3e,0x9b50df7,0x9b53614,0x9b55e30,0x9b5865f,0x9b5ae89,0x9b5d6a6,0x9b606b2,0x9b63736],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 18",
		addresses=[0x9b3ae03,0x9b3d620,0x9b3fe3c,0x9b4266b,0x9b44e95,0x9b47eb2,0x9b4aebe,0x9b4df42,0x9b50dfb,0x9b53618,0x9b55e34,0x9b58663,0x9b5ae8d,0x9b5d6aa,0x9b606b6,0x9b6373a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 19",
		addresses=[0x9b3ae07,0x9b3d624,0x9b3fe40,0x9b4266f,0x9b44e99,0x9b47eb6,0x9b4aec2,0x9b4df46,0x9b50dff,0x9b5361c,0x9b55e38,0x9b58667,0x9b5ae91,0x9b5d6ae,0x9b606ba,0x9b6373e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 20",
		addresses=[0x9b3ae0b,0x9b3d628,0x9b3fe44,0x9b42673,0x9b44e9d,0x9b47eba,0x9b4aec6,0x9b4df4a,0x9b50e03,0x9b53620,0x9b55e3c,0x9b5866b,0x9b5ae95,0x9b5d6b2,0x9b606be,0x9b63742],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 21",
		addresses=[0x9b3ae0f,0x9b3d62c,0x9b3fe48,0x9b42677,0x9b44ea1,0x9b47ebe,0x9b4aeca,0x9b4df4e,0x9b50e07,0x9b53624,0x9b55e40,0x9b5866f,0x9b5ae99,0x9b5d6b6,0x9b606c2,0x9b63746],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 22",
		addresses=[0x9b3ae13,0x9b3d630,0x9b3fe4c,0x9b4267b,0x9b44ea5,0x9b47ec2,0x9b4aece,0x9b4df52,0x9b50e0b,0x9b53628,0x9b55e44,0x9b58673,0x9b5ae9d,0x9b5d6ba,0x9b606c6,0x9b6374a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 23",
		addresses=[0x9b3ae17,0x9b3d634,0x9b3fe50,0x9b4267f,0x9b44ea9,0x9b47ec6,0x9b4aed2,0x9b4df56,0x9b50e0f,0x9b5362c,0x9b55e48,0x9b58677,0x9b5aea1,0x9b5d6be,0x9b606ca,0x9b6374e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 24",
		addresses=[0x9b3ae1b,0x9b3d638,0x9b3fe54,0x9b42683,0x9b44ead,0x9b47eca,0x9b4aed6,0x9b4df5a,0x9b50e13,0x9b53630,0x9b55e4c,0x9b5867b,0x9b5aea5,0x9b5d6c2,0x9b606ce,0x9b63752],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 25",
		addresses=[0x9b3ae1f,0x9b3d63c,0x9b3fe58,0x9b42687,0x9b44eb1,0x9b47ece,0x9b4aeda,0x9b4df5e,0x9b50e17,0x9b53634,0x9b55e50,0x9b5867f,0x9b5aea9,0x9b5d6c6,0x9b606d2,0x9b63756],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 26",
		addresses=[0x9b3ae23,0x9b3d640,0x9b3fe5c,0x9b4268b,0x9b44eb5,0x9b47ed2,0x9b4aede,0x9b4df62,0x9b50e1b,0x9b53638,0x9b55e54,0x9b58683,0x9b5aead,0x9b5d6ca,0x9b606d6,0x9b6375a],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),
	Attribute(
		name="CONDA ITEM 27",
		addresses=[0x9b3ae27,0x9b3d644,0x9b3fe60,0x9b4268f,0x9b44eb9,0x9b47ed6,0x9b4aee2,0x9b4df66,0x9b50e1f,0x9b5363c,0x9b55e58,0x9b58687,0x9b5aeb1,0x9b5d6ce,0x9b606da,0x9b6375e],
		number_of_bytes=3,
		possible_values=ChooseShopItems("CONDA"),
		is_little_endian=False, ),

	# START OF WEAPON STAT STUFF

	Attribute(
		name="MAX_ATK_DUR_VALUES",
		addresses=[0xda87830,0xda878d0,0xda87971,0xda87d74,0xda87e14,0xda87eb7,0xda87f5b,0xda88157,0xda882a7,0xda8834a,0xda8860b,0xda886aa,0xda8874b,0xda887ee,0xda88892,0xda889e8,0xda88bf0,0xda88eae,0xda892d2,0xda89376,0xda8941a,0xda894bc,0xda8955e,0xda89604,0xda89756,0xda897fa,0xda89aa6,0xda89f6e,0xda8a21e,0xda8a374,0xda8a4c8,0xda8a779,0xda8a81b,0xda8b332,0xda8b3d1,0xda8b474,0xda8b516,0xda8b5bb,0xda8bc97,0xda8c0cb,0xda8c2bf,0xda8c16a,0xda8c214,0xda8bd40,0xda8bdf3,0xda8bea1,0xda8bf57,0xda8c015,0xda8b65f,0xda8b70e,0xda8b7c1,0xda8b86d,0xda8b91a,0xda8b9cf,0xda8ba7d,0xda8bb33,0xda8bbe6,0xda8a8c0,0xda8a96f,0xda8aa1c,0xda8ab83,0xda8ac38,0xdabace9,0xda8ada0,0xdabae4f,0xda8aeff,0xda8afb5,0xda8b064,0xda8b113,0xda8b1c9,0xda8b27e,0xda8a56c,0xda8a619,0xda8a6c7,0xda8a419,0xda8a2c2,0xda8a00f,0xdabadbd,0xda8a16e,0xda89b4a,0xda89bfd,0xda89d5a,0xda89e09,0xda89ebd,0xda8989d,0xda89949,0xda899f8,0xda896a8,0xda88f53,0xda89002,0xda890b3,0xda89168,0xda8921b,0xda88c97,0xda88d46,0xda88df8,0xda88a8d,0xda88b40,0xda88938,0xda883ee,0xda884a0,0xda88555,0xda881fa,0xda87ffe,0xda880ad,0xda87a14,0xda87ac0,0xda87b6d,0xda87c19,0xda87cc5],
		number_of_bytes=8,
		possible_values=[4123389795935795515],
		is_little_endian=False, ),
	Attribute(
		name="MAX_ELEMENT_VALUES",
		addresses=[0xda8785e,0xda878ff,0xda879a2,0xda87da2,0xda87e44,0xda87ee7,0xda87f8b,0xda88187,0xda882d7,0xda88379,0xda88639,0xda886d8,0xda8877a,0xda8881e,0xda888c4,0xda88a19,0xda88c23,0xda88edf,0xda89302,0xda893a6,0xda8944a,0xda894eb,0xda89590,0xda89634,0xda89786,0xda8982a,0xda89ad7,0xda89f9c,0xda8a24f,0xda8a3a5,0xda8a4f8,0xda8a7a8,0xda8a84c,0xda8b360,0xda8b400,0xda8b4a3,0xda8b545,0xda8b5ea,0xda8bcc6,0xda8c0fb,0xda8c2ed],
		number_of_bytes=23,
		possible_values=[5480906228986172978959068208691145648854632458265311545],
		is_little_endian=False, ),
	Attribute(
		name="MAX_ELEMENT_VALUES2",
		addresses=[0xda8c19b,0xda8c245,0xda8bd76,0xda8be24,0xda8bf96,0xda8c04c,0xda8b68f,0xda8b744,0xda8b7f2,0xda8b89e,0xda8b94f,0xda8ba00,0xda8bb68,0xda8bc18,0xda8a9a0,0xda8aa4e,0xda8ab04,0xda8ac6b,0xdabad20,0xdabadd1,0xda8ae84,0xda8af36,0xda8b098,0xda8b147,0xda8b200,0xda8b2b5,0xda8a59e,0xda8a64b,0xda8a6fb,0xda8a44b,0xda8a2f6,0xda8a041,0xda8a0f0,0xda8a19f,0xda89b7f,0xda89c2e,0xda89ce0,0xda89d8c,0xda89e41,0xda89ef4,0xda898ce,0xda8997b,0xda89a29,0xda896da,0xda88f86,0xda89036,0xda890ea,0xda8919d,0xda89255,0xda88cc9,0xda88d78,0xda88e33,0xda88ac0,0xda88b72,0xda8896b,0xda88424,0xda884d7,0xda88590,0xda8822d,0xda8802f,0xda880de,0xda87a45,0xda87af2,0xda87b9e,0xda87c4a,0xda87cfa],
		number_of_bytes=31,
		possible_values=[101105223608376224214622900865844532370874575435817963151290961177349798201],
		is_little_endian=False, ),

# DUNGEON CHEST DROPS
	# SEWERS
	Attribute(
		name="SEWER CHEST 1",
		addresses=[0x5A4170FA],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 2",
		addresses=[0x5A417103],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 3",
		addresses=[0x5A41710C],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 4",
		addresses=[0x5A417115],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 5",
		addresses=[0x5A41711E],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 6",
		addresses=[0x5A41712E],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 7",
		addresses=[0x5A41714B],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 8",
		addresses=[0x5A417154],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 9",
		addresses=[0x5A41715D],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 10",
		addresses=[0x5A417166],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 11",
		addresses=[0x5A417184],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 12",
		addresses=[0x5A41718D],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 13",
		addresses=[0x5A417196],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 14",
		addresses=[0x5A41719F],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 15",
		addresses=[0x5A4171A8],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 16",
		addresses=[0x5A4171B8],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 16",
		addresses=[0x5A4171B8],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 17",
		addresses=[0x5A4171C2],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 18",
		addresses=[0x5A4171CC],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 19",
		addresses=[0x5A4171D5],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 20",
		addresses=[0x5A4171DE],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 21",
		addresses=[0x5A4171EE],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 22",
		addresses=[0x5A41720A],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 23",
		addresses=[0x5A417213],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 24",
		addresses=[0x5A41721C],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 25",
		addresses=[0x5A417225],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="SEWER CHEST 26",
		addresses=[0x5A41722E],
		number_of_bytes=3,
		possible_values=ChooseSewerChestDrops(),
		is_little_endian=False, ),
# Sindain
	Attribute(
		name="Sindain CHEST 1",
		addresses=[0X5A4178D5],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 2",
		addresses=[0X5A4178DE],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 3",
		addresses=[0X5A4178E7],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 4",
		addresses=[0X5A4178F0],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 5",
		addresses=[0X5A4178F9],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 6",
		addresses=[0X5A417908],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 7",
		addresses=[0X5A417911],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 8",
		addresses=[0X5A41791A],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 9",
		addresses=[0X5A417923],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 10",
		addresses=[0X5A41792C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 11",
		addresses=[0X5A41793C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 12",
		addresses=[0X5A417945],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 13",
		addresses=[0X5A417962],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 14",
		addresses=[0X5A417969],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 15",
		addresses=[0X5A417970],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 16",
		addresses=[0X5A417978],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 16",
		addresses=[0X5A417980],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 17",
		addresses=[0X5A41798F],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 18",
		addresses=[0X5A417997],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 19",
		addresses=[0X5A4179B4],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 20",
		addresses=[0X5A4179BD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 21",
		addresses=[0X5A4179C6],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 22",
		addresses=[0X5A4179CF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 23",
		addresses=[0X5A4179D8],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 24",
		addresses=[0X5A4179E8],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 25",
		addresses=[0X5A4179F1],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 26",
		addresses=[0X5A4179FA],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
#
	Attribute(
		name="Sindain CHEST 27",
		addresses=[0X5A417A03],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 28",
		addresses=[0X5A417A0D],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 29",
		addresses=[0X5A417A2B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 30",
		addresses=[0X5A417A36],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 31",
		addresses=[0X5A417A41],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 32",
		addresses=[0X5A417A4C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 33",
		addresses=[0X5A417A57],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 34",
		addresses=[0X5A417A69],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 35",
		addresses=[0X5A417A74],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 36",
		addresses=[0X5A417A7F],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 37",
		addresses=[0X5A417A8A],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 38",
		addresses=[0X5A417A94],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 39",
		addresses=[0X5A417AA5],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 40",
		addresses=[0X5A417AAF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 41",
		addresses=[0X5A417AB9],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 42",
		addresses=[0X5A417AC3],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 43",
		addresses=[0X5A417ACD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 44",
		addresses=[0X5A417ADF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 45",
		addresses=[0X5A417AEA],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 46",
		addresses=[0X5A417AF5],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 47",
		addresses=[0X5A417B14],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 48",
		addresses=[0X5A417B1C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 49",
		addresses=[0X5A417B24],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 50",
		addresses=[0X5A417B2C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 51",
		addresses=[0X5A417B34],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 52",
		addresses=[0X5A417B43],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 53",
		addresses=[0X5A417B5F],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Sindain CHEST 54",
		addresses=[0X5A417B66],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 55",
		addresses=[0X5A417B6E],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 56",
		addresses=[0X5A417B76],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 57",
		addresses=[0X5A417B7E],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 58",
		addresses=[0X5A417B8D],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 59",
		addresses=[0X5A417B95],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 60",
		addresses=[0X5A417B9E],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 61",
		addresses=[0X5A417BBB],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 62",
		addresses=[0X5A417BC4],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 63",
		addresses=[0X5A417BCD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 64",
		addresses=[0X5A417BD6],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 65",
		addresses=[0X5A417BDF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 66",
		addresses=[0X5A417BFD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 67",
		addresses=[0X5A417C06],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 68",
		addresses=[0X5A417C0F],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 69",
		addresses=[0X5A417C18],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 70",
		addresses=[0X5A417C22],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 71",
		addresses=[0X5A417ADF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 72",
		addresses=[0X5A417C32],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 73",
		addresses=[0X5A417C3B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 74",
		addresses=[0X5A417C44],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 75",
		addresses=[0X5A417C4D],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 76",
		addresses=[0X5A417C56],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 77",
		addresses=[0X5A417C66],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 78",
		addresses=[0X5A417C85],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 79",
		addresses=[0X5A417C8C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 80",
		addresses=[0X5A417C93],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Sindain CHEST 81",
		addresses=[0X5A417C9B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 82",
		addresses=[0X5A417CA3],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 83",
		addresses=[0X5A417CB2],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 84",
		addresses=[0X5A417CBC],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 85",
		addresses=[0X5A417CC6],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 86",
		addresses=[0X5A417CD0],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 87",
		addresses=[0X5A417CDA],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 88",
		addresses=[0X5A417CEA],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 89",
		addresses=[0X5A417CF4],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 90",
		addresses=[0X5A417CFE],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 91",
		addresses=[0X5A417D08],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 92",
		addresses=[0X5A417D12],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 93",
		addresses=[0X5A417D22],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 94",
		addresses=[0X5A417D2C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 95",
		addresses=[0X5A417D36],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 96",
		addresses=[0X5A417D40],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 97",
		addresses=[0X5A417D49],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 98",
		addresses=[0X5A417D59],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 99",
		addresses=[0X5A417D62],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 100",
		addresses=[0X5A417D6B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 101",
		addresses=[0X5A417D89],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 102",
		addresses=[0X5A417D92],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 103",
		addresses=[0X5A417D9B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 104",
		addresses=[0X5A417DA4],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 105",
		addresses=[0X5A417DAD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 106",
		addresses=[0X5A417DBD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 107",
		addresses=[0X5A417DC6],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Sindain CHEST 108",
		addresses=[0X5A417DCF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 109",
		addresses=[0X5A417DD8],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 110",
		addresses=[0X5A417DE1],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 111",
		addresses=[0X5A417DFF],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 112",
		addresses=[0X5A417E0A],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 113",
		addresses=[0X5A417E15],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 114",
		addresses=[0X5A417E20],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 115",
		addresses=[0X5A417E2B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 116",
		addresses=[0X5A417E3D],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 117",
		addresses=[0X5A417E48],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 118",
		addresses=[0X5A417E53],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 119",
		addresses=[0X5A417E5C],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 120",
		addresses=[0X5A417E66],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 121",
		addresses=[0X5A417E77],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 122",
		addresses=[0X5A417E81],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 123",
		addresses=[0X5A417E8B],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 124",
		addresses=[0X5A417E95],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 125",
		addresses=[0X5A417EA0],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 126",
		addresses=[0X5A417EB2],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 127",
		addresses=[0X5A417EBD],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 128",
		addresses=[0X5A417EC8],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 129",
		addresses=[0X5A417EE7],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 130",
		addresses=[0X5A417EF0],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 131",
		addresses=[0X5A417EF9],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 132",
		addresses=[0X5A417F02],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Sindain CHEST 133",
		addresses=[0X5A417F02],
		number_of_bytes=3,
		possible_values=ChooseSindainChestDrops(),
		is_little_endian=False, ),	
# Rainbow Butterfly Wood
	# Section3
	Attribute(
		name="Section3 CHEST 1",
		addresses=[0X5A4188D3],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 2",
		addresses=[0X5A4188DA],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 3",
		addresses=[0X5A4188E1],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 4",
		addresses=[0X5A4188E9],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 5",
		addresses=[0X5A4188F1],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 6",
		addresses=[0X5A418900],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 7",
		addresses=[0X5A418907],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 8",
		addresses=[0X5A418924],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 9",
		addresses=[0X5A41892D],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 10",
		addresses=[0X5A418936],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 11",
		addresses=[0X5A418940],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 12",
		addresses=[0X5A418949],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 13",
		addresses=[0X5A418959],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 14",
		addresses=[0X5A418963],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 15",
		addresses=[0X5A41896C],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 16",
		addresses=[0X5A418975],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 16",
		addresses=[0X5A41897E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 17",
		addresses=[0X5A41898E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 18",
		addresses=[0X5A418998],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 19",
		addresses=[0X5A4189A1],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 20",
		addresses=[0X5A4189AB],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 21",
		addresses=[0X5A4189B4],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 22",
		addresses=[0X5A4189C4],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 23",
		addresses=[0X5A4189CD],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 24",
		addresses=[0X5A4189EC],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 25",
		addresses=[0X5A4189F6],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 26",
		addresses=[0X5A418A00],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Section3 CHEST 27",
		addresses=[0X5A418A0A],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 28",
		addresses=[0X5A418A14],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 29",
		addresses=[0X5A418A25],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 30",
		addresses=[0X5A418A2F],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 31",
		addresses=[0X5A418A39],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 32",
		addresses=[0X5A418A43],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 33",
		addresses=[0X5A418A4D],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 34",
		addresses=[0X5A418A5E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 35",
		addresses=[0X5A418A68],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 36",
		addresses=[0X5A418A72],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 37",
		addresses=[0X5A418A7B],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 38",
		addresses=[0X5A418A84],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 39",
		addresses=[0X5A418A94],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 40",
		addresses=[0X5A418A9D],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 41",
		addresses=[0X5A418AA6],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 42",
		addresses=[0X5A418AAF],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 43",
		addresses=[0X5A418AB9],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 44",
		addresses=[0X5A417ADF],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 45",
		addresses=[0X5A418AC9],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 46",
		addresses=[0X5A418AE6],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 47",
		addresses=[0X5A418AED],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 48",
		addresses=[0X5A418AF5],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 49",
		addresses=[0X5A418AFD],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 50",
		addresses=[0X5A418B05],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 51",
		addresses=[0X5A418B14],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 52",
		addresses=[0X5A418B30],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 53",
		addresses=[0X5A418B37],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Section3 CHEST 54",
		addresses=[0X5A418B3F],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 55",
		addresses=[0X5A418B47],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 56",
		addresses=[0X5A418B4F],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 57",
		addresses=[0X5A417B7E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 58",
		addresses=[0X5A418B5E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 59",
		addresses=[0X5A418B66],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 60",
		addresses=[0X5A418B6F],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 61",
		addresses=[0X5A418B8D],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 62",
		addresses=[0X5A418B96],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 63",
		addresses=[0X5A418B9F],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 64",
		addresses=[0X5A418BA9],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 65",
		addresses=[0X5A418BB2],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 66",
		addresses=[0X5A418BC2],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 67",
		addresses=[0X5A418BCC],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 68",
		addresses=[0X5A418BD5],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 69",
		addresses=[0X5A418BDF],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 70",
		addresses=[0X5A418BE8],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 71",
		addresses=[0X5A418BF8],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 72",
		addresses=[0X5A418C02],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 73",
		addresses=[0X5A418C0B],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 74",
		addresses=[0X5A418C15],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 75",
		addresses=[0X5A418C1E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 76",
		addresses=[0X5A418C2E],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 77",
		addresses=[0X5A418C37],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section3 CHEST 78",
		addresses=[0X5A418C40],
		number_of_bytes=3,
		possible_values=ChooseSection3ChestDrops(),
		is_little_endian=False, ),
	# Valley
	Attribute(
		name="Valley CHEST 1",
		addresses=[0X5A4190D4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 2",
		addresses=[0X5A4190DC],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 3",
		addresses=[0X5A4190E3],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 4",
		addresses=[0X5A4190EB],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 5",
		addresses=[0X5A4190F3],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 6",
		addresses=[0X5A419102],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 7",
		addresses=[0X5A41910A],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 8",
		addresses=[0X5A419112],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 9",
		addresses=[0X5A41911A],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 10",
		addresses=[0X5A419137],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 11",
		addresses=[0X5A419140],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 12",
		addresses=[0X5A419149],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 13",
		addresses=[0X5A419152],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 14",
		addresses=[0X5A41915B],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 15",
		addresses=[0X5A41916B],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 16",
		addresses=[0X5A419174],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 16",
		addresses=[0X5A41917D],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 17",
		addresses=[0X5A419186],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 18",
		addresses=[0X5A41918F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 19",
		addresses=[0X5A41919F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 20",
		addresses=[0X5A4191A8],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 21",
		addresses=[0X5A4191B1],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 22",
		addresses=[0X5A4191BB],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 23",
		addresses=[0X5A4191D9],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 24",
		addresses=[0X5A4191E4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 25",
		addresses=[0X5A4191EF],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 26",
		addresses=[0X5A4191FA],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Valley CHEST 27",
		addresses=[0X5A419205],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 28",
		addresses=[0X5A419217],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 29",
		addresses=[0X5A419222],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 30",
		addresses=[0X5A41922D],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 31",
		addresses=[0X5A419236],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 32",
		addresses=[0X5A41923F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 33",
		addresses=[0X5A419250],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 34",
		addresses=[0X5A41925B],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 35",
		addresses=[0X5A419265],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 36",
		addresses=[0X5A41926F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 37",
		addresses=[0X5A41927A],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 38",
		addresses=[0X5A41928C],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 39",
		addresses=[0X5A419297],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 40",
		addresses=[0X5A4192B6],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 41",
		addresses=[0X5A4192BD],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 42",
		addresses=[0X5A4192C5],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 43",
		addresses=[0X5A4192CD],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 44",
		addresses=[0X5A4192D5],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 45",
		addresses=[0X5A4192E4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 46",
		addresses=[0X5A4192EC],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 47",
		addresses=[0X5A4192F5],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 48",
		addresses=[0X5A419313],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 49",
		addresses=[0X5A41931C],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 50",
		addresses=[0X5A419325],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 51",
		addresses=[0X5A41932E],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 52",
		addresses=[0X5A419337],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 53",
		addresses=[0X5A419347],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Valley CHEST 54",
		addresses=[0X5A419350],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 55",
		addresses=[0X5A419359],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 56",
		addresses=[0X5A419362],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 57",
		addresses=[0X5A41936B],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 58",
		addresses=[0X5A419389],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 59",
		addresses=[0X5A419393],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 60",
		addresses=[0X5A41939D],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 61",
		addresses=[0X5A4193A7],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 62",
		addresses=[0X5A4193B0],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 63",
		addresses=[0X5A418B9F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 64",
		addresses=[0X5A4193C0],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 65",
		addresses=[0X5A4193C9],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 66",
		addresses=[0X5A4193D2],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 67",
		addresses=[0X5A4193DB],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 68",
		addresses=[0X5A4193E4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 69",
		addresses=[0X5A4193F4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 70",
		addresses=[0X5A4193FD],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 71",
		addresses=[0X5A419406],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 72",
		addresses=[0X5A41940F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 73",
		addresses=[0X5A419418],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 74",
		addresses=[0X5A419435],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 75",
		addresses=[0X5A41943E],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 76",
		addresses=[0X5A419447],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 77",
		addresses=[0X5A419450],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 78",
		addresses=[0X5A419459],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Valley CHEST 79",
		addresses=[0X5A419350],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 80",
		addresses=[0X5A419359],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 81",
		addresses=[0X5A419477],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 82",
		addresses=[0X5A419482],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 83",
		addresses=[0X5A41948D],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 84",
		addresses=[0X5A419498],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 85",
		addresses=[0X5A4194A3],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 86",
		addresses=[0X5A4194B5],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 87",
		addresses=[0X5A4194C0],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 88",
		addresses=[0X5A4194CB],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 89",
		addresses=[0X5A4194D4],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 90",
		addresses=[0X5A4194DE],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 91",
		addresses=[0X5A4194F0],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 92",
		addresses=[0X5A4194FA],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 93",
		addresses=[0X5A419505],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 94",
		addresses=[0X5A41950F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 95",
		addresses=[0X5A41951A],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 96",
		addresses=[0X5A41952C],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 97",
		addresses=[0X5A419537],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 98",
		addresses=[0X5A419556],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 99",
		addresses=[0X5A41955F],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 100",
		addresses=[0X5A419568],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 101",
		addresses=[0X5A419571],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Valley CHEST 102",
		addresses=[0X5A41957A],
		number_of_bytes=3,
		possible_values=ChooseValleyChestDrops(),
		is_little_endian=False, ),
	# Veniccio
	Attribute(
		name="Veniccio CHEST 1",
		addresses=[0X5A4198D4],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 2",
		addresses=[0X5A4198DB],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 3",
		addresses=[0X5A4198E3],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 4",
		addresses=[0X5A4198EB],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 5",
		addresses=[0X5A4198F3],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 6",
		addresses=[0X5A419902],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 7",
		addresses=[0X5A41990A],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 8",
		addresses=[0X5A419912],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 9",
		addresses=[0X5A41991A],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 10",
		addresses=[0X5A419922],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 11",
		addresses=[0X5A419931],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 12",
		addresses=[0X5A41994E],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 13",
		addresses=[0X5A419957],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 14",
		addresses=[0X5A419960],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 15",
		addresses=[0X5A419969],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 16",
		addresses=[0X5A419973],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 16",
		addresses=[0X5A419983],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 17",
		addresses=[0X5A41998C],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 18",
		addresses=[0X5A419995],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 19",
		addresses=[0X5A41999E],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 20",
		addresses=[0X5A4199A7],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 21",
		addresses=[0X5A4199B7],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 22",
		addresses=[0X5A4199C0],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 23",
		addresses=[0X5A4199C9],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 24",
		addresses=[0X5A4199D3],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 25",
		addresses=[0X5A4199F2],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 26",
		addresses=[0X5A4199FD],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Veniccio CHEST 27",
		addresses=[0X5A419A08],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 28",
		addresses=[0X5A419A13],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 29",
		addresses=[0X5A419A1E],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 30",
		addresses=[0X5A419A30],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 31",
		addresses=[0X5A419A3B],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 32",
		addresses=[0X5A419A44],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 33",
		addresses=[0X5A419A4E],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 34",
		addresses=[0X5A419A57],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 35",
		addresses=[0X5A419A67],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 36",
		addresses=[0X5A419A72],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 37",
		addresses=[0X5A419A7D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 38",
		addresses=[0X5A419A88],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 39",
		addresses=[0X5A419AA7],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 40",
		addresses=[0X5A419AAE],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 41",
		addresses=[0X5A419AB6],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 42",
		addresses=[0X5A419ABE],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 43",
		addresses=[0X5A419AC6],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 44",
		addresses=[0X5A419AD5],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 45",
		addresses=[0X5A419ADD],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 46",
		addresses=[0X5A419AE5],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 47",
		addresses=[0X5A419B02],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 48",
		addresses=[0X5A419B0B],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 49",
		addresses=[0X5A419B14],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 50",
		addresses=[0X5A419B1D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 51",
		addresses=[0X5A419B26],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 52",
		addresses=[0X5A419B44],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 53",
		addresses=[0X5A419B4D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Veniccio CHEST 54",
		addresses=[0X5A419B56],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 55",
		addresses=[0X5A419B5F],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 56",
		addresses=[0X5A419B69],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 57",
		addresses=[0X5A419B79],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 58",
		addresses=[0X5A419B82],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 59",
		addresses=[0X5A419B8B],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 60",
		addresses=[0X5A419B94],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 61",
		addresses=[0X5A419B9D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 62",
		addresses=[0X5A419BAD],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 63",
		addresses=[0X5A419BCB],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 64",
		addresses=[0X5A419BD4],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 65",
		addresses=[0X5A419BDD],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 66",
		addresses=[0X5A419BE6],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 67",
		addresses=[0X5A419BEF],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 68",
		addresses=[0X5A419BFF],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 69",
		addresses=[0X5A419C08],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 70",
		addresses=[0X5A419C11],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 71",
		addresses=[0X5A419C1A],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 72",
		addresses=[0X5A419C23],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 73",
		addresses=[0X5A419C41],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 74",
		addresses=[0X5A419C4C],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 75",
		addresses=[0X5A419C57],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 76",
		addresses=[0X5A419C62],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 77",
		addresses=[0X5A419C6D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 78",
		addresses=[0X5A419C7F],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Veniccio CHEST 79",
		addresses=[0X5A419C8A],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 80",
		addresses=[0X5A419C93],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 81",
		addresses=[0X5A419C9D],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 82",
		addresses=[0X5A419CA6],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 83",
		addresses=[0X5A419CB8],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 84",
		addresses=[0X5A419CC3],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 85",
		addresses=[0X5A419CCE],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 86",
		addresses=[0X5A419CED],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 87",
		addresses=[0X5A419CF6],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 88",
		addresses=[0X5A419CFF],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 89",
		addresses=[0X5A419D08],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Veniccio CHEST 90",
		addresses=[0X5A419D11],
		number_of_bytes=3,
		possible_values=ChooseVeniccioChestDrops(),
		is_little_endian=False, ),
	# Heim
	Attribute(
		name="Heim CHEST 1",
		addresses=[0X5A41A0D8],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 2",
		addresses=[0X5A41A0DE],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 3",
		addresses=[0X5A41A0E5],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 4",
		addresses=[0X5A41A0ED],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 5",
		addresses=[0X5A41A0F5],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 6",
		addresses=[0X5A41A104],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 7",
		addresses=[0X5A41A10C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 8",
		addresses=[0X5A41A114],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 9",
		addresses=[0X5A41A11C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 10",
		addresses=[0X5A41A123],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 11",
		addresses=[0X5A41A132],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 12",
		addresses=[0X5A41A139],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 13",
		addresses=[0X5A41A141],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 14",
		addresses=[0X5A41A149],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 15",
		addresses=[0X5A41A151],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 16",
		addresses=[0X5A41A160],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 16",
		addresses=[0X5A41A17C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 17",
		addresses=[0X5A41A185],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 18",
		addresses=[0X5A41A18E],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 19",
		addresses=[0X5A41A197],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 20",
		addresses=[0X5A41A1A0],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 21",
		addresses=[0X5A41A1B0],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 22",
		addresses=[0X5A41A1B9],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 23",
		addresses=[0X5A41A1C2],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 24",
		addresses=[0X5A41A1CB],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 25",
		addresses=[0X5A41A1D4],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 26",
		addresses=[0X5A41A1E4],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Heim CHEST 27",
		addresses=[0X5A41A202],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 28",
		addresses=[0X5A41A20C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 29",
		addresses=[0X5A41A217],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 30",
		addresses=[0X5A41A217],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 31",
		addresses=[0X5A41A22D],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 32",
		addresses=[0X5A41A23F],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 33",
		addresses=[0X5A41A24A],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 34",
		addresses=[0X5A41A254],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 35",
		addresses=[0X5A41A25E],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 36",
		addresses=[0X5A41A268],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 37",
		addresses=[0X5A41A27A],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 38",
		addresses=[0X5A41A285],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 39",
		addresses=[0X5A41A290],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 40",
		addresses=[0X5A41A2AF],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 41",
		addresses=[0X5A41A2B6],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 42",
		addresses=[0X5A41A2BE],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 43",
		addresses=[0X5A41A2C6],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 44",
		addresses=[0X5A41A2CE],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 45",
		addresses=[0X5A41A2DD],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 46",
		addresses=[0X5A41A2FA],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 47",
		addresses=[0X5A41A303],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 48",
		addresses=[0X5A41A30C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 49",
		addresses=[0X5A41A315],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 50",
		addresses=[0X5A41A31E],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 51",
		addresses=[0X5A41A33C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 52",
		addresses=[0X5A41A345],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 53",
		addresses=[0X5A41A34F],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Heim CHEST 54",
		addresses=[0X5A41A358],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 55",
		addresses=[0X5A41A361],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 56",
		addresses=[0X5A41A371],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 57",
		addresses=[0X5A41A37A],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 58",
		addresses=[0X5A41A383],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 59",
		addresses=[0X5A41A38C],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 60",
		addresses=[0X5A41A395],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 61",
		addresses=[0X5A41A3A5],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 62",
		addresses=[0X5A41A3C3],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 63",
		addresses=[0X5A41A3CC],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 64",
		addresses=[0X5A41A3D5],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 65",
		addresses=[0X5A41A3DE],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 66",
		addresses=[0X5A41A3E7],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 67",
		addresses=[0X5A41A3F7],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 68",
		addresses=[0X5A41A400],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 69",
		addresses=[0X5A41A409],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 70",
		addresses=[0X5A41A412],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 71",
		addresses=[0X5A41A41B],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 72",
		addresses=[0X5A41A439],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 73",
		addresses=[0X5A41A444],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 74",
		addresses=[0X5A41A44F],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 75",
		addresses=[0X5A41A45A],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 76",
		addresses=[0X5A41A465],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 77",
		addresses=[0X5A41A477],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 78",
		addresses=[0X5A41A480],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Heim CHEST 79",
		addresses=[0X5A41A48A],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 80",
		addresses=[0X5A41A494],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 81",
		addresses=[0X5A41A49F],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 82",
		addresses=[0X5A41A4B1],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 83",
		addresses=[0X5A41A4BC],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 84",
		addresses=[0X5A41A4DB],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 85",
		addresses=[0X5A41A4E4],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 86",
		addresses=[0X5A41A4ED],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 87",
		addresses=[0X5A41A4F6],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Heim CHEST 88",
		addresses=[0X5A41A4FF],
		number_of_bytes=3,
		possible_values=ChooseHeimChestDrops(),
		is_little_endian=False, ),
	# Moon
	Attribute(
		name="Moon CHEST 1",
		addresses=[0X5A41A8D2],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 2",
		addresses=[0X5A41A8DC],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 3",
		addresses=[0X5A41A8E5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 4",
		addresses=[0X5A41A8EE],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 5",
		addresses=[0X5A41A8F7],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 6",
		addresses=[0X5A41A908],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 7",
		addresses=[0X5A41A912],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 8",
		addresses=[0X5A41A91B],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 9",
		addresses=[0X5A41A924],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 10",
		addresses=[0X5A41A92D],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 11",
		addresses=[0X5A41A93D],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 12",
		addresses=[0X5A41A946],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 13",
		addresses=[0X5A41A94F],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 14",
		addresses=[0X5A41A958],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 15",
		addresses=[0X5A41A961],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 16",
		addresses=[0X5A41A971],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 16",
		addresses=[0X5A41A97A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 17",
		addresses=[0X5A41A983],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 18",
		addresses=[0X5A41A98D],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 19",
		addresses=[0X5A41A996],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 20",
		addresses=[0X5A4179BD],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 21",
		addresses=[0X5A41A9A7],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 22",
		addresses=[0X5A41A9C6],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 23",
		addresses=[0X5A41A9CD],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 24",
		addresses=[0X5A41A9D5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 25",
		addresses=[0X5A41A9DD],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 26",
		addresses=[0X5A41A9E5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Moon CHEST 27",
		addresses=[0X5A41A9F4],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 28",
		addresses=[0X5A41A9FC],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 29",
		addresses=[0X5A41AA04],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 30",
		addresses=[0X5A41AA0C],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 31",
		addresses=[0X5A41AA15],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 32",
		addresses=[0X5A41AA31],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 33",
		addresses=[0X5A41AA3B],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 34",
		addresses=[0X5A41AA44],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 35",
		addresses=[0X5A41AA4D],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 36",
		addresses=[0X5A41AA57],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 37",
		addresses=[0X5A41AA68],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 38",
		addresses=[0X5A41AA71],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 39",
		addresses=[0X5A41AA7B],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 40",
		addresses=[0X5A41AA9A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 41",
		addresses=[0X5A41AAA5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 42",
		addresses=[0X5A41AAB0],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 43",
		addresses=[0X5A41AABB],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 44",
		addresses=[0X5A41AAC6],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 45",
		addresses=[0X5A41AAD8],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 46",
		addresses=[0X5A41AAE3],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 47",
		addresses=[0X5A41AAEE],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 48",
		addresses=[0X5A41AAF9],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 49",
		addresses=[0X5A41AB04],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 50",
		addresses=[0X5A41AB16],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 51",
		addresses=[0X5A41AB21],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 52",
		addresses=[0X5A41AB2C],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 53",
		addresses=[0X5A41AB37],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Moon CHEST 54",
		addresses=[0X5A41AB42],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 55",
		addresses=[0X5A41AB54],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 56",
		addresses=[0X5A41AB73],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 57",
		addresses=[0X5A41AB7A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 58",
		addresses=[0X5A41AB82],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 59",
		addresses=[0X5A41AB8A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 60",
		addresses=[0X5A41AB92],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 61",
		addresses=[0X5A41ABA1],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 62",
		addresses=[0X5A41ABA9],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 63",
		addresses=[0X5A41ABC6],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 64",
		addresses=[0X5A41ABD0],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 65",
		addresses=[0X5A41ABD9],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 66",
		addresses=[0X5A41ABE2],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 67",
		addresses=[0X5A41ABEC],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 68",
		addresses=[0X5A41ABFD],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 69",
		addresses=[0X5A41AC06],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 70",
		addresses=[0X5A41AC0F],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 71",
		addresses=[0X5A41AC18],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 72",
		addresses=[0X5A41AC21],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 73",
		addresses=[0X5A41AC31],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 74",
		addresses=[0X5A41AC3A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 75",
		addresses=[0X5A41AC43],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 76",
		addresses=[0X5A41AC4C],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 77",
		addresses=[0X5A41AC55],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 78",
		addresses=[0X5A41AC65],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 79",
		addresses=[0X5A41AC6E],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 80",
		addresses=[0X5A41AC78],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Moon CHEST 81",
		addresses=[0X5A41AC81],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 82",
		addresses=[0X5A41AC8B],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 83",
		addresses=[0X5A41ACAA],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 84",
		addresses=[0X5A41ACB3],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 85",
		addresses=[0X5A41ACBC],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 86",
		addresses=[0X5A41ACC5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 87",
		addresses=[0X5A41ACCE],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 88",
		addresses=[0X5A41ACDE],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 89",
		addresses=[0X5A41ACE7],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 90",
		addresses=[0X5A41ACF0],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 91",
		addresses=[0X5A41ACF9],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 92",
		addresses=[0X5A41AD02],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 93",
		addresses=[0X5A41AD20],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 94",
		addresses=[0X5A41AD2B],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 95",
		addresses=[0X5A41AD36],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 96",
		addresses=[0X5A41AD41],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 97",
		addresses=[0X5A41AD4C],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 98",
		addresses=[0X5A41AD5E],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 99",
		addresses=[0X5A41AD69],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 100",
		addresses=[0X5A41AD72],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 101",
		addresses=[0X5A41AD7D],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 102",
		addresses=[0X5A41AD88],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 103",
		addresses=[0X5A41AD9A],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 104",
		addresses=[0X5A41ADA5],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 105",
		addresses=[0X5A41ADB0],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 106",
		addresses=[0X5A41ADBB],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Moon CHEST 107",
		addresses=[0X5A41ADC6],
		number_of_bytes=3,
		possible_values=ChooseMoonChestDrops(),
		is_little_endian=False, ),
	# Zelmite
	Attribute(
		name="Zelmite CHEST 1",
		addresses=[0X5A41B0DA],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 2",
		addresses=[0X5A41B0E4],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 3",
		addresses=[0X5A41B0EE],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 4",
		addresses=[0X5A41B0F8],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 5",
		addresses=[0X5A41B102],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 6",
		addresses=[0X5A41B113],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 7",
		addresses=[0X5A41B11D],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 8",
		addresses=[0X5A41B127],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 9",
		addresses=[0X5A41B131],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 10",
		addresses=[0X5A41B13B],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 11",
		addresses=[0X5A41B14C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 12",
		addresses=[0X5A41B156],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 13",
		addresses=[0X5A41B160],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 14",
		addresses=[0X5A41B16A],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 15",
		addresses=[0X5A41B173],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 16",
		addresses=[0X5A41B184],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 16",
		addresses=[0X5A41A97A],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 17",
		addresses=[0X5A41B198],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 18",
		addresses=[0X5A41B1A2],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 19",
		addresses=[0X5A41B1AC],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 20",
		addresses=[0X5A41B1BD],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 21",
		addresses=[0X5A41B1C7],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 22",
		addresses=[0X5A41B1D1],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 23",
		addresses=[0X5A41B1F0],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 24",
		addresses=[0X5A41B1F7],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 25",
		addresses=[0X5A41B1FF],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 26",
		addresses=[0X5A41B207],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Zelmite CHEST 27",
		addresses=[0X5A41B20F],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 28",
		addresses=[0X5A41B21E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 29",
		addresses=[0X5A41B226],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 30",
		addresses=[0X5A41B22E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 31",
		addresses=[0X5A41B236],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 32",
		addresses=[0X5A41B23E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 33",
		addresses=[0X5A41B24D],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 34",
		addresses=[0X5A41B255],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 35",
		addresses=[0X5A41B25E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 36",
		addresses=[0X5A41B27C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 37",
		addresses=[0X5A41B285],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 38",
		addresses=[0X5A41B28E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 39",
		addresses=[0X5A41B297],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 40",
		addresses=[0X5A41B2A0],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 41",
		addresses=[0X5A41B2B0],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 42",
		addresses=[0X5A41B2B9],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 43",
		addresses=[0X5A41B2C2],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 44",
		addresses=[0X5A41B2CB],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 45",
		addresses=[0X5A41B2D4],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 46",
		addresses=[0X5A41B2E4],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 47",
		addresses=[0X5A41B2ED],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 48",
		addresses=[0X5A41B2F6],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 49",
		addresses=[0X5A41B2FF],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 50",
		addresses=[0X5A41B31D],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 51",
		addresses=[0X5A41B326],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 52",
		addresses=[0X5A41B32F],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 53",
		addresses=[0X5A41B338],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Zelmite CHEST 54",
		addresses=[0X5A41B341],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 55",
		addresses=[0X5A41AB54],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 56",
		addresses=[0X5A41B35A],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 57",
		addresses=[0X5A41B363],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 58",
		addresses=[0X5A41B36C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Zelmite CHEST 59",
		addresses=[0X5A41B375],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	# Zelmite
	Attribute(
		name="Section8 CHEST 1",
		addresses=[0X5A41B8DA],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 2",
		addresses=[0X5A41B8E4],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 3",
		addresses=[0X5A41B8EE],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 4",
		addresses=[0X5A41B8F8],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 5",
		addresses=[0X5A41B902],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 6",
		addresses=[0X5A41B913],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 7",
		addresses=[0X5A41B91D],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 8",
		addresses=[0X5A41B927],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 9",
		addresses=[0X5A41B931],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 10",
		addresses=[0X5A41B93B],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 11",
		addresses=[0X5A41B94C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 12",
		addresses=[0X5A41B956],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 13",
		addresses=[0X5A41B960],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 14",
		addresses=[0X5A41B96A],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 15",
		addresses=[0X5A41B973],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 16",
		addresses=[0X5A41B984],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 16",
		addresses=[0X5A41B98E],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 17",
		addresses=[0X5A41B998],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 18",
		addresses=[0X5A41B9A2],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 19",
		addresses=[0X5A41B9AC],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 20",
		addresses=[0X5A41B9BD],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 21",
		addresses=[0X5A41B9C7],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 22",
		addresses=[0X5A41B9D1],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 23",
		addresses=[0X5A41B9F0],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 24",
		addresses=[0X5A41B9F7],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 25",
		addresses=[0X5A41B9FE],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 26",
		addresses=[0X5A41BA05],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	#
	Attribute(
		name="Section8 CHEST 27",
		addresses=[0X5A41BA0D],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 28",
		addresses=[0X5A41BA1C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 29",
		addresses=[0X5A41BA24],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 30",
		addresses=[0X5A41BA2C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 31",
		addresses=[0X5A41BA34],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 32",
		addresses=[0X5A41BA3C],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 33",
		addresses=[0X5A41BA4B],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 34",
		addresses=[0X5A41BA53],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 35",
		addresses=[0X5A41BA5B],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 36",
		addresses=[0X5A41BA63],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 37",
		addresses=[0X5A41BA6B],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 38",
		addresses=[0X5A41BA7A],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 39",
		addresses=[0X5A41BA82],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 40",
		addresses=[0X5A41BA9F],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 41",
		addresses=[0X5A41BAA8],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 42",
		addresses=[0X5A41BAB1],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 43",
		addresses=[0X5A41BABA],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 44",
		addresses=[0X5A41BAC3],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 45",
		addresses=[0X5A41BAD3],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 46",
		addresses=[0X5A41BADC],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 47",
		addresses=[0X5A41BAE5],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 48",
		addresses=[0X5A41BAEE],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 49",
		addresses=[0X5A41BAF7],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 50",
		addresses=[0X5A41BB07],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 51",
		addresses=[0X5A41BB10],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 52",
		addresses=[0X5A41BB19],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
	Attribute(
		name="Section8 CHEST 53",
		addresses=[0X5A41BB22],
		number_of_bytes=3,
		possible_values=ChooseZelmiteChestDrops(),
		is_little_endian=False, ),
]
Required_Rules = [

]

Optional_Rulesets = [

]