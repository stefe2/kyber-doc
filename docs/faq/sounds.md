# Sounds & Audio

Audio configuration, speakers, sound files and effects.

!!! info "Community Knowledge Base"
    These questions and answers come from the **Kyber Control Systems**
    Facebook group (~2000 members).
    Click on any question to expand the answers.

---

## Sound Files

??? question "So I dropped my SD card into the depths of my Chopper. I grabbed a different SD card and loaded it up with sounds. They..."

    *Posted by **Steven Dodds**:*
    > So I dropped my SD card into the depths of my Chopper.
    I grabbed a different SD card and loaded it up with sounds.  They’re labeled as you see below.  Did I do something wrong?  Because they’re not playing at all when plugged into the Kyber.  They’re numbers exactly the same as the original card was.  I can play them on my computer just fine when I plug the card in.

    **Community answers:**

    **1. Mark Smith:**
    > What hardware does it use? The reason I ask is there are two firmwares for the MP3 triggers, for example. One that goes by name, one that goes by number of the file, decided not by the name, but the order in which it was uploaded to the card. Do other cards/players have that issue?

    **2. Mark Smith:**
    > What hardware does it use? The reason I ask is there are two firmwares for the MP3 triggers, for example. One that goes by name, one that goes by number of the file, decided not by the name, but the order in which it was uploaded to the card. Do other cards/players have that issue?

    **3. Steven Brierley:**
    > This labeling should work… there has to be another reason. Did you run through everything in double check … amp, speakers, connected?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2737081333291182/){ .md-button }

??? question "I don't know what you are asking just screen? You put whatever number mp3 you want to play on the button setup screen. I..."

    *Posted by **Sam Morton**:*
    > I don't know what you are asking just screen? You put whatever number mp3 you want to play on the button setup screen. If it's… Afficher plus

    **Community answers:**

    **1. Sam Morton:**
    > I don't know what you are asking just screen? You put whatever number mp3 you want to play on the button setup screen. If it's a single put the same number in both columns... If you want a random in a range put the range and choose the random checkbox.

    **2. Sam Morton:**
    > I don't know what you are asking just screen? You put whatever number mp3 you want to play on the button setup screen. If it's a single put the same number in both columns... If you want a random in a range put the range and choose the random checkbox.

    **3. Matt Hobbs:**
    > So many ways of doing this. You can set up the rc switches in the kyber user interface or you can map the switch to the same channel as the kyberpad and then go into the mix and set the offsets so that the sound you want to play is activated when you flip the switch. Then you just have to return the switch to the neutral position.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2762626894069959/){ .md-button }

??? question "With Kyber MP3 player is it possible to trigger a MP3 by serial command? For instance I would like to create a routine..."

    *Posted by **Brian Dodds**:*
    > With Kyber MP3 player is it possible to trigger a MP3 by serial command?  For instance I would like to create a routine that would send roam a dome to home, turn on the front holo on for 38 seconds, play leia message with a 3 second delay.
    *Update*
    I reached out to Greg Hulette to see how he handles timed animations.  His response was to update the WCB's code to support timing.  
    https://github.co...

    **Community answers:**

    **1. Gary Isle:**
    > Hey Cory could you provide an example as a serial command.  Within the Kyber GUI I can see the sound delay.  The problem is when triggering the  following ;W1;S5\nDPH:W45\r^\nS1|33\r.  The holoprojector turns on and does it's animation  before the dome has returned to home.  I'm looking to be able to set a timed delay in between the actions.

    **2. Gary Isle:**
    > Hey Cory could you provide an example as a serial command. Within the Kyber GUI I can see the sound delay. The problem is when triggering the following ;W1;S5\nDPH:W45\r^\nS1|33\r. The holoprojector turns on and does it's animation before the dome has returned to home. I'm looking to be able to set a timed delay in between the actions.

    **3. Brian Dodds:**
    > The Kyber can play sound files but you can also control other serial devices.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2561549854177665/){ .md-button }

