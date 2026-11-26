
import time
from xlcalcnet import gui, fpm, mpm, dpm
if gui.has_gpm: from xlcalcnet import gpm
if gui.has_apm: from xlcalcnet import apm
if gui.has_xlcalcnet2: from xlcalcnet import mreal
from xlcalcnet import math53, sreal, dreal, ereal, qreal, oreal

def main_tests():
    #main_manual_tests()
    main_manual_plots()
    #main_full_tests()

def main_manual_tests():
    print('<H1 Title="Manual Tests">')

    demo_manual_math53_pdf()
    demo_manual_math53_cdf()
    demo_manual_math53_qtf()

    demo_manual_pdf()
    demo_manual_cdf()
    demo_manual_sf()
    demo_manual_hf()
    demo_manual_chf()
    demo_manual_qtf()
    demo_manual_isf()

    demo_manual_mode()
    demo_manual_median()
    demo_manual_mean()

    demo_manual_variance()
    demo_manual_stdev()
    demo_manual_skewness()
    demo_manual_kurtosis()
    demo_manual_kurtosis_excess()

    demo_manual_support_lower_endpoint()
    demo_manual_support_upper_endpoint()
    demo_manual_range_lower_endpoint()
    demo_manual_range_upper_endpoint()

    demo_manual_c_x()
    demo_manual_m_x()
    demo_manual_k_x()

    demo_manual_raw_moments()
    demo_manual_cumulants()

    print('</H1>')


def main_manual_plots():
    print('<H1 Title="Plot Tests">')
    demo_manual_plot_pdf()
    demo_manual_plot_cdf()
    demo_manual_plot_sf()
    demo_manual_plot_hf()
    demo_manual_plot_chf()
    #demo_manual_plot_spf()
    demo_manual_plot_qtf()
    demo_manual_plot_isf()

    demo_manual_plot_c_x()
    demo_manual_plot_m_x()
    demo_manual_plot_k_x()
    print('</H1>')


def main_full_tests():
    print('<H1 Title="Full Tests">')

    demo_full_pdf()
    demo_full_cdf()
    demo_full_sf()
    demo_full_hf()
    demo_full_chf()
    demo_full_qtf()
    demo_full_isf()

    demo_full_mode()
    demo_full_median()
    demo_full_mean()
    demo_full_variance()
    demo_full_stdev()
    demo_full_skewness()
    demo_full_kurtosis()
    demo_full_kurtosis_excess()

    demo_full_c_x()
    demo_full_m_x()
    demo_full_k_x()

    demo_full_raw_moments()
    demo_full_cumulants()

    print('</H1>')


''' Start of demos in manual '''
def demo_manual_math53_pdf():
    print('<H2 Title="demo_manual_math53_pdf()">')
    #from xlcalcnet import *
    nu = 10; x = 8.6
    print('math53:', math53.chi2_pdf(nu, x))
    print(' dreal:', dreal.dist_chi2(nu).pdf(x))
    print('   fpm:', fpm.dist_chi2(nu).pdf(x))
    print('</H2>')


def demo_manual_math53_cdf():
    print('<H2 Title="demo_manual_math53_cdf()">')
    #from xlcalcnet import *
    nu = 10; x = 8.6
    print('math53:', math53.chi2_cdf(nu, x))
    print(' dreal:', dreal.dist_chi2(nu).cdf(x))
    print('   fpm:', fpm.dist_chi2(nu).cdf(x))
    print('</H2>')


def demo_manual_math53_qtf():
    print('<H2 Title="demo_manual_math53_qtf()">')
    #from xlcalcnet import *
    nu = 10; q = 0.9;
    print('math53:', math53.chi2_qtf(nu, q))
    print(' dreal:', dreal.dist_chi2(nu).qtf(q))
    print('   fpm:', fpm.dist_chi2(nu).qtf(q))
    print('</H2>')



