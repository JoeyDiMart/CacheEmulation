'''
Name: Joseph DiMartino
Program: Program 3 - CPU Class
Date: 10.24.24
Subroutines: hitRate(), clearCache()
'''
from Cache import Cache

class CPU:
    def __init__(self, cache=None, hits=0, hit_rate=0.0):
        self._hits = hits
        self._hit_rate = hit_rate
        self.cache = cache

    def get_hits(self):
        return self._hits
    def set_hits(self, hits):
        self._hits = hits

    def get_hit_rate(self):
        return self._hit_rate
    def set_hit_rate(self, new_hit_rate):
        self._hit_rate = new_hit_rate

    hits = property(get_hits, set_hits)
    hit_rate = property(get_hit_rate, set_hit_rate)

    def clearCache(self):
        self.cache.set_cache_list(['---'] * self.cache.num_blocks)

    def deleteBlock(self, index):
        temp_list = self.cache.get_cache_list()
        temp_list[index] = '---'
        self.cache.set_cache_list(temp_list)

    def hitRate(self, instruction, instruction_count, bin_num, TBO):
        block_num = self.cache.findBlockNum(bin_num[0:TBO[0]+TBO[1]], TBO)
        if self.cache.get_cache_list()[block_num] == instruction:
            self.hits += 1
            self.set_hit_rate(self.hits / instruction_count)
        return self.hit_rate