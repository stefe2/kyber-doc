# Troubleshooting

Solving common problems, errors and unexpected behavior.

!!! info "Community Knowledge Base"
    These questions and answers come from the **Kyber Control Systems**
    Facebook group (~2000 members).
    Click on any question to expand the answers.

---

## Startup Issues

??? question "Happy New Year, everyone! I have a 15 button board for my Taranis QX7, and am trying to set up my button values for the..."

    *Posted by **Matt Hobbs**:*
    > Happy New Year, everyone! 
    I have a 15 button board for my Taranis QX7, and am trying to set up my button values for the Kyber (I have done them successfully before for 2 other droids). I am running into the following problem: I have a released sBus Value of 172 and have set that for Released, and the value does change when I press one of the buttons. But the value when I press any of the buttons ...

    **Community answers:**

    **1. Group Member:**
    > Jeanne DeWitt Todd Harrington The red and white wires that came with the button board were reversed

    **2. Group Member:**
    > Jeanne DeWitt Todd Harrington The red and white wires that came with the button board were reversed

    **3. Matt Hobbs:**
    > PM me and send me some pictures of the front and back of the board

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2717468541919128/){ .md-button }

??? question "So I’m probably not the first to have come across this. I had recently bought a tray for my X20RS Radio by Frsky to whic..."

    *Posted by **Thomas Arroyo**:*
    > So I’m probably not the first to have come across this. I had recently bought a tray for my X20RS Radio by Frsky to which I found didn’t fit. Strangely the box says it’s suitable for the X20 series radios? Well isn’t the X20RS an X20 series radio? Firstly the hand rests weren’t compatible with my radio as my radio has a straight bottom and is not the style which has the tapered bottom so I had to ...

    **Community answers:**

    **1. Derek Kastning:**
    > Yeah you bought the wrong one. There is a model made specifically for the RS. This is the model I bought and it fits perfect no mods needed.

    **2. Derek Kastning:**
    > Yeah you bought the wrong one. There is a model made specifically for the RS. This is the model I bought and it fits perfect no mods needed.

    **3. Steven Dodds:**
    > The RS has this version.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2564487087217275/){ .md-button }

??? question "hope someone can help with this. I am programming my Meastro with Kyber and Kyber wants a script number. Where can I fin..."

    *Posted by **Jim McCann**:*
    > hope someone can help with this. I am programming my Meastro with Kyber and Kyber wants a script number. Where can I find that number? I made one and assumed it was 0 but I was wrong
    Still a problem. Is the a document or video anyone can point me at? I can't seem to find anything on search or in the manual.

    **Community answers:**

    **1. Jim McCann:**
    > I'm sure someone more knowledgeable than me will chime in for a better assist but I made a blank script at the beginning of the script and used that as the 0 zero script for I could use 1,2,3....... etc etc from there and it worked for me. Make sure you have the maestro number in as well.

    **2. Dave Stapley:**
    > Create 0 with nothing in, then for animations 1,2,3 onwards. Once done write all sequences to script. Then change the returns to quit within the script and apply.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2248368715495782/){ .md-button }

??? question "Does Kyber serial command not support double quotes '. When I try to add them to the serial command line after hitting s..."

    *Posted by **Jacob Amundsen**:*
    > Does Kyber serial command not support double quotes ". When I try to add them to the serial command line after hitting save to memory everything after the double quotes doesn't save and disappears.
    Is this a limitation of the serial command line? Is there a fix for this?
    Stephane Beaulieu

    **Community answers:**

    **1. Jacob Amundsen:**
    > Hey John Geb I ran into the same problem and worked with Stephane Beaulieu on it. There is a conflict in the code that
    > Doesn't recognize the quotes. The way we got around it is by completely bypassing the marcduino and sending the serial lines directly to the Kyber system. Then you can drop the prefix of the code. Hey John Geb I ran into the same problem and worked with Stephane Beaulieu on it. There is a conflict in the code that Doesn't recognize the quotes. The way we got around it is by completely bypassing the marcduino and sending the serial lines directly to the Kyber system. Then you can drop the prefix of the code.

    **2. Brian Dodds:**
    > What serial command needs double quotes?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2123034941362494/){ .md-button }

