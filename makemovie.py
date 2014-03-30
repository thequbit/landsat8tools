import os
import sys

class MovieMaker(object):

    def __init__(self,DEBUG):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "MovieMaker() init completed successfully."

    def makemovie(self,imagepath):

        os.system("mkdir {0}".format(imagepath))

        dirs = []
        for dirname, dirnames, filenames in os.walk('.'):
            dirs = dirnames 
            break

        print "Copying review images ..."

        for d in dirs: 
            if imagepath in d:
                os.system("cp ./{0}/*_PREVIEW* ./{1}/".format(d,imagepath))

        print "Resizing images ..."

        os.system("cd {0}; mogrify -resize 1024x1024! *.JPG".format(imagepath))

        self._rename(imagepath)

        print "Creating Movie ..."

        os.system("cd ./{0}; ffmpeg -i %03d.JPG \"fade=in:5:8\" {0}.MPG".format(imagepath))

        print "Done."

    def _rename(self,imagepath):

        print "Renaming images for sequence ..."

        i = 0;
        for filename in os.listdir("./{0}/".format(imagepath)):
            print "Working on '{0}'".format(filename)
            if ".JPG" in filename:
                if i < 10:
                    name = "00{0}.JPG".format(i)
                elif i < 100:
                    name = "0{0}.JPG".format(i)
                else:
                    name = "{0}.JPG".format(i)

                print "New Name: '{0}'".format(name)

                cmd = "cd ./{0}; mv {1} {2}".format(imagepath,filename,name)

                print "Command: '{0}'".format(cmd)

                os.system(cmd)

                i+=1


if __name__ == '__main__':

    if len(sys.argv) != 2:

        print "Usage:\n\tpython makemovie.py <imagepath>"

    else:

        print "Creating movie from iamge path folders ..."

        imagepath = sys.argv[1]

        mm = MovieMaker(DEBUG=True)

        mm.makemovie(imagepath)

        print "All Done."
