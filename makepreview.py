import sys
import os

class MakePreview(object):

    def __init__(self,DEBUG=False):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "MakePreview() init successfull"

    def makepreview(self,imagename):

        if os.path.isfile("./{0}/{0}_PREVIEW.JPG".format(imagename)):
            if self.DEBUG:
                print "Preview image already exists, skipping."
            return 

        cmd = "convert ./{0}/{0}_CORRECTED.TIF ./{0}/{0}_PREVIEW.JPG".format(imagename)

        if self.DEBUG:
            print "Creating preview image ..."

        os.system(cmd)

        if self.DEBUG:
            print "... Done."

if __name__ == '__main__':

    if len(sys.argv) != 2:

        print "Usage:\n\tpython makepreview.py <imagename>"

    else:

        imagename = sys.argv[1]

        print "Making RGB image preview ..."

        mp = MakePreview()

        mp.makepreview(imagename)

        print "All Done."

