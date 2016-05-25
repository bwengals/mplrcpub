#/usr/bin/env python

import matplotlib.pyplot as plt
import os
import random
from matplotlib import rc

rc('text', usetex=True)
rc('mathtext', default='sf')

rc('font', size=10)
rc('font', family='serif')
rc('font', serif='palatino')
rc('font', weight='medium')

rc("lines", markeredgewidth=1)
rc("lines", linewidth=1)

rc("axes", labelsize=10)
rc("axes", linewidth=0.8)
rc("axes", titlesize='medium')
rc("axes", unicode_minus=False)

rc('xtick',       labelsize=10.0)
rc('xtick.major', pad=4.0)
rc('xtick.major', size=4.0)
rc('xtick.major', width=0.8)
rc('xtick.minor', pad=2.0)
rc('xtick.minor', size=2.0)
rc('xtick.minor', width=0.8)

rc('ytick',       labelsize=10.0)
rc('ytick.major', pad=4.0)
rc('ytick.major', size=4.0)
rc('ytick.major', width=0.8)
rc('ytick.minor', pad=2.0)
rc('ytick.minor', size=2.0)
rc('ytick.minor', width=0.8)

rc('text.latex', unicode=True)
rc('savefig', dpi=300.0)
rc('legend', fontsize=10)
rc('legend', scatterpoints=1)
rc('legend', frameon=False)
rc('image', cmap='afmhot')
rc('image', interpolation='none')
rc('figure', frameon=False)
rc('figure', dpi=300.0)
rc('pdf', compression=6)


green1='#00ff00'
orange='#ffba00'

def make_figure(width="onecolumn", height=2):
    assert width is "onecolumn" or "twocolumn", "Must be 'onecolumn' or 'twocolumn"
    global NUMCOLUMNS
    if width is "onecolumn":
        w = 3.6
        NUMCOLUMNS = 1
    else:
        w = 7.0
        NUMCOLUMNS = 2
    fig = plt.figure(figsize=(w, height), frameon=False)
    return fig

def preview_in_latex():
    if NUMCOLUMNS == 1:
        plt.savefig("/tmp/onecolumn.pdf")
    elif NUMCOLUMNS == 2:
        plt.savefig("/tmp/twocolumn.pdf")
    else:
        raise TypeError("unknown number of columns")
    doc = r"""
%\documentclass[prd, twocolumn, amsmath, floatfix, preprintnumbers, nofootinbib,superscriptaddress,letterpaper]{revtex4-1}
\documentclass[11pt,twocolumn]{article}

%\bibliographystyle{apsrev}

\usepackage{lipsum}
\usepackage{graphicx}
\usepackage{amsbsy}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{layouts}
\usepackage{mdframed}
\usepackage{natbib}
\usepackage{xcolor}
\usepackage{mathtools}
\usepackage{subfigure}
\usepackage{dcolumn}
\usepackage{units}
\usepackage{braket}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

\title{Great title of paper}
\date{\today}
\author{Your name here}
%\email{"""+str(random.randint(1,1000))+r"""@aol.com}
%\affiliation{Banzai Institute for Biomedical Engineering and Strategic Information}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{abstract}
\lipsum[1-1]
\end{abstract}

\maketitle

\section{Introduction}
\lipsum[2-4]

\begin{figure}[t!]
  \centerline{\includegraphics[width=8.6cm]{/tmp/onecolumn.pdf}}
\end{figure}

\begin{figure*}[t!]
  \centerline{\includegraphics[width=17.2cm]{/tmp/twocolumn.pdf}}
\end{figure*}

\lipsum[5-25]

\end{document}
"""
    with open("/tmp/ldoc.tex", 'wb') as f:
        f.write(doc)

    os.system("pdflatex -output-directory /tmp /tmp/ldoc.tex")
    os.system("rm *.log && rm *.bib && rm *.aux")
    os.system("evince /tmp/ldoc.pdf &")




def set_ticklines(ax,major,minor):
    ticklines = ax.xaxis.get_majorticklines()
    plt.setp(ticklines,mew=major)
    ticklines = ax.xaxis.get_minorticklines()
    plt.setp(ticklines,mew=minor)
    ticklines = ax.yaxis.get_majorticklines()
    plt.setp(ticklines,mew=major)
    ticklines = ax.yaxis.get_minorticklines()
    plt.setp(ticklines,mew=minor)

def set_tick_sizes(ax, major, minor):
    for l in ax.get_xticklines() + ax.get_yticklines():
        l.set_markersize(major)
    for tick in ax.xaxis.get_minor_ticks() + ax.yaxis.get_minor_ticks():
        tick.tick1line.set_markersize(minor)
        tick.tick2line.set_markersize(minor)
    ax.xaxis.LABELPAD=10.
    ax.xaxis.OFFSETTEXTPAD=10.

