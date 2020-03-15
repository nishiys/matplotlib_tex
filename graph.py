import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
# OPTIONS -----------------------
# font.family        : serif
# font.serif         : Times, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman
# font.sans-serif    : Helvetica, Avant Garde, Computer Modern Sans serif
# font.cursive       : Zapf Chancery
# font.monospace     : Courier, Computer Modern Typewriter

# text.usetex        : true
# -------------------------------

tmpData = np.random.random(300)

# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
plt.rc('text', usetex=True)

print(plt.rcParams['font.family'])  # 現在使用しているフォントを表示

# ------------
# line settings
plt.rcParams['lines.linewidth'] = 1.5
fontSizeTitle = 13
fontSizeLabel = 11
fontSizeLegend = 11
lineWidth = 1.5
tickPad = 8
tickPad2 = 16
labelPadY = 6
labelPadX = 6
boxPad = 2
tickLength = 4
markerSize = 4
# color settings
graylist = ["0.1", "0.2", "0.3", "0.4",
            "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
newtableau = cycler(color=['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14E',
                           '#EDC949', '#B07AA2', '#FF9DA7', '#9C755F', '#BAB0AC'])
spacegray = cycler(color=['#343d46', '#4f5b66',
                          '#65737e', '#a7adba', '#c0c5ce'])

plt.rcParams['axes.prop_cycle'] = spacegray

# label settings
plt.rcParams["legend.loc"] = "best"         # best position of legend
label1 = "random"
label2 = "random"
# -------------

fig = plt.figure()
ax1 = fig.add_subplot(211)  # row2, column1, 1st
plt.plot(np.arange(300), tmpData, label=label1)
plt.title(r'$\mathrm{W_y}(\tau, j=3)$', fontsize=fontSizeTitle)
plt.setp(ax1.get_xticklabels(), visible=False)
# ax1.set_xlabel(r'$x$ [ - ]', fontsize=fontSizeLabel, labelpad=labelPadX)
ax1.set_ylabel(r'$y$ [m]', fontsize=fontSizeLabel, labelpad=labelPadY)
ax1.grid(axis='x', color=graylist[5], lw=0.5, ls='--')
ax1.grid(axis='y', color=graylist[5], lw=0.5, ls='--')
ax1.legend()
# Create another plot without a tex title
ax2 = fig.add_subplot(212)
plt.plot(np.arange(300), tmpData, label=label2)
plt.title(r'Some random numbers', fontsize=fontSizeTitle)
ax2.set_xlabel(r'$x$ [ - ]', fontsize=fontSizeLabel, labelpad=labelPadX)
ax2.set_ylabel(r'$y$ [m]', fontsize=fontSizeLabel, labelpad=labelPadX)
ax2.grid(axis='x', color=graylist[5], lw=0.5, ls='--')
ax2.grid(axis='y', color=graylist[5], lw=0.5, ls='--')
ax2.legend()

plt.show()
