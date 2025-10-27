#!/bin/bash

# Compile Kyber Controls Manual V3 to PDF
# This script uses XeLaTeX with the float package to ensure proper image placement

echo "=========================================="
echo "Compiling Kyber Controls Manual V3 to PDF"
echo "=========================================="
echo ""

# Add TeX to PATH
export PATH="/Library/TeX/texbin:$PATH"

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed"
    echo "Install with: brew install pandoc"
    exit 1
fi

# Check if xelatex is available
if ! command -v xelatex &> /dev/null; then
    echo "Error: xelatex is not installed"
    echo "Install with: brew install --cask mactex-no-gui"
    exit 1
fi

# Compile with pandoc and xelatex
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

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ PDF generated successfully: Kyber_Controls_Manual_V3.pdf"
    ls -lh Kyber_Controls_Manual_V3.pdf
else
    echo ""
    echo "✗ PDF generation failed"
    exit 1
fi