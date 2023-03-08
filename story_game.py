user_name = input ("what is name ? :")
begins = input("Are u ready for the Game, TYPE yes or no? ").lower()
if begins == "yes":
    print("Then Try to win...")
elif begins == "no":
    print("get lost")
    quit()
else:
    print("Type only yes or no")

story_one = input('There is a fight going on road. you have two option 1.fight or 2.run ?').lower()

if story_one == "fight": 
        print("wrong choice..they have knocked u out")
        quit()

elif story_one == "run":
        print ("smart one u have survived")

story_two = input("heyy buddy now u seen a beautiful girl what are u going to do ? Talk with her are pass her?").lower()

if story_two == "talk":
    print("she ignored u..You idiot")
    quit()
elif story_two == 'pass':
    print("my man ! you have my respect, see u in next level")



