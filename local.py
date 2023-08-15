#!/usr/bin/python3
import os

# NOTE!!!! Change paths to absolute ones before runnind this!

# This is a list of sources from which to pull STACK-Maxima content
SRCS = ['php81.local:/opt/moodle/4.2/question/type/stack/stack/maxima/',
        'localhost:/Users/aharjula/dev/moodle-qtype_stack/stack/maxima/']

# This is a directory where we hold copies of those.
TMP = './.stack-maxima-temps'

# This is the target config directory i.e. the ansible files source dir.
TRG = './mpfiles/opt/maximapool-configs'

# This describes the Maxima versions and maxima-local contents applied for
# versions that are larger than or equal to the key of this dictionary.
CONFIGS = {'2022071400': {
 'maxima': '5.44.0',
 'stackmaxima.mac': """
file_search_maxima:append( [sconcat("/opt/maximapool-configs/%{version}s/maxima/###.{mac,mc}")] , file_search_maxima)$
file_search_lisp:append( [sconcat("/opt/maximapool-configs/%{version}s/maxima/###.{lisp}")] , file_search_lisp)$

STACK_SETUP(ex):=block(
    MAXIMA_VERSION_NUM_EXPECTED:44,
    MAXIMA_PLATFORM:"server",
    maxima_tempdir:"/tmp/",
    IMAGE_DIR:"/tmp/",
    PLOT_SIZE:[450,300],
    PLOT_TERMINAL:"svg",
    PLOT_TERM_OPT:"dynamic font \\",11\\" linewidth 1.2",
    DEL_CMD:"rm",
    GNUPLOT_CMD:"gnuplot",
    MAXIMA_VERSION_EXPECTED:"5.44.0",
    URL_BASE:"!ploturl!",
    /* Define units available in STACK. */
    stack_unit_si_prefix_code:[y, z, a, f, p, n, u, m, c, d, da, h, k, M, G, T, P, E, Z, Y],
    stack_unit_si_prefix_multiplier:[10^-24, 10^-21, 10^-18, 10^-15, 10^-12, 10^-9, 10^-6, 10^-3, 10^-2, 10^-1, 10, 10^2, 10^3, 10^6, 10^9, 10^12, 10^15, 10^18, 10^21, 10^24],
    stack_unit_si_prefix_tex:["\\\\mathrm{y}", "\\\\mathrm{z}", "\\\\mathrm{a}", "\\\\mathrm{f}", "\\\\mathrm{p}", "\\\\mathrm{n}", "\\\\mu ", "\\\\mathrm{m}", "\\\\mathrm{c}", "\\\\mathrm{d}", "\\\\mathrm{da}", "\\\\mathrm{h}", "\\\\mathrm{k}", "\\\\mathrm{M}", "\\\\mathrm{G}", "\\\\mathrm{T}", "\\\\mathrm{P}", "\\\\mathrm{E}", "\\\\mathrm{Z}", "\\\\mathrm{Y}"],
    stack_unit_si_unit_code:[m, l, L, g, t, s, h, Hz, Bq, cd, N, Pa, cal, Cal, Btu, eV, J, W, Wh, A, ohm, C, V, F, S, Wb, T, H, Gy, rem, Sv, lx, lm, mol, M, kat, rad, sr, K, VA, eV, Ci],
    stack_unit_si_unit_conversions:[m, m^3/1000, m^3/1000, kg/1000, 1000*kg, s, s*3600, 1/s, 1/s, cd, (kg*m)/s^2, kg/(m*s^2), 4.2*J, 4200*J, 1055*J, 1.602177e-19*J, (kg*m^2)/s^2, (kg*m^2)/s^3, 3600*(kg*m^2)/s^2, A, (kg*m^2)/(s^3*A^2), s*A, (kg*m^2)/(s^3*A), (s^4*A^2)/(kg*m^2), (s^3*A^2)/(kg*m^2), (kg*m^2)/(s^2*A), kg/(s^2*A), (kg*m^2)/(s^2*A^2), m^2/s^2, 0.01*Sv, m^2/s^2, cd/m^2, cd, mol, mol/(m^3/1000), mol/s, rad, sr, K, VA, 1.602176634E-19*J, Ci],
    stack_unit_si_unit_tex:["\\\\mathrm{m}", "\\\\mathrm{l}", "\\\\mathrm{L}", "\\\\mathrm{g}", "\\\\mathrm{t}", "\\\\mathrm{s}", "\\\\mathrm{h}", "\\\\mathrm{Hz}", "\\\\mathrm{Bq}", "\\\\mathrm{cd}", "\\\\mathrm{N}", "\\\\mathrm{Pa}", "\\\\mathrm{cal}", "\\\\mathrm{cal}", "\\\\mathrm{Btu}", "\\\\mathrm{eV}", "\\\\mathrm{J}", "\\\\mathrm{W}", "\\\\mathrm{Wh}", "\\\\mathrm{A}", "\\\\Omega", "\\\\mathrm{C}", "\\\\mathrm{V}", "\\\\mathrm{F}", "\\\\mathrm{S}", "\\\\mathrm{Wb}", "\\\\mathrm{T}", "\\\\mathrm{H}", "\\\\mathrm{Gy}", "\\\\mathrm{rem}", "\\\\mathrm{Sv}", "\\\\mathrm{lx}", "\\\\mathrm{lm}", "\\\\mathrm{mol}", "\\\\mathrm{M}", "\\\\mathrm{kat}", "\\\\mathrm{rad}", "\\\\mathrm{sr}", "\\\\mathrm{K}", "\\\\mathrm{VA}", "\\\\mathrm{eV}", "\\\\mathrm{Ci}"],
    stack_unit_other_unit_code:[min, amu, u, mmHg, bar, ha, cc, gal, mbar, atm, torr, rev, deg, rpm, au, Da, Np, B, dB, day, year, hp, in, ft, yd, mi, lb],
    stack_unit_other_unit_conversions:[s*60, amu, amu, 133.322387415*Pa, 10^5*Pa, 10^4*m^2, m^3*10^(-6), 3.785*l, 10^2*Pa, 101325*Pa, 101325/760*Pa, 2*pi*rad, pi*rad/180, pi*rad/(30*s), 149597870700*m, 1.660539040E-27*kg, Np, B, dB, 86400*s, 3.156e7*s, 746*W, in, 12*in, 36*in, 5280*12*in, 4.4482*N],
    stack_unit_other_unit_tex:["\\\\mathrm{min}", "\\\\mathrm{amu}", "\\\\mathrm{u}", "\\\\mathrm{mmHg}", "\\\\mathrm{bar}", "\\\\mathrm{ha}", "\\\\mathrm{cc}", "\\\\mathrm{gal}", "\\\\mathrm{mbar}", "\\\\mathrm{atm}", "\\\\mathrm{torr}", "\\\\mathrm{rev}", "\\\\mathrm{{}^{o}}", "\\\\mathrm{rpm}", "\\\\mathrm{au}", "\\\\mathrm{Da}", "\\\\mathrm{Np}", "\\\\mathrm{B}", "\\\\mathrm{dB}", "\\\\mathrm{day}", "\\\\mathrm{year}", "\\\\mathrm{hp}", "\\\\mathrm{in}", "\\\\mathrm{ft}", "\\\\mathrm{yd}", "\\\\mathrm{mi}", "\\\\mathrm{lb}"],
    true)$
/* Load the main libraries. */
load("stackmaxima.mac")$
load("stats")$
load("distrib")$
load("descriptive")$
load("simplex")$
print(sconcat("[ STACK-Maxima started, library version ", stackmaximaversion, " ]"))$

:lisp (sb-ext:save-lisp-and-die "maxima-optimised" :toplevel #'run :executable t)
"""
}}



