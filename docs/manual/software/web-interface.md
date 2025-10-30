# Web Interface

The Kyber Control System provides a powerful web-based interface for configuration. The interface is designed to be intuitive and responsive, allowing you to configure your system from any supported web browser.

![Web Interface Home](../../assets/web_interface/web_home.png)

!!! info "Interface Overview"
    Top menu provides quick access to all major functions of the system.  
    The web interface will adjust dynamically to your configuration.

## Browser Compatibility

The web interface is officially supported on:

- Google Chrome (Recommended)
- Internet Explorer
- Safari

!!! tip "Browser Recommendation"
    For the best experience, we recommend using Google Chrome as it provides optimal performance and compatibility.
---
## General Page

The General Page is where you do basic configuration of the Kyber Controller.  
Start Kyber configuration with this page first

![General](../../assets/web_interface/web_general.png){ align=center }

---

![General](../../assets/web_interface/web_general_features.png){ align=center }

## Features
- **Serial Command** - Enables sending commands via the serial port "Marcduino on the Kyber Board" to any devices that support this type of connexion. 
- **Human Cyborg Relations (HCR)** - When enabled, this will add HCR configuration menu in General page.  Connexion to the HCR will be with the same Serial port "Marcduino"

---

![General](../../assets/web_interface/web_general_RC.png){ align=center }
## RC Channels Settings
- **Button PAD** - Enter RC channel for the External Button PAD or Kyberpad.
- **Toggle for PAD 2** - Enter RC channel to switch between Button PAD 1 and PAD 2.  This will be set on a 2 position toggle switch.
- **Volume Control** - Enter RC channel to control volume.  This will be set on a slider or POT on the remote.
- **Buttons 1-2 3-4 5-6** - Enter RC channel to act like a set of 2 buttons.  This wil be set on a 3 positions toggle switch for each channels. (See Buttons RC section)
- **Random On/Off** - Enter RC channel to enable Random sounds and events.  This will be set on a 3 positions toggle switch. (See Random Section for more Info)

---

![General](../../assets/web_interface/web_general_maestro.png){ align=center }
## Maestro
- **Quantity** - Enter how many Maestro you will be using. Kyber support up to 2 Maestro, from 6 to 24 channels. After saving, a new Maestro Menu will be displayed

---

![General](../../assets/web_interface/web_general_maestro2.png){ align=center }
## Maestro menu
- **Startup Script** - A script Will play on selected Maestro after Kyber boot.
- **Delay** - Set a delay to postpone the script.
- **Enable Script Check** - Check if a script is already running before starting a new one.  When enabled, if a script is already running, new script will not start.

---

<div class="grid" markdown>
![Image1](../../assets/web_interface/web_general_sound1.png){ width="36%" align=left }
![Image2](../../assets/web_interface/web_general_sound2.png){ width="40%" align=right }
</div>

## Sound
- **Volume Level** - Left picture: no RC channel is set for Volume Control, you can manually set the volume level from 0 to 30

- **Volume Level** - Right picture: RC channel set for volume control.  Sound level will be displayed depending on the slider/pot position

- **Start Sound** - Will be played after the Kyber boot sequence is finished.
- **Delay** - Add a delay before playing Start Sound.
- **Equalizer** - Set the Equalizer to your liking.  This is a feature built in the DFPlayer and cannot be adjusted manually.

---

![HCR Menu](../../assets/web_interface/web_HCR.png){ align=center width=70% }
## Human Cyborg Relation (HCR)
- **RC Channel** - Used to control HCR volume.  You can use the same channel for all 3.
- **Offset** - Used to adjust the sound level offset between each HCR channels.
- **Startup Scrip** - Used to send a command to HCR when the Kyber boot.
- **Delay** - Used to postpone startup script.

---

![General](../../assets/web_interface/web_general_registration.png){ align=center width=50% }
## Registration
- Add the name of your droid or your own name.  This will be displayed on the web interface footer

---

!!! warning "Save to Memory"
    Do not forget to save to memory when you edit settings. Change will be lost if you click on top menu.
---

## RC Settings Page

