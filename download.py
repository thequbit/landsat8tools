import sys
import os
import os.path

class Downloader(object):

    def __init__(self,username,password,DEBUG=False):

        self._username = username
        self._password = password

        self.DEBUG = DEBUG

        self._authurl = "https://earthexplorer.usgs.gov/login/"

        if self.DEBUG:
            print "Downloader() init successfull"

    def _login(self,):

        cmd = "wget -O dummy.txt --keep-session-cookies --save-cookies cookies.txt --post-data 'username={0}&password={1}&rememberMe=0&submit=' {2}".format(self._username,self._password,self._authurl)

        if self.DEBUG:
            print "Generating credential cookies ..."

        os.system(cmd)

        if self.DEBUG:
            print "... Done."

    def download(self,imagename):

        if os.path.isfile("{0}.tar.gz".format(imagename)):

            if self.DEBUG:
                print "File exists, skipping."

            return

        self._login()

        url = "http://earthexplorer.usgs.gov/download/4923/{0}/STANDARD/EE".format(imagename)

        cmd = "wget --load-cookies cookies.txt -O {0}.tar.gz {1}".format(imagename,url)

        if self.DEBUG:
            print "URL:\n\t{0}".format(url)

        if self.DEBUG:
            print "Downloading image archive ..."

        os.system(cmd)

        if self.DEBUG:
            print "... Done."

if __name__ == '__main__':

    if len(sys.argv) != 2:

        print "Usage:\n\tpython download.py <imagename>"

    else:
    
        imagename = sys.argv[1]

        print "Downloading landsat data ..."

        with open("creds.txt","r") as f:
            lines = f.readlines()
        username = lines[0].strip()
        password = lines[1].strip()

        #imagename = "LC80160302014073LGN00"

        d = Downloader(username=username,password=password,DEBUG=True)

        d.download(imagename)

        print "All done."



