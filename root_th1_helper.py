import ROOT
from ROOT import TCanvas, TH1D, TH2D

def Histo1D(df, column, weights=ROOT.nullptr,
            name="h", title="h",
            nbins=100, xmin=0, xmax=0,
            line_color=0, line_width=0,
            marker_color=0, marker_size=0,
            draw_opt="",
            fit_function="", fit_opt="QM",
            fit_line_color=2,
            set_grid=False,
            logx=False, logy=False,
            draw=True):
    

    x = df[column].to_numpy()
    

    h = TH1D(name, title, nbins, xmin, xmax)
    
    if weights != ROOT.nullptr:
        weights = df[weights].to_numpy()

    h.FillN(len(x), x, weights)
    

    if line_color != 0:
        h.SetLineColor(line_color)
    if line_width != 0:
        h.SetLineWidth(line_width)
    if marker_color != 0:
        h.SetMarkerColor(marker_color)
    if marker_size != 0:
        h.SetMarkerSize(marker_size)
    

    c = TCanvas(name, title, 600, 500)
    

    if fit_function != "":
        f = ROOT.TF1("f", fit_function)
        f.SetLineColor(fit_line_color)
        h.Fit(f, fit_opt)
        
    if(set_grid):
        c.SetGrid()
    
    if(logx):
        c.SetLogx()
    if(logy):
        c.SetLogy()
        
    if draw_opt != "":
        h.Draw(draw_opt)
    else:
        h.Draw()
        
    if(draw):
        c.Draw()
    
    if fit_function != "":
        return h,c,f
    else:
        return h,c