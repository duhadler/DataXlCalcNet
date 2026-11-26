
import time
from xlcalcnet import gui, fpm, mpm, dpm
if gui.has_gpm: from xlcalcnet import gpm
if gui.has_apm: from xlcalcnet import apm
if gui.has_xlcalcnet2: from xlcalcnet import mreal
from xlcalcnet import math53, sreal, dreal, ereal, qreal, oreal

def main_tests():
    #main_manual_tests()
    #main_full_tests()
    main_plot_tests()

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


def main_plot_tests():
    print('<H1 Title="Plot Tests">')

    demo_plot_dist('pdf')
#    demo_plot_dist('cdf')
#    demo_plot_dist('sf')
#    demo_plot_dist('hf')
#    demo_plot_dist('chf')
#    demo_plot_dist('qtf')
#    demo_plot_dist('isf')
#    demo_plot_dist('m_x')
#    demo_plot_dist('k_x')

#    demo_plot_dist_cplx('c_x')

    print('</H1>')


''' Start of tests in manual'''
def demo_manual_math53_pdf():
    print('<H2 Title="demo_manual_math53_pdf()">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6
    print('math53:', math53.arcsine_pdf(a,b,x))
    print(' dreal:', dreal.dist_arcsine(a, b).pdf(x))
    print('   fpm:', fpm.dist_arcsine(a, b).pdf(x))
    print('</H2>')


def demo_manual_math53_cdf():
    print('<H2 Title="demo_manual_math53_cdf()">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6;
    print('math53:', math53.arcsine_cdf(a,b,x))
    print(' dreal:', dreal.dist_arcsine(a, b).cdf(x))
    print('   fpm:', fpm.dist_arcsine(a, b).cdf(x))
    print('</H2>')


def demo_manual_math53_qtf():
    print('<H2 Title="demo_manual_math53_qtf()">')
    #from xlcalcnet import *
    a = 0; b = 1; q = 0.9;
    print('math53:', math53.arcsine_qtf(a, b, q))
    print(' dreal:', dreal.dist_arcsine(a, b).qtf(q))
    print('   fpm:', fpm.dist_arcsine(a, b).qtf(q))
    print('</H2>')



def demo_manual_pdf():
    print('<H2 Title="demo_manual_pdf">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).pdf(x)))
    print('</H2>')


def demo_manual_cdf():
    print('<H2 Title="demo_manual_cdf">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).cdf(x)))
    print('</H2>')


def demo_manual_sf():
    print('<H2 Title="demo_manual_sf">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).sf(x)))
    print('</H2>')


def demo_manual_hf():
    print('<H2 Title="demo_manual_hf">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).hf(x)))
    print('</H2>')


def demo_manual_chf():
    print('<H2 Title="demo_manual_chf">')
    #from xlcalcnet import *
    a = 0; b = 1; x = 0.6; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).chf(x)))
    print('</H2>')


def demo_manual_qtf():
    print('<H2 Title="demo_manual_qtf">')
    #from xlcalcnet import *
    a = 0; b = 1; q = 0.9; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).qtf(q)))
    print('</H2>')


def demo_manual_isf():
    print('<H2 Title="demo_manual_isf">')
    #from xlcalcnet import *
    a = 0; b = 1; q = 0.9; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).isf(q)))
    print('</H2>')



def demo_manual_mode():
    print('<H2 Title="demo_manual_mode()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).mode()))
    print('</H2>')


def demo_manual_median():
    print('<H2 Title="demo_manual_median()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).median()))
    print('</H2>')


def demo_manual_mean():
    print('<H2 Title="demo_manual_mean()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).mean()))
    print('</H2>')


def demo_manual_variance():
    print('<H2 Title="demo_manual_variance()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).variance()))
    print('</H2>')


def demo_manual_stdev():
    print('<H2 Title="demo_manual_stdev()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).stdev()))
    print('</H2>')


def demo_manual_skewness():
    print('<H2 Title="demo_manual_skewness()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).skewness()))
    print('</H2>')


def demo_manual_kurtosis():
    print('<H2 Title="demo_manual_kurtosis()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).kurtosis()))
    print('</H2>')


def demo_manual_kurtosis_excess():
    print('<H2 Title="demo_manual_kurtosis_excess()">')
    #from xlcalcnet import *
    a = 0; b = 1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).kurtosis_excess()))
    print('</H2>')


def demo_manual_support_lower_endpoint():
    print('<H2 Title="demo_manual_support_lower_endpoint()">')
    #from xlcalcnet import *
    a = -10.1; b = 20.1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).support_lower_endpoint()))
    print('</H2>')


def demo_manual_support_upper_endpoint():
    print('<H2 Title="demo_manual_support_upper_endpoint()">')
    #from xlcalcnet import *
    a = -10.1; b = 20.1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).support_upper_endpoint()))
    print('</H2>')


def demo_manual_range_lower_endpoint():
    print('<H2 Title="demo_manual_range_lower_endpoint()">')
    #from xlcalcnet import *
    a = -10.1; b = 20.1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).range_lower_endpoint()))
    print('</H2>')


