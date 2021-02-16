# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:07:14 2020

@author: ychen
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:39:37 2020

@author: ychen
"""

import numpy as np

#open the mcnp output file as the input file to python
input_file=open("surface3_f2.txt","r")

spectra = []
spectra_uncertainties = []
energylist=np.zeros(50)

# check if a string can be converted into float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

temporary_line = []
for item in range(0,50):
    temporary_line.append( 0.0 )
spectra.append( temporary_line.copy() )
spectra_uncertainties.append( temporary_line.copy() )

while 1 :
    input_file.readline()[65150:]
    # read a single line
    temporary_line = input_file.readline()
    # if we've gotten to the end of the file and there's nothing left, even a blank line with an endline character will have length of 1
    if( len(temporary_line) < 1 ) :
        print( 'found an end of file condition and will break' )
        break
    #split that line of characters at the whitespace
    temporary_line_split = temporary_line.split()
    
    #now you will have a list of items

    # #check to see if the first, second, third list item has any of the keywords for an f* tally.
    if(temporary_line_split[:1]==['surface']):
        if(is_number(temporary_line_split[1])==True):
            # skip current line
            input_file.readline()
            # read tallies and uncertainties
            for i in range (0,50):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                energylist[i]=temp_line_split[0]
                spectra[0][i]=float(temp_line_split[1])
                spectra_uncertainties[0][i]=float(temp_line_split[2])
        
input_file.close()

text_string = ""
for i in range(0,180):
    text_string += "\n"
    text_string += "SI"
    text_string += str(i+1)
    text_string += " "
    text_string += "L"
    for j in range(0,50):
        text_string += " "
        text_string += str(energylist[j])
        if (j>1 and j%5==0):
            text_string += "\n"
            text_string += "      "
    text_string += "\n"
    text_string += "SP"
    text_string += str(i+1)
    text_string += "  "
    for j in range(0,50):
        text_string += " "
        a3=spectra[0][j]
        text_string += "{:.8e}".format(a3)
        if (j>1 and j%5==0):
            text_string += "\n"
            text_string += "      "

output_file3=open("source_n.txt","w")
output_file3.write(text_string)
output_file3.close()

print(spectra)