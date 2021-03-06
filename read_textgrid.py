# -*- coding:utf-8 -*-
import textgrids
import pympi.Praat as prt
import os


def parse_textgrid(filepath, tier_num):
    ptg = prt.TextGrid(file_path=filepath)
    itv = ptg.get_tier(name_num=tier_num).get_intervals()
    itv = list(itv)
    return itv


fp_chk = r".\tg_chked\smcs0127.TextGrid"
fp_ori = r".\tg_ori\smcs0127.TextGrid"

t1 = parse_textgrid(fp_ori, 3)
t2 = parse_textgrid(fp_chk, 3)
print(os.path.basename(fp_ori), "Interval num:", len(t1), sep=" ")
print(os.path.basename(fp_chk), "Interval num:", len(t2), sep=" ")
print("Max num of intervals:", max(len(t1), len(t2)), sep=" ")

for i in range(max(len(t1), len(t2))):
    # print("Original:", t1[i][2], "; Modified:", t2[i][2])
    try:
        if t1[i][2] != t2[i][2]:
            print("Original:", t1[i][2], "; Modified:", t2[i][2])
    except IndexError:
        print("IndexError: the number of intervals are not identical")

# ptg = prt.TextGrid(file_path=fp_ori)
# tiernames = list(ptg.get_tier_name_num())
# print(tiernames)
# print(list(ptg.get_tier(name_num=2).get_intervals()))


# tg_chk = textgrids.TextGrid(read_file=fp_chk)
# tg = textgrids.TextGrid(read_file=fp_ori)
