#!/usr/bin/env python3
"""
Create exact overlay matching the original PDF for Kyber board
"""

import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Please install Pillow: pip3 install Pillow")
    sys.exit(1)

def create_exact_board_overlay():
    """Create the exact overlay as shown in the original PDF"""
    
    input_path = "/Users/nh1584/Documents/DroidCode/Kyber130/docs/images/hardware/main_board_layout.jpg"
    output_path = "/Users/nh1584/Documents/DroidCode/Kyber130/docs/images/hardware/main_board_layout_annotated.jpg"
    
    if not os.path.exists(input_path):
        print(f"Error: Input image not found at {input_path}")
        return False
    
    # Open the image
    img = Image.open(input_path)
    width, height = img.size
    print(f"Image dimensions: {width}x{height}")
    
    # Create overlay
    draw = ImageDraw.Draw(img)
    
    # Try to load a good font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)  # Larger font
    except:
        font = ImageFont.load_default()
    
    # Component positions based on the original PDF image
    # These are adjusted based on the actual board layout shown
    components = [
        # Component 1: SD Card (silver box on the right side of DFPlayer)
        {
            'number': '1',
            'circle_pos': (520, 880),  # Moved right to be over the silver SD card reader
            'arrow_end': None,         # No arrow for this one
        },
        # Component 2: Speaker output (left of SD card)
        {
            'number': '2',
            'circle_pos': (270, 880),  # Speaker terminals
            'arrow_end': (100, 950),    # Where arrow points to label
        },
        # Component 3: Audio jack (black rectangle on DFPlayer)
        {
            'number': '3',
            'circle_pos': (850, 650),  # Moved down to be over the black rectangle
            'arrow_end': None,         # No arrow for this one
        },
        # Component 4: Power Input (green terminal, right)
        {
            'number': '4',
            'circle_pos': (900, 380),  # Green power terminal
            'arrow_end': (950, 330),    # Where arrow points to label
        },
        # Component 5: Kyber I/O (header pins, top right - will use L-shaped box instead)
        {
            'number': '5',
            'circle_pos': None,        # Will use L-shaped box instead
            'arrow_end': None,         # No arrow needed
        },
    ]
    
    # Draw styles
    circle_radius = 30                    # Larger circles
    circle_color = (255, 0, 0)           # Brighter red
    circle_outline = (255, 255, 255)     # White
    text_color = (255, 255, 255)         # White
    arrow_color = (255, 0, 0)            # Brighter red
    box_color = (255, 0, 0)              # Brighter red for boxes
    line_width = 5                        # Thicker lines
    
    # Draw L-shaped box for component 5 (Kyber I/O pins)
    # This covers all the header pins in an L-shape
    # Based on the original PDF, this should encompass the pin headers
    l_box_points = [
        (380, 120),   # Top left of horizontal part (moved left)
        (680, 120),   # Top right of horizontal part
        (680, 250),   # Right side going down
        (580, 250),   # Turn corner inward (making the L)
        (580, 450),   # Bottom of vertical part
        (380, 450),   # Left side of vertical part
        (380, 120),   # Back to start
    ]
    draw.polygon(l_box_points, outline=box_color, fill=None, width=line_width)
    
    # Draw "5" in the middle of the L-shaped box
    bbox = draw.textbbox((0, 0), "5", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = 530 - text_width // 2  # Centered in the L-shape
    text_y = 185 - text_height // 2
    
    # White background for the number
    draw.ellipse(
        [text_x - 25, text_y - 25,
         text_x + text_width + 25, text_y + text_height + 25],
        fill=circle_outline,
        outline=circle_outline
    )
    # Red circle with number
    draw.ellipse(
        [text_x - 20, text_y - 20,
         text_x + text_width + 20, text_y + text_height + 20],
        fill=circle_color,
        outline=(150, 0, 0),
        width=2
    )
    draw.text((text_x + 10, text_y + 5), "5", fill=text_color, font=font)
    
    # Draw components with circles and arrows
    for comp in components:
        if comp['number'] == '5':
            continue  # Already handled with L-shaped box
            
        circle_pos = comp.get('circle_pos')
        if not circle_pos:
            continue
            
        x, y = circle_pos
        num = comp['number']
        arrow_end = comp.get('arrow_end')
        
        # Draw white background circle (for contrast)
        draw.ellipse(
            [x - circle_radius - 3, y - circle_radius - 3,
             x + circle_radius + 3, y + circle_radius + 3],
            fill=circle_outline,
            outline=circle_outline,
            width=2
        )
        
        # Draw red circle
        draw.ellipse(
            [x - circle_radius, y - circle_radius,
             x + circle_radius, y + circle_radius],
            fill=circle_color,
            outline=(150, 0, 0),  # Darker red outline
            width=2
        )
        
        # Draw number in circle
        # Center the text
        bbox = draw.textbbox((0, 0), num, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = x - text_width // 2
        text_y = y - text_height // 2
        
        draw.text((text_x, text_y), num, fill=text_color, font=font)
        
        # Draw arrow only if arrow_end is specified
        if arrow_end:
            arrow_x, arrow_y = arrow_end
            # Calculate arrow start point (edge of circle)
            dx = arrow_x - x
            dy = arrow_y - y
            distance = (dx**2 + dy**2)**0.5
            if distance > 0:
                # Normalize and scale to circle radius
                start_x = x + (dx / distance) * circle_radius
                start_y = y + (dy / distance) * circle_radius
                
                # Draw arrow line
                draw.line([(start_x, start_y), (arrow_x, arrow_y)], 
                         fill=arrow_color, width=line_width)
                
                # Draw arrowhead
                arrow_size = 20  # Larger arrowhead
                angle = 0.5  # radians
                
                # Calculate arrowhead points
                head_angle = 3.14159 - angle
                head_x1 = arrow_x - arrow_size * (dx / distance)
                head_y1 = arrow_y - arrow_size * (dy / distance)
                
                # Draw arrowhead lines
                draw.line([(arrow_x, arrow_y), (head_x1 - 12, head_y1 - 12)], 
                         fill=arrow_color, width=line_width)
                draw.line([(arrow_x, arrow_y), (head_x1 + 12, head_y1 - 12)], 
                         fill=arrow_color, width=line_width)
    
    # Save the annotated image
    img.save(output_path, quality=95)
    print(f"✓ Saved annotated image: {output_path}")
    
    return True

def adjust_manual_image_placement():
    """Create a note about fixing image placement in the manual"""
    
    fix_note = """
# Fix for Image Placement in Manual

The main board layout image needs to be placed immediately after the component list,
not below it. Update the markdown as follows:

## Main Board Layout

![Main Board Layout](images/hardware/main_board_layout_annotated.jpg)

### Main Board Components:

1. **SD Card Slot** - Insert SD card with MP3 files
2. **Speaker Output** - 3W maximum (terminal closest to DFPlayer is negative)
3. **3.5mm Audio Jack** - For external amplifier connection
4. **Power Input** - 7.5V to 36V DC
5. **Kyber I/O Connections** - 5V output, 2.5A maximum current

(Additional components in red box are Marcduino/Maestro connections)

This way the numbered overlay image appears right with the numbered list.
"""
    
    with open("/Users/nh1584/Documents/DroidCode/Kyber130/docs/image_placement_fix.md", "w") as f:
        f.write(fix_note)
    
    print("✓ Created image placement fix instructions")

if __name__ == "__main__":
    print("="*50)
    print("Creating Exact Board Overlay from Original PDF")
    print("="*50)
    print()
    
    if create_exact_board_overlay():
        adjust_manual_image_placement()
        print()
        print("✓ Overlay created successfully!")
        print()
        print("Note: You may need to fine-tune the positions in the")
        print("      components array to match your exact board image.")
    else:
        print("✗ Failed to create overlay")