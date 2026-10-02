# Hardware & Wiring

Kyber board, wiring, servos, Maestro controllers and hardware compatibility.

!!! info "Community Knowledge Base"
    These questions and answers come from the **Kyber Control Systems**
    Facebook group (~2000 members).
    Click on any question to expand the answers.

---

## Kyber Board

??? question "Serial setup questions. I'm trying to use serial to communicate with another ESP32. I have RX/TX/5v/GND plugged into t..."

    *Posted by **Cory Hall**:*
    > Serial setup questions.  I'm trying to use serial to communicate with another ESP32.  I have RX/TX/5v/GND plugged into the top set of Marcduino pins.  I have this connected to the corresponding pins on the external ESP32.  I have clicked to enable Serial Commands.  I selected Button 11 and only entered CL=h0000FF \r (I just want to transmit "CL=h0000FF" via serial) in the line for that button.  Do...

    **Community answers:**

    **1. Group Member:**
    > Chris Carpenter Cory Hall Thanks.  I got one transmission but the data received was definitely not CL=h0000FF.  Haven't got it to work since.  Do you need a space after the command before the \r?  I connected to the USB port of the Kyber. I see button 11 triggering. I don't see anything saying its sending serial commands.  Is there a way to see if its sending the command via Serial Monitor?

    **2. Group Member:**
    > Chris Carpenter Cory Hall Thanks. I got one transmission but the data received was definitely not CL=h0000FF. Haven't got it to work since. Do you need a space after the command before the \r? I connected to the USB port of the Kyber. I see button 11 triggering. I don't see anything saying its sending serial commands. Is there a way to see if its sending the command via Serial Monitor?

    **3. Brian Dodds:**
    > The output from the Kyber is level shifted to 5V logic out.  Your other ESP32 is likely 3.3v logic in.    You will need a level shifter.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2710992415900074/){ .md-button }

??? question "My R2 unit has a lot of LEDs being controlled by WLED. I want to be able to control the colors and effects via touchpad..."

    *Posted by **Cory Hall**:*
    > My R2 unit has a lot of LEDs being controlled by WLED.  I want to be able to control the colors and effects via touchpad.  Can Kyber send JSON commands via serial? WLED has an API that supports JSON over serial.

    **Community answers:**

    **1. Jerrod Hofferth:**
    > Kyber’s serial command character length is pretty limited.
    > You may look into using Greg Hulette’s WCB system as an intermediary. That system can save much longer serial commands that Kyber can then trigger with a very short command.
    > https://github.com/.../Wireless_Communication_Board-WCB/wiki Kyber’s serial command character length is pretty limited. You may look into using Greg Hulette’s WCB system as an intermediary. That system can save much longer serial commands that Kyber can then trigger with a very short command. https://github.com/.../Wireless_Communication_Board-WCB/wiki GITHUB.COM Home

    **2. Jerrod Hofferth:**
    > Kyber’s serial command character length is pretty limited. You may look into using Greg Hulette’s WCB system as an intermediary. That system can save much longer serial commands that Kyber can then trigger with a very short command.https://github.com/.../Wireless_Communication_Board-WCB/wiki Kyber’s serial command character length is pretty limited. You may look into using Greg Hulette’s WCB system as an intermediary. That system can save much longer serial commands that Kyber can then trigger with a very short command. https://github.com/.../Wireless_Communication_Board-WCB/wiki GITHUB.COM Home

    **3. Group Member:**
    > Chris Carpenter Cory Hall This one https://www.amazon.com/dp/B0F8NWLKGP AMAZON.COM ESP32 WLED LED Strip Light Controller 4 Channel Output 15A Fuse Link Level Shifter UART Download DIY Dynamic Lighting Mode APP Voice Control for Digital WS2811 WS2812 WS2815 SK6812 RGB IC String

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2690339174632065/){ .md-button }

??? question "Question for the group. I currently don't run a slip ring for power to the dome; dome has its own batteries. Has anyone..."

    *Posted by **Robert Schubert**:*
    > Question for the group. I currently don't run a slip ring for power to the dome; dome has its own batteries.  Has anyone tried a wireless solution between the Kyber in the body and a Maestro in the dome?  Maybe something like the Feather boards that Kevin Holme was using?

    **Community answers:**

    **1. Brian Dodds:**
    > The more wireless devices in your build and other builds, the more likely interference issues.  Better to use a slip ring hardwired.

    **2. Brian Dodds:**
    > The more wireless devices in your build and other builds, the more likely interference issues. Better to use a slip ring hardwired.

    **3. Craig Gurrie:**
    > Depending on your RC you could have a receiver in both the dome and the body to get the rc signal to both in parallel

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1733026053696720/){ .md-button }

??? question "I do not know anything about kyber control but most of the r2-d2 stuff i have seen wants to use arduino mega adk boards...."

    *Posted by **Stephane Beaulieu**:*
    > I do not know anything about kyber control but most of the r2-d2 stuff i have seen wants to use arduino mega adk boards. But the mega adk is no longer made by the main arduino folks. There is the arduino giga that replaces it and has wifi and Bluetooth and other upgrades.  Does a kyber need an arduino? Will it work with the giga boards ?

    **Community answers:**

    **1. Group Member:**
    > Knightshade von Legion Glenn Pablo agreed... Padawan 360 or Shadow.    ADk used to be the all in one solution for those - but now days more use a mega and a host shield (paying special attention to the chip set).  Not needed Kfor Kyber

    **2. Group Member:**
    > Knightshade von Legion Glenn Pablo agreed... Padawan 360 or Shadow. ADk used to be the all in one solution for those - but now days more use a mega and a host shield (paying special attention to the chip set). Not needed Kfor Kyber

    **3. Stephane Beaulieu:**
    > No need for any Arduino with the Kyber, just a RC remote and receiver.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2540344999631484/){ .md-button }

??? question "Just got my new Kyber Control system this weekend (thanks Matt ) any chance I can get a updated pin out diagram since t..."

    *Posted by **Cory Hall**:*
    > Just got my new Kyber Control system this weekend (thanks Matt 
    ) any chance I can get a updated pin out diagram since this is 1000% different then older models. And 5v input on the power connector???

    **Community answers:**

    **1. Sean Fuchs:**
    > Is there a link to an updated feature list for this new version?  Curious on what is new to see if I should upgrade.  Thx!

    **2. Sean Fuchs:**
    > Is there a link to an updated feature list for this new version? Curious on what is new to see if I should upgrade. Thx!

    **3. Group Member:**
    > Cory Hall Matt Hobbs is the S bus inputs the 3 sets just to the left of the power inputs?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2004037616595561/){ .md-button }

??? question "Howdy from Texas!! Has anyone here used Kyber for a BB-8 with a Joe’s drive set up? I’ve never used Kyber but it seems l..."

    *Posted by **Derek Kastning**:*
    > Howdy from Texas!! Has anyone here used Kyber for a BB-8 with a Joe’s drive set up? I’ve never used Kyber but it seems like it would be easier than all these crazy boards

    **Community answers:**

    **1. Matt Hobbs:**
    > The kyber isn’t designed for BB units. It doesn’t have gyro logic so it won’t give you any balancing control.

    **2. Matt Hobbs:**
    > The kyber isn’t designed for BB units. It doesn’t have gyro logic so it won’t give you any balancing control.

    **3. Chris Neill:**
    > Braiding wires seems like a great idea until you have one bad wire in the bunch.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2069264920072830/){ .md-button }

??? question "Howdy all, Could someone provide a sample syntax for the Kyber to send a command to the Logic Engine via WCB. I have tr..."

    *Posted by **Gary Isle**:*
    > Howdy all,
    Could someone provide a sample syntax for the Kyber to send a command to the Logic Engine via WCB.  I have tried:
    ;W3;S1~RTLE30000\r
    ;W3;S1<~RTLE30000>\r
    ;W3;S1@1T3\r
    ;W3;S1<@1T3>\r
    The logic engine is connected via serial port 1 RX to serial port 1 TX on the WCB.  set at 9600 baud.
    https://github.com/reeltwo/WLogicEngine32
    Current setup is 3 WCB's for Body, dome plate and dome.
    When se...

    **Community answers:**

    **1. Gary Isle:**
    > I'm still struggling with trying to get a serial command to run on the logics. The snapshot is a console connection directly to the logic engine. the syntax i have been using is ~RTLE30008 or ~RTLE30008\r (leia effect for only 8 seconds).

    **2. Gary Isle:**
    > connecting USB and using terminal the commands for logic engine do not work. In an effort to troubleshoot connectivity I was able to pass serial commands to other devices from W3 to W2 and W1 via usb terminal session. Running code from January 25

    **3. Greg Hulette:**
    > Gary Isle , can you control them via the WCB 3 directly? If you use the IDE terminal, and issue any of these commands, does it work?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2448997822099536/){ .md-button }

??? question "Since Matt Hobbs is going to see if he can have the Kyberboards for building B2EMO shipped to the Netherlands, I notice..."

    *Posted by **John Geb**:*
    > Since Matt Hobbs  is going to see if he can have the Kyberboards for building B2EMO shipped to the Netherlands, I noticed that the Kyberboard has a DF player. The B2EMO light logics boards I bought from www.printed-droid.com also have a DF player. Which one should I use if I received the boards from both? greetings from Holland

    **Community answers:**

    **1. John Geb:**
    > Let me know if you have any issues with shipping, I recently shipped a couple circuit boards to Germany. Took a while and was kinda confusing but it worked out

    **2. Ben Rieß:**
    > Use the Kyber Sound system 
    > My system was originally designed for other controls Use the Kyber Sound system My system was originally designed for other controls

    **3. Group Member:**
    > Maikel Jegerings Matt Hobbs For your information....

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2494745770858074/){ .md-button }

??? question "Loss of radio signal when R2D2 is moving aroung when standing within 10 feet of it. After regaining signal it restarts..."

    *Posted by **Cory Hall**:*
    > Loss of radio signal when R2D2 is moving aroung when standing within 10 feet of it.  After regaining signal it restarts start-up song and panel movement.  Using FrySky x20 and TD R10. What could be causing this? Transmitter is showing 100% on the screen for both frequency antennas.
    I'll re-address issue after drafting circuit design to help those helping.

    **Community answers:**

    **1. Jason Charlton:**
    > I'll add that I encountered a similar issue with B2 and in retrospect it was entirely obvious what I did wrong. Kyber was being powered off of the same voltage regulator as the servos and when Bee started up and all the servos reset, the current draw was high enough to cause a voltage drop, resulting in the Kyber rebooting. It got stuck in a loop and I just kept hearing my transmitter telling me "telemetry lost, telemetry restored". Switched things around so the Kyber is no longer downstream of a regulator and it's worked perfectly ever since. It's great that Kyber runs off of full battery voltage.

    **2. Mark Enright:**
    > Are you sure it is the radio which is loosing signal, would be very unusual. You would need to post more information, circuit design, what ESC you are using etc so it would be easier to diagnose the issue.

    **3. Matt Hobbs:**
    > Sounds like something is loosing power. Maybe a loose connection or possibly something pulling to much power through the kyber or the receiver. Would need to see your wiring diagram

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2208089772857010/){ .md-button }

??? question "Hi, I am building a B2 (mr baddeley). Already have the frsky x20s and a tdr10 receiver. I have already ordered a kyber b..."

    *Posted by **Steven Sloan**:*
    > Hi,
    I am building a B2 (mr baddeley). Already have the frsky x20s and a tdr10 receiver.
    I have already ordered a kyber board and have the  kyberpad working but what should I use for motor controllers? I have already ordered 6 gobilda ones but all I can see here are  Sabertooths and Syrens.
    Do I have to cancel my order or can these be configured too?
    Have not found any B2 specific wiring, are there...

    **Community answers:**

    **1. Group Member:**
    > Stephane Beaulieu 2 years ago when Baddeley B2 V1 was released, I did a custom version of the Kyber to control B2EMO. All the mixing was made internally in the code. This was helping a lot with the need for more channels then what the remote could handle. Has of today with the newer remote and ETHOS I would recommend using the Kyber as is and do most of the mixing in the remote itself like Michael McMaster and David did. Kyber will be used for sounds and different animation if needed.

    **2. Group Member:**
    > Rafa Martin Steven Sloan I am a bit confused with the Kyber system… can I use the Gobilda drivers with it? Or do I need to use sabertooth?
    > Where is the mixing done?
    > Any schematics por B2 available? Steven Sloan I am a bit confused with the Kyber system… can I use the Gobilda drivers with it? Or do I need to use sabertooth? Where is the mixing done? Any schematics por B2 available?

    **3. Steven Sloan:**
    > The Gobilda drivers can be fitted to the feet using industrial velcro (hook & loop).
    > Photo courtesy of Michael McMaster and Dave David Ferreira The Gobilda drivers can be fitted to the feet using industrial velcro (hook & loop). Photo courtesy of Michael McMaster and Dave David Ferreira

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2385230131809639/){ .md-button }

??? question "Any advice would be appreciated. Two Maestros are used to control the chopper, and the Kyber board has two sets of pins..."

    *Posted by **Kenzō Barlow**:*
    > Any advice would be appreciated.
    Two Maestros are used to control the chopper, and the Kyber board has two sets of pins for the Maestros. Do Maestros 1 and 2 come from the same place? Or do they go where the arrows show in this photo? 
    There are two Maestros on the Kyber. Should the pins go on the top or bottom?

    **Community answers:**

    **1. Group Member:**
    > Toshio Fujisawa Thank you very much.
    > Is it correct to distribute control of two Maestro's from this pin? Thank you very much. Is it correct to distribute control of two Maestro's from this pin?

    **2. Kenzō Barlow:**
    > Made the same mistake I did, all the Maestros pins need to go on the 2nd row not the 1st

    **3. Brian Dodds:**
    > First row is Marcduino pins, 2nd row are Maestro pins.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2276267942705859/){ .md-button }

??? question "Hello again. I'm trying to use Kyber with HCR but I can't get it to work. The board connected via USB and tested on a PC..."

    *Posted by **Trevor Zaharichuk**:*
    > Hello again. I'm trying to use Kyber with HCR but I can't get it to work. The board connected via USB and tested on a PC works correctly, but with Kyber it doesn't do anything.
    Is it necessary to have the V125 version installed? I have V123.
    I really don't know what can happen. I'm leaving an image of what I have set on button 1.
    Thanks!!!

    **Community answers:**

    **1. Ricardo Juntas Asensio:**
    > I think I'll do a simple test. I'll use an arduino board, connect it to the HCR via serial port and see if that works. That way I'll know if the problem is in the HCR (config file for example, or in the sd card) or it's in the Kyber output.
    > As soon as I can do it I'll let you know. I think I'll do a simple test. I'll use an arduino board, connect it to the HCR via serial port and see if that works. That way I'll know if the problem is in the HCR (config file for example, or in the sd card) or it's in the Kyber output. As soon as I can do it I'll let you know.

    **2. Ricardo Juntas Asensio:**
    > Problem solved!! I just changed the SD card and all works fine!!
    > Thanks to all for the help!! Problem solved!! I just changed the SD card and all works fine!! Thanks to all for the help!!

    **3. Trevor Zaharichuk:**
    > Did you setup the config file on the HCR to enable the serial port you are connected to and the baud rate?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2267241663608487/){ .md-button }