def demo_manual_range_upper_endpoint():
    print('<H2 Title="demo_manual_range_upper_endpoint()">')
    #from xlcalcnet import *
    a = -10.1; b = 20.1; gui.setdps(90)
    for ctx in gui.ctxlist_boost2_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).range_upper_endpoint()))
    print('</H2>')




def demo_manual_c_x():
    print('<H2 Title="demo_manual_c_x">')
    #from xlcalcnet import *
    a = 0; b = 1; t = 0.9; gui.setdps(40)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.cplxctx.fmt(ctx.dist_arcsine(a, b).c_x(t)))
    print('</H2>')


def demo_manual_m_x():
    print('<H2 Title="demo_manual_m_x">')
    #from xlcalcnet import *
    a = 0; b = 1; t = 0.9; gui.setdps(90)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).m_x(t)))
    print('</H2>')


def demo_manual_k_x():
    print('<H2 Title="demo_manual_k_x">')
    #from xlcalcnet import *
    a = 0; b = 1; t = 0.9; gui.setdps(90)
    for ctx in [fpm, mpm, dpm, gpm, apm]: print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).k_x(t)))
    print('</H2>')


def demo_manual_raw_moments():
    print('<H2 Title="demo_manual_raw_moments()">')
    #from xlcalcnet import *
    a = 0; b = 1; k=4; gui.setdps(90)
    for i in range(1, k+1):
        for ctx in [fpm, mpm, dpm, gpm, apm]:
            mu = ctx.dist_arcsine(a, b).moments(i)
            print(ctx.fmtname + ', mu['+ str(i) + ']:', mu[i])
        print()
    print('</H2>')


def demo_manual_cumulants():
    print('<H2 Title="demo_manual_cumulants()">')
    #from xlcalcnet import *
    a = 0; b = 1; k=4; gui.setdps(90)
    for i in range(1, k+1):
        for ctx in [fpm, mpm, dpm, gpm, apm]:
            kappa = ctx.dist_arcsine(a, b).cumulants(k)
            print(ctx.fmtname + ', kappa['+ str(i) + ']:', kappa[i])
        print()
    print('</H2>')















