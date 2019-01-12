import os, sys, PIL
from PIL import Image
import sys

size = 96, 96
cc=sys.argv[1]
path = 'Images/'+cc+'/'

for x in os.listdir('Images/'+cc):
    #print(x)
    if x.endswith('_blurred.png'):
            outfile = os.path.splitext(x)[0] + "_resize.png"
            #print(outfile)
            if x != outfile:
                try:
                    im = Image.open(path+x)
                    im.thumbnail(size, Image.ANTIALIAS)
                    im.save(path+outfile, "PNG", subsampling=0, quality=100)
                except IOError as e:
                    print ("cannot create thumbnail for '%s'" % x)
                    print (e)


'''for x in os.listdir():
    if os.path.isdir(x):
        for y in os.listdir(x):
            outfile = os.path.splitext(y)[0] + "_resize.png"
            if y != outfile:
                try:
                    im = Image.open(x+"/"+y)
                    im.thumbnail(size, Image.ANTIALIAS)
                    im.save(x+"/"+outfile, "PNG", subsampling=0, quality=100)
                except IOError as e:
                    print ("cannot create thumbnail for '%s'" % y)
                    print (e)
'''
print ("done")