??? question "Help and/or guidance needed. Have Kyber, plus marcduinos and maestros, but also have the HCR vocalizer (using the fanta..."

    *Posted by **Trevor Zaharichuk**:*
    > Help and/or guidance needed.  Have Kyber, plus marcduinos and maestros, but also have the HCR vocalizer (using the fantastic add-on board by Trevor Zaharichuk) BUT I cannot figure out a good way to connect all three using only the two main outputs (marcduino/masestro) from the kyber.  Does anybody have experience with the RS-485 connector between kyber and HCR vocalizer board?  they both have what...

    **Community answers:**

    **1. Andrew S Harris:**
    > I guess I really needed some clarification on the marcduino port just being a serial port, which is what it is, nothing super special about it. So can use that port for all communications to other serial ports via Greg Hulette's Wireless Communication Boards. Big shout out to Cory Hall for helping me get back on track.

    **2. Trevor Zaharichuk:**
    > For the cable you only need the 4 wires. A to a, b to b. If you have an external 5V supply for the vocalizer then don't connect the 5V pin. But I think the kyber should have enough power to power up the vocalizer as well.

    **3. Brian Dodds:**
    > Make a Y cable with Kyber TX signal and ground. Send one to MDs RX and one to HCR RX. No need to hook up MD TX to the Kyber, that's only used by the R2Touch App.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2206060099726644/){ .md-button }

??? question "On the Kyber Board where it reads 'Marcduino', there are two of pins. The 1st pin is Gnd, the 2nd is 5v, etc, etc. I h..."

    *Posted by **Matt Hobbs**:*
    > On the Kyber Board where it reads "Marcduino", there are two of pins. The 1st pin is Gnd, the 2nd is 5v, etc, etc. 
    
    I have the row of gnd and 5v running to power the body Maestro Board.
    
    1. Can I use the second row of gnd and 5v to run the same Maestro Board for the servos? 
    
    2.  The Maestro Board has three LEDs. Red, Yellow and Green.  What should be lit with power to the board for both the boar...

    **Community answers:**

    **1. Group Member:**
    > Al Cordera Matt Hobbs well, I did it before reading this post thinking that as long as I don't have servos plugged in the Maestro pulling power it won't harm it.
    > Now I have no lights on the kyber board at all. Yup, I'm a dumb ass, but it sounded logical.
    > Any way of fixing the kyber board? Matt Hobbs well, I did it before reading this post thinking that as long as I don't have servos plugged in the Maestro pulling power it won't harm it. Now I have no lights on the kyber board at all. Yup, I'm a dumb ass, but it sounded logical. Any way of fixing the kyber board?

    **2. Matt Hobbs:**
    > No….DO NOT power your servos through the Kyber. The power supply on this board is only rated for 2 amps. You will burn up the power supply.

    **3. Group Member:**
    > Matt Hobbs Cory Hall you can power the logic side of the maestros with the Kyber. Just do not power the servos.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2145810649084923/){ .md-button }

??? question "Hello. i'm thinkig about purchase the embedded R2-D2 Vocalizer. In the documentation, it say that the support for Kyber..."

    *Posted by **Ricardo Juntas Asensio**:*
    > Hello.
    i'm thinkig about purchase the embedded R2-D2 Vocalizer. In the documentation, it say that the support for Kyber is coming soon. Is this true? 
    If yes, i have a couple of doubts that i need to solve before to purchase the vocalizer board.
    - Will be compatible the vocalizer with marcduino? I'm thinking about they would use the same serial port for both....
    - What about the volume control? I ...

    **Community answers:**

    **1. Group Member:**
    > Ricardo Juntas Asensio Alec Muir Thanks
    > But i think i haven't express my self correctly. I don't say that the marcduino send serial data to the vocalizer. I'm thinking that kyber send serial data directly to vocalizer. Currently, i use a serial port from Kyber to send data to marcduino (only for sequences), so my fear is that kyber use the same serial port for comuinicated with the vocalizer. I hope use a different serial port and that both will be compatible. I know this is a question for the Kyber team Alec Muir Thanks But i think i haven't express my self correctly. I don't say that the marcduino send serial data to the vocalizer. I'm thinking that kyber send serial data directly to vocal...

    **2. Alec Muir:**
    > From the vocaliser perspective,
    > 1. Marcduino can run serial commands for which the vocalizer can read and react to
    > 2. There are commands to adjust the volume of all three channels on the boards
    > For Kyber support, I’ll defer to the team. From the vocaliser perspective, 1. Marcduino can run serial commands for which the vocalizer can read and react to 2. There are commands to adjust the volume of all three channels on the boards For Kyber support, I’ll defer to the team.

    **3. Matt Hobbs:**
    > The new kyber boards that are currently being tested will have additional serial ports plus I2C and RJ45 connection points. The plan for the older boards is to make an adapter board that will replace the sound board on the kyber and that will attach to the vocalizer. There are a lot of things to still plan out.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1870572929942031/){ .md-button }

??? question "How do you integrate the Marcduino 2.0 to the kyber system. Looking at the Marcduino version 2.0. Both the Marcduino P..."

    *Posted by **Jacob Amundsen**:*
    > How do you integrate the Marcduino 2.0 to the kyber system.  Looking at the Marcduino version 2.0.  Both the Marcduino PCB's don't have serial silkscreened on any of the connections.  They include the following: 
     debug which has:  -,+RX &TX.  
     aux ports:  -,+ & S  
     RC in:  -,+ & S
    
    Alternatively if the Marcduino 2.0 doesn't support serial can it be connected via i2c?

    **Community answers:**

    **1. Brian Dodds:**
    > There is a way to hook up serial to the 2.0 master. Trying to remember how.... I want to say you hook the Kyber MD TX to the Master DEBUG RX and a shared ground.
    > No, you can't use I2C.
    > I wouldn't use a maestro instead because all the other functionality would be lost.
    > I run Kyber with MD in my dome and it's great! ￼￼ There is a way to hook up serial to the 2.0 master. Trying to remember how.... I want to say you hook the Kyber MD TX to the Master DEBUG RX and a shared ground. No, you can't use I2C. I wouldn't use a maestro instead because all the other functionality would be lost. I run Kyber with MD in my dome and it's great! ￼￼

    **2. Jacob Amundsen:**
    > Do you mainly want it for servo control? Because I ended up using a maestro in the dome for servo control (easier to program) and then I used Greg Hulette's wireless control boards to send serial from the Kyber up to the dome to control my logics, magic panel, holos, periscope, and more. It was easier for me to customize.

    **3. Gary Isle:**
    > Thanks guys for the input. As Brian suggested I connected via the debug and was able to pass Marcduino commands. Jacob could you provide an example of the syntax you use for the logics and periscope.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2201929960139658/){ .md-button }

??? question "Has anyone deisgned a mount for the Kyber Board? I'm building R-DUO's elcetrical panel and was hoping to skip a step if..."

    *Posted by **Tim Hebel**:*
    > Has anyone deisgned a mount for the Kyber Board?  I'm building R-DUO's elcetrical panel and was hoping to skip a step if someone has it done already.

    **Community answers:**

    **1. Matt Hobbs:**
    > I have a box that it can go in. You could build off if that. I think it’s in the files section

    **2. Group Member:**
    > Tim Hebel Matt Hobbs Thanks, I don't know Why I did not see that. I even looked in the files section... hehe.

    **3. Stephane Beaulieu:**
    > I don’t think so… as always you will need to design a new part Tim Hebel

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1751857645146894/){ .md-button }

??? question "I received this guy in the mail today. I’d like to snap off these side pieces in order for this board to fit. Is that po..."

    *Posted by **Jody Smith**:*
    > I received this guy in the mail today. I’d like to snap off these side pieces in order for this board to fit. Is that possible to do so or is that part functional in some way?

    **Community answers:**

    **1. Brian Dodds:**
    > Those are manufacturing parts that can snap off ￼

    **2. Trevor Zaharichuk:**
    > You can snap those off carefully no problem.

    **3. Jody Smith:**
    > It just barely fits

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2017803755218947/){ .md-button }

??? question "I'm to understand and compile a list of everything I'd need for a R2 build. Can I control logic and holo lighting (Astro..."

    *Posted by **Brian Dodds**:*
    > I'm to understand and compile a list of everything I'd need for a R2 build. Can I control logic and holo lighting (Astropixels  probably) with Kyber? Would they connect through a Maestro or directly to the Kyber board?

    **Community answers:**

    **1. Brian Dodds:**
    > I use it to control Marcduino's and they control the logic and holo lighting. I recommend Joymonkey logics over Astropixels. You can control anything that accepts serial commands at 9600 baud.

    **2. Group Member:**
    > Andrew Oldham Brian Dodds thanks. I'll take a look at Joymonkey logics

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2570408579958459/){ .md-button }

??? question "Hello everyone! With permission from admin, I would like to share with you all my capstone project I have been working..."

    *Posted by **Steven Dodds**:*
    > Hello everyone! 
    With permission from admin, I would like to share with you all my capstone project I have been working on for the past few months. 
    Me and my group partner are preparing to present our project, named Astraeus, which is a prototype solar support rover for mars. 
    As a summary:
    NASA wants manned missions on mars by 2026 and to power stations on mars is extensive and dangerous with RT...

    **Community answers:**

    **1. Group Member:**
    > Mark Figueroa Steven Dodds it doesn’t but admin allows me to post for those who want to contribute to my survey. If you don’t that’s totally fine

    **2. Steven Dodds:**
    > That’s cool.
    > But what does it have to do with Kyber Control Systems?? That’s cool. But what does it have to do with Kyber Control Systems??

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2461341224198529/){ .md-button }

??? question "Hello. I have a question about Kyber and the HCR board. I'm using the Kyber serial output to connect to my R2's marcduin..."

    *Posted by **Cory Hall**:*
    > Hello. I have a question about Kyber and the HCR board. I'm using the Kyber serial output to connect to my R2's marcduino boards. Taking this into account, can I connect Kyber with HRC in some way?
    Thanks!!

    **Community answers:**

    **1. Group Member:**
    > Ricardo Juntas Asensio Cory Hall Then I would put both instructions (marcduino & HRC) in the same place in kyber app?

    **2. Cory Hall:**
    > Yes you can y the wires

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2266229117043075/){ .md-button }

??? question "I immediately printed out the board base and switch cover. Which is the correct orientation of the switch in relation to..."

    *Posted by **Kenzō Barlow**:*
    > I immediately printed out the board base and switch cover. Which is the correct orientation of the switch in relation to the cover?
    Buttons are different lengths
    Board switch No.01 is short, No.15 is long

    **Community answers:**

    **1. Kenzō Barlow:**
    > I don't own one but just a guess, the button cover looks sloped so I assume the buttons that are taller will face the top of the slope so all the buttons poke out of the cover at the same height.

    **2. Cory Hall:**
    > Matt Hobbs I'm sure you know.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2251487885183865/){ .md-button }

??? question "Question I’m trying to send a serial command for random events to turn on HCR random emotes and nothing happens but I ca..."

    *Posted by **Stephane Beaulieu**:*
    > Question I’m trying to send a serial command for random events to turn on HCR random emotes and nothing happens but I can send that same command on any of the buttons and works just fine what am I forgetting to add ?

    **Community answers:**

    **1. Brian Dodds:**
    > The formatting should be the same for both. Maybe the switch is not set right?

    **2. Stephane Beaulieu:**
    > Did you enable HCR support under General web page ?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2143344122664909/){ .md-button }

??? question "I’m in the process of wiring the 15 button board into my FRSky QX7s and I have a question: Does the 2 position (momentar..."

    *Posted by **Michael Shugg**:*
    > I’m in the process of wiring the 15 button board into my FRSky QX7s and I have a question: Does the 2 position (momentary) switch on the right need to be replaced with a 2 position (on-off) switch in order to switch Wi-Fi on and off? I’m trying to do everything while I have the case open.

    **Community answers:**

    **1. Group Member:**
    > Michael Shugg Steven Dodds Thanks for the reply. To confirm, the momentary switch will function to toggle between the 2 pages of buttons. Based on location on my TX this is opposite of the orientation in the manual. Sorry if I’m being dense. It’s just that I’m an RC nube and not certain on TX setup yet.

    **2. Steven Dodds:**
    > No
    > Use one of the other switches for that.
    > You can use the momentary like a shift key to have twice as many buttons!
    > (Well almost, the STOP button is always the same) Use one of the other switches for that. You can use the momentary like a shift key to have twice as many buttons! (Well almost, the STOP button is always the same)

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1795204757478849/){ .md-button }

??? question "The R2-D2 Vocalizer Human-Cyborg Relations Vocalizers just found it digging on the net, I see they said Kyber support wa..."

    *Posted by **Cory Hall**:*
    > The R2-D2 Vocalizer Human-Cyborg Relations Vocalizers just found it digging on the net, I see they said Kyber support was coming soon on a post from 6 months ago. Can one of the Admin share any info ? I kinda like the idea of a less "canned" approach to R2's

    **Community answers:**

    **1. Tim Hebel:**
    > I have a V2 Kyber board. I am going to see if I can use the Serial commands from the Marcduino field to trigger the HCR. I think this should work. However, I also want to send commands to the Roam-A-Dome system.

    **2. Max Cervantes:**
    > Ohh very cool I’d be interested in this too

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2050281798637809/){ .md-button }

## Wiring

??? question "I'm back... Y'all I am pretty tech savvy IDK why this is whipping me. X20S TDR6 rcvr Everything!!!! is updated to the la..."

    *Posted by **FrSky Ben**:*
    > I'm back... Y'all I am pretty tech savvy IDK why this is whipping me.
    X20S
    TDR6 rcvr
    Everything!!!! is updated to the latest firmware.
    I for the life of me cannot get a radio signal now.
    I briefly had one last night before all the firmware updates but now nada... I have double checked wiring and I am using the white wire on the micro connector. I am just at a loss maybe I need a different receiver...

    **Community answers:**

    **1. FrSky Ben:**
    > need more info... Did you enable the Kyberpad lua source ? Did you set up a mix for the Kyberpad lua source ? What channel did you assign the Kyberpad lua source on the mix to ? Did you enter the channels on the Kyberpad RC input page ?

    **2. FrSky Ben:**
    > need more info... Did you enable the Kyberpad lua source ? Did you set up a mix for the Kyberpad lua source ? What channel did you assign the Kyberpad lua source on the mix to ? Did you enter the channels on the Kyberpad RC input page ?

    **3. Jackie Wah:**
    > dumb question - have you just tested the tdr6 (power with 5v) and coonect a servo on ch1, pair it with reciever and see if reciever can move the servo  (without kyber) ??

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2721806924818623/){ .md-button }