''' Start of full tests with parameter lists'''
def demo_full_pdf():
    print('<H2 Title="demo_full_pdf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    xlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for x in xlist:
                print('<H3 Title="dist_arcsine(a, b).pdf(x); a=' + str(a) + ', b=' + str(b) + ', x=' + str(x) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).pdf(x)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_cdf():
    print('<H2 Title="demo_full_cdf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    xlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for x in xlist:
                print('<H3 Title="dist_arcsine(a, b).cdf(x); a=' + str(a) + ', b=' + str(b) + ', x=' + str(x) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).cdf(x)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_sf():
    print('<H2 Title="demo_full_sf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    xlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for x in xlist:
                print('<H3 Title="dist_arcsine(a, b).sf(x); a=' + str(a) + ', b=' + str(b) + ', x=' + str(x) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).sf(x)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_hf():
    print('<H2 Title="demo_full_hf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    xlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for x in xlist:
                print('<H3 Title="dist_arcsine(a, b).hf(x); a=' + str(a) + ', b=' + str(b) + ', x=' + str(x) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).hf(x)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_chf():
    print('<H2 Title="demo_full_chf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    xlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for x in xlist:
                print('<H3 Title="dist_arcsine(a, b).chf(x); a=' + str(a) + ', b=' + str(b) + ', x=' + str(x) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).chf(x)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_qtf():
    print('<H2 Title="demo_full_qtf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    qlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for q in qlist:
                print('<H3 Title="dist_arcsine(a, b).qtf(x); a=' + str(a) + ', b=' + str(b) + ', q=' + str(q) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).qtf(q)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_isf():
    print('<H2 Title="demo_full_isf">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    qlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for q in qlist:
                print('<H3 Title="dist_arcsine(a, b).isf(x); a=' + str(a) + ', b=' + str(b) + ', q=' + str(q) + '">')
                for ctx in gui.ctxlist_boost2_real:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).isf(q)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_mode():
    print('<H2 Title="demo_full_mode">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).mode(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).mode()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_median():
    print('<H2 Title="demo_full_median">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).median(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).median()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_mean():
    print('<H2 Title="demo_full_mean">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).mean(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).mean()))
            print('</H3>')
            print()
    print('</H2>')

def demo_full_variance():
    print('<H2 Title="demo_full_variance">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).variance(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).variance()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_stdev():
    print('<H2 Title="demo_full_stdev">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).stdev(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).stdev()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_skewness():
    print('<H2 Title="demo_full_skewness">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).skewness(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).skewness()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_kurtosis():
    print('<H2 Title="demo_full_kurtosis">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).kurtosis(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).kurtosis()))
            print('</H3>')
            print()
    print('</H2>')


def demo_full_kurtosis_excess():
    print('<H2 Title="demo_full_kurtosis_excess">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="dist_arcsine(a, b).kurtosis_excess(); a=' + str(a) + ', b=' + str(b) + '">')
            for ctx in gui.ctxlist_boost2_real:
                print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).kurtosis_excess()))
            print('</H3>')
            print()
    print('</H2>')



def demo_full_c_x():
    print('<H2 Title="demo_full_c_x">')
    gui.setdps(40)
    alist = [0, -2.3]
    blist = [1, 3.2]
    tlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for t in tlist:
                print('<H3 Title="dist_arcsine(a, b).c_x(t); a=' + str(a) + ', b=' + str(b) + ', t=' + str(t) + '">')
                for ctx in [fpm, mpm, dpm, gpm, apm]:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).c_x(t)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_m_x():
    print('<H2 Title="demo_full_m_x">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    tlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for t in tlist:
                print('<H3 Title="dist_arcsine(a, b).m_x(t); a=' + str(a) + ', b=' + str(b) + ', t=' + str(t) + '">')
                for ctx in [fpm, mpm, dpm, gpm, apm]:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).m_x(t)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_k_x():
    print('<H2 Title="demo_full_k_x">')
    gui.setdps(90)
    alist = [0, -2.3]
    blist = [1, 3.2]
    tlist = [0.001, 0.5, 0.999]
    for a in alist:
        for b in blist:
            for t in tlist:
                print('<H3 Title="dist_arcsine(a, b).k_x(t); a=' + str(a) + ', b=' + str(b) + ', t=' + str(t) + '">')
                for ctx in [fpm, mpm, dpm, gpm, apm]:
                    print(ctx.fmtname + ': ' + ctx.fmt(ctx.dist_arcsine(a, b).k_x(t)))
                print('</H3>')
                print()
    print('</H2>')


def demo_full_raw_moments():
    print('<H2 Title="demo_full_raw_moments()">')
    gui.setdps(90)
    k = 4
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="ctx.dist_arcsine(a, b).moments(i); a=' + str(a) + '; b=' + str(b) + '; i=1,..,' + str(k) + '">')
            for i in range(1, k+1):
                for ctx in [fpm, mpm, dpm, gpm, apm]:
                    mu = ctx.dist_arcsine(a, b).moments(i)
                    print(ctx.fmtname + ', mu['+ str(i) + ']:', ctx.fmt(mu[i]))
                print()
            print('</H3>')
            print()
    print('</H2>')


def demo_full_cumulants():
    print('<H2 Title="demo_full_cumulants()">')
    gui.setdps(90)
    k = 4
    alist = [0, -2.3]
    blist = [1, 3.2]
    for a in alist:
        for b in blist:
            print('<H3 Title="ctx.dist_arcsine(a, b).cumulants(i); a=' + str(a) + '; b=' + str(b) + '; i=1,..,' + str(k) + '">')
            for i in range(1, k+1):
                for ctx in [fpm, mpm, dpm, gpm, apm]:
                    kappa = ctx.dist_arcsine(a, b).cumulants(i)
                    print(ctx.fmtname + ', mu['+ str(i) + ']:', ctx.fmt(kappa[i]))
                print()
            print('</H3>')
            print()
    print('</H2>')


''' Start plot tests'''
def demo_plot_dist(target):
    from A01_ExamplesPython.B18_FunctionsAndCurvesPlots.C01_Intro_Parametric2D \
        import D07_DistPlotContinuous;
    DistPlot = D07_DistPlotContinuous.DistPlotContinuous

    Title = 'Arcsine distribution'
    a = [-1.5, 0.0, 1.5]
    b = [5.1, 6.1, 8.8]
    xlim = [-2.0, 8.8]
    ylim = None
    if target=='hf': ylim=[0, 6]
    mlim = [0, 1]
    klim = [-1, 1]

    dlist = []
    ltext = []
    for j in range(len(a)):
#        dlist.append(dreal.dist_arcsine(a[j], b[j]))
        dlist.append(fpm.dist_arcsine(a[j], b[j]))
        ltext.append('a=' + str(a[j]) + ', b=' + str(b[j]))
    DistPlot(Title = Title, dlist=dlist, xlim = xlim,  ylim = ylim, mlim = mlim,
        klim = klim, target = target, ltext = ltext)


def demo_plot_dist_cplx(target):
    from A01_ExamplesPython.B18_FunctionsAndCurvesPlots.C01_Intro_Parametric2D \
        import D09_FuncPlot2d;
    DistPlot = D09_FuncPlot2d.FuncPlot2d

    Title = 'Arcsine distribution'
    a = [-1.5, 0.0, 1.5]
    b = [5.1, 6.1, 8.8]
    xlim = [-2.0, 8.8]
    ylim = None
    if target=='hf': ylim=[0, 6]

    dlist = []
    ltext = []
    for j in range(len(a)):
#        dlist.append(dreal.dist_arcsine(a[j], b[j]))
        dlist.append(mpm.dist_arcsine(a[j], b[j]))
        ltext.append('a=' + str(a[j]) + ', b=' + str(b[j]))
    DistPlot(Title = Title, dlist=dlist, xlim = xlim,  ylim = ylim,
        target = target, ltext = ltext)




try:
    if __name__ == '__main__':
        start0 = time.time()
        main_tests()
        end0 = time.time()
        print('Elapsed time:', format(end0 - start0, '.4g'), 'seconds' )

except Exception:
    import traceback
    print(traceback.format_exc())











