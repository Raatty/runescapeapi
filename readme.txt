Help on module runescapeapi:

NAME
    runescapeapi

DESCRIPTION
    A slightly memes wrapper for the runescape api, hopefully helps people
    best way to contact me with any problems is on discord raatty#3522
    read the rest of the docs for module usage step one is
        import runescapeapi as runescape
    the code in here might not be done in the best way but everything you
    need should be there

CLASSES
    builtins.object
        Beasts
        Clan
        GrandExchange
        Highscores
        Player
    _Wikia(builtins.object)
        Rs3Wikia
        osrsWikia
    
    class Beasts(builtins.object)
     |  a bunch of methods for getting stats and seaching for monsters
     |  
     |  Static methods defined here:
     |  
     |  area_names()
     |      returns a list of area names
     |      usage:
     |          runescape.Beasts.area_names()
     |      it returns the same list every time so you should only need to call this
     |      once in your code
     |  
     |  by_area(area:str)
     |      returns a list of beasts in a specific area
     |      see runescape.Beasts.area_names() for the list
     |      usage:
     |          runescape.Beasts.by_area('Rat pits')
     |      gives you a list of all the  beasts in the rat pits
     |  
     |  by_category(cat)
     |      returns a list of monsters of a given slayer category
     |      input a category id as an int or a str of the category name
     |      searching by string will take longer tho
     |      see runescape.Beasts.category_names() for categorys
     |  
     |  by_id(id:int)
     |      returns stats and info about a beast by id
     |      usage:
     |          runescape.Beasts.by_id(47)
     |      returns information about level 1 rats
     |      to get the ids use runescape.Beasts.search(name)
     |  
     |  by_letter(letter:str)
     |      list of beasts starting with a letter
     |      usage:
     |          runescape.Beasts.by_letter('r')
     |      will give a list of all the beasts starting with 'r'
     |  
     |  by_level(lower_:int, upper_:int)
     |      returns a list of beasts within a given level range, takes
     |      two arguments both ints first argument is the lowest level
     |      you want to see and the second is the highest level
     |      you can use 1 for the first and a high number like 10000
     |      for the second to get a list of all the beasts
     |  
     |  by_weakness(weakness)
     |      returns a list of beasts with a given weakness, input a weakness
     |      id or a weakness name searching by name will take longer tho
     |      see runescape.Beasts.weakness_names() for weaknesses
     |  
     |  category_names()
     |      returns a list of slayer categorys
     |  
     |  search(query:str)
     |      searches the beast database for a name and returns a list seperate with +
     |      usage:
     |          runescape.Beasts.search('rat+cat')
     |      will give you a list of all the beasts that have rat or cat in their name
     |      also that gives you the id
     |  
     |  weakness_names()
     |      returns a list of weaknesses
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Clan(builtins.object)
     |  Gets a list of members in a clan
     |  usage:
     |  list(runescape.Clan('empire of elitez'))
     |  or
     |  for member in runescape.Clan('empire of elitez')
     |      #do stuff
     |  
     |  Methods defined here:
     |  
     |  __init__(self, clan:str)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __len__(self)
     |  
     |  adminish(self)
     |      will give a list of the adminish ranks in clan
     |      (the ones that kind of look like little badges like admin rank)
     |      usage:
     |      list(runescape.Clan('empire of elitez').adminish())
     |      or
     |      for member in runescape.Clan('empire of elitez').adminish():
     |          #do stuff
     |  
     |  bannanas(self)
     |      will give a list of the banana ranks in clan
     |      usage:
     |      list(runescape.Clan('empire of elitez').bananas())
     |      or
     |      for member in runescape.Clan('empire of elitez').bananas():
     |          #do stuff
     |  
     |  keys(self)
     |      will give a list of the key ranks in clan
     |      usage:
     |      list(runescape.Clan('empire of elitez').keys())
     |      or
     |      for member in runescape.Clan('empire of elitez').keys():
     |          #do stuff
     |  
     |  rank(self, rank:str)
     |      will give a list of the members with a specific rank in a clan
     |      usage:
     |      list(runescape.Clan('empire of elitez').rank('Owner'))
     |      or
     |      for member in runescape.Clan('empire of elitez').rank('Owner'):
     |          #do stuff
     |  
     |  stars(self)
     |      will give a list of the star ranks in clan
     |      usage:
     |      list(runescape.Clan('empire of elitez').stars())
     |      or
     |      for member in runescape.Clan('empire of elitez').stars():
     |          #do stuff
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  CLAN_MEM_URL = 'http://services.runescape.com/m=clan-hiscores/members_...
     |  
     |  CLAN_MOTIF_URL = 'http://services.runescape.com/m=avatar-rs/{}/clanmot...
    
    class GrandExchange(builtins.object)
     |  provides methods for fetching information about items in the grandexchange
     |  
     |  Static methods defined here:
     |  
     |  cat_count(id:int)
     |      tells you how many items there are for each letter in a category
     |      give the id from 0 to 37 check runescape.GrandExchange.CATEGORYS for ids
     |      usage:
     |          runescape.cat_count(12)
     |      will display the letter counts of the food and drink category
     |      yes thats where you can find cheese!
     |  
     |  graph(id:int)
     |      gets info on the prices over time
     |      usage:
     |          runescape.GrandExchange.graph(1985)
     |      that ^ will give you data plot points to create a graph
     |      of cheese over time
     |  
     |  item(id:int)
     |      gets information on a single item usage
     |      usage:
     |          runescape.GrandExchange.item(1985)
     |      that ^ will give you information about Cheese
     |  
     |  iter_category(category:int, page_sleep:int=0)
     |      iterates through an entire category in put an int from 0 to 37
     |      if you start getting errors use the second argument that is how many seconds
     |      to sleep between pages default is 0 whitch will be fine for short bursts
     |      anouther way to use this is:
     |      ge = [c for i in range(0,38) for c in runescape.GrandExchange.iter_category(i, 5)]
     |      to get the full grand exchange in one list, will take some time tho
     |      so its best to only be getting one category at a time
     |      regurlar usage:
     |          for i in runescape.GrandExchange.iter_category(12, 1):
     |              #do stuff
     |  
     |  iter_letter(letter:str, category:int, page_sleep:int=0)
     |      iterates through a letter (a-z or #(for number)) in a category
     |      see runescape.GrandExchange.CATEGORYS for categorys
     |      usage:
     |          for item in runescape.GrandExchange.iter_leter('c', 12, 1):
     |              #do stuff (find cheese maybe?)
     |      that loop will go through all the items in the food and drink
     |      category that start with the letter 'c' will also sleep for a second 
     |      each grand exchange page to be nice to the runescape servers and to reduce
     |      errors
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  CATEGORYS = {'ammo': 1, 'arrows': 2, 'bolts': 3, 'construction materia...
     |  
     |  LETTER_URL = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/...
    
    class Highscores(builtins.object)
     |  fetches highscores and gives em back as a list of dicts
     |  6 different types hiscore, hiscore_ironman, hiscore_hardcore_ironman
     |  'hiscore_oldschool', 'hiscore_oldschool_ironman',
     |  'hiscore_oldschool_ultimate
     |  this class takes two arguments rsn and type 'hiscore' is the default
     |  usage:
     |  person = runescape.Highscores('raatty', 'hiscore')
     |  or person = runescape.Highscores('raatty') would give same effect
     |  person.skills will give a list of skills in game order
     |  person.total will give you the total
     |  person.rsn in case you forget who you looked up
     |  
     |  Methods defined here:
     |  
     |  __init__(self, rsn:str, type_:str=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  skill(self, name)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  HIGHSCORES_URL = 'http://services.runescape.com/m={}/index_lite.ws?pla...
     |  
     |  SKILL_NAMES = {'Agility': 5, 'Attack': 1, 'Constitution': 2, 'Construc...
    
    class Player(builtins.object)
     |  will look up lots about a player
     |  the required argument is the rsn as a string but
     |  there is also a second argument auto_fetch which
     |  is of type bool, delfault is False but if it is
     |  True this class will auto maticly visit all the different
     |  links to get information but if its left blank or set
     |  to False the data will just be fetched as needed
     |  LookupError will be raised if the rsn does not exist
     |  usage:
     |      me = runescape.Player('raatty', True)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, rsn:str, auto_fetch:bool=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  alog(self)
     |      returns a list of all the activitys on a persons alog or
     |      an empty list for private people
     |      usage:
     |          me.alog()
     |  
     |  clan(self)
     |      returns the clan name if they are in one
     |      usage:
     |          me.clan()
     |  
     |  combat(self)
     |      returns the combat level either strait from
     |      runemetics or calculated from highscores for
     |      private people
     |      usage:
     |          me.combat()
     |  
     |  forum_pic(self)
     |      returns a url of the forum picture
     |      usage:
     |          me.forum_pic()
     |  
     |  overall_total(self)
     |      returns total level, total xp and rank
     |      usage:
     |          me.overall_total()
     |  
     |  quest(self, name)
     |      searches throught the quest list then returns the quest
     |      that matches that name
     |      usage:
     |          me.quest('rat catchers')
     |  
     |  quest_list(self)
     |      returns a list of all the quests and the lookuped players
     |      progree in them
     |      usage:
     |          me.quest_list()
     |  
     |  quest_summary(self)
     |      returns the counts of the started finished and not started quests
     |      or None for thease three values if they are private
     |      usage:
     |          me.quest_summary()
     |  
     |  rsn(self)
     |      will return the rsn of the looked up player
     |      correctly capitalised if their runemetics wasnt private
     |      usage:
     |          me.rsn()
     |  
     |  stats(self)
     |      returns a list of a persons levels
     |      usage:
     |          me.stats()
     |  
     |  title(self)
     |      returns the title and weather its a suffix
     |      usage:
     |          me.title()
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  CLAN_AND_TITLE_URL = 'http://services.runescape.com/m=website-data/pla...
     |  
     |  FORUM_PIC_URL = 'http://services.runescape.com/m=avatar-rs/{}/chat.png...
     |  
     |  RUNEMETRICS_BASE_URL = 'https://apps.runescape.com/runemetrics/'
     |  
     |  RUNE_METRICS_QUESTS_URL = 'https://apps.runescape.com/runemetrics/ques...
     |  
     |  RUNE_METRICS_URL = 'https://apps.runescape.com/runemetrics/profile/pro...
    
    class Rs3Wikia(_Wikia)
     |  methords for exploring the rs3 wikia
     |  
     |  Method resolution order:
     |      Rs3Wikia
     |      _Wikia
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _Wikia:
     |  
     |  isearch(self, searchTerm:str)
     |      returns a generator that iterates though the search results pages
     |  
     |  page(self, pageName:str)
     |      returns an instance of a wikia page
     |  
     |  search(self, searchTerm:str)
     |      just returns a list of search results from the wikia
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Wikia:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class osrsWikia(_Wikia)
     |  methods for exploring the osrs wikia
     |  
     |  Method resolution order:
     |      osrsWikia
     |      _Wikia
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _Wikia:
     |  
     |  isearch(self, searchTerm:str)
     |      returns a generator that iterates though the search results pages
     |  
     |  page(self, pageName:str)
     |      returns an instance of a wikia page
     |  
     |  search(self, searchTerm:str)
     |      just returns a list of search results from the wikia
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _Wikia:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    BASE_URL = 'http://services.runescape.com/'

