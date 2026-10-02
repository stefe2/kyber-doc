# Software & Firmware

Installation, firmware updates, configuration and web interface.

!!! info "Community Knowledge Base"
    These questions and answers come from the **Kyber Control Systems**
    Facebook group (~2000 members).
    Click on any question to expand the answers.

---

## Installation

??? question "Hello builders, I am opening up this thread for the ransom sounds and events that I would like to add to the Kyber. I n..."

    *Posted by **Stephane Beaulieu**:*
    > Hello builders, I am opening up this thread for the ransom sounds and events that I would like to add to the Kyber.  I need your input on this subject, how should I do that ?
    - Toggle switch to enable it ?
    - Multiple sounds ?
    - Multiple Maestro Scripts
    There is no bad answers or questions, all ideas are welcome, let's do a group brainstorm.

    **Community answers:**

    **1. Andrew Smith:**
    > If you are essentially wanting to emulate padawan's random sound function then I think just a simple toggle on/off is fine, then configure what bank of sounds to use and delay between them on the web interface. That would be the sort of thing you do outside of an event anyway so having it configurable only on the web interface isn't that much of a hassle. 
    > But calling random meastro scripts at the same time would be cool. Chopper grumbling to himself and occasionally raising his periscope up, looking around and then bringing it back down. Then maybe stretching his dome arm out a bit. If you are essentially wanting to emulate padawan's random sound function then I think just a simple toggle o...

    **2. Stephane Beaulieu:**
    > What about using the web interface to set the timing instead of a POT ?
    > On the web interface we would have:
    > - Min Sound Number
    > - Max Sound Number
    > - Min Time Delay
    > - Max Time Delay
    > Since we will have a 3 positions toggle switch:
    > - Position 1 = Random OFF
    > - Position 2 = Random ON
    > - Position 3 = ???
    > What should we have in position 3 ? What about using the web interface to set the timing instead of a POT ? On the web interface we would have: - Min Sound Number - Max Sound Number - Min Time Delay - Max Time Delay Since we will have a 3 positions toggle switch: - Position 1 = Random OFF - Position 2 = Random ON - Position 3 = ??? What should we have in position 3 ?

    **3. Justin Tomlinson:**
    > Random sounds: enable by a switch and being able to adjust how often it happens(example every 10-30 seconds) turn a pot on transmitter so you can adjust on the fly.
    > Nice thing with adding random sounds is if you park your droid at an event the droid will still make sounds randomly adding to the magic Random sounds: enable by a switch and being able to adjust how often it happens(example every 10-30 seconds) turn a pot on transmitter so you can adjust on the fly. Nice thing with adding random sounds is if you park your droid at an event the droid will still make sounds randomly adding to the magic

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2012934455705877/){ .md-button }

??? question "Setting up 2.0. I'm assigning the 15 button panel sbus signals. I can get a few done, then one will show ACTIVE. So I a..."

    *Posted by **Cory Hall**:*
    > Setting up 2.0. I'm assigning the 15  button panel sbus signals. I can get a few done, then one will show ACTIVE. So I adjust and start did the list again. Same thing. Any tips? Does it really matter?

    **Community answers:**

    **1. Darren Moser:**
    > So you will push button one and then read the sbus value it gives you (listed right below “Button Values Configuration”)
    > Then you put in that value for button 1. Repeat for all 15 buttons. So you will push button one and then read the sbus value it gives you (listed right below “Button Values Configuration”) Then you put in that value for button 1. Repeat for all 15 buttons.

    **2. Darren Moser:**
    > So you will push button one and then read the sbus value it gives you (listed right below “Button Values Configuration”)Then you put in that value for button 1. Repeat for all 15 buttons. So you will push button one and then read the sbus value it gives you (listed right below “Button Values Configuration”) Then you put in that value for button 1. Repeat for all 15 buttons.

    **3. Group Member:**
    > Jon Robinson Cory Hallit's not that. Like I'll program 1-5 just fine. I do 6. But then 2 also shows active also. They are both close values. So I'll adjust to get a new base sbus value. Then do 1-4 then when I do 5, 3 also shows active. And so on

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2765994640399851/){ .md-button }