??? question "So I am currently having trouble with trying to get the Maestro to work. What will happen is that it will work when plug..."

    *Posted by **Stephane Beaulieu**:*
    > So I am currently having trouble with trying to get the Maestro to work. What will happen is that it will work when plugged into the computer but when I unplug it nothing will happen. I’ve double checked the wiring and it seems to be correct, at least I thought it was. Would anyone be able to help me with this issue please? Here is a video of what is happening and photos of how I have it wired
    Tha...

    **Community answers:**

    **1. Group Member:**
    > Nick Marino Stephane Beaulieu Update few of the wires went bad, I was able to repair it

    **2. Group Member:**
    > Nick Marino Stephane Beaulieu Update few of the wires went bad, I was able to repair it

    **3. Group Member:**
    > Nick Marino Tyler Bower Few of the wires went bad I was able to figure it out

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2688445551488094/){ .md-button }

??? question "Hi gang. When connecting the Kyber to an SBUS receiver and Syren and Sabertooth, do I connect the positive wire from Kyb..."

    *Posted by **Robert Schubert**:*
    > Hi gang. When connecting the Kyber to an SBUS receiver and Syren and Sabertooth, do I connect the positive wire from Kyber to SBUS and a positive from saber or Syren to SBUS? Or just either kyber or saber? Thanks!

    **Community answers:**

    **1. Matt Hobbs:**
    > ONLY connect one power source to the receiver.  I would suggest powering the receiver from the Kyber.  If you are controlling the saber and the syren from the same receiver then you will only need signal and ground from them connected to the Kyber. Check out the wiring diagrams in the new Kyber manual.

    **2. Matt Hobbs:**
    > ONLY connect one power source to the receiver. I would suggest powering the receiver from the Kyber. If you are controlling the saber and the syren from the same receiver then you will only need signal and ground from them connected to the Kyber. Check out the wiring diagrams in the new Kyber manual.

    **3. Brian Dodds:**
    > Kyber, Syren and Sabertooth all get powered on their own and have 5V outputs for the RX.   Pick ONE of those 5V to power the RX and do not hook up the other two 5V wires.  If you do and all three get hooked up you can damage one or more of the components.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2069600423372613/){ .md-button }

??? question "Thought I would share my experience with this crowd. So I finished wiring all of the relays and RC controls on the head..."

    *Posted by **Jose Velazquez**:*
    > Thought I would share my experience with this crowd. So I finished wiring all of the relays and RC controls on the head of the probe. They would switch, but no voltage (light would turn on). I took out the volt meter and tested it at the relay 10.5v ??? Tested it at the source (head fuse box) 10.6v … it goes from another source through a slip ring to the dome. So I tested the body source 10.6v, th...

    **Community answers:**

    **1. Scott Smith:**
    > That block... I had it. Theres a light that comes on when you blow a fuse? It's problematic and I returned it. Mine was slightly low also, I read a few reviews and other people had the same issue. There was a work around, but I can't remember what it was now.

    **2. Thomas LeBlanc:**
    > Sounds like a connection internal to that block, that should be 0 ohms, is faulty and sitting somewhere around 1.5-2 ohms in order to get that voltage drop at 1 amp. If it was me, I'd ditch it and get a quality unit from some place like Blue Sea Systems.

    **3. Group Member:**
    > Jose Velazquez Thomas LeBlanc I think I’m going to do that man… you just can’t go cheap with this….

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2101922573473731/){ .md-button }

??? question "does any one know If you can bind more than one tdr10 receiver to the same model? by doing this I could have one in the..."

    *Posted by **Greg Hulette**:*
    > does any one know If you can bind more than one tdr10 receiver to the same model?  by doing this I could have one in the the body and one in the dome. reducing the lioad os a slip ring. and getting more direct servo connections.

    **Community answers:**

    **1. Group Member:**
    > Austin Heinrich Greg Hulette how does one wire up the servo pass through?  When I was purchasing all my electronics over a year ago that was what I thought the maestro would do. Then some one told me I was going to have to do some coding to have the maestro work the servos in my dome.  So I have been looking for other ways to control the servos ever since.

    **2. Group Member:**
    > Austin Heinrich Greg Hulette how does one wire up the servo pass through? When I was purchasing all my electronics over a year ago that was what I thought the maestro would do. Then some one told me I was going to have to do some coding to have the maestro work the servos in my dome. So I have been looking for other ways to control the servos ever since.

    **3. Jason Charlton:**
    > You definitely can - but after you bind the second receiver, within your transmitter open the options for the second receiver and you can "remap" all the pins/channels to different values - so pin 1 on the second receiver becomes CH11, and so on, otherwise, if I'm not mistaken, both receivers CH1 will operate simultaneously.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2589627114703272/){ .md-button }

??? question "Is there a way with kyber to talk to multiple serial devices? I see the board has a marcduino and maestro. I was lookin..."

    *Posted by **Chase Norman**:*
    > Is there a way with kyber to talk to multiple serial devices?  I see the board has a marcduino and maestro. I was looking at adding hcr and roam a dome which both take serial commands, but I assume I need to pick one of those and put it as the marcduino?
    I could put a wcb as well and have that be the standard serial (marcduino) and then connect both to that. 
    I also see there is an option for pwm ...

    **Community answers:**

    **1. Brian Dodds:**
    > I have marcduino and HCR, roam a dome and other things all hooked up without issue.The marcduino can also forward commands to other devices using the custom extension commands.  Thats how my periscope in the dome works. I have marcduino and HCR, roam a dome and other things all hooked up without issue. The marcduino can also forward commands to other devices using the custom extension commands.  Thats how my periscope in the dome works.

    **2. Brian Dodds:**
    > I have marcduino and HCR, roam a dome and other things all hooked up without issue.
    > The marcduino can also forward commands to other devices using the custom extension commands. Thats how my periscope in the dome works. I have marcduino and HCR, roam a dome and other things all hooked up without issue. The marcduino can also forward commands to other devices using the custom extension commands. Thats how my periscope in the dome works.

    **3. John Geb:**
    > You should have no issue with multiple devices receiving serial command. The issue arises when you multiple device transmitting. You can only have one. You can use a 2:1 mux to activate multiple devices transmitting on a single serial line.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2585755048423812/){ .md-button }

??? question "I'm thrilled to have my Kyber Control System up and running with my X20S (thanks Cory Hall!) Now to connect it to my Mar..."

    *Posted by **Michael Ostrom**:*
    > I'm thrilled to have my Kyber Control System up and running with my X20S (thanks Cory Hall!) Now to connect it to my Marcduinos. Anyone know where on my Marcduinos I should connect my Kyber Marcduino output onto my Marcduinos?

    **Community answers:**

    **1. Brian Dodds:**
    > If you have one of the Xbee interface boards that let you run the Xbee and Kyber at the same time you plug the Kyber MD out to one of the interface boards inputs along with a shared ground.   If you don't ￼have the Xbee interface board then you plug the Kyber MD out into the MD master RX input pin where the Xbee would have been hooked up along with a shared ground.  ￼(can't use the Xbee and Kyber at the same time without the interface board)

    **2. Brian Dodds:**
    > If you have one of the Xbee interface boards that let you run the Xbee and Kyber at the same time you plug the Kyber MD out to one of the interface boards inputs along with a shared ground. If you don't ￼have the Xbee interface board then you plug the Kyber MD out into the MD master RX input pin where the Xbee would have been hooked up along with a shared ground. ￼(can't use the Xbee and Kyber at the same time without the interface board)

    **3. Thomas Arroyo:**
    > Installed my XBee Interface board and it is working with R2 Touch.  Now to figure out how to program the kyber buttons.  I’m getting closer now as I’m also up and running with the X20RS.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2013221725677150/){ .md-button }

??? question "Well I'm making the switch from Shadow MD to Kyber Control so I figured now was as good a time as any to update the wiri..."

    *Posted by **Jacob Amundsen**:*
    > Well I'm making the switch from Shadow MD to Kyber Control so I figured now was as good a time as any to update the wiring diagram.
    I'd love any feedback yall have, especially when it comes to the relay with the master switch. I've never used a relay before, so I'm not certain on the wiring. My master switch is rated for 20A but I'm not sure what the maximum current draw of my droid is so better t...

    **Community answers:**

    **1. Matt Hobbs:**
    > One thing I see is to use the kybers 4 pin connector to send the signal and the power to the maestros logic side input. Do not connect the power jumper on the maestro. Then run the voltage that you will be running for your servos into the maestro or run the power to the servos separately if they are not all the same voltage. Then tun all the signal wires and a ground to the servos.

    **2. Matt Hobbs:**
    > One thing I see is to use the kybers 4 pin connector to send the signal and the power to the maestros logic side input. Do not connect the power jumper on the maestro. Then run the voltage that you will be running for your servos into the maestro or run the power to the servos separately if they are not all the same voltage. Then tun all the signal wires and a ground to the servos.

    **3. Group Member:**
    > Jacob Amundsen Anthony DeFrancesco Outer Rim is a pcb board designed by the brilliant Douglas A. Bickert to better manage dome wiring. I like the marcduinos for some of the settings to control lights, sounds, holos, and dome servos. It works in tandem with Kyber from what I understand.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2044162422583080/){ .md-button }

??? question "Sorry guys, I have a question. I'm stuck right now because I'm kind of stuck in my head. If I connect 5V to an ESP32 and..."

    *Posted by **Tim Hebel**:*
    > Sorry guys, I have a question. I'm stuck right now because I'm kind of stuck in my head.
    If I connect 5V to an ESP32 and then turn it on, it activates the ESP and starts the program on it. Is there any way to activate an ESP32 with a Maestro, or to supply it with power? Or with the Kyber? I'm looking for a way to simply start an ESP, like with a switch.

    **Community answers:**

    **1. Tim Hebel:**
    > I would use the a pin on the Maestro as a trigger for your program on the esp32. (Check it can handle a 5V input on a pin or use a board that can.) Just amend your code to trigger when the voltage goes to 5V (HIGH) on the input pin you choose.
    > You could power the microcontroller with the 5V power but then you have to wait for it to boot before action you want to trigger happens. Although it is easier to implement a power-on strategy as you don't have to edit the code. A more elegant strategy is to trigger it via code. I have done both, but prefer the trigger approach. I would use the a pin on the Maestro as a trigger for your program on the esp32. (Check it can handle a 5V input on a pin or ...

    **2. Group Member:**
    > Dejan Delic Tim Hebel Is this a relay, like the ones you're used to? I used one here too, but somehow I can't get it to work the way I want it to. I've assigned the relay to channel 2 on the Maestro6, and when I start the warning light servo, the relay also gets power and activates the ESP with the program. But when I turn the servo down, the relay isn't supposed to get any more power. But here the light stays on. It's stationary, and only two LEDs are lit. But it's not off. It's as if there's still residual current flowing through it. It's really annoying.

    **3. Matt Hobbs:**
    > These relays are great for Turing things on and off with either the maestro or a switch on the transmitter
    > Apex RC Products RC Remote... https://www.amazon.com/dp/B07BKSGW3D... These relays are great for Turing things on and off with either the maestro or a switch on the transmitter Apex RC Products RC Remote... https://www.amazon.com/dp/B07BKSGW3D... AMAZON.COM Apex RC Products RC Remote Electronic AUX Channel On/Off Switch #9025

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2513867032279281/){ .md-button }

??? question "Hello Kyber group, I need assistance with my Kyber to Maestro communication. The sounds plays fine pressing the assigned..."

    *Posted by **Brian Dodds**:*
    > Hello Kyber group,
    I need assistance with my Kyber to Maestro communication. The sounds plays fine pressing the assigned button on the Kyberpad but no servo movement. 
    I left Sequence 0 blank and added the quit line in the script with no  improvements. And using premade cables to connect the two to make sure it's not a connection issue (RX 2 TX/TX 2 RX). The servo and sequence runs just fine if I'...

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Wiring look good, but I am not sure about the soldering of the serial pins on the bottom of the Maestro, maybe it's only the picture ? remove return on line 7-16 and 25.

    **2. Group Member:**
    > Tim Hebel Hehe, I did the same thing on R2-DEVO. The print is soooo small. The good news is I have Marcduino, Maestro, and HCR working. Roam-A-Dome is getting added to the Mix today.

    **3. Matt Hobbs:**
    > I don’t think you need both the quit and the return command. Remove the return command from each of the 2 sequences

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2256385061360814/){ .md-button }

??? question "I'm still new to electronics so please bear with me. Going with the x20r controller. Will have a maestro for body and..."

    *Posted by **Matt Hobbs**:*
    > I'm still new to electronics so please bear with me.  Going with the x20r controller.  Will have a maestro for body and one for the dome.  One thing I'm confused with is the need for marcduino.  Can someone please tell me what the use is for and will I need one for body and one for dome.  Also, what does Mowee's Xbee interface do?  Does the interface allow the use of the screen buttons on the x20r...

    **Community answers:**

    **1. Brian Dodds:**
    > Marcduinos are plug and play dome controllers that control all dome systems and have many preprogrammed sequences.  The Kyber can be used to control them with no need to program your own sequences.  I don't see a need for the extra MD master in the body, using a maestro there makes more sense.  The Mowee Xbee interface lets you hookup and use both the Kyber and R2Touch app via the Xbee  to control the MDs in the dome.

    **2. Brian Dodds:**
    > Marcduinos are plug and play dome controllers that control all dome systems and have many preprogrammed sequences. The Kyber can be used to control them with no need to program your own sequences. I don't see a need for the extra MD master in the body, using a maestro there makes more sense. The Mowee Xbee interface lets you hookup and use both the Kyber and R2Touch app via the Xbee to control the MDs in the dome.

    **3. Matt Hobbs:**
    > The marcduino is not required. It is another control system that existed before the kyber came along. There are builders that already have the marcduino installed and they wanted the ability to keep using it but also have the control that the kyber system offers.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2630136763985640/){ .md-button }

