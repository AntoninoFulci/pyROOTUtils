import ROOT

class set_style():
    def __init__(self, style=ROOT.TStyle("Modern", "Modern Style")):
        self.style = style

    def __enter__(self):
        # Save the current style name
        self.old_style = ROOT.gStyle.GetName()
        
        # Set the new style
        global myStyle
        myStyle = self.style
        ROOT.SetOwnership(myStyle, False)
        ROOT.gROOT.SetStyle(myStyle.GetName())
        del myStyle

    def __exit__(self, type, value, traceback):
        # Restore the old style
        ROOT.gROOT.SetStyle(self.old_style)

