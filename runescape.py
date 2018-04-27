import wikia
import requests
from operator import attrgetter

BASE_URL = 'http://services.runescape.com/'


class highScores:
    '''3 types hiscore, hiscore_ironman, hiscore_hardcore_ironman'''
    HIGHSCORES_URL = BASE_URL + 'm={}/index_lite.ws?player={}'
    SKILL_NAMES = {'Total': 0, 'Attack': 1, 'Defence': 7, 'Strength': 4,
                   'Constitution': 2, 'Ranged': 10, 'Prayer': 13,
                   'Magic': 16, 'Cooking': 12, 'Woodcutting': 18,
                   'Fletching': 17, 'Fishing': 9, 'Firemaking': 15, 
                   'Crafting': 14, 'Smithing': 6, 'Mining': 3,
                   'Herblore': 8, 'Agility': 5, 'Thieving': 11,
                   'Slayer': 20, 'Farming': 21, 'Runecrafting': 19,
                   'Hunter': 23, 'Construction': 22, 'Summoning': 24,
                   'Dungeoneering': 25, 'Divination': 26, 'Invention': 27}
    def _fetch(self, rsn, type):
        url = self.HIGHSCORES_URL.format(type, rsn.replace(' ', '+'))
        fetched_scores = requests.get(url).text
        levels = []
        for row in fetched_scores.split('\n'):
            for col in row.split(' '):
                if len(levels) <= 27:
                    levels.append(col)
        for index, lvl in enumerate(levels):
            lvl_split = lvl.split(',')
            yield {'level': lvl_split[1], 'xp': lvl_split[2], 'rank': lvl_split[0], 'id': index, 'name': list(self.SKILL_NAMES.keys())[index]}

    def __init__(self, rsn: str, type: str = None):
        self.rsn = rsn
        if type is None:
            self.type = 'hiscore'
        else:
            if type in ['hiscore', 'hiscore_ironman', 
                        'hiscore_hardcore_ironman']:
                self.type = type
            else:
                raise AttributeError
        self.skills =  list(self._fetch(self.rsn, self.type))
        self.total = self.skills[0]
        self.skills = sorted(self.skills[1:], key=lambda x: list(self.SKILL_NAMES.values())[x['id']])


class player:
    def __init__(self, rsn: str, auto_fetch: bool):
        pass


class clan:
    CLAN_MEM_URL = BASE_URL + 'm=clan-hiscores/members_lite.ws?clanName={}'

    def __init__(self, clan: str):
        self.name = clan
        self.members = requests.get(self.CLAN_MEM_URL.format(clan.replace(' ', '+'))).content.replace(b'\xa0', b' ').decode('ascii').split('\n')[1:-1]

    def __iter__(self):
        for member in self.members:
            member = member.split(',')
            yield {'rsn': member[0], 'rank': member[1], 'clanxp': member[2], 'kills': member[3]}

    def __len__(self):
        return len(self.members)

    def keys(self):
        for i in self.members:
            keyRanks = ['Owner', 'Deputy Owner', 'Overseer']
            i = i.split(',')
            if i[1] in keyRanks:
                yield {'rsn': i[0], 'rank': i[1], 'clanxp': i[2], 'kills': i[3]}

    def adminish(self):
        for i in self.members:
            adminishRanks = ['Coordinator', 'Organiser', 'Admin']
            i = i.split(',')
            if i[1] in adminishRanks:
                yield {'rsn': i[0], 'rank': i[1], 'clanxp': i[2], 'kills': i[3]}

    def stars(self):
        for i in self.members:
            starRanks = ['General', 'Captain', 'Lieutenant']
            i = i.split(',')
            if i[1] in starRanks:
                yield {'rsn': i[0], 'rank': i[1], 'clanxp': i[2], 'kills': i[3]}

    def bannanas(self):
        for i in self.members:
            bananaRanks = ['Sergeant', 'Corporal', 'Recruit']
            i = i.split(',')
            if i[1] in bananaRanks:
                yield {'rsn': i[0], 'rank': i[1], 'clanxp': i[2], 'kills': i[3]}

    def rank(self, rank: str):
        for i in self.members:
            i = i.split(',')
            if i[1] == rank:
                yield {'rsn': i[0], 'rank': i[1], 'clanxp': i[2], 'kills': i[3]}


class _wikia:
    def __init__(self, wiki: str):
        self.wiki = wiki

    def page(self, pageName: str):
        '''returns an instance of a wikia page'''
        return wikia.page(self.wiki, pageName)

    def search(self, searchTerm: str):
        '''just returns a list of search results from the wikia'''
        return wikia.search(self.wiki, searchTerm)

    def isearch(self, searchTerm: str):
        '''returns a generator that iterates though the search results pages'''
        for i in wikia.search(self.wiki, searchTerm):
            yield wikia.page(self.wiki, i)


osrsWikia = _wikia('2007runescape')
rs3Wikia = _wikia('runescape')


class beasts:
    pass


class grandExchange:
    pass
