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
    prefix = 'LC8016030'
    postfix = 'LGN01'
    images = [
        '2013102LGN01', # April 12t, 2013
        '2013118LGN02',
        '2013134LGN03',
        '2013150LGN00',
        '2013157LGN00',
        '2013166LGN00',
        '2013173LGN00',
        '2013182LGN00',
        '2013189LGN00',
        '2013198LGN00',
        '2013205LGN00',
        '2013214LGN00',
        '2013221LGN00',
        '2013230LGN00',
        '2013237LGN00',
        '2013246LGN00',
        '2013253LGN00',
        '2013262LGN00',
        '2013269LGN00',
        '2013278LGN00',
        '2013285LGN00',
        '2013294LGN00',
        '2013301LGN00',
        '2013310LGN00',
        '2013317LGN00',
        '2013326LGN00',
        '2013333LGN00',
        '2013342LGN00',
        '2013349LGN00',
        '2013358LGN00',
        '2013365LGN00',
        '2014009LGN00',
        '2014016LGN00',
        '2014025LGN00',
        '2014032LGN00',
        '2014041LGN00',
        '2014048LGN00',
        '2014057LGN00',
        '2014064LGN00',
        '2014073LGN00',
        '2014080LGN00', # Marth 21st, 2014
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
