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
        '2013102', # April 12t, 2013
        '2013118',
        '2013134',
        '2013150',
        '2013157',
        '2013166',
        '2013173',
        '2013182',
        '2013189',
        '2013198',
        '2013205',
        '2013214',
        '2013221',
        '2013230',
        '2013237',
        '2013246',
        '2013253',
        '2013262',
        '2013269',
        '2013278',
        '2013285',
        '2013294',
        '2013301',
        '2013310',
        '2013317',
        '2013326',
        '2013333',
        '2013342',
        '2013349',
        '2013358',
        '2013365',
        '2014009',
        '2014016',
        '2014025',
        '2014032',
        '2014041',
        '2014048',
        '2014057',
        '2014064',
        '2014073',
        '2014080', # Marth 21st, 2014
    ]

    print "Processing {0} image archives ...".format(len(images))

    for image in images:

        imagename = "{0}{1}{2}".format(prefix,image,postfix)

        dler.download(imagename)

        uncomp.uncompress(imagename)

        rgb.makergb(imagename)

        prev.makepreview(imagename)

        #cleanup
        os.system('rm ./{0}/*_PROJECTED*')
        os.system('rm ./{0}/*_RGB*')
        
        print "Done with {0}".format(imagename)

    print "Done creating JPEG preview files for all {0} image archives.".format(len(images))
