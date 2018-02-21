import zipfile, os, sys, csv

#this script will open every zip file in a directory, extract it's csv and strip column's (maxlinenum) and combine into single csv (outputfile)

directory = "d:\customreports\\" # windows directory location where files sit
maxlinenum = 14 # amount of lines to skip in each csv that is unpackaged from zip
outputfile = "d:\customreports\webreportmaster.csv" # location and name of master output csv

i = 0

fout = open(outputfile,"a")
for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        with zipfile.ZipFile(filename,"r") as zip_ref:
            archive = zip_ref.namelist()
            zip_ref.extractall(directory)
            src = str(directory +  archive[0])
            
            f = open(src)
            linenum = 0
            for line in f:
                if(linenum > maxlinenum):
                    fout.write(line)
                linenum = linenum +1    
            f.close
            
        print(filename + " has been extracted")
fout.close()
