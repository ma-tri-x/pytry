import json
import re

with open('replacedict.json') as data_file:    
    repl_dict = json.load(data_file)
    
with open('somethingtoreplace.txt') as data_file:    
    str_file = data_file.read()

print repl_dict[0]
print str_file

scientific_num = re.compile("^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$")
bla