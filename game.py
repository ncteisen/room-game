import time
import random

def ur():
    user_response = raw_input("> ")
    return user_response

def inv(inv):
    print "\nHere is your hand;"
    print "\t",
    print inv,
    print "\n"
    

def confused():
    rand = random.randrange(1,8)
    if rand == 1:
        print "\nUh... don't do that\n"
    elif rand == 2:
        print "\nNo, I don't think that will work\n"
    elif rand == 3:
        print "\nTry again\n"
    elif rand == 4:
        print "\nThink of something else to try\n"
    elif rand == 5:
        print "\nNo, that won't do\n"
    elif rand == 6:
        print "\nRemember, you can always type help\n"
    elif rand == 7:
        print "\nHmm, seems like you need use the help command\n"
    elif rand == 8:
        print "\nI have a hot tip that the help command is really useful\n"


def start():
    print """
Welcome. The journey ahead of you is tough, but with determination
you will succeed. Try to use simple text commands to work through
each puzzle. My hint would be to start each puzzle by looking around
with the command 'look'. After that, keep your commands as simple as
possible; use words like 'examine <object>' and 'take <object>' and
so on. Remember, those are just examples, the command words can be
anything if you are ever confused, try typing 'help'
"""
    room1()

#########################################################################

def room1():
    resp = ur()
    if resp == "look": 
        print """
You find yourself in a small dark room. It smells a little moldy,
and you see some water pooled in dark puddle on the floor. There
are no windows. You see one small door in front of you.
"""
        room1()
    elif "door" in resp:
        print """
The door creaks open. You duck down and shuffle into the next room
"""
        room2()
    elif "window" in resp:
        print "\nThere is no window you fool\n"
        room1()
    elif "puddle" in resp or "water" in resp:
        print "\nNo, that's disgusting\n"
        room1()
    elif "help" in resp:
        print "\nKISS; Keep It Simple Stupid\n"
        room1()
    else:
        confused()
        room1()

#########################################################################

def room2():
    note = False #true is user has note
    examined = False
    key = False
    inventory = []
    while True:
        
        resp = ur()
        
        if "examine" in resp and " bed" in resp:
            print """
There are three ants, a spider, and a note under the bed
"""
            examined = True
            
        elif "search" in resp and "bed" in resp:
            print """
There are three ants, a spider, and a note under the bed
"""
            examined = True
            
        elif "look" in resp and "bed" in resp:
            print """
There are three ants, a spider, and a note under the bed
"""
            examined = True
            
        elif "look" in resp and "note" in resp:
            if note == True:
                print """
The note says, "introspection is the key to living a happy life"
"""
            else:
                print """
What note? The one under the bed? It's still there, you have to
pick it up before you use it you philistine
"""
                
        elif "read" in resp and "note" in resp:
            if note == True:
                print """
The note says, "introspection is the key to living a happy life"
"""
            else:
                print """
What note? The one under the bed? It's still there, you have to
pick it up before you use it you philistine
"""
                
        elif "examine" in resp and "note" in resp:
            if note == True:
                print """
The note says, "introspection is the key to living a happy life"
"""
            else:
                print """
What note? The one under the bed? It's still there, you have to
pick ut up before you use it you philistine
"""
                
        elif "take" in resp and "note" in resp:
            if note == False:
                print """
The note is now in your hand and you can interact with it. See what's in
your hand with the command 'hand'
"""
                inventory = "note"
                note = True
            else:
                print "\nYou already have the note\n"
                
        elif "pick up" in resp and "note" in resp:
            if note == False:
                print """
The note is now in your hand and you can interact with it. See what's in
your hand with the command 'hand'
"""
                note = True
                inventory = "note"
            else:
                print "\nYou already have the note\n"
                
        elif resp == "hand":
            inv(inventory)
            
        elif resp == "look":
            print """
You are now in a room slightly bigger than last. The smell has gotten
noticably stronger, and now the walls are stained with a green, slimy
substance. There is a door in front of you and small, dirty bed in the
corner
"""
            
        elif "go" in resp and "back" in resp:
            print "\nOk\n"
            room1()
            
        elif "door" in resp:
            if key == True:
                print """
The door opens with a satisfying click, and swings inward silently. You
walk through the doorway into the next room
"""
                room3()
            else:
                print """
It's locked you jerk. Did you really think that this room would be as
easy as the last room?
"""
                
        elif "examine" in resp and "self" in resp:
            print """
As you search your deep and inner psyche, you feel a sudden pressure in
your pocket. You reach in and alas, there is a small key. It is now in
your hand
"""
            key = True
            inventory = "key"
            
        elif "look" in resp and "mind" in resp:
            print """
As you search your deep and inner psyche, you feel a sudden pressure in
your pocket. You reach in and alas, there is a small key. It is now in
your hand
"""
            key = True
            inventory = "key"

        elif "sleep" in resp:
            print """
You lie down on the plank-like mattress and shut your eyes. As you will
yourself to fall into the comfort of a dream, a bug scurries over your
leg and bites it. You jump off the bed; sleeping probably isn't the best
idea right now
"""
            
        elif "examine" in resp and "slime" in resp:
            print "\nEw, that's disgusting. No\n"
            
        elif "help" in resp:
            if key == False and note == False and examined == False:
                print """
Try examining different things in the room to see what is there
"""
            elif key == False and note == False:
                print """
You must pick items up to use them
"""
            elif key == False:
                print """
What must you examine in order to be introspective?
"""
            else:
                print "\nCome on, this one's easy\n"
                
        elif "introspect" in resp:
            print """
As you search your deep and inner psyche, you feel a sudden pressure in
your pocket. You reach in and alas, there is a small key. It is now in
your hand
"""
            key = True
            inventory = "key"
            
        else:
            confused()