The RC Settings Page is where you do most of the configuration for the RC channels.  This page will adapt depending of the configuration you made in General Page

![RC Settings](../../assets/web_interface/web_RC.png){ align=center }

!!! failure "Fail"
     - No sBus connexion from the receiver to the Kyber, check wiring and receiver configuration
     ![RC Settings](../../assets/web_interface/web_RC_red.png){ align=center }

!!! success "Success"
     - Good sBus connexion from the receiver to the Kyber, support sbus16 and sbus24
     ![RC Settings](../../assets/web_interface/web_RC_green16.png){ align=center }
     ![RC Settings](../../assets/web_interface/web_RC_green24.png){ align=center }
---
![RC Settings](../../assets/web_interface/web_RC_PAD23.png){ align=center width=75% }
## Button PAD Configuration
- **Button PAD Mode** - Select 3 pads for a 3 positions toggle switch and 2 pads for a 2 positions
- **Toggle Channel** - Display RC channel set under General web page
- **Current SBUS Value** - Display SBUS value of the switch position coming from RC channel
- **Pad 1-2-3 SBUS Value** - Toggle the switch and write the current SBUS value for each toggle positions
---
![RC Settings](../../assets/web_interface/web_RC_Buttons.png){ align=center width=60% }
## Button Values Configuration
- This is where you will register each buttons PWM value for your configuration (Kyberpad or physical buttons)
- **Ch x SBUS Values** - Display the PWM value of RC channel x set under General tab.  Value displayed without pressing any buttons will be the released state
- **Button x PWM Value** - Register each buttons value in this field
- **Released PWM Value** - Register the released state value in this field
---
![RC Settings](../../assets/web_interface/web_RC_Passthrough.png){ align=center width=100% }
## RC Channels Pass Through
- Passthrough are used to map a RC channel to a Maestro servo output.  This give direct control on multiple servos
- **Description** - Enter a descrition or a name for the passthrough
- **RC Channel** - Set the RC channel you want to use. First you need to do a mix in the remote and assign it to a channel.
- **Maestro ID** - Set the ID of the Maestro you want to control. (1 or 2)
- **Maestro Channel** - Set the channel of the Maestro you want to control (0 to 23)
- **Maestro PWM Min/Max** - Set min and max PWM for this channel.
- **Maestro Disable Deadband** - Select for direct control on the servo without a deadband.

!!! hint "Tip"
     - Same RC channel can be used multiple time
     - PWM MIN and MAX can be inverted to change servo direction
     - If you set servo limit in Maestro Control Center, use the same values for MIN and MAX
     - Disabling Deadband will prevent the servo to move freely if used in a script (Maestro limitation)

!!! example "Example"
     - Servo #1 is connected to Maestro #1 port 5 and controlled by RC channel #1
     - Servo #2 is connected to Maestro #2 port 6 and controlled by RC channel #2.  
     Since Deadband is disabled, the servo cannot be controlled by a script
---

## Button Configuration Page

The Button Configuration Page is where all the buttons will be given a funtion.  It's the main feature of the Kyber Controller.

![Button Configuration](../../assets/web_interface/web_buttons_overview.png){ align=center width=100% }

- **PAD 1-2-3** - Depending on your configuration, PAD 1, 2 and 3 will be displayed.  Chose one to edit the buttons for this PAD
- **Name** - Enter a descrition for the Button
- **Sound MIN** - Set MIN sound to play.
- **Sound MAX** - Set MAX sound to play
- **Sound Delay** - Set a Delay before playing a sound.
- **Sound Random** - Sounds will be played randomly if a range is set between MIN and MAX
- **Maestro Script** - Set script number to play
- **Maestro Script2** - Set second script number to play
- **Maestro Script Delay** - Set a delay before playing a script
- **Serial Command** - Enter commands to be sent to Serial port. Need to finish with "\r" to be executed
- **Stop All** - This button will be the same on all PADs.  It stop sounds and action immediately.  A serial command can be send too

!!! hint "Sounds Tip"
     - **MIN/MAX** - To play only one sound, set the same value for MIN and MAX 
     - **Delay**  - Helpul to sync sound and motion
     - **Random** - If not selected, sound will play sequentially