??? question "I have a first gengeneration Kyber control in my R-DUO. I’ve added Roam-A-Dome to him. RAD can accept serial commands..."

    *Posted by **Tim Hebel**:*
    > I have a first gengeneration Kyber control in my R-DUO.  I’ve added Roam-A-Dome to him.  RAD can accept serial commands to perform actions.  The commands look a lot like Marcduino serial strings.  Where do I connect the serial output to talk to the RAD?

    **Community answers:**

    **1. Tim Hebel:**
    > So, I've read the discussion on the 3.3 vs 5V interface between Kyber and Roam-A-Dome. I am not super familiar with the architecture of these chips. But to sum up it seems a modified Kyber V1 board would output 5V and the R-A-D board is expecting 3.3V? So, sending a 5v signal to would be bad.
    > I have a couple of questions. Could the V1 board be modded to send 3.3V information? Maybe add a resistor?
    > Does a V2 board have the same issue? I have one that I was planning on using for R5, but I could swap it to R-DUO. So, I've read the discussion on the 3.3 vs 5V interface between Kyber and Roam-A-Dome. I am not super familiar with the architecture of these chips. But to sum up it seems a modified K...

    **2. Trevor Zaharichuk:**
    > Is roam a dome a 3.3V or 5V interface. I believe your Kyber would be 3.3 if just simply connecting it to the ESP32 pins. If you're going through the translator then it would be 5V. Just something to check to ensure you have the correct voltages. The ESP32 may not be happy if a 5V signal is applied to it.

    **3. Tim Hebel:**
    > Hmm I did the mod. I tested the connection to the ground pin and I test continuity for the jumper wires. How can I troubleshoot the connection as it doesn’t seem to send commands. Baud is set at 9600. Do I have to explicitly send a \r at the end of the text strings?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1976765942656062/){ .md-button }

??? question "Wiring up my Kyber system today! I've got everything working but Rome a Dome. Anyone have any instructions on how to wir..."

    *Posted by **Jacob Amundsen**:*
    > Wiring up my Kyber system today! I've got everything working but Rome a Dome. Anyone have any instructions on how to wire the syren, receiver and RAD board? I know it's PWM not serial but I seem to just be stuck...

    **Community answers:**

    **1. Group Member:**
    > Jacob Amundsen Cory Hall I only have power in the 5v terminal. What's your setup? Does it go from receiver (ground and data on pin 1) to the RAD PWM input and then from RAD PWM output to the ground and serial one on the syren?

    **2. Group Member:**
    > Jacob Amundsen Cory Hall I only have power in the 5v terminal. What's your setup? Does it go from receiver (ground and data on pin 1) to the RAD PWM input and then from RAD PWM output to the ground and serial one on the syren?

    **3. Cory Hall:**
    > One thing that is VERY important do not run power in anywhere but the green 5v power input. I killed 2 RADs by having power on the pwm inputs

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2049460948719894/){ .md-button }

??? question "Hello everyone. So I'm at the point where I am trying to get my B2 to walk for the first time. I got everything wired up..."

    *Posted by **Cricket Lee**:*
    > Hello everyone. So I'm at the point where I am trying to get my B2 to walk for the first time. I got everything wired up (or so I thought) and I'm running into an issue.
    I can't seem to activate the Maestro 18 through the Kyber/Receiver but I'm able to activate the servos through the Maestro USB interface. Then the other weird thing is this...my Sabertooths are behaving very odd. One is running bo...

    **Community answers:**

    **1. Cricket Lee:**
    > "I can't seem to activate the Maestro 18 through the Kyber/Receiver but I'm able to activate the servos through the Maestro USB interface."
    > I had the same problem when setting up my Kyber with the Maestro. I swapped the TX/RX wires to the Maestro and that fixed things. "I can't seem to activate the Maestro 18 through the Kyber/Receiver but I'm able to activate the servos through the Maestro USB interface." I had the same problem when setting up my Kyber with the Maestro. I swapped the TX/RX wires to the Maestro and that fixed things.

    **2. Jason Charlton:**
    > Did you remember to remove the red/center leads on the servo wires connecting the Sabertooths to the Maestro? Also, what are the status lights doing on all the components?

    **3. Jason Charlton:**
    > Oh, and in the Maestro Control Center, what are the serial settings you’re using? There are a lot of pieces in the chain so troubleshooting can be tricky.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2209047236094597/){ .md-button }

??? question "I'm working on setting up a little demo of the R-DUO drive system. Since it is a tricycle gear system, the whole thing..."

    *Posted by **Tim Hebel**:*
    > I'm working on setting up a little demo of the R-DUO drive system.  Since it is a tricycle gear system, the whole thing will be able to move with just the base plate of R-DUO connecting things.  
    
    I have a couple of questions.
    1. Does the S-Bus connection to the FR-Sky X-8R supply power to the receiver?
    1. What dip switches are recommended for the Sabertooth (2x32) and (eventually) the Syren 10A?

    **Community answers:**

    **1. Stephane Beaulieu:**
    > 1. Yes sbus connector from the Kyber will power the receiver. But if you plan on using servos on the receiver itself the little power converter on Kyber will not give you enough amps to handle them.
    > 2. The DIP switches need to be set for RC control. For safety reason the PWM signal to control the Sabertooth should not go through the Maestro, it should be directly wired to the RC receiver. For an R2 unit, with dome control on a Syren, it can be controlled by the Maestro if you need to do animation.
    > I hope this help. 1. Yes sbus connector from the Kyber will power the receiver. But if you plan on using servos on the receiver itself the little power converter on Kyber will not give you enough a...

    **2. Tim Hebel:**
    > Thanks for the response this helps.
    > Hmm, never thought about controlling the dome with a Maestro. Since R-DUO can move his head in X and Y plus rotate, It might be helpful... I'll work that out eventually for now, I just want to learn how the transmitter works as this is my first RC project. My other three droids are SHADOW. Thanks for the response this helps. Hmm, never thought about controlling the dome with a Maestro. Since R-DUO can move his head in X and Y plus rotate, It might be helpful... I'll work that out eventually for now, I just want to learn how the transmitter works as this is my first RC project. My other three droids are SHADOW.

    **3. Brian Dodds:**
    > If also connecting servos to the RC receiver, power the RX from separate power and do not connect ￼center power wire to the Kyber.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1752082065124452/){ .md-button }

??? question "I am working on modding my RadioMaster TX16S transmitter. I have it open and ran into a. question that I hope is easy t..."

    *Posted by **Tim Hebel**:*
    > I am working on modding my RadioMaster TX16S transmitter.  I have it open and ran into a. question that I hope is easy to answer.  So, the resistor board has S - +.  The example video showed tapping into the connector of a pot that had yellow, black, and red wires (like a servo) and they mapped to the S - +.  On my transmitter, there is a daughter board with five wires. Black, White, Red, Yellow, ...

    **Community answers:**

    **1. Trevor Zaharichuk:**
    > I think you can measure which is + and which is S with your meter. Measure the Red wire (wrt GND) and see what it says. Turn the pot, if the voltage is constant, it would be the +, if it changes, it would be the S. If doesn't change, than verify the white wire is the S by measuring it. You should it change voltage when you turn the pot.

    **2. Group Member:**
    > Tim Hebel Trevor Zaharichuk Thanks Trevor! Just for my education on this topic. Would it hurt anything if they were backward or would it just not work, or produce inverse values?

    **3. Matt Hobbs:**
    > It won’t hunt anything. It just won’t work. Trevor has the right idea. That should get you to where you need to be.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1785445875121404/){ .md-button }

??? question "This diagram says not to connect the power wire from the Sbus of the Kyber to the RX. It also says, do not connect any o..."

    *Posted by **Brian Dodds**:*
    > This diagram says not to connect the power wire from the Sbus of the Kyber to the RX. It also says, do not connect any other power sources to the RX.
    I am currently using this Kyber board for audio only. Can I leave the power connected to my receiver, which is where all of my servos are connected, then only connect signal and ground of the Sbus of the Kyber ￼￼￼to the RX?
    This is in BB-8 with the C...

    **Community answers:**

    **1. Brian Dodds:**
    > You can power the RX off the Kyber only if your not also powering servos off the RX.  If you are then power the RX from its own regulator.In that diagram it's showing the RX gets power from the Kyber and the servos are powered separately. You can power the RX off the Kyber only if your not also powering servos off the RX.  If you are then power the RX from its own regulator. In that diagram it's showing the RX gets power from the Kyber and the servos are powered separately.

    **2. Brian Dodds:**
    > You can power the RX off the Kyber only if your not also powering servos off the RX. If you are then power the RX from its own regulator.
    > In that diagram it's showing the RX gets power from the Kyber and the servos are powered separately. You can power the RX off the Kyber only if your not also powering servos off the RX. If you are then power the RX from its own regulator. In that diagram it's showing the RX gets power from the Kyber and the servos are powered separately.

    **3. Group Member:**
    > Jason DelValle Brian Dodds thanks Brian! It’s working. Left the servos and power connected to the RX, powered the Kyber, connected the Sbus, sig and gnd only, from the RX to the Kyber

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2578951165770867/){ .md-button }

??? question "Question on wiring and whether or not I should be cutting the power wire of the SBUS connection. I plane to run 2 maest..."

    *Posted by **Brian Dodds**:*
    > Question on wiring and whether or not I should be cutting the power wire of the SBUS connection. 
    I plane to run 2 maestros off the Kyber. Maestro will have 3 servos connected. Mastero 2 will have at least 5 servos (potentially more down the road) and 3 channels being used for controlling a mecanum drive. 
    Question is: If I am only running the servos via RC pass through and not connecting any to t...

    **Community answers:**

    **1. Matt Hobbs:**
    > Looks like you got it figured out. The main thing to note is that you only want one power source going to the receiver and that will run only the receiver. If you are wanting to control things directly from the receiver only run the signal and ground wires to the receiver. Do not power any servos from the receiver. The logic side of the maestro can also be powered by the Kyber. The reason for this is as Brian stated, you only want one power regulator powering the receiver. If you connect another one it would back power into the kyber and destroy it. The reason for not powering any servos from the kyber/receiver is that the power supply on the kyber is only rated to handle 2 amps of current d...

    **2. Brian Dodds:**
    > You can power the logics of the Maestro's off the Kyber, but it's recommended you use Maestro's option to power the servos locally from each Maestro.
    > Figure out where you want to power the Receiver from and don't use the power wire from any other location.
    > My Kyber powers my receiver, so every other device plugged into it that also sends power has that wire cut. You don't want multiple regulators feeding the same thing. You can power the logics of the Maestro's off the Kyber, but it's recommended you use Maestro's option to power the servos locally from each Maestro. Figure out where you want to power the Receiver from and don't use the power wire from any other location. My Kyber powers my ...

    **3. Group Member:**
    > Hunter Smoke Brian Dodds my plan was/is to use the servo power rail on the maestros to power the servos and to use the 5V pin at the maestro connection point on the Kyber to power the maestro itself.
    > So no connection to the receiver other than the SBUS Brian Dodds my plan was/is to use the servo power rail on the maestros to power the servos and to use the 5V pin at the maestro connection point on the Kyber to power the maestro itself. So no connection to the receiver other than the SBUS

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2501869053479079/){ .md-button }

??? question "Need advice with either a Maestro or maybe wiring? For some reason the left Door (and only the left Door) on Chopper jus..."

    *Posted by **Jose Velazquez**:*
    > Need advice with either a Maestro or maybe wiring? For some reason the left Door (and only the left Door) on Chopper just stops working randomly. Not a jam either as I can freely move it powered on.
    
    I ran just the head connected to my laptop and power supply from my desk with it opening and closing the doors on a loop for 5 mins and ran just fine... It only does it when it's connected to the main...

    **Community answers:**

    **1. Jeanne DeWitt:**
    > I had a similar problem and it needed more amperage going up to the dome electronics from the main power in the body. Am currently running two 14.8v batteries in parallel and supplying dedicated 6V power through a buck converter separately to maestro servo power and maestro board power.

    **2. Jose Velazquez:**
    > Hook the servo to a servo tester if you have one

    **3. Group Member:**
    > Kenzō Barlow Runs just fine with one

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2321254738207179/){ .md-button }

??? question "(Resolved) Help! I wired everything together with 1 ryobi battery. When we went to move him forward, the wheel on channe..."

    *Posted by **Cory Hall**:*
    > (Resolved) Help!
    I wired everything together with 1 ryobi battery. When we went to move him forward, the wheel on channel 1 got to power immediately. The wheel in channel 2 wouldn't turn until we were at 80% throttle. 
    Then we thought we needed to have more power, we wired the second battery in parallel. Now the SSR connecting to the sabertooth would not stay on. We checked the phsyical connection...

    **Community answers:**

    **1. David Chino Chau:**
    > Hey all, turns out the issue is that there was a loose connection on one of the legs. It caused the SSR to switch off because the input and outputs.
    > How we figured it out was that we unhooke everything except for the power going into the sabertooth. Turned it on, the SSR remained on.
    > Then we hooked one leg and powered it back on, SSR stayed on and we had motion.
    > Last we hooked the last leg, the SSR turned on. So we redid the connection.
    > Solved all of our problems. Chopper is getting enough juice. And he’s running now! Hey all, turns out the issue is that there was a loose connection on one of the legs. It caused the SSR to switch off because the input and outputs. How we figured it out was t...

    **2. Matthew Geraci:**
    > I used 2-18 V Ryobi batteries. One battery is wired to the siren, the sabertooth, and the amplifier - it controls the foot and dome movement in the amplifier. The second battery is stepped down to 5 V and runs all of the ancillary electronics, lights and his piped into the dome to run the markdiino boards.
    > Here’s a link to my build log with a view of the electronics:
    > ￼ https://www.instagram.com/p/C18uUZRA9wY/?igsh=MTZyMTRtdGQxMHNmeQ== I used 2-18 V Ryobi batteries. One battery is wired to the siren, the sabertooth, and the amplifier - it controls the foot and dome movement in the amplifier. The second battery is stepped down to 5 V and runs all of the ancillary electronics, lights and his pi...

    **3. Cory Hall:**
    > Well not the Kyber for sure. First thing get your droid off the ground so you can test. Check with the motors not loaded. then look at wire connections and make sure your dip switches are set right

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2252701888395798/){ .md-button }

??? question "Question. Based on wiring diagram. The Maestro Board in the dome has two separate pos/neg leads: one for the servos and..."

    *Posted by **Matt Hobbs**:*
    > Question. Based on wiring diagram. The Maestro Board in the dome has two separate pos/neg leads: one for the servos and one to power the board that comes off the kyer board down in the body and is labeled 5 volts.  (Rx, Tx, 5v, and Gnd)
    Can I use a 5 volt power source in the dome (Filthy 5v regulator) vice running a pos/neg lead from the body kyer board to the dome Maestro?
    Running out of wires on...

    **Community answers:**

    **1. Group Member:**
    > Al Cordera Matt Hobbs I'm running 12v from body to dome, then using voltage regulator to drop to 5 volts. Based on what you're saying, the pos/neg off the kyber Maestro leads does not have to be wired up into the dome and can be added to any pos/neg 5v leads?

    **2. Matt Hobbs:**
    > You should only need 4 wires to go to the dome. Power, Gnd, TX, and RX. Run full voltage from the battery to the dome and then use voltage regulators in the dome to run various things.

    **3. Group Member:**
    > Al Cordera Stephane Beaulieu can I run that gnd from the Kyber to the Ov (gnd) on the SyRen10 to solve that problem? Mastro gnd in the dome can be ran to one of the other gnd?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2145718245760830/){ .md-button }

