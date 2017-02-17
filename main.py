import os
import sys

filename = sys.argv[1]

with open ( filename ) as file:
    content = file.readlines()
content = [ line.strip() for line in content ]

while ( arg = content.pop() ):
    os.system( "git checkout " + arg )
    print( "git checkout " + arg )
    input( "Press enter to continue..." )

print( "IT'S OVER!" )