??? question "Total Noob here, so I'll start by apologing. I recently got my R2 setup with a FrSky20s, got Kyber installed and I can p..."

    *Posted by **Darren Moser**:*
    > Total Noob here, so I'll start by apologing. I recently got my R2 setup with a FrSky20s, got Kyber installed and I can play noises, but I still have a couple of questions:
    1. Are the naming of the buttons on the touchpad done thru the Kyber Control Systems on the Button 1/2 pages? Or are they done on the actual controller itself? I've assigned the sound and name in the tabs in KCS, but the control...

    **Community answers:**

    **1. Brian Dodds:**
    > 1 buttons are named in the Kyber pad settings on the controller.
    > 2 yes they must be the correct format like the ones that work. 1 buttons are named in the Kyber pad settings on the controller. 2 yes they must be the correct format like the ones that work.

    **2. Alden Burtt:**
    > Are there diff MP3 specs out there? What is ID3? I have matched bit depth and sample rate but still no dice. Sorta out of ideas of what to look at next.

    **3. Alden Burtt:**
    > Thanks Darren, helpful video and certainly clears some stuff up for me. I think my naming and everything is alright, just for whatever reason, the MP3s I'm exporting are not playing.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2240485446284109/){ .md-button }

??? question "So I turned the new kyber I got from Matt Hobbs and everything worked great and was able to start programming sounds. I..."

    *Posted by **Matt Hobbs**:*
    > So I turned the new kyber I got from Matt Hobbs and everything worked great and was able to start programming sounds. I did the sounds but then turned it off then back on again and now it won’t play any sounds. Replaced the audio cables and the sd card but still nothing. Next best guess would be the ground loop isolator?

    **Community answers:**

    **1. Matt Hobbs:**
    > He blue light on the DF player is coming on when you play a sound so the kyber is working properly. I would look at everything past that such as cables, amp and speakers

    **2. Group Member:**
    > Rob N Kristien Matt Hobbs yep, looks like it triggered... check the audio out of the player to the Amp then to the speakers.

    **3. Group Member:**
    > Ryan Nowak Matt Hobbs thank you for confirming that! My volume control channel changed to 0 on kyber for some weird reason

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2309251469407506/){ .md-button }

??? question "I’m working on the Maestro scripts for running off the Kyber. Can someone give me a file name example? Does it need to j..."

    *Posted by **Steven Dodds**:*
    > I’m working on the Maestro scripts for running off the Kyber. Can someone give me a file name example? Does it need to just be 1.file or 01.file with no text in the file name?
    Edited - Ok I figured out the issue. Part of it was the naming. Now my scripts are all 1, 2, 3 etc. With a blank 0. But I wasn't doing the step to write the sequences to the script. I missed that part. Working now.

    **Community answers:**

    **1. Darren Moser:**
    > Ok I figured out the issue. Part of it was the naming. Now my scripts are all 1, 2, 3 etc. With a blank 0. But I wasn't doing the step to write the sequences to the script. I missed that part. Working now.

    **2. John Geb:**
    > If it's a script you just put the script number that you want to be played in the m Maestro Field in Kyber.

    **3. Steven Dodds:**
    > The name isn’t referenced in Kyber
    > Just the sequence number? The name isn’t referenced in Kyber Just the sequence number?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2152235611775760/){ .md-button }

??? question "How to install the Kyber Controls 10 button module into a QX7. Sorry for the bad audio. I am going to have to look into..."

    *Posted by **Matt Hobbs**:*
    > How to install the Kyber Controls 10 button module into a QX7. Sorry for the bad audio. I am going to have to look into getting a better recording system. This is a little more complex than installing the 15 button module which only requires 3 wires. I will do a video on it a little later on.

    **Community answers:**

    **1. Mick Croskery:**
    > Nice video Matt. I'm assuming the 15 way is just direct to the pot (for example) as your little 15 button box is already all wired up internally right?

    **2. Group Member:**
    > Matt Hobbs Mick Croskery that is correct.

    **3. Matt Cook:**
    > Great tutorial. Nice clean mod

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1401423613523634/){ .md-button }