??? question "Hi all, Could I get some eyes on this wiring diagram for Chopper? Sorry if it's messy! Based on Kenzo's diagram and c..."

    *Posted by **Kenzō Barlow**:*
    > Hi all,
    
    Could I get some eyes on this wiring diagram for Chopper?  Sorry if it's messy!  Based on Kenzo's diagram and components, I added Wago connection points throughout.  
    Wire guages are 14 for everthing except Syren and Sabertooth to their motors (12, just by chance!) I anticipate using 16 or 20 guage for the maestros.
    Can servo wires go from the Sabertooth and Syren to the receiver?
    How doe...

    **Community answers:**

    **1. Kenzō Barlow:**
    > Channel # isn't something super strict as you'll be assigning them later. If I recall correctly, I used Channel 1 - 3 for the Saber, Syren, and Relay/Killswitch.
    > There's a PWN/GND from the Kyber to power the receiver
    > Hard to see on my phone but looks correct, from the double stack, it's the bottom of the two
    > I personally have mine outputting 12 volts to the dome and making sure it has at least 5ma to avoid any brown outs. I step it down inside the dome. Just make sure the slip ring is rated to handle a higher milliamps for safety as most are rated for 2ma. Channel # isn't something super strict as you'll be assigning them later. If I recall correctly, I used Channel 1 - 3 for the Saber, Syre...

    **2. Cory Hall:**
    > thats alot of questings in one post 
    >  feel free to pm me if you want to talk wiring for chopper I helped Kenzō Barlow get his kyber working right

    **3. Group Member:**
    > Joe Brausam Cory Hall it definitely is a lot of questions 
    > Will do! Cory Hall it definitely is a lot of questions Will do!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2385808861751766/){ .md-button }

??? question "So when you turn off WiFi, does it stop the web and DHCP servers and ethernet handling? (Is there a measurable reduction..."

    *Posted by **Brian Dodds**:*
    > So when you turn off WiFi, does it stop the web and DHCP servers and ethernet handling? (Is there a measurable reduction in processing overhead without those additional daemons running in the background?)

    **Community answers:**

    **1. Brian Dodds:**
    > It turns off the WiFi radio so that you're not adding to the RF noise and saves a bit of power use.

    **2. Group Member:**
    > Joey Furr But the other (unused) services continue to run in the background then...

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2274988629500457/){ .md-button }

??? question "The wire diagram is showing the main 12 volt system going through a voltage regulator to reduce to it appears is 7.5 vol..."

    *Posted by **Tim Hebel**:*
    > The wire diagram is showing the main 12 volt system going through a voltage regulator to reduce to it appears is 7.5 volts for the Maestro board. Is that too much for board and servos, I was told in another post to keep the servos powered at 5 volts?  Not sure which is right.  Request some experienced guidance!

    **Community answers:**

    **1. Tim Hebel:**
    > It depends on the servo. Inexpensive "hobby servos" typically run on 5V. However, beefier "pro" servos can run at much higher voltages. For example, I run B2-EMO's servos strait off of my 2S lLiPo battery at 8.4V.

    **2. Cory Hall:**
    > 6 - 6.5 is normally all you need for servos

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2142125326120122/){ .md-button }

??? question "I just ordered a Taranis Q X7, once it gets here I’m going to install my Kyber Control system in my Wall-E. I figured I’..."

    *Posted by **David Alvarez**:*
    > I just ordered a Taranis Q X7, once it gets here I’m going to install my Kyber Control system in my Wall-E. I figured I’d do some upgrading to my batteries and wiring while I’m at it. 
    I had a question for you guys. What kind of power distribution block do you prefer? Do you use the fused ones, I’ve heard some use ones with breakers. The one I’m looking at now has a 30amp per circuit and 100amp to...

    **Community answers:**

    **1. Jorge L. Ortiz:**
    > I would love to see when you do the upgrade to your droid. I’ll be doing the same to my R2 once the parts get here.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1508568999475761/){ .md-button }

## Maestro

??? question "What stepdown bucks are people using with thier Maestros servo power rail. I am stepping down a 6s to 7.5V but when I op..."

    *Posted by **James M Henley**:*
    > What stepdown bucks are people using with thier Maestros servo power rail. I am stepping down a 6s to 7.5V but when I operate 8 servos at once I draw enough amps that I cooked the drok step down I was using.

    **Community answers:**

    **1. Steven Dodds:**
    > In the world of power components, you get what you pay for rings very true.
    > I use castle for the high current stuff and pololu for almost everything else.
    > Those are the top 2 anyway In the world of power components, you get what you pay for rings very true. I use castle for the high current stuff and pololu for almost everything else. Those are the top 2 anyway

    **2. Steven Dodds:**
    > In the world of power components, you get what you pay for rings very true. I use castle for the high current stuff and pololu for almost everything else. Those are the top 2 anyway In the world of power components, you get what you pay for rings very true. I use castle for the high current stuff and pololu for almost everything else. Those are the top 2 anyway

    **3. James M Henley:**
    > https://www.amazon.com/dp/B01HXU1C6U...
    > https://www.amazon.com/dp/B01N1T7W1C...
    > https://www.amazon.com/dp/B000MXAR12... https://www.amazon.com/dp/B01HXU1C6U... https://www.amazon.com/dp/B01N1T7W1C... https://www.amazon.com/dp/B000MXAR12... AMAZON.COM HiLetgo 5pcs DC-DC Buck Step Down Module 6-20V 12V/20V to 5V 3A USB Charger Module

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2758892714443377/){ .md-button }

??? question "How many channel RX will I need for my Frsky X20s If I am planning on expanding R2's options. I already have the perisco..."

    *Posted by **Jason Southard**:*
    > How many channel RX will I need for my Frsky X20s If I am planning on expanding R2's options. I already have the periscope lights purchased and will be my first option installed along with all the pie doors and main body doors. I have been looking at this one, too much or not enough? Any help or suggestions would be awesome!

    **Community answers:**

    **1. Matt Hobbs:**
    > This would work great. I mainly use these. You should run the drives through the receiver and possibly the dome motor as well and also a rc switch for a drive system on and off. So a total of 4 channels plus the sbus and telemetry devices. Everything else you can run through the pass thru on the kyber to the maestros.

    **2. Matt Hobbs:**
    > This would work great. I mainly use these. You should run the drives through the receiver and possibly the dome motor as well and also a rc switch for a drive system on and off. So a total of 4 channels plus the sbus and telemetry devices. Everything else you can run through the pass thru on the kyber to the maestros.

    **3. Jason Southard:**
    > It's shuts the whole system down. If setup properly with your failsafe it's should power down when you switch off your controller. Correct Matt Hobbs ?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2006432673022722/){ .md-button }

??? question "I have decided to ditch the Maestros and go direct control with my servos. While I wait for a PCB to come in to start w..."

    *Posted by **Steven Dodds**:*
    > I have decided to ditch the Maestros and go direct control with my servos.  While I wait for a PCB to come in to start working on that part of it I moved on to adopting Patrick's Ring Control setup.  The Sbus connects to an ESP32 with just the GND and Signal wires.  In the code I see a spot for 3 Sbus RC Values and an SBUS RX on channel 16.  How do I find these values on the TX or on the webserver...

    **Community answers:**

    **1. Steven Dodds:**
    > One thing about SBUS is, the values it uses are not what you see in the radio….
    > Anyway, I believe they range from 172 to 1811 with the middle around 992. (As seen in the Kyber when setting up the values there for various buttons and switches)
    > So if you use a default 3 way switch the values would be 1811, 992, 172…
    > Where is Patrick’s code? One thing about SBUS is, the values it uses are not what you see in the radio…. Anyway, I believe they range from 172 to 1811 with the middle around 992. (As seen in the Kyber when setting up the values there for various buttons and switches) So if you use a default 3 way switch the values would be 1811, 992, 172… Where is Patrick’s code?

    **2. Steven Dodds:**
    > One thing about SBUS is, the values it uses are not what you see in the radio….Anyway, I believe they range from 172 to 1811 with the middle around 992.  (As seen in the Kyber when setting up the values there for various buttons and switches) So if you use a default 3 way switch the values would be 1811, 992, 172…Where is Patrick’s code? One thing about SBUS is, the values it uses are not what you see in the radio…. Anyway, I believe they range from 172 to 1811 with the middle around 992.  (As seen in the Kyber when setting up the values there for various buttons and switches) So if you use a default 3 way switch the values would be 1811, 992, 172… Where is Patrick’s code?

    **3. Group Member:**
    > Dustin Wyer Thanks for help.  This is the link that was in another post https://github.com/circuitBurn/B2EMO/tree/development Thanks for help. This is the link that was in another post https://github.com/circuitBurn/B2EMO/tree/development GITHUB.COM github.com

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2762141694118479/){ .md-button }

??? question "Guys, I'm having a problem with Bee. This afternoon I wanted to test the servos in the main unit, but Bee wouldn't budge..."

    *Posted by **Tim Hebel**:*
    > Guys, I'm having a problem with Bee.
    This afternoon I wanted to test the servos in the main unit, but Bee wouldn't budge.
    It turns out the Kyberboard had reset to factory defaults, so I lost all the settings.
    I've reconfigured everything, but the Kyberboard just won't communicate with the Maestro. The sound is working correctly, so the transmitter is connected and communicating with the Kyberboard...

    **Community answers:**

    **1. Maikel Jegerings:**
    > Problem solved! Stephane saved the day! ID was set to 0. It should be 1. But why the Kyberboard reseted to factory is a mystery.

    **2. Maikel Jegerings:**
    > Problem solved! Stephane saved the day! ID was set to 0. It should be 1. But why the Kyberboard reseted to factory is a mystery.

    **3. Group Member:**
    > Cory Hall Maikel Jegerings if you power it on and off rapidly sometimes they will reset

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2581838335482150/){ .md-button }

??? question "Hi all! Totally newb here with electromechanical parts. After much research, I deduced that my servo’s will be controlle..."

    *Posted by **David Chino Chau**:*
    > Hi all! Totally newb here with electromechanical parts. After much research, I deduced that my servo’s will be controlled by maestro’s and landed in the Kyber system to communicate with them. 
    What is next? Find a controller? Help!

    **Community answers:**

    **1. Joe Brausam:**
    > Stephane Beaulieu - I’m working on putting together chopper and I think I’ll likely go with your system, it seems like a great option!  I’m a beginner with a lot of this, so for now I was curious - things like the servos, maestro boards, dome lights - am I able to follow all the instructions and use the parts that Michael B recommends for those in his instructions, or will I need to do something different?

    **2. Joe Brausam:**
    > Stephane Beaulieu - I’m working on putting together chopper and I think I’ll likely go with your system, it seems like a great option! I’m a beginner with a lot of this, so for now I was curious - things like the servos, maestro boards, dome lights - am I able to follow all the instructions and use the parts that Michael B recommends for those in his instructions, or will I need to do something different?

    **3. Stephane Beaulieu:**
    > Hi and welcome ! First, tell us which droid you are building ?  In the Kyber doc you will find a few wiring exemples that you can adapt tou you rbuild.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2010940825905240/){ .md-button }

??? question "My R5's buzz saw used an endstop switch when retracting to turn off the servo when I had an Ardunio controling it. How..."

    *Posted by **Tim Hebel**:*
    > My R5's buzz saw used an endstop switch when retracting to turn off the servo when I had an Ardunio controling it.  How do I setup that feature using the endstop feature of Kyber?

    **Community answers:**

    **1. Tim Hebel:**
    > Hmm, I'm not sure how to turn a servo power off in the script... I think it might be just setting it 0. Would something like this work if I pasted it to the top of the automatically generated script. (Obviously adding the quit commands in the auto-generated stuff).
    > # When the script is not doing anything else,
    > # this loop will listen for button presses. When a button
    > # is pressed it runs the corresponding sequence.
    > begin
    > button_a if sequence_a endif
    > repeat
    > # These subroutines each return 1 if the corresponding
    > # button is pressed, and return 0 otherwise.
    > # Currently button_a is assigned to channel 14,
    > # These channels must be configured as Inputs in the
    > # Channel Settings tab.
    > sub button_a
    > 1...

    **2. Tim Hebel:**
    > Hmm, I'm not sure how to turn a servo power off in the script... I think it might be just setting it 0.  Would something like this work if I pasted it to the top of the automatically generated script.  (Obviously adding the quit commands in the auto-generated stuff).# When the script is not doing anything else,# this loop will listen for button presses.  When a button# is pressed it runs the corresponding sequence.begin  button_a if sequence_a endifrepeat# These subroutines each return 1 if the corresponding# button is pressed, and return 0 otherwise.# Currently button_a is assigned to channel 14, # These channels must be configured as Inputs in the# Channel Settings tab.sub button_a  14 get...

    **3. Matt Hobbs:**
    > The maestro has an on and off state for the servos. This is programmable in the scripts. I usually keep all the servos off that are not passthru then turn them on in the script, do the action, then turn off the servos

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2039968849669104/){ .md-button }

??? question "I'm replacing the Marcduino system in my dome with a Maestro so I can write more sequences. I also use Douglas A. Bicker..."

    *Posted by **Douglas A. Bickert**:*
    > I'm replacing the Marcduino system in my dome with a Maestro so I can write more sequences. I also use Douglas A. Bickert's outer rim system, and the servos get their power directly from that. Taking that into consideration, would I just not provide power to the terminal on the Maestro (servo power), and ONLY power it through the pins on the left side of the board? Then i'll just have the signal l...

    **Community answers:**

    **1. Douglas A. Bickert:**
    > Yup! Just plug the signal lines into the Rim servo signal bank and you are good to go! There are a couple ground options on segment OR1 if you need too. If the grounds are common then you shouldn’t need an additional ground to the Maestro.

    **2. Group Member:**
    > Jacob Amundsen Douglas A. Bickert Cool, thanks! Excited to try this out. I know you can build new sequences with the MarcDuino but the ease of Maestro coding for a gungan like me just seemed like a better long term solution. Thanks!!

    **3. Group Member:**
    > Jacob Amundsen Dan Coe Oh good point. I didn't even think of that. I'm running the GND VIN RX & TX through the slip ring and up from the maestro in the body

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2149286682070653/){ .md-button }

