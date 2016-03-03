# -*- coding: utf-8 -*-

# regular expression match
# time zone
# 24 hour clock

'''
2016-03-01T10:23:49.151-05:00
2016/03/01 11:27:24.769
 2016-02-26T15:22:09.237Z
03/01/2016, 09:29:17.639>

####
^\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d.\d\d\d

^\d\d/\d\d/\d\d\d\d, \d\d:\d\d:\d\d.\d\d\d

'''
import re 

testfile = "test_match2.txt"
start_time = "2016-03-01 10:23:49"
end_time = "2016-03-01 11:23:49"


class time_pattern:
    # "2016-03-01 10:23:49"
    
    def __init__(self, init_pattern):
        self.year = init_pattern[0:4]
        self.month = init_pattern[5:7]
        self.day = init_pattern[8:10]
        self.hour = init_pattern[11:13]
        self.minute = init_pattern[14:16]
        self.second = init_pattern[17:19]
        
    def outto_tatget_a(self):
        # fuzzy_targt_a 
        # "^\d\d\d\d-\d\d-\d\d.\d\d:\d\d:\d\d.\d\d\d"
        # 2016/03/01 11:27:24
        fuzzy_targt_a = "^" + self.year + "-" + self.month + "-" + self.day + "." + self.hour + ":" + self.minute + ":" + self.second
        fuzzy_targt_a = fuzzy_targt_a.replace("x", "\d")
        return fuzzy_targt_a

    def outto_tatget_b(self):
        # fuzzy_targt_b
        # "^\d\d/\d\d/\d\d\d\d, \d\d:\d\d:\d\d.\d\d\d"
        # 03/01/2016, 09:29:17.639
        fuzzy_targt_b = "^" + self.month + "/" + self.day + "/" + self.year + ", " + self.hour + ":" + self.minute + ":" + self.second
        fuzzy_targt_b = fuzzy_targt_b.replace("x", "\d")
        return fuzzy_targt_b




def get_fuzzy_target(start_time, end_time):

    # Longest Common Prefix
    # start_time = "2016-03-01 10:23:49"
    # end_time = "2016-03-01 11:23:49"
    if len(start_time) != len(end_time):
        print "Error length of start_time or end_time"
        return "@@@@@@@"
    time_prefix = "xxxx-xx-xx xx:xx:xx"
    time_prefix_list = list(time_prefix) 
    # 'str' object does not support item assignment. so convert to list
    time_str_len = len(start_time)
    for idx in range(0, time_str_len):
        if start_time[idx] == end_time[idx]:
            time_prefix_list[idx] = start_time[idx]
        else:
            break
    time_prefix = ''.join(time_prefix_list) # convert back to str
    
    
    # substitution
    fuzzy_time = time_pattern(time_prefix)
    # print fuzzy_time.year, fuzzy_time.month, fuzzy_time.day, fuzzy_time.hour, fuzzy_time.minute, fuzzy_time.second
    
    fuzzy_targt_a = fuzzy_time.outto_tatget_a()
    fuzzy_targt_b = fuzzy_time.outto_tatget_b()
    fuzzy_target = fuzzy_targt_a + "|" + fuzzy_targt_b
    #print "Fuzzy target is " + fuzzy_target
    return fuzzy_target


    
def match_period(targetfile, start_time, end_time):
    
    fuzzy_target = get_fuzzy_target(start_time, end_time)
    
    tfile = open(targetfile)
    for line in tfile:
        pattern = re.compile(fuzzy_target)
        match = pattern.search(line)
        if match:
            #print match.group()
            return True
    tfile.close()
    return False
    
    
 
 
 
if __name__ == '__main__':
    print "test for match_period."
    print match_period(testfile, start_time, end_time)