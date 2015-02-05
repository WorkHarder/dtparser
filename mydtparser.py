#!/usr/bin/python
#encoding:utf-8
#
import re
from datetime import datetime
from regexdepot import RegexDepot
from multilang import Multilang

class Parser():
    def __init__(self, langlist = []):
        """ language     langclass     for short
            French      Multilang_fr      fr
            Chinese     Multilang_ch      ch
        """
        self.rd = RegexDepot()
        clslist = []
        if langlist:
            clslist += [ "Multilang_" + short for short in langlist ]
        self.mtl = Multilang(clslist)
    
    def parse(self,datetimeStr):
        datetimeStr = datetimeStr.strip().lower()
        datetimeStr = re.sub("\xc2\xa0"," ",datetimeStr) ## unicode space
        if datetimeStr == "":
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            datetimeStr = self.mtl.replace(datetimeStr)
            date_str,date_fmt = self.parseDate(datetimeStr)
            time_str,time_fmt = self.parseTime(datetimeStr)
            #print date_str,date_fmt
            #print time_str,time_fmt
            try:
                dt = datetime.strptime(date_str+" "+time_str, date_fmt+" "+time_fmt)
                return dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                print datetimeStr,date_str, time_str
                return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
    def parseDate(self,datetimeStr):
        for rangeStr in self.rd.Date.keys():
            match = re.search(self.rd.Date[rangeStr], datetimeStr)
            if match:
                date_str = match.group().strip()
                for yr in [ "y", "Y" ]:
                    if match.group(yr):
                        rangeStr = rangeStr.replace("year",yr)
                for mth in [ "m", "b", "B" ]:
                    if match.group(mth):
                        rangeStr = rangeStr.replace("month",mth)
                for dy in [ "d" ]:
                    if match.group(dy):
                        rangeStr = rangeStr.replace("day",dy)
                shortList = rangeStr.split("_")
                #print shortList
                d1 = match.group("delimiter1")
                d2 = match.group("delimiter2")
                fmttuple = (shortList[0],d1,shortList[1],d2,shortList[2])
                #print fmttuple,match.group()
                date_fmt = "%{0}{1}%{2}{3}%{4}".format(*fmttuple)
                return date_str, date_fmt
            else:
                pass
        return datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d"

    def parseTime(self,datetimeStr):
        for rangeStr in self.rd.Time.keys():
            match = re.search(self.rd.Time[rangeStr], datetimeStr)
            if match:
                #print match.group(),"-"
                match_dict = match.groupdict()
                #print match_dict
                time_str = match.group().strip()
                if isinstance(match_dict["addition"], str):
                    if "pm" in match_dict["addition"]:
                        hr = eval(match_dict["H"])+12
                        if hr == 24:
                            hr = 0
                        time_str = time_str.replace(match_dict["H"],str(hr),1)
                else:
                    match_dict["addition"] = ""

                if isinstance(match_dict["S"], str):
                    time_fmt = "%{0}{1}%{2}{3}%{4}".format("H",match_dict["delimiter1"],
                                "M",match_dict["delimiter2"],"S") + match_dict["addition"]
                else:
                    time_fmt = "%{0}{1}%{2}".format("H",match_dict["delimiter1"],
                                                     "M") + match_dict["addition"]
                return time_str,time_fmt
            else:
                pass
        return datetime.now().strftime("%H:%M:%S"), "%H:%M:%S"

if __name__ == "__main__":
    dtp = Parser(langlist = ["ch","fr"])
    #print dtp.parse("October 05, 2012")
    #"""
    with open("./date_list","r") as f:
        with open("./date_test.txt","w") as g:
            for l in f:
                rst = dtp.parse(l)
                g.write(rst + "\t" + l + "\n")
    #"""