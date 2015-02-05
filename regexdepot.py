#!/usr/bin/python
#encoding:utf-8
#
import re

class RegexDepot():
    def __init__(self):
        pass
    
    Date_mdy  = r"""
                    (\s?|^)                                                     ## begin with space or match the head of string
                    (
                        (?P<b>[a-zA-Z]{3})|(?P<B>[a-zA-Z]{4,10})|               ## month as word
                        (?P<m>1[0-2]|(0?[1-9]))                                   ## month as num
                    )
                    (?P<delimiter1>(\s|/){1,3})                                 ## delimiter1
                    (?P<d>([1-2][0-9]|3[0-1]|0?[1-9]))                            ## day
                    (?P<delimiter2>([a-zA-Z]{2})?(\s|/|,){1,3})                 ## delimiter2
                    ((?P<Y>\d{4})|(?P<y>\d{2}))                                 ## year
                """
    
    Date_ymd = r"""
                    (\s?|^)                                                     ## 
                    ((?P<Y>\d{4})|(?P<y>\d{2}))                           ## year
                    (?P<delimiter1>(-|/){1,3})                                  ## delimiter1
                    (
                        (?P<b>[a-zA-Z]{3})|(?P<B>[a-zA-Z]{4,10})|
                        (?P<m>(1[0-2]|0?[1-9]))
                    )
                    (?P<delimiter2>(-|/){1,3})                                  ## delimiter2
                    (?P<d>([1-2][0-9]|3[0-1]|0?[1-9]))                            ## day
                """
    
    Date_dmy = r"""
                    (\s?|^)
                    (?P<d>([1-2][0-9]|3[0-1]|0?[1-9]))
                    (?P<delimiter1>([a-zA-Z]{2})?(\s){1,3})
                    (
                        (?P<b>[a-zA-Z]{3})|(?P<B>[a-zA-Z]{4,10})|
                        (?P<m>(1[0-2]|0?[1-9]))
                    )
                    (?P<delimiter2>(\s){1,3})
                    ((?P<Y>\d{4})|(?P<y>\d{2}))
                """
    
    Date = { 
                "month_day_year": re.compile(Date_mdy, re.VERBOSE), 
                "year_month_day": re.compile(Date_ymd, re.VERBOSE),
                "day_month_year": re.compile(Date_dmy, re.VERBOSE)
             }
    
    Time_HMS = r"""
                    (\s?|^)
                    (?P<H>(1[0-9]|2[0-3]|[0-9]))
                    (?P<delimiter1>:\s?)
                    (?P<M>([0-5][0-9]|[0-9]))
                    (
                        (?P<delimiter2>:\s?)
                        (?P<S>([0-9]|[0-5][0-9]))
                    )?
                    (?P<addition>,?\s?(pm|am))?
                """
    Time = { "hour_minute_second": re.compile(Time_HMS, re.VERBOSE)}

