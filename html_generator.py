# -*- coding: utf-8 -*-
# this module help to generate a html page to 
# display result files via html access
import os

class output_html:
    def __init__(self, outputid, title, start_time, end_time):
        self.id = outputid
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.links = []
        self.filename = "result-id-" + str(outputid) + ".html"
        
    def __del__(self):
        return

    def add_link(self,link_str):
        self.links.append(link_str)
        
        
    def generate_html(self, path):
        html_str = "<!DOCTYPE html><html><head><title>"
        html_str += self.title
        html_str += "</title></head><body>"
        html_str += "<h2>" + self.title + "</h2>"
        html_str += "<h4>Start-time: " + str(self.start_time) + "<br>End-time: " + str(self.end_time) +"</h4>"
        for link in self.links:
            html_str += "<a href=\"" + link + "\">" + link + "</a><br>"
        html_str += "</body></html>"
        
        self.htmlfile = file(os.path.join(path, self.filename), "w")
        self.htmlfile.write(html_str)
        self.htmlfile.close()



if __name__ == '__main__':
    print "test for html_generator."
    testobj = output_html(101, "test-title", "2016-03-01 10:23:49", "2016-03-01 10:23:49")
    testobj.add_link("main.py")
    testobj.add_link("html_generator.py")
    testobj.generate_html("")
    
    
