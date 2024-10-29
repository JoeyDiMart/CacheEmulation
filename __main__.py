'''
Name: Joseph DiMartino
Program: Program 3 - emulating a cache memory
Date: 10.24.24
'''
import math
from Cache import Cache
from CPU import CPU
first_go = True

def bitsPerTBO(bits, num_words, max_blocks): # subroutine that returns a list showing how many bits for Tag, block, and offset
    word_size = len(bits)
    block_bits = int(math.log(max_blocks, 2))
    offset_bits = int(math.log(num_words, 2))
    tag_bits = word_size - (block_bits + offset_bits)
    TBO = [tag_bits, block_bits, offset_bits]
    return TBO

def toBinary(num): # convert hex to binary
    bin_num = ""
    bin_dict = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110",
        "F": "1111"
    } # use a dictionary since I don't need to convert any other base to binary except base 16
    for char in num:
        bin_num += bin_dict[char]
    return bin_num

def toDecimal(num, base=16):  # convert to decimal, default is hex to decimal
    p = 0
    total = 0  # count total
    for i in num[::-1]:  # go through number in reverse order
        total = total + base ** p * int(i)
        p += 1  # increase power
    total = str(total)
    return total # this was taken from my program 1

while True: # take user input to read any of 10 files
    input = int(input("Select a file number to scan through (0-9): "))
    if input in range(0, 10):
        break

file = open(f'sample{input}.txt', 'r') # open specific file
first_line = file.readline().strip().split(' ')  # put first line into a list without \n, split each element by the SPACE
num_words = int(first_line[0])
max_blocks = int(first_line[1])
cache = Cache(max_blocks, num_words)  # initialize a cache object
cpu = CPU(cache) # a CPU object


for j, i in enumerate(file, start=1):  # loop through starting from second line
    i = i.strip()  # remove \n
    if first_go: # only find Tag Block and Offset bits on the first line
        TBO = bitsPerTBO(toBinary(i), num_words, max_blocks)
        first_go = False


    if "CLEAR" in i:  # instruction to empty the cache
        cpu.clearCache()

    elif "DEL" in i:  # instruction to delete a specific block 
        split_i = (i.split(' '))
        cpu.deleteBlock(int(split_i[1]))

    else:  # add this decimal value to the cache in the specified block
        bin_num = toBinary(i)
        instruction = toDecimal(bin_num[0:TBO[0]+TBO[1]] + ("0" * TBO[2]), 2)
        cpu.hitRate(instruction, j, bin_num, TBO)
        cache.toCache(instruction, bin_num, TBO)

    if j % 100 == 0: # print every 100th instruction
        #print(f"Hits - {cpu.hits} \nMisses - {j-cpu.hits}")
        print(f"Instruction # - {j} \nH - {cpu.hit_rate:.3f}\n{cache}\n")