??? question "The Kyber Wiring guide for using 12 channel Mini-Maestro in the dome and body, states, 'Do not install Jumper'. The mini..."

    *Posted by **Matt Hobbs**:*
    > The Kyber Wiring guide for using 12 channel Mini-Maestro in the dome and body, states, "Do not install Jumper". The mini maestro board (picture below) has a blue clip, and only one side is attached to a pin, but not on any of servo pins. Its even with the battery pins. 
    
    Should I remove it all together, or is it fine where it is at?

    **Community answers:**

    **1. Steven Dodds:**
    > Haven’t looked at the wire diagram
    > But that jumper is IF you want to power the board from the servo power in.
    > The 3 pins to the right of it are the servo power in pins. If you did install the jumper for use, it would go in the orange box in this image. Haven’t looked at the wire diagram But that jumper is IF you want to power the board from the servo power in. The 3 pins to the right of it are the servo power in pins. If you did install the jumper for use, it would go in the orange box in this image.

    **2. Matt Hobbs:**
    > It will more than likely fall off later or get knocked off so I would just go ahead and remove it.

    **3. Scott Kraft:**
    > If it’s only on one pin it’s not doing anything

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2142121399453848/){ .md-button }

??? question "Anyone powering higher power servos through the maestro? If so what wires are you using to run power to the maestro for..."

    *Posted by **Jon Sprinkle**:*
    > Anyone powering higher power servos through the maestro? If so what wires are you using to run power to the maestro for the servos? The standard breadboard jumpers don't seem like they would be able to handle that much current.

    **Community answers:**

    **1. Group Member:**
    > Jon Sprinkle Matt Hobbs This is what I leaning towards. Just reading those 24 awg jumpers can only carry a little over 1 amp. I should of went with the 18 channel. It at least has a screw terminal. Just trying to throw something together before Halloween and short on time.

    **2. Matt Hobbs:**
    > One thing you can do is externally power the servos and then just use the signal line from the maestro.

    **3. Group Member:**
    > Bryan Stubblefield Michael McMaster no. Just got lucky and found one.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1550920881907239/){ .md-button }

??? question "I have all my sequences working on the maestro as I want. Kyber is communicating and kyberpad is working. I am having an..."

    *Posted by **Krank Meister**:*
    > I have all my sequences working on the maestro as I want. Kyber is communicating and kyberpad is working. I am having an issue with some of the sequences. For example: when I do the gripper sequence when connected to maestro the door opens and the gripper comes up. Closing the gripper goes down and the door closes. But when I activate the sequence by kyberpad, the door opens and the gripper comes ...

    **Community answers:**

    **1. Krank Meister:**
    > The maestro auto sets each frame in the script at 500 milliseconds. Try adjusting the milliseconds within each frame to set the duration of each function.

    **2. Matt Hobbs:**
    > It would not be on the kyber side. The kyber only triggers the start of an animation.

    **3. Group Member:**
    > Cory Henry Matt Hobbs so I guess I don’t understand why it runs fine through maestro?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2357970417868944/){ .md-button }

??? question "UPDATED: New video with changes to speed and acceleration made per Stephane's suggestions. Any suggestions on how to smo..."

    *Posted by **Darren Moser**:*
    > UPDATED: New video with changes to speed and acceleration made per Stephane's suggestions.
    Any suggestions on how to smooth out this pair of door servos? There are 2 each 25 Kg digital 180 degree servos for the door. The door is 1/4" plywood with plastic veneers. I've tried speeding up and slowing down the servos in the maestro program but no difference in how they performed. Thank you.

    **Community answers:**

    **1. Darren Moser:**
    > Numbers are way too low for speed. 2 is not twice the speed of 1. Think of it as a 1-10 scale. When at 0 moves directly with the servo. Snaps to the position. 1 or 2 is very slow. I don’t recall what number gets it faster. But how high are you going?

    **2. Group Member:**
    > Michael Janes Stephane Beaulieu Perfect Stephane, thanks! But I had to move acceleration down from 10 to1 because the door shot closed like a bullet

    **3. Group Member:**
    > Michael Janes Darren Moser thanks Darren, speed of 0 was the key. Set acceleration to 1 and it moved very naturally.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2286624825003504/){ .md-button }

??? question "I asked this question before, and was told that the Kyber system can control the Maestro's programs and store and run se..."

    *Posted by **Brian Dodds**:*
    > I asked this question before, and was told that the Kyber system can control the Maestro's programs and store and run several patterns of movement programs. Can the Maestro store several different patterns of movement programs for the droid? Or do I store the Maestro's programs in the Kyber system? I would appreciate some advice.
    
    Is it a good idea to save the programs I create with Maestro on my ...

    **Community answers:**

    **1. Toshio Fujisawa:**
    > Thank you for your advice. After checking the servo movement, convert it into a program, then save it as a script, right?
    > Are there any rules for file names? Thank you for your advice. After checking the servo movement, convert it into a program, then save it as a script, right? Are there any rules for file names?

    **2. Brian Dodds:**
    > The Maestro stores a script and that script can have multiple different sequences in it that the Kyber can trigger. ￼ I would recommend saving the script to you PC as a backup.

    **3. Kelly Larson:**
    > I work in IT application development, always save your work to your computer. In the end it is just a script that you save but ALWAYS SAVE IT.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2260809434251710/){ .md-button }

??? question "First time programming the Maestro for Kyber, apologies in advance if this is a very basic question. I have 2 servos tha..."

    *Posted by **Mark Enright**:*
    > First time programming the Maestro for Kyber, apologies in advance if this is a very basic question. I have 2 servos that are very difficult to access without major effort. I cannot find in the pololu maestro programming pdf if I need to have the servos in a "0" or home position before programming or if I can just set the servo position where it needs to be on installation, then program its moveme...

    **Community answers:**

    **1. Mark Enright:**
    > Yes you can set any start position you like for the servo in programming. Only thing you need to consider is the physical end points of the servo in relation to the build. For example if you just connected up a servo to a dome flap then powered on the servo it will auto center maybe causing damage to the item the servo was connected to. Best to center the servo first either physically or with the maestro then connect the item to control.Hope that makes sense.

    **2. Brian Dodds:**
    > I would recommend you do not have the horn and linkage installed on any servo before you start programming unless you used a servo tester to know 100% it's in the correct position.

    **3. Group Member:**
    > Michael Janes Mark Enright thanks Mark. I used a servo tester and worked through the movements manually. Would this be an equivalent to doing a test through the maestro for end points and distance of motion?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2129248377407817/){ .md-button }

??? question "Hey guys, trying to understand the setup for the random events setup. My goal is to have the SD switch start a loping se..."

    *Posted by **Cory Hall**:*
    > Hey guys, trying to understand the setup for the random events setup. My goal is to have the SD switch start a loping sequence on the mauestro that will move the arms of my RX droid. A few questions:
    1. I have the random on off set to channel 13. Do I  also need to set a passthrough for channel 13?
    2. What do the mastero min an max correspond to on the random events tab? Would this be what sequenc...

    **Community answers:**

    **1. Cory Hall:**
    > Shoot me a pm if you need help I can walk you through the steps to set it up

    **2. Cory Hall:**
    > You need to have a channel in the mix for random.

    **3. Group Member:**
    > Hunter Smoke Cory Hall will do

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2582117205454263/){ .md-button }

??? question "Hello everyone, I am building my first droid! A Chopper based on Mr.Baddeley's amazing stuff. Any advice on how to get s..."

    *Posted by **Andrew Lindley**:*
    > Hello everyone, I am building my first droid! A Chopper based on Mr.Baddeley's amazing stuff. Any advice on how to get started with Kyber BEFORE I start purchasing electronics that aren't servos?

    **Community answers:**

    **1. Group Member:**
    > Chris Lizyness Andrew Lindley will this system work with marcduino? Kids and I want to kinda go overboard with the gadgets and whatnot. Just curious as to compatibility or if what I got is redundant.

    **2. Andrew Lindley:**
    > Motor controllers, dome motor and drive motors and figure out if you want 12v,18v,24v but I love the kyber system since I installed on my chopper and you saw it at the Con

    **3. Group Member:**
    > Omar Abdelgawad Andrew Lindley I did! Building the live action one to follow me around in my Ezra costume.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2177189429280378/){ .md-button }

??? question "I need some help getting the 6 RC buttons set up. My understanding is buttons 1-2 go into the same channel. For me it’s..."

    *Posted by **Darren Moser**:*
    > I need some help getting the 6 RC buttons set up. My understanding is buttons 1-2 go into the same channel. For me it’s CH6. And I have two mixes. One goes high? One goes low? Free mix? Variable? Not sure how to set this part up. Any help appreciated.

    **Community answers:**

    **1. Darren Moser:**
    > The solution we found was that I need to adjust the wires in the shoulder buttons so that half of them go down from a 3 position switch setting and half go up.
    > As for the two buttons on the gimbals they are tapped into momentary switches. So at this point they are only able to do one thing. The solution we found was that I need to adjust the wires in the shoulder buttons so that half of them go down from a 3 position switch setting and half go up. As for the two buttons on the gimbals they are tapped into momentary switches. So at this point they are only able to do one thing.

    **2. Group Member:**
    > Darren Moser Cory Hall Ok, what does that mean? In the mix what is high what is low?

    **3. Cory Hall:**
    > Yeah button one is high and 2 will be low.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2151854241813897/){ .md-button }

??? question "Matt Hobbs.... the schematics for the Kyber System that I have show that the Speed (Fwd & Bkwd) & Steering (Left & Right..."

    *Posted by **Brian Moore**:*
    > Matt Hobbs.... the schematics for the Kyber System that I have show that the Speed (Fwd & Bkwd) & Steering (Left & Right) signals arrive on two channels of the Rx (Channels 6 & 7 for example) ?? and go direct to the Motor Driver Board. But in your video on YouTube you talk about setting two channels on the Maestro as "pass through" for the Speed and Steering signals which then go to the Motor Driv...

    **Community answers:**

    **1. Matt Hobbs:**
    > You do not have to put the steering through the maestros. Plus I would advise against that. I may have mentioned that as an example. I would put the drive speed abs steering directly into the RC Receiver.

    **2. Brian Dodds:**
    > I personally would not send drive though a Maestro. That could be unsafe.

    **3. Michael McMaster:**
    > Is IA still making these?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1591954301137230/){ .md-button }

??? question "Regarding the Maestros. Does the Kyber system require the use of two Maestros of the same size/capability (two 24s or..."

    *Posted by **Todd Harrington**:*
    > Regarding the Maestros.   Does the Kyber system require the use of two Maestros of the same size/capability (two 24s or two 12s, etc.)?  Or, can you have a larger Maestro, say the 24, for the body and a smaller Maestro, like the 12 or 18, for the dome?  Thanks in advance!

    **Community answers:**

    **1. Group Member:**
    > Todd Harrington but they don't have to both be the same, correct? Thank you!

    **2. Brian Dodds:**
    > I don't think so... ??? I use Marcduinos in the dome though...

    **3. Stephane Beaulieu:**
    > You can use any size Maestro you want.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1919615275037796/){ .md-button }

??? question "SO WHEN I ORDER A MAESTRO DO I JUST NEED TO COUNT FOR SERVOS ? OR DO I NEED A BIGGER MAESTRO IF I'M GOING RUN SCRIPT COM..."

    *Posted by **Cory Hall**:*
    > SO WHEN I ORDER A MAESTRO DO I JUST NEED TO COUNT FOR SERVOS ? OR DO I NEED A BIGGER MAESTRO IF I'M GOING RUN SCRIPT COMMANDS FROM THE MAESTRO.

    **Community answers:**

    **1. Tim Hebel:**
    > Also, you can control other things with maestros such as PWM actuated relays or sending HIGH/LOW commands to a Nano. I do both to activate lighting and other effects in my droid (Bad Motivator). Even though you may not have these in your droid when you build it, a few extra Maestro pins can future-proof your droid build a bit and make those upgrades trivial to implement.
    > https://www.amazon.com/dp/B08FLZXSD7... Also, you can control other things with maestros such as PWM actuated relays or sending HIGH/LOW commands to a Nano. I do both to activate lighting and other effects in my droid (Bad Motivator). Even though you may not have these in your droid when you build it, a few extra Maestro pin...

    **2. Stephane Beaulieu:**
    > 6 channels one has less memory for scripts. Better go with at least 12 channels or more if you need to control more servos.

    **3. Group Member:**
    > Brian Dodds Stephane Beaulieu GIPHY

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2006030859729570/){ .md-button }

??? question "Question. I'm planning out dome plate animations currently. I've got the maestro in the body and one in the dome, and I'..."

    *Posted by **Jacob Amundsen**:*
    > Question. I'm planning out dome plate animations currently. I've got the maestro in the body and one in the dome, and I've got Doug's fantastic Warp Core plate and PCB with servo power and signal. I'm guessing I need a third microcontroller to handle those (a few servos, actuators and maybe a relay) that can receive serial commands from Kyber? do you all have any recommendations? Or is there a bet...

    **Community answers:**

    **1. Tim Hebel:**
    > You can use the Marcduino to control the panels and the maestro/ Kyber to control the dome tools. Basically, use Kyber to send serial commands to the Marcduino and maestros to send Commands to the other things. I use some RC enabled relays to control effects in R5-D4’s body. There two techniques. One is set a direct pass-through in Kyber to have a switch directly control a device. The other is to set a button to trigger a maestro sequence.
    > For example, I use a maestro pass-through to use the right gimbal to control chopper’s head wobble. Additionally, I have the couple of head wobble sequences that I can have triggered from the random events interface on the Kyber web interface. You can use ...

    **2. David Carriere:**
    > I reached out to some builders and kind of tracked it down with their help. Doesn’t look to be anyone in the club. The fibregl… Afficher plus

    **3. Matt Hobbs:**
    > Tim Hebel or Brian Dodds may be able to answer this. They have a lot going on in there domes.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2103790996620222/){ .md-button }

??? question "Setting up my Maestro... what controls the band positions. The Maestro or Kyber. i.e. If I have the Meastro tuned perfec..."

    *Posted by **Stephane Beaulieu**:*
    > Setting up my Maestro... what controls the band positions. The Maestro or Kyber. i.e. If I have the Meastro tuned perfectly does the Kyber just pass through and use the Maestro to limit the PWM or do I need to tune the Kyber to the PWM limits. .. Or Both?    Which one wins?
    UPDATE: Kyber sends the min-max entered on Kyber ... Mastro filters it to the range set in the Maestro. Best to just match th...

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Maestro will always be the final reference. If you set it to go to a maximum position it will never go pass this position.  To get full range of RC channel, set the same min and max in Kyber.  If the servo is reversed, revers the values.

    **2. Stephane Beaulieu:**
    > Maestro will always be the final reference. If you set it to go to a maximum position it will never go pass this position. To get full range of RC channel, set the same min and max in Kyber. If the servo is reversed, revers the values.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2731408933858422/){ .md-button }

