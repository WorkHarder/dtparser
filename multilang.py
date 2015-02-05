#!/usr/bin/python
#encoding:utf-8
#
import re


class Multilang_base():
    
    refer = """
        ##  month    shortmonth    translate
    """
        
class Multilang_fr(Multilang_base):

    refer = """
        ##  months_fr    shortmth_fr  short_mth_en
            janvier         janv         jan
            février         févr         feb
            mars            mars         mar
            avril           avril        apr
            mai             mai          may
            juin            juin         jun
            juillet         juli         jul
            août            août         aug
            septembre       sept         sep
            octobre         oct          oct
            novembre        nov          nov
            décembre        déc          dec
    """

class Multilang_ch(Multilang_base):

    refer = """
            year        年                         -
            month       月                         -
            day         日                         -
            """

class Multilang():
    
    #LangClass_list = [ Multilang_fr, Multilang_ch ]
    
    def __init__(self, langclass = []):
        if isinstance(langclass, list):
            pass
        else:
            langclass = [ langclass ]
        
        self.langrefdict = {}
        
        for cls in langclass:
            if isinstance(cls, str):
                cls = eval(cls)
            else:
                pass
            
            ref = cls().refer
            refer_list = [ re.sub("\s+", " ", i.strip()) for i in ref.split("\n") ]
            for r in refer_list:
                if r.startswith("#") or not r:
                    pass
                else:
                    rf_list = r.split()
                    self.langrefdict[ rf_list[ 1 ] ] = rf_list[ 2 ]
    
    def replace(self,datetimeStr):
        #print datetimeStr
        ptn = """%s[a-zA-Z]*"""
        for key,value in self.langrefdict.iteritems():
            datetimeStr = re.sub(ptn%key, value, datetimeStr)
        return datetimeStr

if __name__ == "__main__":
    mtl = Multilang(["Multilang_ch","Multilang_fr"])
    print mtl.replace("décembre février 年 月日")