??? question "Is anyone using the Human-Cyborg Relations sound module with Kyber? I'm converting R5 to Kyber and would love to use HC..."

    *Posted by **Tim Hebel**:*
    > Is anyone using the Human-Cyborg Relations sound module with Kyber?  I'm converting R5 to Kyber and would love to use HCR as the sound.

    **Community answers:**

    **1. Ken Rowan:**
    > I think I’ve seen it with a RX droid

    **2. Brian Dodds:**
    > I can't see any reason why it wouldn't work?

    **3. John Geb:**
    > I second this question,

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1941037426228914/){ .md-button }

??? question "Have a question. Is there a program file for the cantina, scream, and wave animations? Not sure if there is a community..."

    *Posted by **Brian Dodds**:*
    > Have a question. Is there a program file for the cantina, scream, and wave animations? Not sure if there is a community share for file like that. I'm aware I'd still have to do further setup with the meistros for servo range and whatnot. Or that's what I believe needs to be done. Just had a milestone of getting the x20 to talk to the kyberpad and got it to play the desired sounds. Now looking to l...

    **Community answers:**

    **1. KCSync:**
    > IA de Kyber Control Systems I found some answers for you! Browse these past group posts:
    > Ok, Ive figured out how to program the sequences in Maestro. What...

    **2. Brian Dodds:**
    > I have all that by linking the Kyber to the Marcduinos in the dome. No maestros used up there.

    **3. Group Member:**
    > Chris Lizyness Brian Dodds wouldn't I need the maestro if I incorporate warpcell modular system?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2475195909479727/){ .md-button }

??? question "questions: When setting up a button it allows for a min and max sound. Then plays them in order as you push the button...."

    *Posted by **Cory Hall**:*
    > questions: 
    When setting up a button it allows for a min and max sound. Then plays them in order as you push the button. Is there a way to make it random pick a sound from the range? Does it remember the sequence number it's on through additional pushes of other buttons?
    Desired Example:
    B1 - Random sound 1-99
    B2 - Random song - 100-199
    B3 - Random song - 200-299
    I would use this in the manner B1,...

    **Community answers:**

    **1. Group Member:**
    > Sam Morton TY sir! Follow up question ... lets say I have 1000 tracks, but it's not contiguous. IF I do a random that does not exist will it play the next or does it random on filenames present or would it just play nothing

    **2. Cory Hall:**
    > If you update to kyber 2.0 there is the option to randomize the tracks played.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2754621531537162/){ .md-button }

## Audio Hardware

??? question "Hey guys/gals, For someone who is currently using a Sparkfun MP3 trigger connected to an arduino for sound on my droid,..."

    *Posted by **Cory Hall**:*
    > Hey guys/gals,
    For someone who is currently using a Sparkfun MP3 trigger connected to an arduino for sound on my droid, is Kyber a good alternative?
    I’m unimpressed with the audio quality off the sparkfun unit. 
    I use flysky ibus to communicate with the arduino so that I can use my radios toggles to control sounds and “moods” on chopper. From the sparkfun sound goes to a ZK-1002t amp, which works ...

    **Community answers:**

    **1. Cory Hall:**
    > The kyber is definitely a better option for sound clarity. You will need to look into a different radio the flysky is not compatible. I would recommend using a FrSky radio x18 or x20 or twin light are good options.

    **2. Cory Hall:**
    > The kyber is definitely a better option for sound clarity. You will need to look into a different radio the flysky is not compatible. I would recommend using a FrSky radio x18 or x20 or twin light are good options.

    **3. Mark Enright:**
    > What is it you don't like about the spark fun MP3 trigger with regards to sound quality?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2643120376020612/){ .md-button }

??? question "I got my Kyber Control System installed and running with my sounds. This part is working well, however, I’m getting quit..."

    *Posted by **Steve Hargrave**:*
    > I got my Kyber Control System installed and running with my sounds. This part is working well, however, I’m getting quite a bit of RF interference; general background noise, some clicking and “amplified” servo noise when I move them. I fear I have created multiple antennas with my longer wire runs. Has anyone else experienced this?  When I simply played the sounds via a Bluetooth receiver, I did n...

    **Community answers:**

    **1. Matt Hobbs:**
    > Golvery Ground Loop Noise... https://www.amazon.com/dp/B076WKDH46... AMAZON.COM Golvery Ground Loop Noise Isolator, Auido Humming Hissing Buzzing Noise Filter Eliminator for Bluetooth Car Audio, Home, PC Stereo System with 3.5mm or RCA Aux Jack

    **2. Matt Hobbs:**
    > I just realized this was a video. Something defiantly different going on there. I would try installing a ground loop isolator. I will post a link to what I am using.

    **3. Matt Hobbs:**
    > Send me a picture of the DFplayer. It may be one of the fake ones I received from Amazon. I have ordered new ones directly from the manufacture.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1461671547498840/){ .md-button }

