import os

from download import Downloader
from uncompress import Uncompresser
from makergb import MakeRGB
from makepreview import MakePreview

if __name__ == '__main__':

    with open("creds.txt","r") as f:
        lines = f.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

    # create tool instances
    dler = Downloader(username=username,password=password,DEBUG=True)
    uncomp = Uncompresser(DEBUG=True)
    rgb = MakeRGB(DEBUG=True)
    prev = MakePreview(DEBUG=True)

    # create list of known images
    #LC80130312013273LGN00
    prefix = 'LC8012031'
    #postfix = 'LGN01'
    images = [
        '2014077LGN00',
        '2014061LGN01',
        '2014045LGN00',
        '2014029LGN00',
        '2014013LGN00',
        '2013362LGN00',
        '2013346LGN00',
        '2013330LGN00',
        '2013314LGN00',
        '2013266LGN00',
        '2013250LGN00',
        '2013234LGN00',
        '2013218LGN00',
        '2013202LGN00',
        '2013186LGN00',
        '2013170LGN00',
        '2013154LGN00',
        '2013138LGN01',
        '2013122LGN01',
        '2013106LGN01',
    ]

    print "Processing {0} image archives ...".format(len(images))

    for image in images:

        imagename = "{0}{1}".format(prefix,image)

        print "Working on '{0}' ...".format(imagename)

        dler.download(imagename)

        uncomp.uncompress(imagename)

        rgb.makergb(imagename)

        prev.makepreview(imagename)

        #cleanup
        os.system("rm ./{0}/*_B*.TIF".format(imagename))
        #os.system("rm ./{0}/*_PROJECTED*".format(imagename))
        #os.system('rm ./{0}/*_RGB*')

        print "Done with {0}".format(imagename)

    print "Done creating JPEG preview files for all {0} image archives.".format(len(images))


