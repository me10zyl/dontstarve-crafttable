#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Item:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def get_detail_list(self, thing, detail, new_list):
        for item in thing.items:
            if len(item.items) > 0 and detail:
                self.get_detail_list(item, detail, new_list)
            else:
                new_list.append(item.name)
        return new_list

    def print_items(self, detail=True):
        detail_list = self.get_detail_list(self, detail, [])
        new_list = []
        names = {}
        for item in detail_list:
            if item in names:
                names[item] += 1
            else:
                names[item] = 1
        for name in names:
            if names[name] == 1:
                new_list.append(name)
            else:
                new_list.append(name + '*' + str(names[name]))
        print self.name + " =",
        for item in new_list:
            print item,
        print '\n'

    def combine(self, obj):
        self.name = self.name + ' + ' + obj.name;
        self.items.extend(obj.items)
        return self

class Stone(Item):
    def __init__(self):
        Item.__init__(self, '石头')


class Gold(Item):
    def __init__(self):
        Item.__init__(self, '金子')


class Log(Item):
    def __init__(self):
        Item.__init__(self, '木头')


class Brick(Item):
    def __init__(self):
        Item.__init__(self, '石砖', [Stone(), Stone(), Stone()])


class Electron(Item):
    def __init__(self):
        Item.__init__(self, '电子元件', [Brick(), Gold()])


class Science2(Item):
    def __init__(self):
        Item.__init__(self, '炼金术引擎',
                      [Plank(), Plank(), Plank(), Plank(), Brick(), Brick(), Gold(), Gold(), Gold(), Gold(), Gold(),
                       Gold()])


class Plank(Item):
    def __init__(self):
        Item.__init__(self, '木板', [Log(), Log(), Log(), Log()])


class Science(Item):
    def __init__(self):
        Item.__init__(self, '科学仪器', [Gold(), Log(), Log(), Log(), Log(), Stone(), Stone(), Stone(), Stone()])


brick = Brick()
electron = Electron()
science = Science()
science2 = Science2()


science.print_items()
science2.print_items()
science2.combine(science).print_items()