??? question "Just finished the shell on my B2EMO unit, and I'm working on my shopping list for electronics. A Kyber is standard with..."

    *Posted by **Sean Fuchs**:*
    > Just finished the shell on my B2EMO unit, and I'm working on my shopping list for electronics.
    A Kyber is standard with all the other guys building B2 with the exception of a guy making custom boards that aren't yet available.
    But I've found almost zero information online about the specs of what I've assumed is the main control board for the robot, and cannot seem to find it anywhere to purchase, ...

    **Community answers:**

    **1. Sean Fuchs:**
    > Contact Matt Hobbs to purchase. Here's the ones I can answer 1. Yes
    > 2. Having a regular is wise to make sure the supply is good.
    > 3. No you should supply separate power. Contact Matt Hobbs to purchase. Here's the ones I can answer 1. Yes 2. Having a regular is wise to make sure the supply is good. 3. No you should supply separate power.

    **2. Cory Henry:**
    > 7. These things have a habit of becoming additive so if you invest early in the controller you can use it for everything, to include your RC models

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2446259042373414/){ .md-button }

??? question "Instead of triggering maestros could this system trigger arduino routines instead? Currently have all my routines implem..."

    *Posted by **Craig Gurrie**:*
    > Instead of triggering maestros could this system trigger arduino routines instead?
    Currently have all my routines implementated that way - but really like the idea of triggering them via this system

    **Community answers:**

    **1. Rob N Kristien:**
    > I don't see why not

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1403681953297800/){ .md-button }

??? question "The use of the mini-maestro boards with Kyber Controls. If I'm using 16 panels in the dome with servos plus the movement..."

    *Posted by **Al Cordera**:*
    > The use of the mini-maestro boards with Kyber Controls. If I'm using 16 panels in the dome with servos plus the movement of the Halo Projectors (2 x 3). Would I not need a 24 Channel Master Board for the Dome and a 12-Channel for the body servos?

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Yes exactly

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2069558156710173/){ .md-button }

## Power

??? question "Has anyone noticed sounds playing on the Kyber, on boot up, that are not the ‘start’ sound, if you have one? When I plug..."

    *Posted by **Steven Dodds**:*
    > Has anyone noticed sounds playing on the Kyber, on boot up, that are not the ‘start’ sound, if you have one?
    When I plug the battery in, I get a totally different sound than expected, at full volume.

    **Community answers:**

    **1. John Geb:**
    > I had this issue but it would play a sequence on the maestro. Turned out to be I had that sequence triggered on a momentary switch. The active position should be around pwm 1000 or 2000 and released state should be 1500 so in the remote +100 or -100 then 0 at rest.

    **2. Steven Dodds:**
    > After more testing, it seems that maybe even with failsafe set to -100% (no buttons pressed) if you power up the Kyber and your radio doesn’t have physical buttons and Kyber pad hasn’t run yet, you get the wrong sound.

    **3. Steven Dodds:**
    > I think I figured it out.
    > My failsafe was set to no pulses.
    > I changed it to -100% on Kyber channel. I think I figured it out. My failsafe was set to no pulses. I changed it to -100% on Kyber channel.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2520879878244663/){ .md-button }

??? question "Quick wire check. I'm following the 3rd wire guide. I'll go back to get the servos connect, but right now I'm just focus..."

    *Posted by **Edwin Zuluaga**:*
    > Quick wire check. I'm following the 3rd wire guide. I'll go back to get the servos connect, but right now I'm just focused on getting chopper mobile. The terminals will be jumped and I do have a power switch that i will put in but I want to see where I'm at so far. Especially since I have only one of each part and electronics take forever to arrive lol Also, the guides are for 12 volt battery but ...

    **Community answers:**

    **1. Cory Hall:**
    > On just a quick view it looks good

    **2. Group Member:**
    > Stephane Beaulieu Edwin Zuluaga in the Kyber manual

    **3. Edwin Zuluaga:**
    > Where did you find the wiring diagrams?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2173907652941889/){ .md-button }

??? question "I see the new Kyber pad will monitor 2 battery voltages, how is this done? I have a voltmeter inconspicuously placed on..."

    *Posted by **Brian Dodds**:*
    > I see the new Kyber pad will monitor 2 battery voltages, how is this done? I have a voltmeter inconspicuously placed on my droid but displayed on my x20 would be nicer

    **Community answers:**

    **1. Brian Dodds:**
    > FrSky sells current sensors that also monitor voltage. You have to install one and then change its ID info before installing the 2nd.
    > Or you can use one and use the AIN found on a lot of the RX FrSky sells current sensors that also monitor voltage. You have to install one and then change its ID info before installing the 2nd. Or you can use one and use the AIN found on a lot of the RX

    **2. Group Member:**
    > John Reik Stephane Beaulieu looking like FrSky FLVS ADV
    > and will plug into the balance plug of the battery and smart port of the receiver, am I reading this right? Stephane Beaulieu looking like FrSky FLVS ADV and will plug into the balance plug of the battery and smart port of the receiver, am I reading this right?

    **3. Group Member:**
    > John Reik Stephane Beaulieu x8r

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2754800334852615/){ .md-button }

??? question "More wiring questions, Stephane Beaulieu, I noticed in your Chopper diagram, you put the relay/switch onto the battery s..."

    *Posted by **Tim Hebel**:*
    > More wiring questions, Stephane Beaulieu, I noticed in your Chopper diagram, you put the relay/switch onto the battery supply to the Sabertooth and Syren. 
    On my other droids, I put the switch between the output of the Sabertooth and Syren and the motors.  I did this to prevent the motor from genrating current  when the droid or dome was moved without being powered (or even having batteries instal...

    **Community answers:**

    **1. Stephane Beaulieu:**
    > Tim Hebel I can't say for sure if both techniques you are talking about will have the same result.
    > When I do my electronic, I like to keep things basic and not over think it. And still I did overthink too much Chopper. I placed switches on all the components, Sabertooth, Syren, AMP, Kyber and BEC. After one year of usage I only use one switch and it's the main switch. Redoing it I would remove all the other switches and only keep the maine one.
    > I did not add any swicthes to the motors, most of the time Chopper will move on his own power, I don't really need to push it around. I placed the RC kill switch on the main power line to the Sabertooth. This way I can deactivate the controller on eme...

    **2. Thomas LeBlanc:**
    > You need a main power switch, that's just good practice. A reverse diode across it will allow regen current to flow from motor controllers to batteries even when that main switch is off, as long as the batteries are installed. However, it does nothing to help the regen issue if the batteries are removed. If regen current is made by the motors it must have a path to leave the motor controllers. If you are using a Sabertooth 2x32, you can configure it to not create regen current and things get much simpler. Not true for the 2x25 or Syren as far as I know...but it's been a few years since I've used one.

    **3. Micke Askernäs:**
    > In my R2, I had both of these. One between motor controller and motors to allow R2 to be pushed around or standing still for longer periods without any risk of a stray signal misinterpreted would leave him running.
    > One to battery supply to kill ALL power including electronics.. In my R2, I had both of these. One between motor controller and motors to allow R2 to be pushed around or standing still for longer periods without any risk of a stray signal misinterpreted would leave him running. One to battery supply to kill ALL power including electronics..

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1752243325108326/){ .md-button }

## Mechanics

??? question "What do I need to enable / disable the drive system with kyber? Using the brushless hub motors with ESCs. One for each s..."

    *Posted by **Brian Dodds**:*
    > What do I need to enable / disable the drive system with kyber? Using the brushless hub motors with ESCs. One for each side.
    I thought about a double relay, but how do I trigger it?
    Or could a connect in to the on/off buttons on the esc

    **Community answers:**

    **1. Stephane Beaulieu:**
    > I use a SSR relay with RC switch connected to my receiver. A simple mix in the remote using a 2 position toggle switch turn on/off the relay and activate the SSR.
    > https://www.amazon.com/.../dp/B0D5CGVKMZ/ref=sr_1_2_sspa...
    > https://www.amazon.com/.../dp/B08FLZXSD7/ref=sr_1_1_sspa... I use a SSR relay with RC switch connected to my receiver. A simple mix in the remote using a 2 position toggle switch turn on/off the relay and activate the SSR. https://www.amazon.com/.../dp/B0D5CGVKMZ/ref=sr_1_2_sspa... https://www.amazon.com/.../dp/B08FLZXSD7/ref=sr_1_1_sspa... AMAZON.COM YQSIYU SSR-40DD Single Phase Solid State Relay 40A DC to DC Relay Input 3-32V DC to Output 12-220V DC 40A 3PCS

    **2. Stephane Beaulieu:**
    > I use a SSR relay with RC switch connected to my receiver.  A simple mix in the remote using a 2 position toggle switch turn on/off the relay and activate the SSR.https://www.amazon.com/.../dp/B0D5CGVKMZ/ref=sr_1_2_sspa...https://www.amazon.com/.../dp/B08FLZXSD7/ref=sr_1_1_sspa... I use a SSR relay with RC switch connected to my receiver.  A simple mix in the remote using a 2 position toggle switch turn on/off the relay and activate the SSR. https://www.amazon.com/.../dp/B0D5CGVKMZ/ref=sr_1_2_sspa... https://www.amazon.com/.../dp/B08FLZXSD7/ref=sr_1_1_sspa... AMAZON.COM YQSIYU SSR-40DD Single Phase Solid State Relay 40A DC to DC Relay Input 3-32V DC to Output 12-220V DC 40A 3PCS

    **3. Brian Dodds:**
    > Kyber doesn't control the drive system.  You will not trigger the drives with Kyber.  The RC radio you use will control the drives.  I use an RC relay that turns on or off the drive ESC with a switch on the radio. Kyber doesn't control the drive system.  You will not trigger the drives with Kyber. The RC radio you use will control the drives.  I use an RC relay that turns on or off the drive ESC with a switch on the radio.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2756091988056783/){ .md-button }

??? question "Can someone explain something. I have been looking at using kyber on an r2 droid. In the Mr. Baddeley printed droid grou..."

    *Posted by **Matt Hobbs**:*
    > Can someone explain something. I have been looking at using kyber on an r2 droid. In the Mr. Baddeley printed droid group a member says that kyber is not able to drive. I do not know what he means. Can I use kyber and an rc radio to run the whole r2 or do I need another second controller to drive ?? Thanks!

    **Community answers:**

    **1. Glenn Pablo:**
    > Kyber is the way to go.  It shares the same components as Padawan 360 & Shadow (Sabertooth, Syren, Foot & dome motors, Servos).  Kyber has a self contained MP3 player & amplifier (or you can connect an outboard amp for higher wattage).  But the #1 difference is it uses RC frequencies.  Shadow & Padawan use Bluetooth.  RC has longer range and more available frequencies (something that is very important when at a large convention).  Cost difference is about $200-600, which is really dependent on the controller you choose.  Kyber System ($200) + RC controller ($150-600) vs Arduino ADK ($50) + XBox controller ($50) + MP3 trigger ($50) + XBox dongle ($40).  So it really comes down to #1 your budg...

    **2. Glenn Pablo:**
    > Kyber is the way to go. It shares the same components as Padawan 360 & Shadow (Sabertooth, Syren, Foot & dome motors, Servos). Kyber has a self contained MP3 player & amplifier (or you can connect an outboard amp for higher wattage). But the #1 difference is it uses RC frequencies. Shadow & Padawan use Bluetooth. RC has longer range and more available frequencies (something that is very important when at a large convention). Cost difference is about $200-600, which is really dependent on the controller you choose. Kyber System ($200) + RC controller ($150-600) vs Arduino ADK ($50) + XBox controller ($50) + MP3 trigger ($50) + XBox dongle ($40). So it really comes down to #1 your budget & #2 ...

    **3. Matt Hobbs:**
    > Just like any other control system you will need motor controllers for the drive motors and the dome motor. The kyber is used for mapping buttons to sounds and motions on maestro servo controllers. Look over the kyber manual that is posted in the files section of this group and you can see some example wiring diagrams

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2546198445712806/){ .md-button }

??? question "Hoping to use kybers pass through channels to trigger my maestro 12 to drive relays to kill R2 foot motors and dome moto..."

    *Posted by **Jackie Wah**:*
    > Hoping to use kybers pass through channels to trigger my maestro 12 to drive relays to kill R2 foot motors and dome motor via my FrSky X20. Using x20 channels 4 & 5 to trigger the maestro feeds 0 & 1 set to “output” mode. Hooking up a led to maestro outs 0 & 1 and they light when using pololu app, just not from two x20 toggle switches, Will use 5v miniature relays to drive high current 24v relays ...

    **Community answers:**

    **1. Steven Dodds:**
    > Many motor controllers have ways to tell them to enable and disable the drive motors directly.
    > Check if yours do and how to trigger it.
    > If it’s built in RC then you don’t need RC relays.
    > If it wants a switch, then you can put a small RC relay on it.
    > I don’t have any drawings for how to properly do it if neither are true. Many motor controllers have ways to tell them to enable and disable the drive motors directly. Check if yours do and how to trigger it. If it’s built in RC then you don’t need RC relays. If it wants a switch, then you can put a small RC relay on it. I don’t have any drawings for how to properly do it if neither are true.

    **2. Steven Dodds:**
    > Many motor controllers have ways to tell them to enable and disable the drive motors directly. Check if yours do and how to trigger it. If it’s built in RC then you don’t need RC relays. If it wants a switch, then you can put a small RC relay on it.I don’t have any drawings for how to properly do it if neither are true. Many motor controllers have ways to tell them to enable and disable the drive motors directly. Check if yours do and how to trigger it. If it’s built in RC then you don’t need RC relays. If it wants a switch, then you can put a small RC relay on it. I don’t have any drawings for how to properly do it if neither are true.

    **3. Sam Morton:**
    > You can do this from the Ethos on the controller. You need a couple of logic switches and a mix. Search for Ethos and Replace essentially you use logic switches to replace the channel outputs to zero say when a toggle is switched on. Many airplane folks use this to prevent runaway. I'm. Not in a good place to show you the steps but if you cant find it online message me and I will try and walk you through it.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2762017234130925/){ .md-button }

