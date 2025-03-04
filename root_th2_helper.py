import ROOT
from ROOT import TCanvas
from ROOT import TH2D

def Histo2D(df, column_x, column_y, weights=ROOT.nullptr,
            name="h", title="h",
            nbinsx=100, xmin=0.0, xmax=0.0,
            nbinsy=100, ymin=0.0, ymax=0.0,
            draw_opt="",
            set_grid=False,
            logx=False, logy=False, logz=False,
            draw=True):
    
    x = df[column_x].to_numpy()
    y = df[column_y].to_numpy()
    
    if weights != ROOT.nullptr:
        weights = df[weights].to_numpy()
    
    h = TH2D(name, title, nbinsx, xmin, xmax, nbinsy, ymin, ymax)
    h.FillN(len(x), x, y, weights)
    
    c = TCanvas(name, title, 600, 500)
    
    if draw_opt != "":
        h.Draw(draw_opt)
    else:
        h.Draw()
    
    if(set_grid):
        c.SetGrid()
    
    if(logx):
        c.SetLogx()
    if(logy):
        c.SetLogy()
    if(logz):
        c.SetLogz()
    
    if(draw):
        c.Draw()

    return h,c