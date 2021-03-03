# mplrcpub

RC settings and formatting helper for making publication ready plots.  In particular, getting the sizing correct.  Choice of colors, tickmarks, and other styles is left undone. 

Plot size and appearance is different when viewed in ipython or jupyter, vs. when it's saved as a pdf.  The sizing parameters in `publish` refer to the pdf version.  For instance, the fontsize of 10 refers to the saved pdf version of the figure. When that figure is placed into a latex or word doc without resizing, it's fontsize 10 will match the text's fontsize of 10.

## Example

```python
import mplrcpub
from mplrcpub import publish
import numpy as np

from matplotlib.ticker import (
    MultipleLocator, 
    FormatStrFormatter,
    AutoMinorLocator
)


with publish(
    num_columns=2,
    height=3,
    fontsize=10,
    preview=True,
    top=0.9,
    bottom=0.2,
    filename="/Users/billengels/Desktop/testdoc.pdf"
) as fig:
    
    ax = fig.gca()
    ax.plot(np.random.randn(10), 0.5*np.random.randn(10), lw=3, color=mplrcpub.orange)
    ax.plot(np.random.randn(10), 0.5*np.random.randn(10), lw=3, color="b")
    ax.plot(np.random.randn(10), 0.5*np.random.rand(10), lw=3, color="r")
    
    ax.set_title("This is the title")
    ax.set_xlabel("X direction")
    ax.set_ylabel("Y direction")
    
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    ax.xaxis.set_minor_locator(MultipleLocator(0.1))
    
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    mplrcpub.set_ticklines(ax, 1, 1)
    mplrcpub.set_tick_sizes(ax, 6, 2)
```

![image](https://user-images.githubusercontent.com/6325473/109865821-266bc600-7c2a-11eb-8b76-711985406bb7.png)
