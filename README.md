# Dark-Chronicle-Randomiser

#I'm terrible at creating randomisers, and UI's, so apologies to start.

--------------------------------
#How to Use

1. Run the .exe and click on "Load File" button, finding your DC2 rom ( I know this works with USA rom https://cdromance.com/ps2-iso/dark-cloud-2-usa/)
   Version 2, if you use Version 1 some stuff may not work
   Your Window may freeze, and take a minute or more to actually randomise, as there is a lot of stuff to change in the 4GB rom, but it'll work.
   
* Because I'm unable to create a UI properly, If you want to change the Min MAX value of the enemies for a hard/easy mode playthrough, you can edit directly the randomizer.py file, the Seed Functionality probably doesn't work either, sorry.
* Edit in notepad, find the #CHANGE ME# section near the top and change the MIN/MAX values (defaulted to 100).

Example:
80 for Min would mean that the lowest value it can have is 80% of its normal base value
120 for Max would mean that the highest value it can is 120% of its normal base value.
If you put a higher min value than the max value, it will probably break, please don't.
Be careful with spaces and other things you change in the rom, because if you change anything that breaks it, you'll get "valid randomizer.py file not found error"

---------------------------------------

Things that are Rando'd (All are Optional):
* All Dungeon Monsters's stats ( HP, ABS, GILDA, ATK, DEF, DROPS)
* All Dungeon Chests ( For balance, it's not truly random, you can't get dark chronicle weapon in the first dungeon for example, its usually about within 2 chapters items-ish)
* All Shops ( Is truly random, balanced around price, may make a balanced mode for this, Cedrics shop is excluded as it uses EXP for price)
* All Weapons have Max Stat gains of 999 (Yes even the spheda clubs, although some only have 99 atk and durability due to space given to the value in the rom)


# due to the way ive coded it without foresight, if you want to remove shop randomisation, put /* # on the line before the line that has "# START OF SHOPS"
# and */ on the line before "#END OF SHOPS"
# same with the lines # START DUNGEON CHEST DROPS

Changes I'd like to make, if i could figure out how to do them (someone please help me)
* Rando follower abilities/ability points
* Buff Monicas monsters, because they suck ( or increase EXP gain for it)
* Rando inventions ( So that 2/3 of the components are the same, but 1/3 is different so it isnt crazy), possibly rando photos instead.
* Change Whether it's a Sealed Dungeon or not.

Special Thanks to GateGuy for making the SRM, even if i'm not using it properly. 
Simple Randomizer Maker https://github.com/Mips96/SimpleRandomizerMaker/releases

contact me on alastorlion@hotmail.co.uk if you want to help/if there are any issues.
Alternatively you can post an issue here