??? question "A few more questions that im trying to figure out with the whole Kyber setup. The random switch has a little icon that s..."

    *Posted by **Stephane Beaulieu**:*
    > A few more questions that im trying to figure out with the whole Kyber setup. The random switch has a little icon that switches from up and down to left and right. What is that for? Also whats the purpose of having a wifi on and off on a switch? Dont I just need the wifi on when configuring? Trying to get an idea how all the features work.

    **Community answers:**

    **1. Stephane Beaulieu:**
    > In Kyberpad Version 2, WiFi icon has been replaced with drive on/off icon and in Kyber V2.0, wifi now work with a jumper on pin IN1 (ground and signal). Yes you are right in a convention you really want your wifi turned off and only turned on when changing settings.
    > The Icon on the random Switch mean nothing, it's just a representation that show you the position when the toggle is moved. Actually all the icons are in the folder and you can change them to suit your needs. In Kyberpad Version 2, WiFi icon has been replaced with drive on/off icon and in Kyber V2.0, wifi now work with a jumper on pin IN1 (ground and signal). Yes you are right in a convention you really want your wifi turned off ...

    **2. Stephane Beaulieu:**
    > In Kyberpad Version 2, WiFi icon has been replaced with drive on/off icon and in Kyber V2.0,  wifi now work with a jumper on pin IN1 (ground and signal).  Yes you are right in a convention you really want your wifi turned off and only turned on when changing settings.The Icon on the random Switch mean nothing, it's just a representation that show you the position when the toggle is moved.  Actually all the icons are in the folder and you can change them to suit your needs. In Kyberpad Version 2, WiFi icon has been replaced with drive on/off icon and in Kyber V2.0,  wifi now work with a jumper on pin IN1 (ground and signal).  Yes you are right in a convention you really want your wifi turned ...

    **3. Group Member:**
    > Jacob Ebert Stephane Beaulieu is there a function tied to the random? Im currently trying map out what switches im going to use and which are needed/ best location for my liking and setup

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2763082454024403/){ .md-button }

??? question "Need help, I changed my Kyber password and now I can't see the Kyber in my Wi-Fi settings. Thoughts? RESOLVED!! Matt H..."

    *Posted by **Cory Hall**:*
    > Need help, I changed my Kyber password and now I can't see the Kyber in my Wi-Fi settings.  Thoughts?
    RESOLVED!!  Matt Hobbs to the rescue.  Seems the FW corrupted.  Reflash brought it back to life.

    **Community answers:**

    **1. Sean Fuchs:**
    > And my remote won't communicate now with the Kyber which makes me think because of that the Wi-Fi enable is not reaching the Kyber but why would a password change cause this?

    **2. Sean Fuchs:**
    > Saw on another thread the wi-fi defaults to on. So I am wondering if mine is in a funky state when I reset it being there is no blue light and all. Stephane Beaulieu please advise

    **3. Sean Fuchs:**
    > The only think I can think of is the program corrupted because it won't even respond to the Kyber pad. What are my options? Thanks

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2232494963749824/){ .md-button }

??? question "Kyber on the test/setup bench working beautifully! Installing this week. questions, any update on a random sounds mode ?..."

    *Posted by **Cory Hall**:*
    > Kyber on the test/setup bench working beautifully! Installing this week. questions, any update on a random sounds mode ? And on random, maybe a way to randomly pick a sound from the list of sounds rather than just moving down the list in order there numbered when hitting that button. I’m sure I’ll have more questions soon just forget them. Thanks guys for a great product.

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Yeah definitly I need to work on the random sounds and events.  I did not make my head how I will do it yet.

    **2. Stephane Beaulieu:**
    > Yeah definitly I need to work on the random sounds and events. I did not make my head how I will do it yet.

    **3. Michael Ostrom:**
    > Are you using Maestros or Marcduinos? Also, can you post a screenshot (or send me them) of your Kyber Controls web config screens?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2012610552404934/){ .md-button }

??? question "Feature request: Would it be possible to have multiple profiles on the Kyber? I'm use the modular design for all the ele..."

    *Posted by **Brian Dodds**:*
    > Feature request: Would it be possible to have multiple profiles on the Kyber? I'm use the modular design for all the electronics. It would be nice to be able to swap that between R2s and have a different set of sounds & set up instead of buying everything again.

    **Community answers:**

    **1. Brian Dodds:**
    > Change the SD card?
    > I personally would still have a 2nd Kyber in a 2nd droid. Change the SD card? I personally would still have a 2nd Kyber in a 2nd droid.

    **2. Stephane Beaulieu:**
    > Save the config.json file under firmware and upload a new one depending on which droid you will be using.

    **3. Group Member:**
    > Jon Robinson Its not just the kyber, but another sabretooth, sound card, etc.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2521476831518301/){ .md-button }