!!! hint "Maestro Tip"
     - **Script** Script will always be played sequentially. For only one sricpt, set the same value for both 
     - **Delay** Helpful to sync sound and motion

!!! example "Example"
     - **Button 1** - Play Sound #1 on each button press, play script #1 on first button press and play script #2 on second button press
         - 1st press = open door
         - 2nd press = close door
     - **Button 2** - Play sounds 5 to 10 in a random order.  Sound will never be played 2 ime in a row
     - **Button 3** - Play "The Wave" sequence on Marcduino, at the same time play sound #2 with a slight delay to sync with motion

---


#### Button Controls
![Button Overview](../../assets/web_interface/web_buttons_overview.png){ align=center }

The button control interface allows for:
- Quick preset positions
- Customizable button actions
- Instant command execution
- Sequence triggering

#### Random Movement
![Random Control](../../assets/web_interface/web_random.png){ align=center }

The random movement feature enables:
- Automated position changes
- Customizable movement ranges
- Timing control
- Pattern generation

### Configuration

#### General Settings
![General Settings](../../assets/web_interface/web_general.png){ align=center }

The general settings panel allows you to configure:
- System preferences
- Default values
- Operation modes
- Interface options

#### WiFi Configuration
![WiFi Settings](../../assets/web_interface/web_wifi.png){ align=center }

The WiFi configuration panel provides:
- Network setup
- Connection management
- Security settings
- Signal strength monitoring

#### Firmware Management
![Firmware Updates](../../assets/web_interface/web_firmware.png){ align=center }

The firmware section enables:
- System updates
- Version management
- Update history
- System recovery options

## Mobile Interface

The interface automatically adapts to mobile devices:

1. **Touch-Optimized Controls**
   - Large touch targets
   - Swipe gestures
   - Pull-to-refresh
   - Touch-friendly sliders

2. **Mobile Layout**
   - Compact navigation
   - Collapsible panels
   - Quick action buttons
   - Optimized performance

!!! tip "Mobile Usage"
    When using a mobile device:
    
    - Use landscape orientation for better control
    - Enable screen rotation lock for stability
    - Use two-finger gestures for precise adjustments
    - Consider using a tablet for complex operations

## Keyboard Shortcuts

| Key Combination | Action |
|----------------|--------|
| Space | Emergency Stop |
| Arrow Up/Down | Fine Position Adjust |
| 1-9 | Select Channel |
| Ctrl + S | Save Settings |
| Ctrl + P | Play Sequence |

## Questions for Clarification

!!! question "For Project Owner"
    1. What is the default web interface port?
    2. Are there different user access levels?
    3. What browsers are officially supported?
    4. Should we include custom UI customization instructions?
    5. Are there mobile apps available?

## Accessing the Interface

### Local Access

1. Open a supported web browser
2. Navigate to `http://localhost:8080` (default address)
3. The interface will load automatically (no login required)

!!! info "Default Port"
    The default port is 8080. If you need to change this, you can modify it in the system settings.

### Remote Access

To access your Kyber Control System from outside your local network:

1. Configure port forwarding on your router:
   - Forward port 8080 (or your custom port) to your Kyber system
   - Use TCP protocol
   
2. Access via external IP:
   - Find your external IP address
   - Use `http://your-external-ip:8080`

!!! warning "Security Notice"
    When enabling remote access:
    
    - Use a firewall to restrict access
    - Consider using a VPN for secure remote connections
    - Regularly update your system firmware

!!! info "Custom Title"
    This is a note admonition. The title is optional.

!!! abstract "Abstract"
    Also known as "summary" or "tldr"

!!! info "Info"
    Additional information

!!! tip "Tip"
    Also known as "hint" or "important"

!!! success "Success"
    Also known as "check" or "done"

!!! question "Question"
    Also known as "help" or "faq"

!!! warning "Warning"
    Also known as "caution" or "attention"

!!! failure "Failure"
    Also known as "fail" or "missing"

!!! danger "Danger"
    Also known as "error"

!!! bug "Bug"
    Report a bug

!!! example "Example"
    An example

!!! quote "Quote"
    Also known as "cite"