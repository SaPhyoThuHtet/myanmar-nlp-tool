import sys
import re

#Infix to Postfix
#A Part of Compiler
# 13.10.2020(TUE) Modified:
# Stay At Home (Covid-19)

with open(sys.argv[1],'r') as input_file:
    for input_data in input_file:
        print("InFix:",input_data.strip())
        input_data =  re.sub(r"\s",r"", input_data.strip())

        #Infix to Postfix
        output_data =  re.sub(r"(([\+\*\/\-])([0-9]+))",r"\3\2",input_data)
        print("PostFix:", output_data.strip())
        print()
