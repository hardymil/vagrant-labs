# -*- coding: utf-8 -*-

#import panda as pd 
import os

TEST_PATH = "Setup.Lst"

print("stating to read ...")

# =============================================================================
# with open(TEST_PATH, "r", encoding="utf-8") as f:
#     for line in f :
#         print(line)
#         dir(line)
# =============================================================================

file = open(TEST_PATH, "r", encoding="utf-8")

lines = file.readlines()
file.close()

for line in lines :
         print(line)


print("Directory contents:")

for f in os.listdir():
    print(f)