??? question "Hey Everyone, When I first started researching, I was planning to go with Stealth, but I’ve since decided on the Kyber s..."

    *Posted by **Brian Dodds**:*
    > Hey Everyone,
    When I first started researching, I was planning to go with Stealth, but I’ve since decided on the Kyber system since it seems to better fit my needs. Based on the Kyber PDF, the 24-servo limit should be more than enough—I doubt I’ll ever exceed that.
    I’m reaching out because electronics aren’t my strong suit, and I could use some guidance. This is my first build, going all-metal wit...

    **Community answers:**

    **1. Al Cordera:**
    > All your questions can’t be answered all at once. Your first decision of going to Kyber was the right one. Your next one is what do you want your droid to do within both compartments (Dome and/or Body).
    > I recommend you plan for everything as you design and build your electrical system that way you’re ready to modify and add to it.
    > Based on my last two years of R2D2 driving at events, you get bored with just him driving and making sounds. You’ll want dome panels to open and then you’ll want gizmos coming out of body panels.
    > I put a 24 channel Maestro Board in the dome and an 18 channel in the body and I’ve almost maxed those out as I want more!
    > You will learn to start with 24v coming in for t...

    **2. Al Cordera:**
    > All your questions can’t be answered all at once. Your first decision of going to Kyber was the right one.  Your next one is what do you want your droid to do within both compartments (Dome and/or Body).  I recommend you plan for everything as you design and build your electrical system that way you’re ready to modify and add to it. Based on my last two years of R2D2 driving at events, you get bored with just him driving and making sounds.  You’ll want dome panels to open and then you’ll want gizmos coming out of body panels.  I put a 24 channel Maestro Board in the dome and an 18 channel in the body and I’ve almost maxed those out as I want more!  You will learn to start with 24v coming in ...

    **3. Malcolm MacKenzie:**
    > The wiring diagram you've chosen is a very traditional set up using the Dimension Engineering Sabertooth motor controller which is capable of driving two brushed motors at the same time. It's a VERY robust controller that will run your Warp Drives just fine. The lack of a fuse box is because for the shown components, none is really needed. The Sabertooth and Syren (the dome motor controller) should not be fused. All the other components except for the amplifier are low voltage. You might choose to have fuses on the amp and on various other circuits, but they are not absolutely necessary. Fuse boxes do provide a convenient central 'hub' for electrical connections however, and lots of Droid bu...

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2586893418309975/){ .md-button }

??? question "Hello. SK-138 is happy with the Kyber System. 2 Maestros (body and dome) and Taranis QX7. Very happy with this system..."

    *Posted by **Ricardo Juntas Asensio**:*
    > Hello. 
    SK-138 is happy with the Kyber System. 2 Maestros (body and dome) and Taranis QX7. 
    Very happy with this system and waiting for the new functionality that support Marcduino to test it into my R2-D2. Any idea about the release of this update?
    Thanks!!

    **Community answers:**

    **1. Matt Hobbs:**
    > Looking good. Glad to see that you like the system

    **2. Brian Dodds:**
    > Marcduino support is there now?

    **3. Luis Rodriguez:**
    > Wow,
    >  that looks awesome!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1676584649340861/){ .md-button }

??? question "Hi, apologies if this has been asked but I couldn't find it... Does Kyber allow for an 'expansion module' concept simila..."

    *Posted by **Thomas LeBlanc**:*
    > Hi, apologies if this has been asked but I couldn't find it...
    Does Kyber allow for an "expansion module" concept similar to the Stealth system? I.e., a separate small arduino listening for broadcast I2C commands, where each expander runs custom (user-written) code to determine if it should react to that I2C command or not (and how to). I've done that w/ great success in my R2, and it allows for p...

    **Community answers:**

    **1. Benjamin Essex-Morgan:**
    > Thomas LeBlanc hey! Im working on a J5 as well. I had the same question a few weeks ago. I think I have it down to run more than 2 maestros. This is how I explained it to see if I had the understanding down to Sean and he said I'm on the right track with this example:
    > "So the individual sequence programs are progrmmed to their respective maestro.
    > Those sequence numbers are called up when a button is pressed in kyber, and implemented to their corresponding maestros irrespective of the 2 maestros adressable limit in kyber.
    > So you have a program sequence number 42 that's programmed only on maestro 3 and 4. Maesteo 3 and 4 are cloned to maestro 1. But maestro 1 doesn't have sequence number 42 pr...

    **2. Benjamin Essex-Morgan:**
    > Thomas LeBlanc hey!  Im working on a J5 as well.  I had the same question a few weeks ago.  I think I have it down to run more than 2 maestros.  This is how I explained it to see if I had the understanding down to Sean and he said I'm on the right track with this example:"So the individual sequence programs are progrmmed to their respective maestro.Those sequence numbers are called up when a button is pressed in kyber, and implemented to their corresponding maestros irrespective of the 2 maestros adressable limit in kyber. So you have a program sequence number 42 that's programmed only on maestro 3 and 4.  Maesteo 3 and 4 are cloned to maestro 1.  But maestro 1 doesn't have sequence number 4...

    **3. Matt Hobbs:**
    > Yes we have room for additional expansion modules. You can run more than 2 maestros but they have to be the same serial numbers. For instance you could have 3 maestros that all have serial number 2. When you play a sequence that calls for serial number 2 then all 3 would play the called sequence.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1987194151613241/){ .md-button }

??? question "Problem to Solve: Kyber Control Board reboots as if he's not maintaining power. NOTE: I have triple checked the power wi..."

    *Posted by **Cory Hall**:*
    > Problem to Solve: Kyber Control Board reboots as if he's not maintaining power. NOTE: I have triple checked the power wires from the main power board to the Kyber and nothing is loose. I even rebuilt the leads in case I had a partial break in one of the lines.
    When does it occur? R2D2 can be standing still or on the move.
    What occurs? R2D2 will spasm and jump forward and spin for about a second wh...

    **Community answers:**

    **1. Trevor Zaharichuk:**
    > You have a 12 V buck regulator in the system. I think that may be the issue. Check all the voltages in your system. Looks like you may not actually need it.
    > It looks like you have a different ground for the 12V then the 24V stuff. If so, you may actually have a ground loop going on. Is the 12V regulator you have in there an isolated supply?
    > You say you lose control of the Droid while the cyber reboots. Since you have the drive direct control from the Rx, it shouldn't matter if the kyber reboots. I would change your power to the receiver to come from the saber tooth. That way the drive control is always on the same power. Remove the 5V then between the kyber and receiver if you do that.
    > To fi...

    **2. Darren Moser:**
    > I also have a two Maestro setup in my droids as well. I noticed a difference in your wiring between the two Maestro's than what the Kyber manual says.
    > If your body maestro is M1. then it should have the ground, VIN (5v), RX and TX from the Kyber. With a TXIN connected to M2'(Dome)'s TX connector.
    > Your diagram also doesn't have VIN(5v) or TX going to M2 (Dome) .
    > I'd try looking a the kyber manual again and makeing sure the two maestros are wired together correctly.
    > My 2 cents
    > Let me know if you have any clarification questions. I also have a two Maestro setup in my droids as well. I noticed a difference in your wiring between the two Maestro's than what the Kyber manual says. If your body mae...

    **3. Austin Heinrich:**
    > I am by no means an expert on wiring a droid, yet any way. I have built quite a few drones. What you are describing sounds like a cold solder joint. Could be a bad crip on a connector, or maybe you are drawing too many amps. when that happens on drone motors or controllers will turn off momentarily causing you to crash. To fix the problem on a drone we add a capacitor on the battery feed, look for cold solder joints. for the droid if it is a low amp issue I think you would need to increase the amps available to certain components or maybe add a relay. That said as I haven’t seen you getting any ideas as to how to find your issue I thought I would toss some thoughts your way. Good luck.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2215896078743046/){ .md-button }

??? question "Does the kyber system connect to lights too, or is it just motors and sounds? I have an Astropixels dome light set and..."

    *Posted by **Matt Hobbs**:*
    > Does the kyber system connect to lights too, or is it just motors and sounds? 
    I have an Astropixels dome light set and it can be sent some kinds of commands to do extra features but I haven't dug deep enough to know what. I was also thinkng about adding some other standalone things like a Knight Rider / Cylon light in the large data port that I would like to trigger along with matching sounds

    **Community answers:**

    **1. Group Member:**
    > Justin Hall Matt Hobbs its serial or i2c by default. You can upload some alternative firmware to give marcduino commands too.

    **2. Group Member:**
    > Justin Hall Matt Hobbs its serial or i2c by default. You can upload some alternative firmware to give marcduino commands too.

    **3. Group Member:**
    > Tony Mueller I think it can. Thanks. Do I contact you via messenger to buy, or is there a website?

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2584794568519860/){ .md-button }

??? question "Can someone please help me with some cloudy questions, part one- I wired my setup like pictured below, in the radio for..."

    *Posted by **Matt Hobbs**:*
    > Can someone please help me with some cloudy questions, part one- I wired my setup like pictured below, in the radio for the motor movement for R2 how do I assign the sticks to how I want them to move with the foot motors and dome. Also, Part two- can some please give me an example with maestro script to move a door or something to button setup on controller? Sorry ahead of time on the dumb questio...

    **Community answers:**

    **1. Group Member:**
    > Shawn Krupianik Matt Hobbs I know how to get things moving with the maestro once the script is created and saved to maestro. How do I connect that sequence to the kyber and when the button is pushed from the radio? Say I create a button on the radio for open door , from there connecting the button to tell the kyber to trigger the maestro sequence for the door? I'm not sure how the process goes to connect them all.

    **2. Matt Hobbs:**
    > Both of these questions are pretty detailed and will require some reason on your part. All maestro scripts are unique to everyone’s/your maestro setup and servo connections. You don’t need to know how to write the code, you just need to know how to generate the sequences and then the maestro writes the scripts.

    **3. Mark Smith:**
    > You might want to check on whether you should have two grounds on the speed controllers. Dimension Engineering recommends only one ground on the 0v/5v/S1/S2 blocks.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2507344116264906/){ .md-button }

??? question "Can use some assistance again, trying to set-up the tank drive following Tims video and thought I did it correctly. All..."

    *Posted by **Matt Hobbs**:*
    > Can use some assistance again, trying to set-up the tank drive following Tims video and thought I did it correctly. All it's doing is spinning in circles at the moment, not going forward or backwards. Is there something I am missing? Both Motors are working. Thank you

    **Community answers:**

    **1. Kelly Larson:**
    > Hey Kenzō Barlow, my brother got me hooked on these ferrules for all wire ends. They even work great for wago connectors if you use the red ones. This will reduce crushed wires or connectors coming loose while in use
    > https://a.co/d/2RzeDWT Hey Kenzō Barlow, my brother got me hooked on these ferrules for all wire ends. They even work great for wago connectors if you use the red ones. This will reduce crushed wires or connectors coming loose while in use https://a.co/d/2RzeDWT AMAZON.COM Ferrule Crimping Tool Kit - Sopoby Ferrule Crimper Plier (AWG 28-7) with 1800pcs Wire Ferrules Kit Wire Ends Terminals

    **2. Matt Hobbs:**
    > The easiest thing to do here is reverse the wiring of one of the motors on the motor controller. One you do that you should see it be able to go front and back. Then you can use the reverse function on the transmitter to get it doing what you want it too.

    **3. Group Member:**
    > Kenzō Barlow Thank you! that was it. Guessing because it's carpet it gets stuck and spins so need to avoid that lol

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2248715422127778/){ .md-button }

??? question "I just bought the X20. Is there a minimum receiver that I need? Also, in the manual everything is for no motor lock ou..."

    *Posted by **John Boisvert**:*
    > I just bought the X20. Is there a minimum receiver that I need?
      Also, in the manual everything is for no motor lock out, has is there a good way?

    **Community answers:**

    **1. Matt Hobbs:**
    > I can show you what I do for motor on and off. A new drawing will be included in the new manual as well

    **2. Brian Dodds:**
    > Any of the TD receivers should work. Even the smaller TDR6 has SBUS out, though it's not a normal 3 pin connector.

    **3. Stephane Beaulieu:**
    > The Archers Plus series are the latest one. No need for the S, the basic 6, 8 or 10 channels will do great.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2004570689875587/){ .md-button }

??? question "Hi. With the Kyber system in a r2, is it possible to manually control the dome movement, or put it in auto mode where it..."

    *Posted by **Matthew Collins**:*
    > Hi. With the Kyber system in a r2, is it possible to manually control the dome movement, or put it in auto mode where it makes random movements, or make it carry out a set sequence?

    **Community answers:**

    **1. Matt Hobbs:**
    > You still have to control the dome yourself. We have plans to add in an auto mode but haven’t got to that yet.

    **2. Group Member:**
    > Matthew Collins Matt Hobbs great thanks for your quick reply!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1733693796963279/){ .md-button }

??? question "Is Kyber v2 still limited to 2 Maestros? Working on R2 and looking to see what will be best for controlling Body, Warp C..."

    *Posted by **Amit Patel**:*
    > Is Kyber v2 still limited to 2 Maestros?
    Working on R2 and looking to see what will be best for controlling Body, Warp Core Base and Dome, trying to reduce wires so having 3 Maestros would be ideal but I know in v1 it was limited to 2.

    **Community answers:**

    **1. Group Member:**
    > Amit Patel Brian Dodds yea I have 2 x 24 Servos boards and in theory that does give me all the controls I need I was just trying to reduce the number of wires going from the body to the dome plate.
    > Was hoping to just have 3 Maestros running, 1 in each location so I can keep my wiring clean.
    > I’m installing the Warp Core inner and outter pcbs so might need to see if a Marcduino would be a better option or change up to a 36 channel slipring. Brian Dodds yea I have 2 x 24 Servos boards and in theory that does give me all the controls I need I was just trying to reduce the number of wires going from the body to the dome plate. Was hoping to just have 3 Maestros running, 1 in each location so I ca...

    **2. Brian Dodds:**
    > They make 24 channel versions. You need more channels???
    > I use Marcduinos in the Dome controlled by Kyber and a 12 channel Maestro for the body. More than enough for R2. They make 24 channel versions. You need more channels??? I use Marcduinos in the Dome controlled by Kyber and a 12 channel Maestro for the body. More than enough for R2.

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/1947643482234975/){ .md-button }

??? question "Tank drive issues. Two Flipsky Mini V6 ESC successfully programmed and working with the motors. I setup my mixes but th..."

    *Posted by **Chris Carpenter**:*
    > Tank drive issues. Two Flipsky Mini V6 ESC successfully programmed and working with the motors.  I setup my mixes but the left side seems to be driving harder than the right.  When I rotate him he doesn't spin on the axis it more of a circle. He also jerks hard in one direction when turning.  Forward and revers are good.  Any thoughts?

    **Community answers:**

    **1. Chris Carpenter:**
    > I figured it out. I'm using Aileron and Elevator for drive control and for whatever reason the mix had extra input on the Aileron. I made a new model used a Taileron mix instead and it works great!

    [:fontawesome-brands-facebook: View original post](https://www.facebook.com/groups/1341505756182087/posts/2709496736049642/){ .md-button }
