import ROOT

def article_style():
    ArticleStyle = ROOT.TStyle('ArticleStyle','Article Style by AF')
        
    ArticleStyle.SetOptStat(0)
    ArticleStyle.SetOptTitle(0)

    #Per salvare le immagini in png in alta risoluzione
    ArticleStyle.SetImageScaling(3.)

    #Canvas options
    ArticleStyle.SetCanvasDefW(500)
    ArticleStyle.SetCanvasDefH(500)
    ArticleStyle.SetCanvasColor(0)
    ArticleStyle.SetTitleFillColor(0)
    ArticleStyle.SetStatColor(0)

    #Pad options
    ArticleStyle.SetPadBottomMargin(0.12) # Margins
    ArticleStyle.SetPadTopMargin(0.08)
    ArticleStyle.SetPadLeftMargin(0.125)
    ArticleStyle.SetPadRightMargin(0.145)

    #Frame options
    ArticleStyle.SetFrameLineWidth(2)

    #Palette options
    ArticleStyle.SetPalette(55,0) # avoid default color scheme

    #Title options
    ArticleStyle.SetTitleSize(0.043,"xyz")   # size of axis title font
    ArticleStyle.SetTitleSize(0.05,"")
    ArticleStyle.SetTitleFont(132,"")     # font option
    ArticleStyle.SetTitleFont(132,"xyz")    # font option
    ArticleStyle.SetTitleOffset(1.4, "y")
    ArticleStyle.SetTitleOffset(1.25, "x")

    #Label options
    ArticleStyle.SetLabelSize(0.04,"xyz")  # size of axis value font
    ArticleStyle.SetLabelFont(132,"xyz")

    # #Legend options
    ArticleStyle.SetLegendBorderSize(0)
    ArticleStyle.SetLegendFont(132)
    ArticleStyle.SetLegendFillColor(-1)

    #Other
    ArticleStyle.SetLineWidth(2) #make tick tickier
    ArticleStyle.SetFillStyle(4000)
    
    return ArticleStyle