import json
import re

def main():
    with open('replacedict.json') as data_file:    
        repl_dict = json.load(data_file)
        
    with open('somethingtoreplace.txt') as data_file:    
        str_file = data_file.read()

    for item,value in repl_dict.items():
        print '{} : {}'.format(item,value)
        searchObj = re.search(str_file,item,flags=0)
        if searchObj:
            print "searchObj.group() : ", searchObj.group()
            print "searchObj.group(1) : ", searchObj.group(1)
            print "searchObj.group(2) : ", searchObj.group(2)
    #print str_file

    #scientific_num = re.compile("^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$")


if __name__ == "__main__":
    main()
