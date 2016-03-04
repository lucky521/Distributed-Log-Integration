# -*- coding: utf-8 -*-
#############################################
import os, shutil
from decompress import decompress_zip
from pattern import match_period
from html_generator import output_html
#############################################
# User input
# one uploadId can map to multiple time period's outputId
start_time = "2016-03-01 10:23:49"
end_time   = "2016-03-01 11:23:49"
uploadId = 1
outputId = 1 
#############################################
# folder location configuration
uploadFolder = "./upload/id-" + str(uploadId)
inputFolder = "./input/id-" + str(uploadId)
outputFolder = "./output/id-" + str(outputId)
result_html = output_html(outputId, "Result-id-" + str(outputId), start_time, end_time)
############################################

def traverse_to_extract(path_from, path_to):   
    for lists in os.listdir(path_from):   
        path_from_new = os.path.join(path_from, lists)
        path_to_new = os.path.join(path_to, lists)
        
        if os.path.isdir(path_from_new):
            traverse_to_extract(path_from_new, path_to_new)
            continue
        else:
            print "Extracting: " + path_from_new 
            decompress_zip(path_from_new, path_to)


def extract_all_zipfile(uploadFolder, inputFolder):
    traverse_to_extract(uploadFolder, inputFolder)
    print "extract_all_zipfile Done."



def traverse_to_match(path_from, path_to):
    for lists in os.listdir(path_from):   
        path_from_new = os.path.join(path_from, lists)
        path_to_new = os.path.join(path_to, lists)
        
        if os.path.isdir(path_from_new):
            traverse_to_match(path_from_new, path_to_new)
            continue
        else:
            if match_period(path_from_new, start_time, end_time):
                print "Matching for: " + path_from_new
                #print path_to
                if not os.path.exists(path_to):
                    os.makedirs(path_to)
                
                # copy target file to output
                shutil.copy(path_from_new, path_to_new)
                # generate html file. not good here.
                result_html.add_link("../.." + path_to_new[1:]) 
    

def collect_all_match(inputFolder, outputFolder):
    traverse_to_match(inputFolder, outputFolder)
    print "collect_all_match Done."
    


    
if __name__ == '__main__':
    #extract_all_zipfile(uploadFolder, inputFolder)
    collect_all_match(inputFolder, outputFolder)
    result_html.generate_html("./output/id-" + str(outputId) + "/")
    print "Done."