??? question "FrySky X20 not being received by the TD-R10 Receiver. Wiring between TD-R10 and Kyber Board is correct, but receiver ha..."

    *Posted by **Al Cordera**:*
    > FrySky X20 not being received by the TD-R10 Receiver.  Wiring between TD-R10 and Kyber Board is correct, but receiver has Red Blinking light. 
    Question: should I have performed a registration/binding procedure prior to installation to the R2D2 board panel?   
    FrSky TD R10 Instruction (Version 1.0) off the web has instructions on "Registration & Automatic Binding".  
     According to their LED Color c...

    **Community answers:**

    **1. Al Cordera:**
    > Nope did not do anything like that, just plugged everything in and turned on both devices.

    **2. Group Member:**
    > Brian Dodds look up how to register and bind the receiver. ￼￼

    **3. Brian Dodds:**
    > Did you register and then bind the TD-R10?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2150325135300141/){ .md-button }

??? question "Good Morning everyone, Hopeing someone here can help. I have the the kyber software setup and its playing sounds. The is..."

    *Posted by **Cory Hall**:*
    > Good Morning everyone, Hopeing someone here can help. I have the the kyber software setup and its playing sounds. The issue is that it is playing the same sounds for both pages. Stephane Beaulieu is at Megacon and said that I need to do a mix and output it to a RC channel and set that up in the Kyber board. Can someone help me through that process?

    **Community answers:**

    **1. Cory Hall:**
    > Matt Hobbs. Stephane Beaulieu add another help desk point to my file another Kyber fixed

    **2. Cory Hall:**
    > Shoot me a PM I should be able to walk you through the setup

    **3. Andrew S Harris:**
    > Sounds like my exact problem too.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2121206998211955/){ .md-button }

??? question "Hey guys, I’m having a little problem. I’m working on getting the Kyberpad setup. I have two pages, the default page,..."

    *Posted by **Dan Coe**:*
    > Hey guys,  I’m having a little problem.  I’m working on getting the Kyberpad setup.  I have two pages, the default page, and the Kyber page.   The default looks right, but the Kyber page is missing the header and footer.   Did I do something wrong?   
    FYI, I have the most recent firmware as of today.

    **Community answers:**

    **1. Stephane Beaulieu:**
    > You chose the full screen page layout, use the other one.

    **2. Group Member:**
    > Dan Coe Stephane Beaulieu sent you a dm if you don’t mind.

    **3. Group Member:**
    > Dan Coe Stephane Beaulieu got it thanks!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1961993914133265/){ .md-button }

??? question "So now that I have my Kyber installed……. So what’s up with the random sounds update? I’m kinda miss R2 talking when I’..."

    *Posted by **Cory Hall**:*
    > So now that I have my Kyber installed…….
    So what’s up with the random sounds update? 
     I’m kinda miss R2 talking when I’m in the garage working

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Working on it.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2038880279777961/){ .md-button }

## Firmware Update

??? question "KYBER CONTROL – VERSION 2.0.0 RELEASED! I’m excited to announce the release of Kyber Control v2.0.0, featuring major imp..."

    *Posted by **Hunter Smoke**:*
    > KYBER CONTROL – VERSION 2.0.0 RELEASED!
    I’m excited to announce the release of Kyber Control v2.0.0, featuring major improvements, increased stability, and several new features.
    A huge thank you to Neil Hutchison for bringing the Kyber Code to the next level by porting it to a modern development platform and delivering countless improvements and bug fixes.
    Special thanks to Chris Stroud for the ex...

    **Community answers:**

    **1. Keaton Cole:**
    > Looking to update my Kyber while I have cables out. Can I be added to the update group? OR Also the online installer, does that not have 2.0.0 for download? It says 1.2.7 on the connect page.

    **2. Keaton Cole:**
    > Looking to update my Kyber while I have cables out. Can I be added to the update group? OR Also the online installer, does that not have 2.0.0 for download? It says 1.2.7 on the connect page.

    **3. Andynterri Peacock Mccready:**
    > Hi Stephane, so this update can be used with your existing boards? I bought my Kyber last year sometime. No need to buy a new board?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2690352221297427/){ .md-button }

