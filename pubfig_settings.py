#/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import os
import random
import time


green1='#00ff00'
orange='#ffba00'


test_doc = r"""
\documentclass[10pt,twocolumn]{article}


\usepackage{lipsum}
\usepackage{graphicx}
\usepackage{amsbsy}
\usepackage{layouts}
\usepackage{mathtools}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

\title{Great title of paper}
\date{\today}
\author{George Costanza}
\affiliation{Banzai Institute for Biomedical Engineering and Strategic Information}

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

\lipsum[5-10]

\end{document}
"""



class publish(object):
    def __init__(self, num_columns=1, height=3,
                       top=0.88, bottom=0.11, left=0.125, right=0.9,
                       hspace=0.2, wspace=0.2,
                       fontsize=10, preview=False, filename=None):

        if num_columns == 1:
            self.width = 3.6
        elif num_columns == 2:
            self.width = 7.0
        else:
            raise ValueError("num_columns must be 1 or 2")
        self.num_columns = num_columns
        self.height      = height
        self.top         = top
        self.bottom      = bottom
        self.left        = left
        self.right       = right
        self.hspace      = hspace
        self.wspace      = wspace
        self.fontsize    = fontsize
        self.preview     = preview
        self.filename    = filename

    def __enter__(self):
        matplotlib.rcParams.update(
          {"text.usetex":           False,
           "mathtext.default":      "sf",
           "font.size":             self.fontsize,
           "font.family":           "serif",
           "font.serif":            "Palatino",
           "font.weight":           "medium",
           "lines.markeredgewidth": 1,
           "lines.linewidth":       1,
           "axes.labelsize":        self.fontsize,
           "axes.linewidth":        0.8,
           "axes.titlesize":        "medium",
           "axes.unicode_minus":    False,
           "xtick.labelsize":       self.fontsize,
           "xtick.major.pad":       4.0,
           "xtick.major.size":      4.0,
           "xtick.major.width":     0.8,
           "xtick.minor.pad":       2.0,
           "xtick.minor.size":      2.0,
           "xtick.minor.width":     0.8,
           "ytick.labelsize":       self.fontsize,
           "ytick.major.pad":       4.0,
           "ytick.major.size":      4.0,
           "ytick.major.width":     0.8,
           "ytick.minor.pad":       2.0,
           "ytick.minor.size":      2.0,
           "ytick.minor.width":     0.8,
           "pdf.fonttype":          42,
           "ps.fonttype":           42,
           "pgf.texsystem":         "pdflatex",
           "savefig.dpi":           300,
           "savefig.pad_inches":    0.01,
           "savefig.format":        "pdf",
           "legend.fontsize":       self.fontsize,
           "legend.scatterpoints":  1,
           "legend.frameon":        False,
           "image.cmap":            "inferno",
           "image.interpolation":   "none",
           "image.origin":          "lower",
           "figure.frameon":        False,
           "figure.dpi":            300,
           "figure.subplot.top":    self.top,
           "figure.subplot.bottom": self.bottom,
           "figure.subplot.left":   self.left,
           "figure.subplot.right":  self.right,
           "figure.subplot.hspace": self.hspace,
           "figure.subplot.wspace": self.wspace, 
           "pdf.compression":       6})
        return plt.figure(figsize=(self.width, self.height))

    def __exit__(self, *args):
        if self.filename is not None:
            plt.savefig(self.filename)

        if self.preview:
            plt.savefig(r"/tmp/onecolumn.pdf")
            plt.savefig(r"/tmp/twocolumn.pdf")
            with open("/tmp/ldoc.tex", 'w') as f:
                f.write(test_doc)
            os.system(r"pdflatex -output-directory /tmp /tmp/ldoc.tex")
            os.system(r"evince /tmp/ldoc.pdf && rm *.log && rm *.bib && rm *.aux")
        # revert to orginal settings
        matplotlib.rcParams.update(matplotlib.rcParamsDefault)



def set_ticklines(ax, major, minor):
    ticklines = ax.xaxis.get_majorticklines()
    plt.setp(ticklines, mew=major)
    ticklines = ax.xaxis.get_minorticklines()
    plt.setp(ticklines, mew=minor)
    ticklines = ax.yaxis.get_majorticklines()
    plt.setp(ticklines, mew=major)
    ticklines = ax.yaxis.get_minorticklines()
    plt.setp(ticklines, mew=minor)

def set_tick_sizes(ax, major, minor):
    for l in ax.get_xticklines() + ax.get_yticklines():
        l.set_markersize(major)
    for tick in ax.xaxis.get_minor_ticks() + ax.yaxis.get_minor_ticks():
        tick.tick1line.set_markersize(minor)
        tick.tick2line.set_markersize(minor)
    ax.xaxis.LABELPAD=10.
    ax.xaxis.OFFSETTEXTPAD=10.

