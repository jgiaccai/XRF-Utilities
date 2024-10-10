#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:56:20 2023

@author: jennifergiaccai

Reads in all *.csv files from NMAA Tracer in a folder and converts to a *.txt file in the same folder
"""

import os
import fnmatch
import csv

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.csv'):
        fullFilename = file
        filename = file[:-4]
        print(filename)
        
        with open(fullFilename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            Data = []
            for row in csv_reader:
                if line_count >= 11 and line_count <1035:
                    Data.append(int(row[2]))
                    line_count += 1
                elif line_count == 1035:
                    break
                else:
                    line_count += 1
  
        #print(Data)      
        with open(filename+'.txt', mode='w+') as f:
            f.write('BeginHeader'+'\r\n')
            f.write('Elin=0.040 Eabs=0'+'\r\n')
            f.write('Fano=0.11 FWHM=220' +'\r\n')
            f.write('EndHeader' +'\r\n')
            
            for i in range(0,1024): 
                f.write(str(Data[i])+'\r\n')
            
            f.close()

