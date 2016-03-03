# -*- coding: utf-8 -*-

import zipfile

test_inputfile = "./test.zip"
test_outpath = "."

def decompress_zip(inputfile, outpath):
    fh = open(inputfile, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        z.extract(name, outpath)
    fh.close()
    
if __name__ == '__main__':
    print "test for decompress_zip."
    match_period(test_inputfile, test_outpath)