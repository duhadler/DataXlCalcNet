
import time
from xlcalcnet import gui, fpm, mpm, dpm, ipm
if gui.has_gpm: from xlcalcnet import gpm
if gui.has_apm: from xlcalcnet import apm
if gui.has_xlcalcnet2: from xlcalcnet import ArbPrec, mreal, sflint, dflint, \
    eflint, qflint, oflint, mflint, aflint
from xlcalcnet import math53, sreal, dreal, ereal, qreal, oreal


def main_tests():
    print('real elliptic_k(m)')
    demo_manual_real()
    demo_elliptic_k_real_ctx()
    demo_elliptic_k_real_elliptic_klicit()


def demo_manual_real():
    print('<H1 Title="demo_manual_real">')
    #from xlcalcnet import *
    m = 0.999; gui.setdps(90)
    for ctx in gui.ctxlist_noipm_real: print(ctx.fmtname + ': ' + ctx.fmt(ctx.elliptic_k(m)))
    print('</H1>')


def demo_elliptic_k_real_ctx():
    print('<H1 Title="demo_elliptic_k_real_ctx">')
    mlist = [0.1, 0.999]; gui.setdps(90)
    for m in mlist:
        print('<H2 Title="elliptic_k(m); m=' + str(m) + '">')
        for ctx in gui.ctxlist_noipm_real:
            res = ctx.elliptic_k(m)
            print(ctx.fmtname + ': ' + ctx.fmt(res))
        print('</H2>')
        print()
    print('</H1>')
    print()


def demo_elliptic_k_real_elliptic_klicit():
    print('<H1 Title="demo_elliptic_k_real_elliptic_klicit">')
    mlist = [0.1, 0.999]; gui.setdps(90)
    for m in mlist:
        print('<H2 Title="elliptic_k(m); m=' + str(m) + '">')
        res = math53.elliptic_k(m); print('math53: ' + math53.fmt(res))
        res = sreal.elliptic_k(m); print(' sreal: ' + sreal.fmt(res))
        res = dreal.elliptic_k(m); print(' dreal: ' + dreal.fmt(res))
        res = ereal.elliptic_k(m); print(' ereal: ' + ereal.fmt(res))
        res = qreal.elliptic_k(m); print(' qreal: ' + qreal.fmt(res))
        res = oreal.elliptic_k(m); print(' oreal: ' + oreal.fmt(res))
        if gui.has_xlcalcnet2:
            res = mreal.elliptic_k(m); print(' mreal: ' + mreal.fmt(res))
            res = sflint.elliptic_k(m); print('sflint: ' + sflint.fmt(res))
            res = dflint.elliptic_k(m); print('dflint: ' + dflint.fmt(res))
            res = eflint.elliptic_k(m); print('eflint: ' + eflint.fmt(res))
            res = qflint.elliptic_k(m); print('qflint: ' + qflint.fmt(res))
            res = oflint.elliptic_k(m); print('oflint: ' + oflint.fmt(res))
            res = mflint.elliptic_k(m); print('mflint: ' + mflint.fmt(res))
            res = aflint.elliptic_k(m); print('aflint: ' + aflint.fmt(res))
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




