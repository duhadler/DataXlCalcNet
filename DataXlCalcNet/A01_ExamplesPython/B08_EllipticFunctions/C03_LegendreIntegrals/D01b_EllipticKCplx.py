
import time
from xlcalcnet import gui, fpm, mpm, dpm, ipm
if gui.has_gpm: from xlcalcnet import gpm
if gui.has_apm: from xlcalcnet import apm
if gui.has_xlcalcnet2: from xlcalcnet import ArbPrec, mcplx, sflintc, dflintc, \
    eflintc, qflintc, oflintc, mflintc, aflintc
from xlcalcnet import cmath53, scplx, dcplx, ecplx, qcplx, ocplx


def main_tests():
    print('cplx elliptic_k(x)')
    demo_manual_cplx_short()
    demo_manual_cplx_real_part()
    demo_manual_cplx_imag_part()
    demo_elliptic_k_cplx_ctx()
    demo_elliptic_k_cplx_re_im_ctx()
    demo_elliptic_k_cplx_elliptic_klicit()


def demo_manual_cplx_short():
    print('<H1 Title="demo_manual_cplx_short">')
    #from xlcalcnet import *
    x = -5.1+2j; gui.setdps(40)
    for ctx in [fpm, mpm, cmath53]: print(ctx.fmtname + ': ' + ctx.fmt(ctx.elliptic_k(x)))
    print('</H1>')


def demo_manual_cplx_real_part():
    print('<H1 Title="demo_manual_cplx_real_part">')
    #from xlcalcnet import *
    x = -5.1+2j; gui.setdps(90)
    for ctx in gui.ctxlist_noboost_cplx: print(ctx.fmtname + ': ' +  ctx.realctx.fmt(ctx.real(ctx.elliptic_k(x))))
    print('</H1>')


def demo_manual_cplx_imag_part():
    print('<H1 Title="demo_manual_cplx_imag_part">')
    #from xlcalcnet import *
    x = -5.1+2j; gui.setdps(90)
    for ctx in gui.ctxlist_noboost_cplx: print(ctx.fmtname + ': ' +  ctx.realctx.fmt(ctx.imag(ctx.elliptic_k(x))))
    print('</H1>')




def demo_elliptic_k_cplx_ctx():
    print('<H1 Title="elliptic_k_cplx_ctx">')
    xlist = [-5.1+2j, 8.8+2j]; gui.setdps(50)
    for x in xlist:
        print('<H2 Title="elliptic_k(x); x=' + str(x) + '">')
        for ctx in gui.ctxlist_noboost_cplx:
            res = ctx.elliptic_k(x)
            print(ctx.fmtname + ': ' + ctx.fmt(res))
        print('</H2>')
        print()
    print('</H1>')
    print()


def demo_elliptic_k_cplx_re_im_ctx():
    print('<H1 Title="elliptic_k_cplx_re_im_ctx">')
    xlist = [-5.1+2j, 8.8+2j]; gui.setdps(90)
    for x in xlist:
        print('<H2 Title="Re(elliptic_k(x)); x=' + str(x) + '">')
        for ctx in gui.ctxlist_noboost_cplx:
            res = ctx.elliptic_k(x)
            print(ctx.fmtname + ': ' +  ctx.realctx.fmt(ctx.real(res)))
        print('</H2>')
        print()
        print('<H2 Title="Im(elliptic_k(x)); x=' + str(x) + '">')
        for ctx in gui.ctxlist_noboost_cplx:
            res = ctx.elliptic_k(x)
            print(ctx.fmtname + ': ' +  ctx.realctx.fmt(ctx.imag(res)))
        print('</H2>')
        print()
    print('</H1>')
    print()


def demo_elliptic_k_cplx_elliptic_klicit():
    print('<H1 Title="demo_elliptic_k_cplx_elliptic_klicit">')
    xlist = [-5.1+2j, 8.8+2j]; gui.setdps(90)
    for x in xlist:
        print('<H2 Title="elliptic_k(x); x=' + str(x) + '">')
        res = cmath53.elliptic_k(x); print('cmath53: ' + cmath53.fmt(res))
        if gui.has_xlcalcnet2:
            res = sflintc.elliptic_k(x); print('sflintc: ' + sflintc.fmt(res))
            res = dflintc.elliptic_k(x); print('dflintc: ' + dflintc.fmt(res))
            res = eflintc.elliptic_k(x); print('eflintc: ' + eflintc.fmt(res))
            res = qflintc.elliptic_k(x); print('qflintc: ' + qflintc.fmt(res))
            res = oflintc.elliptic_k(x); print('oflintc: ' + oflintc.fmt(res))
            res = mflintc.elliptic_k(x); print('mflintc: ' + mflintc.fmt(res))
            res = aflintc.elliptic_k(x); print('aflintc: ' + aflintc.fmt(res))
        print('</H2>')
        print()
    print('</H1>')
    print()




try:
    if __name__ == '__main__':
        start0 = time.time()
        main_tests()
        end0 = time.time()
        print('Elapsed time:', format(end0 - start0, '.4g'), 'seconds' )


except Exception:
    import traceback
    print(traceback.format_exc())


