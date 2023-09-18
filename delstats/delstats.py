""" del stats - class collection """
# -*- coding: utf-8 -*-
import logging
import requests
from bs4 import BeautifulSoup


def file_load(file_name):
    """ load file """
    with open(file_name, 'r', encoding='utf8') as fobj:
        content = fobj.read()

    return content


def url_get(logger, url):
    """ get url """
    logger.debug('url_get(%s)', url)

    req = requests.get(url, verify=False, timeout=20)
    if req.status_code == 200:
        html = req.text
    else:
        html = None

    return html


def logger_setup(debug):
    """ setup logger """
    if debug:
        log_mode = logging.DEBUG
    else:
        log_mode = logging.INFO

    # define standard log format
    # log_format = '%(message)s'
    log_format = '%(asctime)s - delstats - %(levelname)s - %(message)s'
    logging.basicConfig(
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S",
        level=log_mode)
    logger = logging.getLogger('delstats')
    return logger


def content_parse(logger, content):
    """ parse content """
    logger.debug('content_parse()')

    soup = BeautifulSoup(content, 'lxml')
    table = soup.find('table', attrs={'class': 'table table-hover table-thead-color table-standings table-standings--full'})

    # parse header
    _header_list = table.findAll("th")
    header_list = []
    header_decription_list = []
    for ele in _header_list:
        try:
            header_decription_list.append(ele['title'])
        except Exception:
            header_decription_list.append('')
        header_list.append(ele.text.strip())

    # parse rows into an dictionary to be returned
    stat_dic = {}
    for row in table.findAll("tr"):
        cols = row.findAll("td")
        cols = [ele.text.strip() for ele in cols]

        if len(cols) > 0:
            stat_dic[cols[1]] = {}
            for idx, col in enumerate(cols):
                stat_dic[cols[1]][header_list[idx]] = {'title': header_decription_list[idx], 'value': col}

    logger.debug(f'content_parse() ended: {len(stat_dic.keys())} keys in dictionary')
    return stat_dic


class DelStats(object):
    """ main class """

    debug = False
    base_url = None
    stat_url = 'https://www.penny-del.org/statistik'
    saison = 'saison-2023-24'
    tournament = 'hauptrunde'

    def __init__(self, debug=False, stat_url=None, saison=None, tournament=None):
        self.logger = logger_setup(debug)
        if stat_url:
            self.stat_url = stat_url
        if saison:
            self.saison = None
        if tournament:
            self.tournament = tournament
        self.base_url = f'{self.stat_url}/{self.saison}/{self.tournament}'

    def __enter__(self):
        """ makes delstat a context manager """
        self.logger.debug('base_url is: %s', self.base_url)
        return self

    def __exit__(self, *args):
        """ cleanup method for context manager """

    def teamstats(self):
        """ initialize Teamstat class """
        return DelStats.Teamstats(self)

    class Teamstats(object):
        """ teamstat class """

        debug = False
        logger = None
        teamstats_url = None

        def __init__(self, outer_instance):
            self.logger = logger_setup(outer_instance.debug)
            self.teamstats_url = f'{outer_instance.base_url}/teamstats'

        def paesse(self):
            """ get paesse statistics """
            self.logger.debug('Delstats.Teamstats.paesse()')
            html = url_get(self.logger, f'{self.teamstats_url}/paesse')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)