??? question "So my rear speaker, and my rear speaker only, is making this sound. Like an idling motor cycle. I’ve jiggled wires, pl..."

    *Posted by **Kelly Larson**:*
    > So my rear speaker, and my rear speaker only, is making this sound.  Like an idling motor cycle.  I’ve jiggled wires, played around with the Pyle amp, etc, but it continues to do it.  Any thoughts on what could cause this?

    **Community answers:**

    **1. Group Member:**
    > Joe Brausam Matt Hobbs I do, actually! Is it possible that could have gone bad somehow?

    **2. Group Member:**
    > Matt Hobbs Does the volume of the sound change when changing the volume on the transmitter?

    **3. Kelly Larson:**
    > Check if your wires are connected and if that looks good check if there is a short

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2478656359133682/){ .md-button }

??? question "Is it possible with the FrSky X20-S to use a two way switch and a pot to control the volume for the HCR and Kyber. For..."

    *Posted by **Trevor Zaharichuk**:*
    > Is it possible with the FrSky X20-S to use a two way switch and a pot to control the volume for the HCR and Kyber.  For example the two way switch set to down pot 1 will control HCR.  Two way switch up pot 1 will control the Kyber.  I tried looking for examples via google and youtube but I'm not sure what this would functionality would be called.  Is it logic switching.

    **Community answers:**

    **1. Gary Isle:**
    > Thanks for the input Darren. Currently I have pot 1 for kyber and pot 2 for HCR. But I would like to have both controlled from the same pot via the two position switch.

    **2. Trevor Zaharichuk:**
    > Just curious, if you are using HCR, it plays wav files, so just wondering why you use both HCR and kyber? Of course not solving your volume issue as you have separate volume in HCR for vocals and wav payback.

    **3. Darren Moser:**
    > I use the red center slider as my volume control. I know in the Kyber you set a channel to be the volume. Not sure about the HCR

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2239506956381958/){ .md-button }

??? question "Hi all I've got Kyber up and running and I'm receiving the sbus value of my buttons on the radio (x7). However during..."

    *Posted by **Eelke Abbink**:*
    > Hi all
    
    I've got Kyber up and running and I'm receiving the sbus value of my buttons on the radio (x7). 
    
    However during testing (going through the buttons) the Kyber will freeze up, blue light will be constantly on instead of blinking. Also web interface will no longer respond. 
    
    Any idea where I went wrong?
    
    Also, I'm not getting a start up sound even though I've got an mp3 named "0001" and in t...

    **Community answers:**

    **1. Eelke Abbink:**
    > Note: maestro not yet connected, only one power source to Kyber
    > Power going from Kyber to receiver (X8R), no other power sources going to the receiver Note: maestro not yet connected, only one power source to Kyber Power going from Kyber to receiver (X8R), no other power sources going to the receiver

    **2. Stephane Beaulieu:**
    > In the web interface under General/Maestro, uncheck « check for script running » or remove every script number you are sending to the Maestro. Since your Maestro is not wired, thats probably your problem.

    **3. Group Member:**
    > Eelke Abbink Stephane Beaulieu yep that looks like it fixed the freezing. I'll try tomorrow to get a sound triggered on a button

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2086054321727223/){ .md-button }

