from __future__ import print_function

sourceFile = open("sourcefile.txt", "r")         
document = sourceFile.read()                          

for i in range(len(document)):

    if (document[i].isalnum()):                    

        print(document[i], end = "")               

    else:

        if (document[i - 1].isalnum()):            

            print("\n" + document[i])