# Copy the data over to our temp.
i = 0 
versionsToActivate = []
for src in SRCS:
    i = i + 1
    os.system("mkdir -p %s/%i" % (TMP, i))
    os.system("rsync -rt %s %s/%i" % (src, TMP, i))
    # Figure out the version that data represents
    vers = None
    with open('%s/%i/stackmaxima.mac' % (TMP, i), 'r') as f:
        content = f.read()
        vers = content.split('stackmaximaversion:')[1].split('$')[0]
    if vers not in versionsToActivate:
        versionsToActivate.append(vers)
    else:
        print("Skipping duplicate config: %s => %s" % (src, vers))
        continue
    # Now that we know the version lets create it at the target side.
    os.system("mkdir -p %s/%s/maxima" % (TRG, vers))
    # Copy over only if changed.
    os.system("rsync -rt %s/%i/ %s/%s/maxima/" % (TMP, i, TRG, vers))

    # Match version for config.
    bestmatch = "1111111111"
    for key in CONFIGS:
        if key <= vers and bestmatch < key:
            bestmatch = key
    print ("Config style %s => %s" % (vers, bestmatch))

    # Write out the extra details.
    with open("%s/%s/process.conf" % (TRG, vers), "r+") as f:
        content = """
name = %{version}s
auto.start = true
working.directory = /tmp
command.line = /opt/maximapool-configs/%{version}s/maxima-optimised
process.ready = Maxima restarted.
file.handling = true
path.command =  maxima_tempdir: "%WORK-DIR%/"$ IMAGE_DIR: "%OUTPUT-DIR%/"$ URL_BASE: "%PLOT-URL-BASE%"$
startup.timeout = 10000
execution.timeout = 30000
maximum.lifetime = 600000
startup.time.estimate = 2000
demand.estimate = 0.1
        """
        # Can't mix things up too much
        content = content.replace("%{version}s", vers)
        existing = f.read()
        if content == existing:
            pass
        else:
            f.seek(0)
            f.write(content)
            f.truncate()

    with open("%s/%s/gen.mac" % (TRG, vers), "r+") as f:
        content = CONFIGS[bestmatch]['stackmaxima.mac'].replace("%{version}s", vers)
        existing = f.read()
        if content == existing:
            pass
        else:
            f.seek(0)
            f.write(content)
            f.truncate()

    with open("%s/%s/gen.sh" % (TRG, vers), "r+") as f:
        content = """#!/bin/sh
/opt/maxima-bin/%{maxima-version}s/bin/maxima -b gen.mac
        """
        content = content.replace("%{maxima-version}s", CONFIGS[bestmatch]['maxima'])
        existing = f.read()
        if content == existing:
            pass
        else:
            f.seek(0)
            f.write(content)
            f.truncate()
            os.system("chmod +x %s/%s/gen.sh" % (TRG, vers))


# Then generate a cleanup script.
content = """#!/bin/sh
# Cleans some excess directories and generates images.
"""
for ver in versionsToActivate:
    content = content + "\ncd /opt/maximapool-configs/%s" % ver
    content = content + "\n/opt/maximapool-configs/%s/gen.sh" % ver

rems = ""
for item in os.scandir(TRG):
    if item.is_dir() and item.name not in versionsToActivate:
        rems = rems + " /opt/maximapool-configs/%s" + item.name
        os.system("rm -rf %s/%s" % (TRG, item.name))
if not rems == "":
    content = content + "\rm -rf " + rems

with open("%s/gen.sh" % TRG, "w") as f:
    f.write(content)
    os.system("chmod +x %s/gen.sh" % TRG)