??? question "Can someone show me the exact format for a Roam-A-Dome command? I have tried: :DPA90:W2:H :DPA90:W2:H /r <:DPA90:W2:H>..."

    *Posted by **Cory Hall**:*
    > Can someone show me the exact format for a Roam-A-Dome command?  I have tried:
    :DPA90:W2:H
    :DPA90:W2:H /r
    <:DPA90:W2:H>
    <:DPA90:W2:H /r>
    and these do not seem to be it
    EDIT: the format for RAD is: command \r. For example
    :DPW10:D90:D-90 \r
    That is wait 10 seconds, rotate 90 degrees, rotate back 90 degrees.

    **Community answers:**

    **1. Tim Hebel:**
    > Almost there. The format is <xxx>|r. The <> act as quotes for the serial command string and the \r is the send command. Here is an example of sound commands for HCR. I know it is a different component, but it works the same and I had the picture handy.

    **2. John Boisvert:**
    > The solution for RAD commands in Kyber

    **3. Cory Hall:**
    > Blast from the past

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2163428993989755/){ .md-button }

## Volume & Setup

??? question "I have no idea if this can happen, but ill ask. Is there a way for kyber to loop a button? I added music to my R2 and ma..."

    *Posted by **Brian Dodds**:*
    > I have no idea if this can happen, but ill ask. Is there a way for kyber to loop a button? I added music to my R2 and made 'DJ' button that is just music. Is there a way to just press it once and it keeps playing through the song until I hit the 'stop all' button.

    **Community answers:**

    **1. Group Member:**
    > Matthew Lizyness Brian Dodds so I just have to make a large mp3 file. I just have several shorter files

    **2. Group Member:**
    > Matthew Lizyness Brian Dodds so I just have to make a large mp3 file. I just have several shorter files

    **3. Cory Hall:**
    > Yeah the kyber will play your mp3 file even if it’s a large file.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2715674828765166/){ .md-button }

??? question "Hey guys, I got my Kyber today. I'd like to use it to power my M-O. I've earmarked the Kyber system for this and wanted..."

    *Posted by **Cricket Lee**:*
    > Hey guys, I got my Kyber today. I'd like to use it to power my M-O. I've earmarked the Kyber system for this and wanted to know if I've forgotten anything.
    So, I have:
    -KyberControl
    -Scorpion Mini Dual 6.5A 6V to 28V R/C DC Motor Driver
    -FrSky R9 SX Enhanced R9 Series Access OTA Long Range Receiver
    -FRSKY X7
    -HiLetgo ILI9341 2.8-inch SPI TFT LCD Display Touch Panel 240X320 with PCB 5V/3.3V STM32
    D...

    **Community answers:**

    **1. Cricket Lee:**
    > If you are planning on having audio, you'll also need an amplifier board and a speaker.
    > Also depending on your battery choice, you may also consider getting a BEC to step down voltage for some components.
    > I am not planning on using a Maestro in my M-O. All head pan/tilt and motor functions can be done via transmitter sticks. Eye animations and audio will be programmed within the Kyber software and Kyberpad. If you are planning on having audio, you'll also need an amplifier board and a speaker. Also depending on your battery choice, you may also consider getting a BEC to step down voltage for some components. I am not planning on using a Maestro in my M-O. All head pan/tilt and motor function...

    **2. Group Member:**
    > Dejan Delic Cricket Lee Hmm, actually. I don't seem to have anything for audio yet.
    > A converter to reduce the voltage from 12V would certainly be beneficial. At first, I thought one of the components already did the job. Cricket Lee Hmm, actually. I don't seem to have anything for audio yet. A converter to reduce the voltage from 12V would certainly be beneficial. At first, I thought one of the components already did the job.

    **3. Group Member:**
    > Cricket Lee Be sure to look through the Kyber Control manual. There are some really good schematics/diagrams in there.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2461100374222614/){ .md-button }

??? question "Just started setting up the Kyber and doing the basics. Set startup sound to #1 (cantina) but volume is low. The book sa..."

    *Posted by **John Reik**:*
    > Just started setting up the Kyber and doing the basics. Set startup sound to #1 (cantina) but volume is low. The book says if not set up on the r/c (soon) you can set the volume in the next setting after startup sound, only it’s not there…
    Any help?

    **Community answers:**

    **1. John Reik:**
    > Kyber has a default (setting) if it isn’t set in the r/c, at least that’s what the instruction sheets say in the quick setup

    **2. Cory Hall:**
    > I’m not sure what you are asking. Volume control is set by setting a rc channel to control it.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2648028195529830/){ .md-button }
