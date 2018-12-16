# A Simple Progress Bar

Little Python module for a nice Unicode progress bar, useful for console applications when you want to give your user a running percentage of some job done.

![A screenshot][screenshot]

Bar can be arbitrarily long, and you can precede it with some text of your choosing.

Simply run the module (i.e., `python ProgBar.py`) to see it demonstrated.

## Requirements

Python 3.x.

## Usage
Just use carriage returns and flushes (i.e., `end="\r"` and `flush=True`) in your `print()` statements to keep writing on the same line:

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ProgBar

thingsToDo = 42
for thingBeingDone in range(thingsToDo):
    progress = (thingBeingDone + 1) / thingsToDo
    # Bar will be 20 spaces long, and preceded by "progress: " (one space appended):
    print(ProgBar.ProgressBar(progress, "progress:", 20), end="\r", flush=True)
```

[screenshot]: ./figures/screenshot.jpg