??? question "I'm not a beginner, but I’m unsure how to use my Kyber. I have a B2EMO and an X20S, and honestly, I’m lost. Does anyone..."

    *Posted by **Matt Hobbs**:*
    > I'm not a beginner, but I’m unsure how to use my Kyber. I have a B2EMO and an X20S, and honestly, I’m lost. Does anyone have a B2 guide? Or is it mostly trial and error? I’m just looking for some guidance, any helpful tips or insights would be greatly appreciated.

    **Community answers:**

    **1. Matt Hobbs:**
    > I believe Stephane Beaulieu has a custom set of software for B2 or you could create your own mixes in the x20

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2411619322504053/){ .md-button }

## Movement Issues

??? question "Hi all, need some help with the maestro scripts. I created 2 sequences. 0 with nothing and a basic sequence 1 just door..."

    *Posted by **Michael Tränkle**:*
    > Hi all,
    need some help with the maestro scripts. I created 2 sequences. 0 with nothing and a basic sequence 1 just door open door close. If I push the button "play sequence" in the maestro software it´s working. The I copied all sequnces to script. If I push run script nothing happens. I also asigned a button int the Kyber config to sequence 1. There also nothing happens. I tried it in the script ...

    **Community answers:**

    **1. Group Member:**
    > Michael Tränkle ### Sequence subroutines: ###
    > # Sequence 0
    > sub Sequence_0
    > quit
    > # Sequence 1
    > sub Sequence_1
    > 500 0 0 8064 0 0 0
    > 0 0 0 0 0 0
    > 0 0 0 0 0 0
    > 0 0 0 0 0 0 frame_0..23 # Frame 0
    > 500 5441 frame_2 # Frame 1
    > 500 8064 frame_2 # Frame 2
    > quit
    > # Sequence 2
    > sub Sequence_2
    > 500 8000 8000 0 0 0 0
    > 0 0 0 0 0 0
    > 0 0 0 0 0 0
    > 0 0 0 0 0 0 frame_0..23 # Frame 0
    > 500 2624 2624 frame_0_1 # Frame 1
    > 500 8000 8000 frame_0_1 # Frame 2
    > 500 2624 frame_1 # Frame 3
    > 500 8000 frame_1 # Frame 4
    > 500 2624 frame_0 # Frame 5
    > 500 8000 frame_0 # Frame 6
    > 500 5103 5285 frame_0_1 # Frame 7
    > 500 5129 8000 frame_0_1 # Frame 8
    > 500 8000 frame_0 # Frame 9
    > 500 0 0 frame_0_1 # Frame 10
    > quit
    > # Sequence 3
    > sub Sequence_3
    > 500 0 0 8064 0 0...

    **2. Michael Tränkle:**
    > found this in the Pololu command reference:
    > Control commands
    > command stack effect description
    > QUIT none stops the script
    > RETURN none ends a subroutine
    > the script finally works:-) found this in the Pololu command reference: Control commands command stack effect description QUIT none stops the script RETURN none ends a subroutine the script finally works:-)

    **3. Brian Dodds:**
    > Is the maestro hooked to the proper pins on the Kyber?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2270051829994137/){ .md-button }

??? question "I have an interesting problem with my Maestro. I have all the servos set and they each work well individually with the..."

    *Posted by **Cory Hall**:*
    > I have an interesting problem with my Maestro.  I have all the servos set and they each work well individually with the slider bar.  I am putting the sequence together to move the gripper up and open and close.  The sequence runs as it should with the door opening, it shows the arm moving up but it doesn't, then the gripper opens and closes as designed but in the arm down position.  So basically e...

    **Community answers:**

    **1. Matt Hobbs:**
    > Hey Cory. This sounds like a timing issue. Post a pic of
    > Your sequence Hey Cory. This sounds like a timing issue. Post a pic of Your sequence

    **2. Cory Hall:**
    > The arm servo is not working at all or not working in the programmed sequence?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2354126814919971/){ .md-button }

??? question "Upgrading to Kyber. Got an event in 3 hours. Motors now working. Does this looks right or am I missing something?"

    *Posted by **James Roman**:*
    > Upgrading to Kyber.  Got an event in 3 hours.  Motors now working.  Does this looks right or am I missing something?

    **Community answers:**

    **1. James Roman:**
    > Figured out the problem. I needed to change the DIP switches on the Syren 10 and Sabertooth 2x32 to tell them they should be in RC mode.

    **2. Matt Hobbs:**
    > Cutting it tight there man. Lol. Glad you got it fixed

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1957344004598256/){ .md-button }