def demo_manual_pdf():
    print('<H2 Title="demo_manual_pdf">')
    #from xlcalcnet import *
    nu = 10; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).pdf(x)))
    print('</H2>')


def demo_manual_cdf():
    print('<H2 Title="demo_manual_cdf">')
    #from xlcalcnet import *
    nu = 10; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).cdf(x)))
    print('</H2>')


def demo_manual_sf():
    print('<H2 Title="demo_manual_sf">')
    #from xlcalcnet import *
    nu = 10; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).sf(x)))
    print('</H2>')


def demo_manual_hf():
    print('<H2 Title="demo_manual_hf">')
    #from xlcalcnet import *
    nu = 10; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).hf(x)))
    print('</H2>')


def demo_manual_chf():
    print('<H2 Title="demo_manual_chf">')
    #from xlcalcnet import *
    nu = 10; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).chf(x)))
    print('</H2>')




def demo_manual_qtf():
    print('<H2 Title="demo_manual_qtf">')
    #from xlcalcnet import *
    nu = 10; q = 0.9; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).qtf(q)))
    print('</H2>')


def demo_manual_isf():
    print('<H2 Title="demo_manual_isf">')
    #from xlcalcnet import *
    nu = 10; q = 0.9; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).isf(q)))
    print('</H2>')



