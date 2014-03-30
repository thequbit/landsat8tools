import sys
import os
import os.path

class Uncompresser(object):

    def __init__(self,DEBUG=False):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "Uncompresser() init successfull."

    def uncompress(self,imagename):

        if os.path.isfile("./{0}/{0}_B1.TIF".format(imagename)):
            if self.DEBUG:
                print "Archive already uncompressed, skipping."
            return

        cmd = "mkdir {0}; tar -zxvf {0}.tar.gz -C ./{0}".format(imagename)

        if self.DEBUG:
            print "Uncompressing image archive ..."

        os.system(cmd)

        if self.DEBUG:
            print "Done."

if __name__ == '__main__':

    if len(sys.argv) != 2:

        print "Usage:\n\tpython uncompress.py <imagename>"

    else:

        imagename = sys.argv[1]

        print "Uncompressing archive ..."

        u = Uncompresser()

        u.uncompress(imagename)

        print "All Done."