??? question "Ok stumped, I went from the physical buttons to the kyber pad. I also switched to the x20 and the td r10 receiver. I a..."

    *Posted by **Sean Fuchs**:*
    > Ok stumped, I went from the physical buttons to the kyber pad.  I also switched to the x20 and the td r10 receiver.  I assume you have to setup the Button Values but I am not getting any response from the remote for this step.  Any advice?    I assume the Kyber itself doesn't need a firmware update.

    **Community answers:**

    **1. Matt Hobbs:**
    > Stephane Beaulieu can you lend a helping hand?  I do know that the kyber software does not need to be updated. Yes you will have to setup new button values in your kyber software. Make sure you set your button pad to channel 9 in the kyber software. Stephane Beaulieu can you lend a helping hand? I do know that the kyber software does not need to be updated. Yes you will have to setup new button values in your kyber software. Make sure you set your button pad to channel 9 in the kyber software.

    **2. Matt Hobbs:**
    > Stephane Beaulieu can you lend a helping hand?
    > I do know that the kyber software does not need to be updated.
    > Yes you will have to setup new button values in your kyber software.
    > Make sure you set your button pad to channel 9 in the kyber software. Stephane Beaulieu can you lend a helping hand? I do know that the kyber software does not need to be updated. Yes you will have to setup new button values in your kyber software. Make sure you set your button pad to channel 9 in the kyber software.

    **3. Sean Fuchs:**
    > Stephane Beaulieu was very helpful tonight and got me sorted out.  After some troubleshooting, it was discovered that I had 2 incorrect settings.  One I had my output set to the wrong channel and I forgotten that I set my receiver to 1-9 vs 1-16.  Once both of those were sorted, the buttons responded as expected on the kyber!  Thanks very much for the assistance!!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2011723242493665/){ .md-button }

??? question "How to bind the Taranis QX7 to the X8R receiver successfully. This is what worked for me with the equipment shown in the..."

    *Posted by **Michael Janes**:*
    > How to bind the Taranis QX7 to the X8R receiver successfully. This is what worked for me with the equipment shown in the attached photos. Note, this did not work with the RX8R Pro receiver.
    Update your Transmitter firmware with what is currently available from Frsky-rc.com. See attached photo.
    Download an older version of the Receiver firmware from here-
    https://www.frsky-rc.com/x8r/
    Note: you wil...

    **Community answers:**

    **1. Cory Pacione:**
    > When I get to the step in the video where it wants me to go to the firmware folder (from the SD card) on the transmitter... I don't have any options. Just shows the SD card (but nothing in it). I have the .frk file on the sd card but it doesn't show anything. I'm on a Mac. Could this be the issue? Any advice?

    **2. Group Member:**
    > Michael Janes Cory Pacione sorry... I've never used a Mac, so no idea. If you unzipped the folders and copied them over then they should be there. You may need a Mac program to unzip them.

    **3. Group Member:**
    > Michael Janes Cory Pacione also, you need all those folders on the SD card. The firmware file .frk will be inside the firmware folder.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1913323382333652/){ .md-button }

??? question "Hello, I have recently upgraded my radio to an X20 and installed Kyberpad. The receiver is an X8R with two 12 channel m..."

    *Posted by **James M Henley**:*
    > Hello, I have recently upgraded my radio to an X20 and installed Kyberpad.  The receiver is an X8R with two 12 channel maestros. One in the body and one in the dome. Connection to dome is via a mag tag.
    My previous radio was a Tranis X7 with a button pad. Was able to run the scrips on both maestros. 
    Updated Kyber to V125, using same receiver, no changes to wiring or scripts. Can play scripts on m...

    **Community answers:**

    **1. Cory Hall:**
    > I’d check your settings on the kyber setup webpage make sure your have 2 maestro’s enabled. And make sure you have updated the kyber to the latest version and kyber pad

    **2. Cory Hall:**
    > I’d check your settings on the kyber setup webpage make sure your have 2 maestro’s enabled. And make sure you have updated the kyber to the latest version and kyber pad

    **3. James M Henley:**
    > Stephane suggested reversing RX and TX on Kyber. I have an older Kyber board. After doing so, all is working! Thanks Stephane!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2144416102557711/){ .md-button }

??? question "I can't seem to get the Random Events audio to work in my current setup for M-O. Running current Ethos firmware 1.6.2,..."

    *Posted by **John Geb**:*
    > I can't seem to get the Random Events audio to work in my current setup for M-O.  Running current Ethos firmware 1.6.2, Kyberpad v.6.  I had it working just fine for Wall-E, never an issue there.  I'm sure I'm missing something stupidly easy.  Audio works fine via the Kyberpad.
    
    In my transmitter (x20s) the Random Toggle Switch source is set to SB.  Output to CH12.  In the Kyber Control panel, Ran...

    **Community answers:**

    **1. John Geb:**
    > I made a post about this the other day, random doesn't seem to work with ethos version 1.6.1 and kyber 1.2.7. I was talking to another builder at an event this past weekend and he's having the same issue. Stephane Beaulieu already knows about it and is looking into it.

    **2. Stephane Beaulieu:**
    > FYI the bug is fixed. go here for the latest version. https://www.facebook.com/groups/492918272019451 Update Page

    **3. Group Member:**
    > Cricket Lee John Geb thank you! I will keep my eyes open for updates, then.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2466848813647770/){ .md-button }

