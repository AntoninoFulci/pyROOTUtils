# pyROOTUtils

This directory contains utilities for customizing ROOT styles to create publication-quality plots. The main script, `article_style.py`, defines three styles for general ROOT canvases, 1D histograms (TH1), and 2D histograms (TH2).

## Files

### `article_style.py`

This script provides three functions to define and apply custom ROOT styles:

1. **`general_style()`**:
   - Configures global settings for ROOT plots.
   - Disables statistics box and title display.
   - Sets canvas, pad, frame, and legend options.
   - Adjusts font sizes, label sizes, and title offsets.
   - Enables high-resolution image scaling for PNG outputs.

2. **`th1_style()`**:
   - Builds upon the general style.
   - Defines a custom color palette using hex colors.
   - Adjusts the right margin for 1D histograms.

3. **`th2_style()`**:
   - Builds upon the general style.
   - Adjusts the right margin to accommodate the color bar for 2D histograms.

### How to Use


1. **Customize Further**:
   - Modify the `article_style.py` file to adjust parameters like margins, fonts, or palettes.

## Dependencies

- [ROOT](https://root.cern/) - A framework for data analysis.
- [NumPy](https://numpy.org/) - Used for handling custom color palettes.

## Author

Developed by AF for creating consistent and high-quality ROOT plots.
