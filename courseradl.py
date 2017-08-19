#! /usr/bin/python3

"""zipper is the main function. It takes two arguments. The zip file name and the
   directory to be zipped, and will zip the contents of the directory into that zipfile."""

import os
import re
import zipfile

def traverse(dirname, func):
	if os.path.isdir(dirname):
		children = [os.path.join(dirname, child) for child in sorted(os.listdir(dirname))]
		for child in children:
			traverse(child, func)
	elif os.path.isfile(dirname):
		func(dirname)

def zipper(zfname, dirname):
	if os.path.exists(zfname):
		os.unlink(zfname)
	with zipfile.ZipFile(zfname, "w") as zfile:
		def handler(rawfname):
			if re.match("^.*%s$" % (zfname), rawfname) is None:
				zfile.write(rawfname)

		traverse(dirname, handler)
