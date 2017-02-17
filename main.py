import os
import sys

filename = sys.argv[1]

with open ( filename ) as file:
    content = file.readlines()
content = [ line.strip() for line in content ]

arg = content.pop()
while ( len( content ) != 0 ):
    os.system( "git checkout " + arg )
    input( "Press enter to continue..." )
    arg = content.pop()

print( "IT'S OVER!" )