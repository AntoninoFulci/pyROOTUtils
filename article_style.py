import ROOT
import numpy as np

def general_style():
    """Define the general style settings."""
    style = ROOT.TStyle('GeneralStyle', 'General Style by AF')
    # Disable statistics box and title display
    style.SetOptStat(0)
    style.SetOptTitle(0)
    
    # Set image scaling for high-resolution PNGs
    style.SetImageScaling(2.)
    
    # Canvas options
    style.SetCanvasDefW(500)
    style.SetCanvasDefH(500)
    style.SetCanvasColor(0)
    style.SetTitleFillColor(0)
    style.SetStatColor(0)
    
    # Pad options
    style.SetPadBottomMargin(0.12)
    style.SetPadTopMargin(0.08)
    style.SetPadLeftMargin(0.125)
    
    # Frame options
    style.SetFrameLineWidth(1)
    
    # Palette options
    style.SetPalette(55, 0)
    
    # Title options
    style.SetTitleSize(0.043, "xyz")
    style.SetTitleSize(0.05, "")
    style.SetTitleFont(132, "")
    style.SetTitleFont(132, "xyz")
    style.SetTitleOffset(1.4, "y")
    style.SetTitleOffset(1.25, "x")
    
    # Label options
    style.SetLabelSize(0.04, "xyz")
    style.SetLabelFont(132, "xyz")
    
    # Legend options
    style.SetLegendBorderSize(0)
    style.SetLegendFont(132)
    style.SetLegendFillColor(-1)
    
    # Other options
    style.SetLineWidth(2)
    style.SetFillStyle(4000)
    return style

def th1_style():
    """Define the style settings for TH1 histograms."""
    style = general_style()
    style.SetName('TH1Style')
    
    # Custom palette
    hex_colors = ["#3f90da", "#ffa90e", "#bd1f01", "#94a4a2", "#832db6", "#a96b59", "#e76300", "#b9ac70", "#92dadd"]
    colors = [ROOT.TColor.GetColor(hex) for hex in hex_colors]
    myPalette = np.array(colors, dtype=np.int32)
    style.SetPalette(9, myPalette)
    
    # Adjust right margin for TH1
    style.SetPadRightMargin(0.05)
    return style

def th2_style():
    """Define the style settings for TH2 histograms."""
    style = general_style()
    style.SetName('TH2Style')
    
    # Adjust right margin for TH2 to accommodate color bar
    style.SetPadRightMargin(0.145)
    return style