def demo_manual_mode():
    print('<H2 Title="demo_manual_mode()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).mode()))
    print('</H2>')


def demo_manual_median():
    print('<H2 Title="demo_manual_median()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).median()))
    print('</H2>')


def demo_manual_mean():
    print('<H2 Title="demo_manual_mean()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).mean()))
    print('</H2>')


def demo_manual_variance():
    print('<H2 Title="demo_manual_variance()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).variance()))
    print('</H2>')


def demo_manual_stdev():
    print('<H2 Title="demo_manual_stdev()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).stdev()))
    print('</H2>')


def demo_manual_skewness():
    print('<H2 Title="demo_manual_skewness()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).skewness()))
    print('</H2>')


def demo_manual_kurtosis():
    print('<H2 Title="demo_manual_kurtosis()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).kurtosis()))
    print('</H2>')


def demo_manual_kurtosis_excess():
    print('<H2 Title="demo_manual_kurtosis_excess()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).kurtosis_excess()))
    print('</H2>')


def demo_manual_support_lower_endpoint():
    print('<H2 Title="demo_manual_support_lower_endpoint()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).support_lower_endpoint()))
    print('</H2>')


def demo_manual_support_upper_endpoint():
    print('<H2 Title="demo_manual_support_upper_endpoint()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).support_upper_endpoint()))
    print('</H2>')


def demo_manual_range_lower_endpoint():
    print('<H2 Title="demo_manual_range_lower_endpoint()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).range_lower_endpoint()))
    print('</H2>')


def demo_manual_range_upper_endpoint():
    print('<H2 Title="demo_manual_range_upper_endpoint()">')
    #from xlcalcnet import *
    nu = 10; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).range_upper_endpoint()))
    print('</H2>')




def demo_manual_c_x():
    print('<H2 Title="demo_manual_c_x">')
    #from xlcalcnet import *
    nu = 10; t = 0.9; gui.setdps(40)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.cplxctx.fmt(ctx.dist_chi2(nu).c_x(t)))
    print('</H2>')


def demo_manual_m_x():
    print('<H2 Title="demo_manual_m_x">')
    #from xlcalcnet import *
    nu = 10; t = 0.9; gui.setdps(90)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).m_x(t)))
    print('</H2>')


def demo_manual_k_x():
    print('<H2 Title="demo_manual_k_x">')
    #from xlcalcnet import *
    nu = 10; t = 0.9; gui.setdps(90)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).k_x(t)))
    print('</H2>')


def demo_manual_raw_moments():
    print('<H2 Title="demo_manual_raw_moments()">')
    #from xlcalcnet import *
    nu = 10; k=4; gui.setdps(90)
    for i in range(1, k+1):
        for ctx in [fpm, mpm, dpm, gpm, apm]:
            mu = ctx.dist_chi2(nu).moments(i)
            print(ctx.fmtname + ', mu['+ str(i) + ']:', mu[i])
        print()
    print('</H2>')


def demo_manual_cumulants():
    print('<H2 Title="demo_manual_cumulants()">')
    #from xlcalcnet import *
    nu = 10; k=4; gui.setdps(90)
    for i in range(1, k+1):
        for ctx in [fpm, mpm, dpm, gpm, apm]:
            kappa = ctx.dist_chi2(nu).cumulants(k)
            print(ctx.fmtname + ', kappa['+ str(i) + ']:', kappa[i])
        print()
    print('</H2>')







''' Start of distribution plots shown in manual '''
def demo_manual_plot_pdf():
    print('<H2 Title="demo_manual_plot_pdf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'pdf', nu = [3, 5, 7], xlim = [0.0, 10])
    print('</H2>')


def demo_manual_plot_cdf():
    print('<H2 Title="demo_manual_plot_cdf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'cdf', nu = [3, 5, 7], xlim = [0.0, 10])
    print('</H2>')


def demo_manual_plot_sf():
    print('<H2 Title="demo_manual_plot_sf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'sf', nu = [3, 5, 7], xlim = [0.0, 10])
    print('</H2>')



def demo_manual_plot_hf():
    print('<H2 Title="demo_manual_plot_hf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'hf', nu = [3, 5, 7], xlim = [0.0, 10])
    print('</H2>')


def demo_manual_plot_chf():
    print('<H2 Title="demo_manual_plot_chf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'chf', nu = [3, 5, 7], xlim = [0.0, 10])
    print('</H2>')


def demo_manual_plot_spf():
    print('<H2 Title="demo_manual_plot_spf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'spf', nu = [3, 5, 7], xlim = [0.0, 1])
    print('</H2>')


def demo_manual_plot_qtf():
    print('<H2 Title="demo_manual_plot_qtf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'qtf', nu = [3, 5, 7], xlim = [0.0, 1])
    print('</H2>')


def demo_manual_plot_isf():
    print('<H2 Title="demo_manual_plot_isf()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = dreal, target = 'isf', nu = [3, 5, 7], xlim = [0.0, 1])
    print('</H2>')


def demo_manual_plot_c_x():
    print('<H2 Title="demo_manual_plot_c_x()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = fpm, target = 'c_x', nu = [120], tlim = [-0.25, 0.25])
    print('</H2>')


def demo_manual_plot_m_x():
    print('<H2 Title="demo_manual_plot_m_x()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = fpm, target = 'm_x', nu = [3, 5, 7], tlim = [-2, 0.1])
    print('</H2>')


def demo_manual_plot_k_x():
    print('<H2 Title="demo_manual_plot_k_x()">')
    #from xlcalcnet import *
    gui_chi2_plot(ctx = fpm, target = 'k_x', nu = [3, 5, 7], klim = [-2, 0.1])
    print('</H2>')




def gui_chi2_plot(**kwargs):
    ctx = kwargs['ctx'] if 'ctx' in kwargs else fpm
    target = kwargs['target'] if 'target' in kwargs else 'pdf'
    Title = kwargs['Title'] if 'Title' in kwargs else 'Chi-squared distribution'
    xlim = kwargs['xlim'] if 'xlim' in kwargs else [-5, 5]
    tlim = kwargs['tlim'] if 'tlim' in kwargs else [-10, 0.5]
    ylim = kwargs['ylim'] if 'ylim' in kwargs else None
    nu = kwargs['nu'] if 'nu' in kwargs else [3, 7, 5]
    funcname = 'dist_chi2'
    FileName = ctx.name + '_' + funcname + '_' + target
    OutputMode = kwargs['OutputMode'] if 'OutputMode' in kwargs else 'svg'


    if (target != 'c_x'):
        from A01_ExamplesPython.B18_FunctionsAndCurvesPlots.C01_Intro_Parametric2D \
            import D07_DistPlotContinuous;
        DistPlot = D07_DistPlotContinuous.DistPlotContinuous
        dlist = []
        ltext = []
        for j in range(len(nu)):
            dlist.append(ctx.dist_chi2(nu[j]))
            ltext.append('nu=' + str(nu[j]) )
        DistPlot(Title=Title, dlist=dlist, xlim=xlim,  ylim=ylim, tlim=tlim,
            target=target, ltext=ltext, FileName=FileName, OutputMode=OutputMode)
    else:
        from A01_ExamplesPython.B18_FunctionsAndCurvesPlots.C01_Intro_Parametric2D \
            import D09_FuncPlot2d;
        DistPlot = D09_FuncPlot2d.FuncPlot2d
        Title += ', characteristic function \n ' + ctx.name + '.' + funcname + '(nu = ' + str(nu[0]) + ')'
        DistPlot(ctx = ctx, f = ctx.dist_chi2(nu[0]).c_x , Title = Title, xlim = tlim,  ylim = ylim,
            target = target, ShiftZero=0.0001, IsCharfunc=True, FileName=FileName, OutputMode=OutputMode)


''' Start of full demos with parameter lists '''
def demo_full_pdf():
    print('<H2 Title="demo_full_pdf">')
    gui.setdps(90)
    nulist = [3, 33]
    xlist = [2.0, 10.0, 20.0]
    for nu in nulist:
        for x in xlist:
            print('<H3 Title="dist_chi2(nu).pdf(x); nu=' + str(nu) + ', x=' + str(x) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).pdf(x)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_cdf():
    print('<H2 Title="demo_full_cdf">')
    gui.setdps(90)
    nulist = [3, 33]
    xlist = [2.0, 10.0, 20.0]
    for nu in nulist:
        for x in xlist:
            print('<H3 Title="dist_chi2(nu).cdf(x); nu=' + str(nu) + ', x=' + str(x) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).cdf(x)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_sf():
    print('<H2 Title="demo_full_sf">')
    gui.setdps(90)
    nulist = [3, 33]
    xlist = [2.0, 10.0, 20.0]
    for nu in nulist:
        for x in xlist:
            print('<H3 Title="dist_chi2(nu).sf(x); nu=' + str(nu) + ', x=' + str(x) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).sf(x)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_hf():
    print('<H2 Title="demo_full_hf">')
    gui.setdps(90)
    nulist = [3, 33]
    xlist = [2.0, 10.0, 20.0]
    for nu in nulist:
        for x in xlist:
            print('<H3 Title="dist_chi2(nu).hf(x); nu=' + str(nu) + ', x=' + str(x) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).hf(x)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_chf():
    print('<H2 Title="demo_full_chf">')
    gui.setdps(90)
    nulist = [3, 33]
    xlist = [2.0, 10.0, 20.0]
    for nu in nulist:
        for x in xlist:
            print('<H3 Title="dist_chi2(nu).chf(x); nu=' + str(nu) + ', x=' + str(x) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).chf(x)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_qtf():
    print('<H2 Title="demo_full_qtf">')
    gui.setdps(90)
    nulist = [3, 33]
    qlist = [0.001, 0.5, 0.999]
    for nu in nulist:
        for q in qlist:
            print('<H3 Title="dist_chi2(nu).qtf(x); nu=' + str(nu) + ', q=' + str(q) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).qtf(q)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_isf():
    print('<H2 Title="demo_full_isf">')
    gui.setdps(90)
    nulist = [3, 33]
    qlist = [0.001, 0.5, 0.999]
    for nu in nulist:
        for q in qlist:
            print('<H3 Title="dist_chi2(nu).isf(x); nu=' + str(nu) + ', q=' + str(q) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).isf(q)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_mode():
    print('<H2 Title="demo_full_mode">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).mode(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).mode()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_median():
    print('<H2 Title="demo_full_median">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).median(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).median()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_mean():
    print('<H2 Title="demo_full_mean">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).mean(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).mean()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_variance():
    print('<H2 Title="demo_full_variance">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).variance(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).variance()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_stdev():
    print('<H2 Title="demo_full_stdev">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).stdev(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).stdev()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_skewness():
    print('<H2 Title="demo_full_skewness">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).skewness(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).skewness()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_kurtosis():
    print('<H2 Title="demo_full_kurtosis">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).kurtosis(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).kurtosis()))
        print('</H3>')
        print()
    print('</H2>')


def demo_full_kurtosis_excess():
    print('<H2 Title="demo_full_kurtosis_excess">')
    gui.setdps(90)
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="dist_chi2(nu).kurtosis_excess(); nu=' + str(nu) +  '">')
        for ctx in gui.ctxlist_boost2_real:
            print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).kurtosis_excess()))
        print('</H3>')
        print()
    print('</H2>')



def demo_full_c_x():
    print('<H2 Title="demo_full_c_x">')
    gui.setdps(40)
    nulist = [3, 33]
    tlist = [0.001, 0.5, 0.999]
    for nu in nulist:
        for t in tlist:
            print('<H3 Title="dist_chi2(nu).c_x(t); nu=' + str(nu) + ', t=' + str(t) + '">')
            for ctx in [fpm, mpm, dpm, gpm, apm]:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).c_x(t)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_m_x():
    print('<H2 Title="demo_full_m_x">')
    gui.setdps(90)
    nulist = [3, 33]
    tlist = [-10, -2.5, 0.1]
    for nu in nulist:
        for t in tlist:
            print('<H3 Title="dist_chi2(nu).m_x(t); nu=' + str(nu) + ', t=' + str(t) + '">')
            for ctx in [fpm, mpm, dpm, gpm, apm]:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).m_x(t)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_k_x():
    print('<H2 Title="demo_full_k_x">')
    gui.setdps(90)
    nulist = [3, 33]
    tlist = [-10, -2.5, 0.1]
    for nu in nulist:
        for t in tlist:
            print('<H3 Title="dist_chi2(nu).k_x(t); nu=' + str(nu) + ', t=' + str(t) + '">')
            for ctx in [fpm, mpm, dpm, gpm, apm]:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_chi2(nu).k_x(t)))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_raw_moments():
    print('<H2 Title="demo_full_raw_moments()">')
    gui.setdps(90)
    k = 4
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="ctx.dist_chi2(nu).moments(i); nu=' + str(nu) +  '; i=1,..,' + str(k) + '">')
        for i in range(1, k+1):
            for ctx in [fpm, mpm, dpm, gpm, apm]:
                mu = ctx.dist_chi2(nu).moments(i)
                print(ctx.fmtname + ', mu['+ str(i) + ']:', ctx.fmt(mu[i]))
            print()
        print('</H3>')
        print()
    print('</H2>')


def demo_full_cumulants():
    print('<H2 Title="demo_full_cumulants()">')
    gui.setdps(90)
    k = 4
    nulist = [3, 33]
    for nu in nulist:
        print('<H3 Title="ctx.dist_chi2(nu).cumulants(i); nu=' + str(nu) +  '; i=1,..,' + str(k) + '">')
        for i in range(1, k+1):
            for ctx in [fpm, mpm, dpm, gpm, apm]:
                kappa = ctx.dist_chi2(nu).cumulants(i)
                print(ctx.fmtname + ', mu['+ str(i) + ']:', ctx.fmt(kappa[i]))
            print()
        print('</H3>')
        print()
    print('</H2>')





try:
    if __name__ == '__main__':
        start0 = time.time()
        main_tests()
        end0 = time.time()
        print('Elapsed time:', format(end0 - start0, '.4g'), 'seconds' )

except Exception:
    import traceback
    print(traceback.format_exc())











