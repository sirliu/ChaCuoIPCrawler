#! /usr/bin/python
# -*- coding:utf-8 -*-
import re
from typing import Any
from modules import iso_3166_1
from modules import country_ip_range
from modules import domestic_operator_ip_range
from modules import domestic_provinces_and_cities_ip_range
from modules import global_as
from modules import country_ip_list
from modules import company_ip_list
from modules import country_as_list

full_url_parser = {
    "http://ipblock.chacuo.net/": country_ip_range.Parser().parse,
    "http://ipcn.chacuo.net/": domestic_operator_ip_range.Parser().parse,
    "http://ips.chacuo.net/": domestic_provinces_and_cities_ip_range.Parser().parse,
    "http://ipblock.chacuo.net/list": country_ip_list.Parser().parse,
    "http://as.chacuo.net/": global_as.Parser().parse,
    "http://as.chacuo.net/company": company_ip_list.Parser().parse,
    "http://as.chacuo.net/list": country_as_list.Parser().parse,
    "http://doc.chacuo.net/iso-3166-1": iso_3166_1.Parser().parse
}

start_url_parser = {
    "http://ipcn.chacuo.net/view/i_": domestic_operator_ip_range.OperatorParser().parse,
    "http://ipblock.chacuo.net/view/c_": country_ip_range.CountryParser().parse,
    "http://ipblock.chacuo.net/down/t_txt=c_": country_ip_range.CountryIPRangeParser().parse,
    "http://ips.chacuo.net/view/s_": domestic_provinces_and_cities_ip_range.ProvinceParser().parse,
    "http://as.chacuo.net/companyview/s_": company_ip_list.CompanyParser().parse,
    "http://as.chacuo.net/as": global_as.ASParser().parse
}

regex_url_parser = {
    r"http://as.chacuo.net/[A-Z]{2}": global_as.CountryParser().parse
}


def find_parser(url: str) -> Any:
    if url in full_url_parser.keys():
        return full_url_parser[url]

    for start_url in start_url_parser.keys():
        if url.startswith(start_url):
            return start_url_parser[start_url]

    for regex_url in regex_url_parser.keys():
        if re.match(regex_url, url):
            return regex_url_parser[regex_url]