??? question "Having a challenge with v2 and unsure where the problem might be. I have four buttons programmed to initiate Maestro seq..."

    *Posted by **Cory Hall**:*
    > Having a challenge with v2 and unsure where the problem might be. I have four buttons programmed to initiate Maestro sequences and when I click each button on KyberPad the first time they work as expected and call the correct sequence. Subsequent presses of the buttons appear to randomly select one of the four sequences from the Maestro - so for example my utility arm button plays the gripper sequ...

    **Community answers:**

    **1. Group Member:**
    > Matthew Modica That was it! Thank you! We should get the Github documentation to specify that if you only want one Maestro script to launch on the button press that it needs to have the same script number in both columns on the Button Pad Config. That was not intuitive. Happy to help update it / provide wording if needed.

    **2. Cory Hall:**
    > Make sure you have the same script number in the box for script 1 and 2 for the selected maestro.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2754611958204786/){ .md-button }

??? question "Question for the hive (or perhaps FrSky Ben) on transmitter configuration. My B2 is running Kyber and I've got an X20 (c..."

    *Posted by **Cory Hall**:*
    > Question for the hive (or perhaps FrSky Ben) on transmitter configuration. My B2 is running Kyber and I've got an X20 (currently Ethos 4.xx but will update tonight). I have a mix set up for driving as well as one for tilting. I would like to configure a 3-way switch such that in one position only the tilt is active on the right stick, in another position only the drives are active, and in the thir...

    **Community answers:**

    **1. FrSky Ben:**
    > UPDATE : New method :
    > For Tilt, Set active condition to SA- then long click it and choose Invert (meaning NOT SA- / !SA- which would be SA ↑ OR SA ↓)
    > Then for Drive mix set the active condition to SA ↑ , long click qnd choose invert. Which means NOT SA ↑ / ! SA ↑
    > Which is SA - OR SA ↓
    > Method using Logic Switches:
    > Set the "Active Condition" of the MIXES for the drive / tilt accordingly
    > You will probably need to create a couple of Logic Switches for them with "OR" condition
    > For example
    > Logic Switch 1
    > Name : Tilt Active
    > Function : OR
    > Condition 1 : SA ↑
    > Condition 2 : SA ↓
    > Logic Switch 2
    > Name : Drive Active
    > Function : OR
    > Condition 1 : SA -
    > Condition 2 : SA ↓ UPDATE : New method : For Tilt, Set ac...

    **2. Cory Hall:**
    > If your kyber pad stops working after you update ethos pm myself or Stephane Beaulieu for the updated version

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2394788450853807/){ .md-button }

??? question "I’m trying to put Kyberpad on an Twin x-lite. The first time I tried to choose Kyberpad source under Lua Sources nothing..."

    *Posted by **Cory Hall**:*
    > I’m trying to put Kyberpad on an Twin x-lite. The first time I tried to choose Kyberpad source under Lua Sources nothing was there. I made sure that the files were loaded. I then checked and noticed that my firmware was not up to date so I updated the firmware and now I don’t even have a Lua Sources option anymore. Anybody got any ideas for me? Hopefully it’s something simple that I overlooked.

    **Community answers:**

    **1. Cory Hall:**
    > Well on the x18 or 20 I know there is onboard memory and the SD card and if it’s on the wrong one you don’t see it in the setup so check where you installed the files vs what the instructions call for

    **2. Group Member:**
    > Rob Saey yep that was it. I had it saved on the SD card and it needed to be in the radio. Thank You!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2129362287396426/){ .md-button }

??? question "I downloaded and printed the Power Point file and the Kyber Control Manual off this group page; however, neither documen..."

    *Posted by **Al Cordera**:*
    > I downloaded and printed the Power Point file and the Kyber Control Manual off this group page; however, neither document has a publishing date or version number on it to see if I have the most up to date information?  I would assume as they are updated the old version get removed but on other Droid builders pages they keep all versions for access to historical information.  Not sure when the last...

    **Community answers:**

    **1. Cory Hall:**
    > It’s out of date, the board info is totally different on the new kyber but the web setup info is still relevant

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2022986611367328/){ .md-button }

