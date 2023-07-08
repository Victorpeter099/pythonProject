#Building a mad lib game
print("Roses are red")
print("violets are blue")
print("i love you")

color = input ("Enter a color: ")
plural_noun = input ("Enter a Plural Noun: ")
celebrity = input ("Enter a Celebrity: ")
print( "Roses are " + color )
print( plural_noun + " are blue")
print("i love " + celebrity )

#New task for a mad lib assignment.
Food = input("Enter a type of food: ")
Name = input("Enter a girl's name: ")
name = input("enter another name: ")
Adjective = input("enter an adjective: ")
noun = input("enter another noun: ")
Noun = input("Enter a noun: ")
verb_1 = input("enter a verb_1: ")
verb_2 = input("enter another verb_2: ")
verb_3 = input("enter a third verb_3: ")

story = " it was" + Food + " day at school, and" + Name + " was super" + Adjective + \
        " for lunch but when she went outside to eat, a" + Noun + " stole her food"\
        + Food + Name + " chased the" + Noun + " all over school."\
        " she" + verb_1 + " ," + verb_2 + " and" + verb_3 + " through the playground."\
        " Then she tripped on her" + noun + " and the" + Noun + " escaped!"\
        " Luckily" + name + " 's friends were willing to share their" + Food + " with her."
print(story)