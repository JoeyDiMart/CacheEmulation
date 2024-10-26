'''
Name: Joseph DiMartino
Program: Program 011 - Cache class
Date: 10.24.24


The Cache class contains functions to get blocks from main memory to cache. This is where the Hash Map is set
'''

class Cache:

    def __init__(self, num_blocks, words_per_block, cache_list=None):
        self._num_blocks = num_blocks
        self._words_per_block = words_per_block
        if cache_list is not None:
            self._cache_list = cache_list
        else:
            self._cache_list = self._num_blocks * ["---"]

    def get_num_blocks(self):
        return self._num_blocks
    def set_num_blocks(self, num_blocks):
        self._num_blocks = num_blocks

    def get_cache_list(self):
        return self._cache_list
    def set_cache_list(self, new_cache_list):
        self._cache_list = new_cache_list

    def get_words_per_block(self):
        return self._words_per_block
    def set_words_per_block(self, words_per_block):
        self._words_per_block = words_per_block

    num_blocks = property(get_num_blocks, set_num_blocks)
    words_per_block = property(get_words_per_block, set_words_per_block)
    cache_list = property(get_cache_list, set_cache_list)


    def findBlockNum(self, bin_num, TBO):  # this should be in Cache class
        place = 0
        block = 0
        for k in bin_num[-1:-TBO[1]-1:-1]:  # TBO[0] is tag, TBO[1] is block, iterate from end of tag to end of block
            block += int(k) * (2**place)
            place += 1
        return block

    def toCache(self, instruction, bin_num, TBO):
        block_num = self.findBlockNum(bin_num[0:TBO[0]+TBO[1]], TBO)
        self.cache_list[block_num] = instruction
        return ""

    def __str__(self):
        return " ".join(self.cache_list)






