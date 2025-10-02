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
    style.SetCanvasDefW(600)
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
    style.SetTitleSize(0.04, "xyz")
    style.SetTitleSize(0.04, "")
    style.SetTitleFont(132, "")
    style.SetTitleFont(132, "xyz")
    style.SetTitleOffset(1.35, "y")
    style.SetTitleOffset(1.2, "x")
    style.SetTitleOffset(1.45, "z")
    
    # Label options
    style.SetLabelSize(0.04, "xyz")
    style.SetLabelFont(132, "xyz")
    
    # Legend options
    style.SetLegendBorderSize(0)
    style.SetLegendFont(132)
    style.SetLegendFillColor(-1)
    
    # Other options
    style.SetMarkerStyle(1)
    style.SetLineWidth(1)
    
    style.SetFillStyle(4000)
    return style

def th1_style():
    """Define the style settings for TH1 histograms."""
    styleh1 = ROOT.TStyle('Th1S', 'Th1Style by AF')
    general_style().Copy(styleh1)
    
    # Custom palette
    hex_colors = ["#3f90da", "#ffa90e", "#bd1f01", "#94a4a2", "#832db6", "#a96b59", "#e76300", "#b9ac70", "#92dadd"]
    colors = [ROOT.TColor.GetColor(hex) for hex in hex_colors]
    myPalette = np.array(colors, dtype=np.int32)
    styleh1.SetPalette(9, myPalette)
    
    # Adjust right margin for TH1
    styleh1.SetPadRightMargin(0.08)
    return styleh1

def th2_style():
    """Define the style settings for TH2 histograms."""
    styleh2 = ROOT.TStyle('Th2S', 'Th2S Style by AF')
    general_style().Copy(styleh2)
    
    # Adjust right margin for TH2 to accommodate color bar
    styleh2.SetPadRightMargin(0.165)
    # styleh2.SetCanvasDefW(700)
    
    return styleh2