""" Complete the story with adjetives and nouns 
that first come to your mind.
Let's see how much creative you are!
Have FUN!!!
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs has stsrted. Enjoy!!!"
name = raw_input("Enter your name: ")
adjetive1 = raw_input("Enter a feeling: ")
adjetive2 = raw_input("Enter an adjetive: ")
adjetive3 = raw_input("Enter a different adjective: ")
verb1 = raw_input("Enter a verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")
animal = raw_input("Enter your favorite animal: ")
food = raw_input("Enter your favorite food: ")
fruit = raw_input("Enter your favorite fruit: ")
superhero = raw_input("Enter your favorite superhero: ")
country = raw_input("Enter a coutry you will like to visit: ")
dessert = raw_input("Enter your favorite dessert: ")
year = raw_input("Enter the year you were born: ")

print STORY %(name, adjetive1, adjetive2, animal, food, verb1, noun1, fruit, adjetive3, name, superhero, name, country, name, dessert, name, year, noun2)

























