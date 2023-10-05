# -*- coding: utf-8 -*-


class Item:
    """DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def _increase_quality(self, item, amount=1):
        item.quality = min(item.quality + amount, 50)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(item.quality - amount, 0)

    def _is_conjured(self, item):
        return "Conjured" in item.name

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._increase_quality(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._increase_quality(item)
                if item.sell_in <= 10:
                    self._increase_quality(item)
                if item.sell_in <= 5:
                    self._increase_quality(item)
                if item.sell_in <= 0:
                    item.quality = 0

            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass

            elif self._is_conjured(item):
                self._decrease_quality(item, 2)
                if item.sell_in <= 0:
                    self._decrease_quality(item, 2)

            else:
                self._decrease_quality(item)
                if item.sell_in <= 0:
                    self._decrease_quality(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

    # def update_quality(self):
    #     for item in self.items:
    #         if (
    #             item.name != "Aged Brie"
    #             and item.name != "Backstage passes to a TAFKAL80ETC concert"
    #         ):
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1
