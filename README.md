# mplrcpub

RC settings and formatting helper for making publication ready plots.

## Example

    import sys
	sys.path.insert(0, 'path/to/pub_fig_settings.py')

    from pubfig_settings import make_figure
    from pubfig_settings import preview_in_latex

    plt.ioff()

    # 'onecolumn' or 'twocolumn', 2nd arg is height of plot in inches
    fig = make_figure("onecolumn", 2)
    fig.subplots_adjust(left  =0.148)
    fig.subplots_adjust(bottom=0.174)
    fig.subplots_adjust(top   =0.915)
    fig.subplots_adjust(right =0.998)
    ax = plt.gca()

    # Plotting code here

    preview_in_latex()
    plt.ion()

