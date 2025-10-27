# Kyber Controls Manual V3 - Generation Guide

This directory contains the source files and scripts needed to generate the Kyber Controls Manual V3 PDF documentation.

## Prerequisites

### Required Software
1. **Pandoc** - Document converter
   ```bash
   brew install pandoc
   ```

2. **MacTeX or BasicTeX** - LaTeX distribution for PDF generation
   ```bash
   brew install --cask mactex-no-gui  # Full installation
   # OR
   brew install --cask basictex        # Smaller installation
   ```

3. **Python 3** with PIL/Pillow (for image processing)
   ```bash
   pip3 install Pillow
   ```

4. **pdfimages** (optional, for extracting images from existing PDFs)
   ```bash
   brew install poppler
   ```

## Directory Structure

```
docs/
├── KYBER_MANUAL_V3_DRAFT.md      # Main manual source in Markdown
├── Kyber_Controls_Manual_V3.pdf   # Generated PDF output
├── compile_pdf.sh                 # PDF generation script
├── compile_pdf_final.sh           # Production PDF generation script
├── create_exact_overlay.py        # Creates component overlays for board images
├── rotate_images.py               # Utility to rotate images
├── PDF_GENERATION_SUCCESS.md      # Generation status/notes
└── images/                        # All manual images
    ├── hardware/                  # Board layouts and hardware photos
    ├── wiring/                    # Wiring diagrams
    ├── transmitters/              # Transmitter setup photos
    ├── maestros/                  # Maestro pinout diagrams
    ├── web_interface/             # Web interface screenshots
    ├── misc/                      # Logo and miscellaneous images
    └── originals/                 # Original extracted images from V2
```

## Generating the Manual

### Quick Generation
```bash
cd docs
bash compile_pdf.sh
```

### Manual Generation with Custom Options
```bash
export PATH="/Library/TeX/texbin:$PATH"
pandoc KYBER_MANUAL_V3_DRAFT.md \
    --from markdown+smart \
    --to pdf \
    --pdf-engine=xelatex \
    --toc \
    --toc-depth=3 \
    -V documentclass=report \
    -V fontsize=11pt \
    -V geometry:margin=1in \
    -V colorlinks=true \
    -V mainfont="Helvetica Neue" \
    -V monofont="Menlo" \
    -V graphics=true \
    -V 'header-includes=\usepackage{float}\let\origfigure\figure\let\endorigfigure\endfigure\renewenvironment{figure}[1][2] {\expandafter\origfigure\expandafter[H]}{\endorigfigure}' \
    -o Kyber_Controls_Manual_V3.pdf
```

## Updating the Manual

### Adding/Updating Content
1. Edit `KYBER_MANUAL_V3_DRAFT.md` using Markdown syntax
2. Place any new images in the appropriate `images/` subdirectory
3. Reference images using relative paths: `![Description](images/category/filename.jpg)`

### Creating Board Overlays
The main board layout image includes numbered component overlays. To regenerate or adjust these:

```bash
python3 create_exact_overlay.py
```

Edit the component positions in the script if adjustments are needed.

### Rotating Images
If images need rotation:

```bash
python3 rotate_images.py
```

## Image Requirements

### Web Interface Screenshots
Place screenshots in `images/web_interface/`:
- `web_home.png` - Home page
- `web_general.png` - General settings
- `web_buttons_overview.png` - Button configuration
- `web_rc_channels.png` - RC settings
- `web_random.png` - Random configuration
- `web_wifi.png` - WiFi settings
- `web_firmware.png` - Firmware management

### Image Specifications
- Format: PNG or JPG
- Resolution: 1920x1080 maximum recommended
- File size: Under 500KB each for optimal PDF size
- Clear labeling and annotations where needed

## Current Manual Status

### Version 3.0 Features
- Updated for firmware V150+
- Support for 45 buttons (3 pads of 15 buttons each)
- 24-channel SBUS documentation
- Modern web interface screenshots
- Enhanced board layout diagrams with component overlays
- Comprehensive wiring guides

### Known Issues
- Some arrow characters (→) don't render in certain fonts (cosmetic issue)
- Minor LaTeX warnings about undefined references (doesn't affect output)

## Troubleshooting

### "pdflatex not found"
Ensure TeX is in your PATH:
```bash
export PATH="/Library/TeX/texbin:$PATH"
```

### Line ending errors in scripts
If you get `^M` or line ending errors:
```bash
dos2unix compile_pdf.sh  # If available
# OR
tr -d '\r' < compile_pdf.sh > compile_pdf_fixed.sh
bash compile_pdf_fixed.sh
```

### Missing images
- Verify all image paths in the markdown match actual file locations
- Check that image files exist in the correct subdirectories
- Use relative paths from the docs directory

## Contributing

When updating the manual:
1. Make changes to `KYBER_MANUAL_V3_DRAFT.md`
2. Test PDF generation locally
3. Verify all images appear correctly
4. Check that internal links and TOC work properly
5. Commit both source files and generated PDF

## License

The Kyber Controls System and this manual are licensed for personal use only under CC BY-NC-ND 4.0.

---

*Manual Generation System - Created August 2024*
*For firmware version 150 and later*