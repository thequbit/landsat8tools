landsat8tools
=============

A set of tools for working with Landsat 8 data

###Background###

The Landsat program is way awesome, and run by the United States Geological Service (USGS)

###Setup###

We need to install Python 2.7 first.  Then do these things:

    > sudo apt-get install imagemagick

Then clone this repo:

    > git clone https://github.com/thequbit/landsat8tools

###Hacking Instructions###

There are three steps: download, uncompress, make RGB, and make preview.  Here is how you can use the files from the command prompt:

First, we need to download the image archive:

    > python download.py LC80160302014073LGN00

Second we need to uncompress the archive:

    > python uncompress.py LC80160302014073LGN00

Third, we need to convert the individual images into a single RGB image:

    > python makergb.py LC80160302014073LGN00

Lastly, we can make a preview JPG that is much smaller and easier to manage (usually less than 15MB):

    > python makepreview.py LC80160302014073LGN00

The output of these commands will be a folder called LC80160302014073LGN00.  In that folder there will now be a number of files.

**NOTE: Each image set (archive) will take about 4GB of data on your drive.  Plan accordingly.**