## Web Interface

??? question "Hey guys, I'm trying to put in the buttons with the sbus value's..but everytime I connect the kyber with the WiFi after..."

    *Posted by **Danny de Koning**:*
    > Hey guys, I'm trying to put in the buttons with the sbus value's..but everytime I connect the kyber with the WiFi after a few seconds the connection is lost. Not with the WiFi and the laptop but with the website.. so I can't save after putting in the value. Anybody know an solution? Thanks in advance

    **Community answers:**

    **1. Dave Stapley:**
    > Maybe you have the channel that the buttons use mapped to the WiFi off toggle in the kyber page?
    > That's just a wild guess though. Maybe you have the channel that the buttons use mapped to the WiFi off toggle in the kyber page? That's just a wild guess though.

    **2. Dave Stapley:**
    > Maybe you have the channel that the buttons use mapped to the WiFi off toggle in the kyber page?That's just a wild guess though. Maybe you have the channel that the buttons use mapped to the WiFi off toggle in the kyber page? That's just a wild guess though.

    **3. Brian Dodds:**
    > Interesting.  I have not run into that issue.  Perhaps provide more details like what your using to connect and load the website?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2033066857025970/){ .md-button }

??? question "Hi Kyber heads ! We are troubleshooting getting Button 2 Pad to work with the 15 button pad...button pad 1 works perfect..."

    *Posted by **Ashly Jo**:*
    > Hi Kyber heads ! We are troubleshooting getting Button 2 Pad to work with the 15 button pad...button pad 1 works perfectly , button pad 2 assigned channel (11- on 2 way switch)  works if it is assigned to volume or the wifi control just not for button 2... we filled up all buttons on pad 1 and 2 but nada... any suggestions? Are we missing another setting in the control interface ? TIA !

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Did you set the toogle switch RC channel UNDER Toggle for PAD 2 ?

    **2. Group Member:**
    > Stephane Beaulieu on your remote you see the channel going from -100 to +100 ?

    **3. Matt Hobbs:**
    > Is it a toggle or a two position switch?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1991261514539838/){ .md-button }

??? question "Ok. So I got everything connected and the button panel installed to my RC (FYI, I’m only going to be using this for open..."

    *Posted by **Jorge L. Ortiz**:*
    > Ok. So I got everything connected and the button panel installed to my RC (FYI, I’m only going to be using this for opening body panels and arms). I tested the RC controller using the Kyber web interface and assigned all the buttons. I loaded a script to the maestro and tested it using the computer (USB) to run the script and it works fine. My first question is when you load a script to the maestr...

    **Community answers:**

    **1. Group Member:**
    > Jorge L. Ortiz Stephane Beaulieu the wiring is correct, ground to ground, Tx to RX, Rx to TX. I have 57692 on the serial setting per the Kyber instruction manual, and Device Number is 1.

    **2. Stephane Beaulieu:**
    > Is your wiring betweene the Maestro and the Kyber right ? And check the serial setup of the Maestro ? 57692 bps and ID #1

    **3. Stephane Beaulieu:**
    > SOLUTION: It's an error in the doc, the tx and rx wire were reversed.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1512666065732721/){ .md-button }

??? question "I also have a second issue - but want to keep the thread separate. . . I cannot seem to get the Kyber to send signals t..."

    *Posted by **David Bowles**:*
    > I also have a second issue - but want to keep the thread separate. . . 
    I cannot seem to get the Kyber to send signals to the Marcduino master.  I have the check box checked in the web interface, and I have the wires connected correctly.  I can also hook up a FTDI cable to the Marcdunio and successfully send commands.  
    Is there another step that I am missing? 
    TIA 
    David

    **Community answers:**

    **1. Tim Hebel:**
    > Is your Marcduino playing a sound on its own?  Many marcduino sequences have a sound embedded if I recall.

    **2. Tim Hebel:**
    > Is your Marcduino playing a sound on its own? Many marcduino sequences have a sound embedded if I recall.

    **3. Stephane Beaulieu:**
    > Show me the command you are sending

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2008683532797636/){ .md-button }

