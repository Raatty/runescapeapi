import wikia
import requests

BASE_URL = 'http://services.runescape.com/'


class highScores:
    def __init__(self, rsn):
        pass


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
        '''subclass this fuction so you dont need to put the wiki augument in all the time'''
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
