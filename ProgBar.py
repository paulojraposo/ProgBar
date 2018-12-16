#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    .-.
#    /v\    L   I   N   U   X   :)
#   // \\
#  /(   )\
#   ^^-^^


def ProgressBar(percent, prefix=None, notches=50, numericalpercent=True):

    """Accepting a number between 0.0 and 1.0 [percent], returns a string containing a UTF-8
    representation of a progress bar of x segments [notches] to the screen, along with an
    optional indication of the progress as the given percentage rounded to two places
    [numericalpercent], and, if given one, a custom string preceding the progress bar
    [prefix]."""

    outString = u"" # Unicode string.
    if prefix:
        prefix = "{} ".format(prefix)
        outString = outString + prefix
    x_of_notches = int(round(percent * notches))
    for i in range(x_of_notches):
        outString = outString + "\u25AE" # Full block
    for i in range(notches - x_of_notches):
        outString = outString + "\u25AF" # Empty block
    if numericalpercent:
        outString = outString + " [{}%]".format(str(round(percent * 100, 2)))
    return outString


if __name__ == "__main__":

    """An example of usage."""

    import time, os, shutil
    steps = 42
    aPrefix = "Job progress:"
    termWidth = shutil.get_terminal_size()[0]
    barLength = termWidth - 30
    for i in range(steps):
        progress = (i + 1) / steps
        print(ProgressBar(progress, aPrefix, barLength), end="\r", flush=True)
        if i == steps - 1:
            print()
        else:
            time.sleep(0.1)