??? question "Is anyone using Kyber with marcduino? That's the setup I have. But I'm experiencing something strange with the web int..."

    *Posted by **Brian Dodds**:*
    > Is anyone using Kyber with marcduino?  That's the setup I have.  But I'm experiencing something strange with the web interface.  After I save the serial commands to the Kyber,  the web interface does not reload the entire command.  
    
    For example the command :SE08\r\p%T25\r\p&25,"A0077|10
    
    reloads in the web interface as (image below).
    
    Anyone else experience this?  Any thoughts on how to fix it?

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Long story short, this command: :SE08\r\p%T25\r\p&25,"A0077|10
    > Will be truncated at " and will be displayed like this: :SE08\r\p%T25\r\p&25,
    > It's a limitation of classic HTML forms and the character " cannot be used in a string.
    > So please do not use " in your commands. Long story short, this command: :SE08\r\p%T25\r\p&25,"A0077|10 Will be truncated at " and will be displayed like this: :SE08\r\p%T25\r\p&25, It's a limitation of classic HTML forms and the character " cannot be used in a string. So please do not use " in your commands.

    **2. Brian Dodds:**
    > I use it with Marcduino's. What version of Kyber firmware are you running? The older version was very limited on command length.

    **3. Cory Hall:**
    > This is definitely a question for Stephane Beaulieu

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2511733742492610/){ .md-button }

??? question "Hi, I have a problem with my kyber. I added the 15 buttons to my radio and connected the receiver with the SBUS channel..."

    *Posted by **Michael Tränkle**:*
    > Hi,
    I have a problem with my kyber. I added the 15 buttons to my radio and connected the receiver with the SBUS channel to the kyber. I just configured some sounds. I can play multible sounds with different pads. After 15 - 20 times the kyber stops working. The flashing blue LED turns off. The web interface is not reachable anymore. Any ideas?

    **Community answers:**

    **1. Danny de Koning:**
    > You probably have WiFi off on one of the buttons. So when you press that button the WiFi of the kyber shuts off, happened to me before

    **2. Michael Tränkle:**
    > reseted all the SBUS values and did a whole new configuration. Now it´working fine. tanks!

    **3. Stephane Beaulieu:**
    > What is the Kyber version ?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2150991481900173/){ .md-button }

??? question "So out of curiosity, between the lines of R3X and the music i feel ill need a lot more buttons, will it be possible to h..."

    *Posted by **Patrick Gray**:*
    > So out of curiosity, between the lines of R3X and the music i feel ill need a lot more buttons, will it be possible to hook up two button interfaces for more options? Forgive me if you answered this already i missed it if so.

    **Community answers:**

    **1. Matt Hobbs:**
    > The thing I see is that you won’t be able to remember what does what. Trying to remember 30 buttons is beyond me without labels. I think we could easily add more but it would require the code to be changed. I can play around with it later. Maybe we make you a custom board for him.

    **2. Steven Dodds:**
    > How many are you thinking?
    > The 15 buttons with toggle gives you 30. How many are you thinking? The 15 buttons with toggle gives you 30.

    **3. Simon Lebel:**
    > . J’en peux plus!!!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1414851775514151/){ .md-button }

??? question "I’m planning on integrating my Kyber Contoller with my project tonight or tomorrow. How do I access the browser based in..."

    *Posted by **Steve Hargrave**:*
    > I’m planning on integrating my Kyber Contoller with my project tonight or tomorrow. How do I access the browser based interface to set it up when plugging in my USB?

    **Community answers:**

    **1. Stephane Beaulieu:**
    > You don't need the USB, power the Kyber via the power socket.
    > - Open wifi config on your laptop/PC
    > - Connect to the SSID "KYBER" with password "12345678"
    > - Open web browser
    > - Type http://192.168.4.1 You don't need the USB, power the Kyber via the power socket. - Open wifi config on your laptop/PC - Connect to the SSID "KYBER" with password "12345678" - Open web browser - Type http://192.168.4.1

    **2. Group Member:**
    > Steve Hargrave Stephane Beaulieu Thanks!

    **3. Simon Lebel:**
    > . J’en peux plus!!!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1453952881604040/){ .md-button }

??? question "I went to go flash the firmware on the Kyber Controls. following the directions. It got to 100% then showed it failed to..."

    *Posted by **Brian Dodds**:*
    > I went to go flash the firmware on the Kyber Controls. following the directions. It got to 100% then showed it failed to upload. Now when i try to connect the they KYBR wifi, it keeps asking for a password and locks up my mouse. I checked the sd card and its blank. How can I recover it?

    **Community answers:**

    **1. Brian Dodds:**
    > First thing you can try is remove power and wait a few seconds then power back and try to long in again.

    **2. Group Member:**
    > Jon Robinson Brian Dodds tried that a few times, also rebooted a few times

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2462536680745650/){ .md-button }

