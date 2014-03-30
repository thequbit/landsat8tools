import sys
import os

class MakeRGB(object):

    def __init__(self,DEBUG=False):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "MakePreview() init successfull"

    def makergb(self,imagename,RED=4,GREEN=3,BLUE=2):

        """
        Info via: http://landsat.usgs.gov/band_designations_landsat_satellites.php
        
        Band 1 - Coastal aerosol .............. 0.43 - 0.45 30
        Band 2 - Blue ......................... 0.45 - 0.51 30
        Band 3 - Green ........................ 0.53 - 0.59 30
        Band 4 - Red .......................... 0.64 - 0.67 30
        Band 5 - Near Infrared (NIR) .......... 0.85 - 0.88 30
        Band 6 - SWIR 1 ....................... 1.57 - 1.65 30
        Band 7 - SWIR 2 ....................... 2.11 - 2.29 30
        Band 8 - Panchromatic ................. 0.50 - 0.68 15
        Band 9 - Cirrus ....................... 1.36 - 1.38 30
        Band 10 - Thermal Infrared (TIRS) 1 .. 10.60 - 11.19 100
        Band 11 - Thermal Infrared (TIRS) 2 .. 11.50 - 12.51 100
        """

        if os.path.isfile("./{0}/{0}_RGB.TIF".format(imagename)):
            if self.DEBUG:
                print "RGB file already exists, skipping."
            return

        cmds = []

        cmds.append("gdalwarp -t_srs EPSG:3857 ./{0}/{0}_B{1}.TIF ./{0}/{0}_B{1}_PROJECTED.TIF".format(imagename,RED))
        cmds.append("gdalwarp -t_srs EPSG:3857 ./{0}/{0}_B{1}.TIF ./{0}/{0}_B{1}_PROJECTED.TIF".format(imagename,GREEN))
        cmds.append("gdalwarp -t_srs EPSG:3857 ./{0}/{0}_B{1}.TIF ./{0}/{0}_B{1}_PROJECTED.TIF".format(imagename,BLUE))

        cmds.append("convert -combine ./{0}/{0}_B{1}_PROJECTED.TIF ./{0}/{0}_B{2}_PROJECTED.TIF ./{0}/{0}_B{3}_PROJECTED.TIF ./{0}/{0}_RGB.TIF".format(imagename,RED,GREEN,BLUE))

        cmds.append("convert -channel B -gamma 0.925 -channel R -gamma 1.03 -channel RGB -sigmoidal-contrast 50x16% ./{0}/{0}_RGB.TIF ./{0}/{0}_CORRECTED.TIF".format(imagename))

        if self.DEBUG:
            print "Creating combined image ..."

        for cmd in cmds:
            os.system(cmd)

        if self.DEBUG:
            print "... Done."

if __name__ == '__main__':

    if len(sys.argv) != 2:

        print "Usage:\n\tpython makergb.py <imagename>"

    else:

        imagename = sys.argv[1]

        print "Making RGB image ..."

        mp = MakeRGB()

        mp.makergb(imagename)

        print "All Done."