#########################################################################

def room3():
    # initialize bools
    is_open = False
    cd = False
    cd_broken = False
    cut = False
    hand = "nothing"

    while True:

        resp = ur()
    
    #conditionals
        if "examine" in resp and "walkman" in resp:
            print """
The walkman appears to be a 1995 model with a Marvin Gaye CD inside
"""
        elif "play" in resp and "music" in resp:
               print """
The room fills with the slow and sensual rythms of Mr. Gaye. This pulsing
beat is making you feel things you haven't felt in years, and you begin
to swoon and sway with the melody. Then you realize that you are in some
creepy dungeon with weird rooms and puzzles and you have no idea why, and
this thought sobers you up pretty quickly
"""
        elif "play" in resp and "walkman" in resp:
            print """
The room fills with the slow and sensual rythms of Mr. Gaye. This pulsing
beat is making you feel things you haven't felt in years, and you begin
to swoon and sway with the melody. Then you realize that you are in some
creepy dungeon with weird rooms and puzzles and you have no idea why, and
this thought sobers you up pretty quickly
"""
        elif "start" in resp and "music" in resp:
            print """
The room fills with the slow and sensual rythms of Mr. Gaye. This pulsing
beat is making you feel things you haven't felt in years, and you begin
to swoon and sway with the melody. Then you realize that you are in some
creepy dungeon with weird rooms and puzzles and you have no idea why, and
this thought sobers you up pretty quickly
"""
        elif "press" in resp and "play" in resp:
            print """
The room fills with the slow and sensual rythms of Mr. Gaye. This pulsing
beat is making you feel things you haven't felt in years, and you begin
to swoon and sway with the melody. Then you realize that you are in some
creepy dungeon with weird rooms and puzzles and you have no idea why, and
this thought sobers you up pretty quickly
"""
        elif "listen" in resp:
            print """
The room fills with the slow and sensual rythms of Mr. Gaye. This pulsing
beat is making you feel things you haven't felt in years, and you begin
to swoon and sway with the melody. Then you realize that you are in some
creepy dungeon with weird rooms and puzzles and you have no idea why, and
this thought sobers you up pretty quickly
"""
        elif "open" in resp and "walkman" in resp:
            print "\nYou open the walkman\n"
            is_open = True
        elif "examine" in resp and "wall" in resp:
            print """
As you examine the wall, it begins to fade away an--
NOT. It's just a simple wall
"""
        elif "examine" in resp and "blood" in resp:
            print  "\nIt's blood\n"
        elif "examine" in resp and "message" in resp:
            print "\nIt seems to be written in blood\n"
        elif "examine" in resp and "writing" in resp:
            print "\nIt seems to be written in blood\n"
        elif "examine" in resp and "poem" in resp:
            print "\nIt seems to be written in blood\n"
        elif "take" in resp and "cd" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "take" in resp and "CD" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "pick up" in resp and "cd" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "pick up" in resp and "CD" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "remove" in resp and "CD" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "remove" in resp and "cd" in resp:
            if is_open == True:
                print "\nThe CD is now in your hand\n"
                cd = True
                hand = "CD"
            else:
                print """
You can't. It seems to be in a walkman or something. I wish you could open the walkman...
"""
        elif "break" in resp and "cd" in resp:
            if hand == "CD":
                print """
The CD breaks easily, leaving two jagged and sharp semicircular pieces of
plastic in your hand
"""
                cd_broken = True
                hand = "broken CD"
            else:
                print "\nDo you have a CD in your hand? didn't think so\n"
        elif "snap" in resp and "CD" in resp:
            if hand == "CD":
                print """
The CD breaks easily, leaving two jagged and sharp semicircular pieces of
plastic in your hand
"""
                cd_broken = True
                hand = "broken CD"
            else:
                print "\nDo you have a CD in your hand? didn't think so\n"
        elif "break" in resp and "CD" in resp:
            if hand == "CD":
                print """
The CD breaks easily, leaving two jagged and sharp semicircular pieces of
plastic in your hand
"""
                cd_broken = True
                hand = "broken CD"
            else:
                print "\nDo you have a CD in your hand? didn't think so\n"
        elif "snap" in resp and "CD" in resp:
            if hand == "CD":
                print """
The CD breaks easily, leaving two jagged and sharp semicircular pieces of
plastic in your hand
"""
                cd_broken = True
                hand = "broken CD"
            else:
                print "\nDo you have a CD in your hand? didn't think so\n"
        elif "cut" in resp and "your" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "your" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "cut" in resp and "self" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "self" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "cut" in resp and "arm" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "cut" in resp and "finger" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "arm" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "cut" in resp and "hand" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "hand" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "cut" in resp and "leg" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "leg" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "slice" in resp and "finger" in resp:
            if hand == "broken CD":
                print "\nYou make the cut and the blood starts dripping onto the floor\n"
            else:
                print "\nThere is nothing in your hand that is sharp enough to do that. Try again\n"
            cut = True
        elif "sign" in resp and "wall" in resp:
            if cut == True:
                print """
As you sign your name on the wall, you hear a hissing behind you. You turn
just in time to see a part of the wall slide down into the floor, leaving
a path  to the next room. You gingerly step through
"""
                room4()
            else:
                print """
But you have nothing with which to sign the wall! (yet)
"""
        elif "sign" in resp and "note" in resp:
            if cut == True:
                print """
As you sign your name on the wall, you hear a hissing behind you. You turn
just in time to see a part of the wall slide down into the floor, leaving
a path  to the next room. You gingerly step through
"""
                room4()
            else:
                print """
But you have nothing with which to sign the wall! (yet)
"""
        elif "write" in resp and "name" in resp and "wall" in resp:
            if cut == True:
                print """
As you sign your name on the wall, you hear a hissing behind you. You turn
just in time to see a part of the wall slide down into the floor, leaving
a path  to the next room. You gingerly step through
"""
                room4()
            else:
                print """
But you have nothing with which to sign the wall! (yet)
"""
        elif resp == "hand":
            inv(hand)
        elif "help2" in resp:
            if cut == False:
                print "\nThe key words from the poem are 'pain' and 'sacrifice'\n"
            else:
                print "\nThe key word from the poem is 'signer'\n"
        elif "help" in resp:
            if is_open == False:
                print "\nTry examining, interacting, and opening different objects in the room\n"
            elif cd == False:
                print "\nTry picking up objects that could be useful (and sharp)\n"
            elif cd_broken == False:
                print "\nHmmm, what could you do with this CD. This fragile little CD\n"
            else:
                print """
Try reading over the poem again, and if you are still confused type help2
"""
        elif "look" in resp:
            print """
You are now in an even bigger room, and this one has white walls. There is
a walkman sitting in the right corner of the room. As you turn to your left
you see a note scribbled in a dark red substance on the wall. It reads,\n
\tBeware the dark, beware the painless,
\tA cowardly quester will wander aimless.
\tThe sacrificial yield become the pen,
\tThe signer continues, on and again.
\tX_________________
"""
        else:
            confused()



def room4():

    resp = ur()

    print """
You blink, then blink again. As your eyes adjust to the oppressive brightness
you hear the omnipresent buzz of civilization all around you. You turn back and
see the room you just exited fading from view. Now that you can see you realize 
that you are sitting in front of your computer, back in the real world.
Congradulations, you have escaped the mysterious challenges. Or have you...
"""
    
    room5()

def room5():

    resp = ur()

    print """
You find yourself in a small dark room. It smells a little moldy,
and you see some water pooled in dark puddle on the floor. There
are no windows. You see one small door in front of you.
"""

    room1()

start()
