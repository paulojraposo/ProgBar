#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    .-.                         
#    /v\    L   I   N   U   X   :)
#   // \\                        
#  /(   )\                       
#   ^^-^^                        

# Copyright (c) 2018 Paulo Raposo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



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
    
    import time, sys, os, shutil
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
