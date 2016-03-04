# -*- coding: utf-8 -*-

import os, shutil, re
#########################################
# This script helps to get certain log bundle from certain place
uploadid = 2
bugid = 1234567
#########################################

def match_keywords(filename, keyword):
    pattern = re.compile(keyword)
    match = pattern.search(filename)
    if match:
        return True
    else:
        return False


def traverse_to_fetch(path_from, path_to, path_to_base):   
    for lists in os.listdir(path_from):   
        path_from_new = os.path.join(path_from, lists)
        path_to_new = os.path.join(path_to, lists)
        
        if os.path.isdir(path_from_new):
            if match_keywords(path_from_new, "vdm-sdct-\d\d\d\d"):
                print "Pass for extracted folder: " + path_from_new
            else:
                traverse_to_fetch(path_from_new, path_to_new, path_to_base)
        else:
            if match_keywords(path_from_new, "vdm-sdct-\d\d\d\d.*\.zip"):
                print "Fetch: " + path_from_new 
                #print path_to_new

                if match_keywords(path_from_new, "vdm-sdct-\d\d\d\d.*client\.zip"): # copy to client
                    path_to_full = os.path.join(path_to_base + "/client", path_to)
                    if not os.path.exists(path_to_full):
                        os.makedirs(path_to_full)
                        #print "mkdir:" + path_to_full
                    shutil.copy(path_from_new, path_to_full)
                    print "Copy done: " + path_from_new
                elif match_keywords(path_from_new, "vdm-sdct-\d\d\d\d.*agent\.zip"): # copy to agent
                    path_to_full = os.path.join(path_to_base + "/agent", path_to)
                    if not os.path.exists(path_to_full):
                        os.makedirs(path_to_full)
                        #print "mkdir:" + path_to_full
                    shutil.copy(path_from_new, path_to_full)
                    print "Copy done: " + path_from_new
                elif match_keywords(path_from_new, "vdm-sdct-\d\d\d\d.*server\.zip"): # copy to server
                    path_to_full = os.path.join(path_to_base + "/server", path_to)
                    if not os.path.exists(path_to_full):
                        os.makedirs(path_to_full)
                        #print "mkdir:" + path_to_full
                    shutil.copy(path_from_new, path_to_full)
                    print "Copy done: " + path_from_new






if __name__ == '__main__':
    print "test for traverse_to_fetch."
    bugid = str(bugid)
    uploadid = str(uploadid)
    
    # path configuration
    path_from = "Z:\\files\\0\\"
    for i in bugid:
        path_from += i
        path_from += "\\"
    path_to_base = "./upload/id-" + uploadid
    path_to = ""
    
    print path_from
    print path_to_base
    print path_to
    traverse_to_fetch(path_from, path_to, path_to_base)