## Configuration

??? question "I saved the config before upgrading to 2.0 but when I reload it, it's not making the changes. Is there an easy way to re..."

    *Posted by **Cory Hall**:*
    > I saved the config before upgrading to 2.0 but when I reload it, it's not making the changes. Is there an easy way to read the file? I dint want to redo everything if I don't have to

    **Community answers:**

    **1. Jon Robinson:**
    > Follow up: I downloaded Notepad++ with the Json plugin. I puled up my old file and a blank new config file that 2.0 uses. Then found the right settings and updated on my pc.

    **2. Jon Robinson:**
    > Follow up: I downloaded Notepad++ with the Json plugin. I puled up my old file and a blank new config file that 2.0 uses. Then found the right settings and updated on my pc.

    **3. Cory Hall:**
    > The config file is just a txt file and you can read it with notepad

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2762054047460577/){ .md-button }

??? question "When updated to 2.0 the Wifi has been disabled. How do I enable via console? KYBER Controls..."

    *Posted by **Edwin Zuluaga**:*
    > When updated to 2.0 the Wifi has been disabled.  How do I enable via console?
           KYBER Controls           
              Version 2.0.0
        Designed By Stephane Beaulieu     
               and Matt Hobbs           
           stefebeaulieu@gmail.com        
              Dec 2025
     This control system is licensed for
      personal use (non commercial use)
         only under CC BY-NC-ND 4.0
    --------------------------...

    **Community answers:**

    **1. Cory Hall:**
    > You need to install the jumper IN1 to ground.

    **2. Cory Hall:**
    > You need to install the jumper IN1 to ground.

    **3. Edwin Zuluaga:**
    > mine wifi is still not showing up

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2697189903946992/){ .md-button }

??? question "Please give me some advice on the Maestro program. When creating a servo movement program, the Kyber manual has Maestro..."

    *Posted by **Brian Dodds**:*
    > Please give me some advice on the Maestro program.
    
    When creating a servo movement program, the Kyber manual has Maestro settings, but would it be better to set this up before creating a program, creating a script, and saving several pattern files?
    
    Would it be better to create separate script files for Maestro as well, 1 and 2?
    
    For example, would the maestro for the head servo movement be 1 and ...

    **Community answers:**

    **1. Group Member:**
    > Toshio Fujisawa Thank you for your advice. It may be my misunderstanding. I know that only one script can be put into one Maestro. I was told that to control multiple movements individually, you need to put them into the Kyber system and control them.
    > For example, I wonder if I have to create separate programs for the script that moves everything in the demonstration, the script that moves only the arms, and the script that opens the door. Sound can be controlled with the Kyber system, but is the servo control of the Maestro a separate operation? Thank you for your advice. It may be my misunderstanding. I know that only one script can be put into one Maestro. I was told that to control multi...

    **2. Mark French:**
    > https://youtu.be/zkbtoDOW7bI?si=n2RupFy3s-5c4qol YOUTUBE.COM How to Program Maestro and setup animations in Kyber Control HD 1080p

    **3. Brian Dodds:**
    > I believe the maestro only stores one script and the sequences are all separate parts of the one script.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2261897827476204/){ .md-button }

??? question "Question, can the Kyber password be reset buy bumping one of the buttons on the esp32 ? My test rig decided to reset the..."

    *Posted by **Stephane Beaulieu**:*
    > Question, can the Kyber password be reset buy bumping one of the buttons on the esp32 ? My test rig decided to reset the password to the default and just the password the rest of the settings were still intact.

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Yes it’s a safety. If a mistake is made while changing the default ssid/password, after a few try, the Kyber will revert back to default.

    **2. Tim Hebel:**
    > I think it resets if you reboot multiple times in a row

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2256979384634715/){ .md-button }

??? question "Having connection problems with the WIFI, its give network security key is wrong, and will not let me log into wifi, unh..."

    *Posted by **Dave Stapley**:*
    > Having connection problems with the WIFI, its give network security key is wrong, and will not let me log into wifi, unhooked from droid and did USB to the computer and no change, any way to re upload the sketch and reset that way?

    **Community answers:**

    **1. Dave Stapley:**
    > I did the same, I set a complex password which it accepted but then couldn't log in, luckily Stephane looked at my password and told me which characters to get rid of and it worked.

    **2. Christopher Lamb:**
    > If you're a member of the update page you should be able to the links on the page and do a fresh install.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2122259418106713/){ .md-button }
