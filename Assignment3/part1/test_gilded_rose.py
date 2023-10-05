# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_Conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].quality)

    def test_Conjured_item_after_sellby(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

    def test_Backstage_passes_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 14, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(23, items[0].quality)

    def test_Backstage_passes_increase_more_10d_(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(24, items[0].quality)

    def test_Backstage_passes_increase_more_5d_(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(25, items[0].quality)

    def test_Backstage_passes_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 22)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_never_negative(self):
        items = [Item("Elixir of the Mongoose", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_never_50_more(self):
        items = [Item("Aged Brie", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_decrease_twice_after_sellby(self):
        items = [Item("+5 Dexterity Vest", 0, 24)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(22, items[0].quality)

    def test_Sulfuras_unchanged(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)


if __name__ == "__main__":
    unittest.main()
