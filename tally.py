# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:11:19 2020

@author: ychen
"""
import numpy as np

#open the mcnp output file as the input file to python
input_file=open("outy","r")

#make a blank memory space 180 lists of 1000 energy groups in a list-of-lists
angular_dependent_spectra = []
angular_dependent_spectra_uncertainties = []
energylist=np.zeros(1001)

# check if a string can be converted into float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for i in range(0,180):
    temporary_line = []
    for item in range(0,1001):
        temporary_line.append( 0.0 )
    angular_dependent_spectra.append( temporary_line.copy() )
    angular_dependent_spectra_uncertainties.append( temporary_line.copy() )

while 1 :
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
    if(temporary_line_split[:1]==['cell']):
        if(is_number(temporary_line_split[1])==True):
            angle=int(temporary_line_split[1])-1000
            # skip current line
            input_file.readline()
            # read tallies and uncertainties
            for i in range (0,1001):
                temp_line=input_file.readline()
                temp_line_split=temp_line.split()
                energylist[i]=temp_line_split[0]
                angular_dependent_spectra[angle][i]=float(temp_line_split[1])
                angular_dependent_spectra_uncertainties[angle][i]=float(temp_line_split[2])
        
# input_file.close()        

#now you should have read through the file. If it is a large file with many PRDMP's
#this routine will continually overwrite with the newest output update.
#your arrays, lists of lists, will be populated.
# now you can output

angle_list=list(range(180))
output_angle_string = str(angle_list)

output_file_string1 = ""
output_file1=open("angular_dependent_spectra.csv","w")
output_file_string1 += "energy"
output_file_string1 += ","
output_file_string1 += " "
output_file_string1 += ","
output_file_string1 += "angle"
output_file_string1 += ","
for angle in range(0,180):
    output_file_string1 += str(angle)
    output_file_string1 += ","
output_file_string1 += "\n"

for energy in range(0,1001):
    output_file_string1 += str(energylist[energy])
    output_file_string1 += ','
    output_file_string1 += " "
    output_file_string1 += ","
    output_file_string1 += " "
    output_file_string1 += ","
    for angle in range(0,180):
        output_file_string1 += str(angular_dependent_spectra[angle][energy])
        output_file_string1 += ","
    output_file_string1 += "\n"

output_file1.write(output_file_string1)     
output_file1.close()
# Open a csv file for the values
# Write the string
# Close values csv file 

output_file_string2 = ""
output_file2=open("angular_dependent_spectra_uncertainties.csv","w")
output_file_string2 += "energy"
output_file_string2 += ","
output_file_string2 += " "
output_file_string2 += ","
output_file_string2 += "angle"
output_file_string2 += ","
for angle in range(0,180):
    output_file_string2 += str(angle)
    output_file_string2 += ","
output_file_string2 += "\n"

for energy in range(0,1001):
    output_file_string2 += str(energylist[energy])
    output_file_string2 += ','
    output_file_string2 += " "
    output_file_string2 += ","
    output_file_string2 += " "
    output_file_string2 += ","
    for angle in range(0,180):
        output_file_string2 += str(angular_dependent_spectra_uncertainties[angle][energy])
        output_file_string2 += ","
    output_file_string2 += "\n"

output_file2.write(output_file_string2)
output_file2.close()

text_string = "SDEF PAR=p POS=0 0 0 RAD=D901 VEC=1 0 0 DIR=D999 ERG FDIR D888"
text_string += "\n"
text_string += "SI901 H 0.0 0.08"
text_string += "\n"
text_string += "SP901 -21 2"
text_string += "\n"
# text_string += "SI902 0.0 0.2"
# text_string += "\n"
# text_string += "SP902 0.0 1.0"
# text_string += "\n"


text_string += "SI999 A"
for i in range(0,180):
    text_string += " "
    a1=np.cos(np.deg2rad(i))
#    a1=1-1/180-2*i/180
#    a1=-1+i*2/180
    text_string += "{:.8e}".format(a1)
    if (i>1 and i%5==0):
        text_string += "\n"
        text_string += "       "
text_string += "\n"

text_string += "SP999"
text_string += "  "
for i in range (0,180):
    text_string += " "
    a2=np.sum(angular_dependent_spectra[179-i][:])
    text_string += "{:.8e}".format(a2)
    if (i>1 and i%5==0):
        text_string += "\n"
        text_string += "       "
text_string += "\n"

text_string += "SB999"
text_string += "  "
for i in range (0,181):
    text_string += " "
    b1=np.sum(10000*1+181-1)
    b2=1/b1
    if (i<165):
        text_string += "{:.8e}".format(b2)
    else:
        text_string += "{:.8e}".format(10000*b2)
    if (i>1 and i%5==0):
        text_string += "\n"
        text_string += "       "
text_string += "\n"

text_string += "DS888 S"
for i in range(0,180):
    text_string += " "
    text_string += str(180-i)
    if (i>1 and i%20==0):
        text_string += "\n"
        text_string += "       "

for i in range(0,180):
    text_string += "\n"
    text_string += "SI"
    text_string += str(i+1)
    text_string += " "
    text_string += "L"
    for j in range(0,900):
        text_string += " "
        text_string += str(energylist[j])
        if (j>1 and j%5==0):
            text_string += "\n"
            text_string += "      "
    text_string += "\n"
    text_string += "SP"
    text_string += str(i+1)
    text_string += "  "
    for j in range(0,900):
        text_string += " "
        a3=angular_dependent_spectra[i][j]
        text_string += "{:.8e}".format(a3)
        if (j>1 and j%5==0):
            text_string += "\n"
            text_string += "      "

#print(text_string)
output_file3=open("source.txt","w")
output_file3.write(text_string)
output_file3.close()