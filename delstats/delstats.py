""" del stats - class collection """
# -*- coding: utf-8 -*-
import logging
import requests
from bs4 import BeautifulSoup
import re


def parse_number_with_guess_for_separator_chars(number_str: str, max_val=None):
    """
    Tries to guess the thousands and decimal characters (comma or dot) and converts the string number accordingly.
    The return also indicates if the correctness of the result is certain or uncertain
    :param number_str: a string with the number to convert
    :param max_val: an optional parameter determining the allowed maximum value.
                     This helps prevent mistaking the decimal separator as a thousands separator.
                     For instance, if max_val is 101 then the string '100.000' which would be
                     interpreted as 100000.0 will instead be interpreted as 100.0
    :return: a tuple with the number as a float an a flag (`True` if certain and `False` if uncertain)
    """
    pattern_comma_thousands_dot_decimal = re.compile(r'^[-+]?((\d{1,3}(,\d{3})*)|(\d*))(\.|\.\d*)?$')
    pattern_dot_thousands_comma_decimal = re.compile(r'^[-+]?((\d{1,3}(\.\d{3})*)|(\d*))(,|,\d*)?$')
    pattern_confusion_dot_thousands = re.compile(r'^(?:[-+]?(?=.*\d)(?=.*[1-9]).{1,3}\.\d{3})$')  # for numbers like '100.000' (is it 100.0 or 100000?)
    pattern_confusion_comma_thousands = re.compile(r'^(?:[-+]?(?=.*\d)(?=.*[1-9]).{1,3},\d{3})$')  # for numbers like '100,000' (is it 100.0 or 100000?)

    number_str = number_str.strip().lstrip('0')
    certain = True
    if pattern_confusion_dot_thousands.match(number_str) is not None:
        number_str = number_str.replace('.', '')  # assume dot is thousands separator
        certain = False
    elif pattern_confusion_comma_thousands.match(number_str) is not None:
        number_str = number_str.replace(',', '')  # assume comma is thousands separator
        certain = False
    elif pattern_comma_thousands_dot_decimal.match(number_str) is not None:
        number_str = number_str.replace(',', '')
    elif pattern_dot_thousands_comma_decimal.match(number_str) is not None:
        number_str = number_str.replace('.', '').replace(',', '.')
    else:
        raise ValueError()  # For stuff like '10,000.000,0' and other nonsense

    number = float(number_str)
    if not certain and max_val is not None and number > max_val:
        number *= 0.001  # Change previous assumption to decimal separator, so '100.000' goes from 100000.0 to 100.0
        certain = True  # Since this uniquely satisfies the given constraint, it should be a certainly correct interpretation

    return number # , certain


def value_convert(value):
    """ convert value to flot """
    unit = None

    try:
        value, unit = value.split(' ', 1)
    except Exception:
        pass

    try:
        value = parse_number_with_guess_for_separator_chars(value)
    except Exception:
        pass

    return value, unit

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
                stat_dic[cols[1]][header_list[idx]] = {'title': header_decription_list[idx], 'value': value_convert(col)}

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

        def all(self):
            """ get all statistics """
            self.logger.debug('Delstats.Teamstats.all()')

            # return output_dic

        def defensive(self):
            """ get shot statistic """
            self.logger.debug('Delstats.Teamstats.paesse()')
            html = url_get(self.logger, f'{self.teamstats_url}/defensive')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def paesse(self):
            """ get pass statistics """
            self.logger.debug('Delstats.Teamstats.paesse()')
            html = url_get(self.logger, f'{self.teamstats_url}/paesse')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def puckbesitz(self):
            """ get pass statistics """
            self.logger.debug('Delstats.Teamstats.puckbesitz()')
            html = url_get(self.logger, f'{self.teamstats_url}/puckbesitz')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def schuesse(self):
            """ get shot statistic """
            self.logger.debug('Delstats.Teamstats.schuesse()')
            html = url_get(self.logger, f'{self.teamstats_url}/schuesse')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def specialteams(self):
            """ get shot statistic """
            self.logger.debug('Delstats.Teamstats.specialteams()')
            html = url_get(self.logger, f'{self.teamstats_url}/special-teams')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def strafen(self):
            """ get teamplay statistic """
            self.logger.debug('Delstats.Teamstats.strafen()')
            html = url_get(self.logger, f'{self.teamstats_url}/strafen')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def teamplay(self):
            """ get teamplay statistic """
            self.logger.debug('Delstats.Teamstats.teamplay')
            html = url_get(self.logger, f'{self.teamstats_url}/team-play')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)

        def zuschauer(self):
            """ get teamplay statistic """
            self.logger.debug('Delstats.Teamstats.zuschauer')
            html = url_get(self.logger, f'{self.teamstats_url}/zuschauer')
            # html = file_load('files/paesse.html')
            return content_parse(self.logger, html)
