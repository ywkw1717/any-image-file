#!/usr/bin/env python

import sys
from PIL import Image

args = sys.argv

image = Image.new("RGB", (int(args[1]), int(args[2])))
image.save("image.png")
