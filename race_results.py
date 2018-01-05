class Race(object):
    """Holds the whole race"""

    def __init__(self, racename):
        self.racename = racename
        self.categories = []

    def list_categories(self):
        for cat in self.categories:
            print(cat)

    def add_category(self, category):
        self.categories.append(category)

    def num_categories(self):
        return len(self.categories)

    def num_racers(self):
        ret = 0
        for cat in self.categories:
            ret += cat.num_racers()
        return ret

class Category(object):
    """Defines a result category"""

    def __init__(self, name):
        self.name = name
        self.racers = []

    def __str__(self):
        ret = 'Category %s (%d racers)' % (self.name, self.num_racers())
        return ret

    def list_racers(self):
        for racer in self.racers:
            print(racer)

    def add_racer(self, racer):
        self.racers.append(racer)

    def num_racers(self):
        return len(self.racers)

class Racer(object):
    """Defines a racer and results"""

    def __init__(self, bib, firstname, lastname, status):
        self.bib = bib
        self.firstname = firstname
        self.lastname = lastname
        self.status = status if status else None
        self.time = None
        self.finish = None
        self.rank = None

    def __str__(self):
        ret = 'Racer %d - %s %s' % (self.bib, self.firstname, self.lastname)
        if self.status is not None:
            ret += ' - ' + self.status
        if self.time is not None:
            ret += ' - ' + self.time
        if self.finish is not None:
            ret += ' - ' + self.finish
        if self.rank is not None:
            ret += ' - ' + self.rank
        return ret

    def as_string_for_scoreboard(self):
        ret = ''
        if self.rank is not None:
            ret += self.rank + ' '
        ret += self.firstname + ' ' + self.lastname + ' ' + str(self.bib)
        ret += ' ' + self.time
        return ret

    def is_finisher(self):
        if not self.status and self.rank.isnumeric():
            return True
        return False
