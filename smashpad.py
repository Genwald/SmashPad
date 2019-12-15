# SmashPad v0.2
# by Birdwards and NyxTheShield

import sys
from pathlib import Path
import zstandard as zstd

def comp(input_name):
    input = open(input_name, 'rb').read()

    # Compress uncomp_file at every level
    print("compressing " + str(input_name))
    smallestSize = 0
    smallestLvl = 0
    lvl = 1
    while lvl<=22:
        cctx = zstd.ZstdCompressor(level=lvl)
        comp_size = len(cctx.compress(input))
        if(comp_size < smallestSize or smallestSize == 0):
            smallestSize = comp_size
            smallestLvl = lvl
        lvl+=1
    print("Level " + str(smallestLvl) + ": " + hex(smallestSize) + " bytes")

howto = "How to use this tool:\npython smashpad.py [input]\n[input] = Name of the file to be compressed/decompressed\n\nExample:\npython smashpad.py ui_spirits_battle_db.prc"

# Main stuff
if len(sys.argv) <= 1:
    sys.exit("SmashPad 0.2\n\n" + howto)
elif len(sys.argv) == 2:
    inputPath = Path(sys.argv[1])
    if inputPath.is_dir():
        for filename in inputPath.rglob('*'):
            if filename.is_file():
                comp(filename)
    elif inputPath.is_file():
        comp(inputPath)
else:
    sys.exit("Error: Wrong number of arguments\n\n" + howto)
input("press enter to exit")

