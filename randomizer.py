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
#Variables
Change_HP = True
Min_HP_Range = 50
Max_HP_Range = 150

Change_ABS = True
Min_ABS_Range = 50
Max_ABS_Range = 1500

Change_GILDA = True
Min_GILDA_Range = 50
Max_GILDA_Range = 1500

Change_ATK = True
Min_ATK_Range = 50
Max_ATK_Range = 1500

Change_DEF = True
Min_DEF_Range = 150
Max_DEF_Range = 150

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
? Price and Shops Set 14 = 9B5E000
? Price and Shops Set 14 = 9B61000


Chapter 1 Prices and Shops? = 9B4E800

Shop 0 = Milane's Weapon Shop
Shop 1 = Polly's Bakery
Shop 2 = Dell's Clinic
Shop 3 = Ferdinand's Takeout
Shop 4 = Morton's Sundries
Shop 5 = Starlight Temple
Shop 6 = Donny Mart
Shop 7 = Borneo's Fine Ore
Shop 8 = Gordon's Bonsai
Shop 9 = Parn's Paints
Shop 10 = Claire's Place


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

####################################################### ChooseSewerItems

def ChooseSewerItems():

	x = random.randint(0, 100)

	if 0 <= x <= 39:
		item_number = 0
	elif 40 <= x <= 69:
		item_number = random.choice(tier1items)
	elif 70 <= x <= 89:
		item_number = random.choice(tierattachments)
	elif 90 <= x <= 97:
		item_number = random.choice(tier1weaponsmax + tier1weaponsmonica + tier1ridepod)
	elif 98 <= x <= 100:
		item_number = random.choice(tier2weaponsmax + tier2weaponsmonica + tier2ridepod + tiergems + tiercoins)
	return [item_number]

####################################################### ChooseSewerItems

Attributes = [
Attribute(
		name="BAT HP",
		addresses=[0x2ff910],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(22),
		max_value=Max_HP_Multiplier(22),
		is_little_endian=True,),
	Attribute(
		name="BAT ABS",
		addresses=[0x2ff916],
		number_of_bytes=2,
		min_value=Min_ABS_Multiplier(6),
		max_value=Max_ABS_Multiplier(6),
		is_little_endian=True,),
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
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="BAT ITEM2",
		addresses=[0x2ff962],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="BAT ITEM3",
		addresses=[0x2ff964],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
#SEWER RAT
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
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ITEM2",
		addresses=[0x2F3302],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="SEWER RAT ITEM3",
		addresses=[0x2F3304],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
#BEACH RAT
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
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ITEM2",
		addresses=[0x2f33ba],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
	Attribute(
		name="BEACH RAT ITEM3",
		addresses=[0x2f33bc],
		number_of_bytes=2,
		possible_values=ChooseSewerItems(),
		is_little_endian=True, ),
]
Required_Rules = [

]

Optional_Rulesets = [

]