#============================================================================
#   FILE NAME:  ManageRPDB.py
#----------------------------------------------------------------------------
# PURPOSE:
#  Tools for creating and managing a Rock Properties Data Base
#
#   Requirements:
#       1. Read standard csv files for database creation
#       2. Create hdf5 files for different databases
#       3. Provide utilities for reading the database in various useful ways
#
#----------------------------------------------------------------------------
# HISTORY:
#
#   Date     Author               Notes
# --------  ----------------  -----------------------------------------------
# 08Mar15   A. K. Jackson     Initial Implementation.
#============================================================================

#   To do

import csv
import numpy as np

#
#   define an object and fill it from a CSV file
#       regressions (regressions file)
#
def openRegcsv(infile):
    #   initialize some stuff
#    index = []
#    name = []
#    func = []
#    form = []
#    units = []
#    source = []
#    priority = []
#    a = []
#    b = []
#    c = []
#    r = []
    #   open the csv file
    try:
        f = open(infile)
    except IOError:
        print("IO error opening ",infile)
    else:
        #   Parse row into lists that will end up becoming numpy arrays
        pass
    return csv.reader(f)
        
        #
#   define an object and fill it from a CSV file
#       Minerals (minerals file)
#
def openMincsv(infile):
    #   initialize some stuff
    index = []
    name = []
    Rho = []
    Rhoerr = []
    VpK = []
    VpKerr = []
    VsMu = []
    VsMuerr = []
    eps = []
    epserr = []
    delta = []
    deltaerr = []
    gamma = []
    gammaerr = []
    priority = []
    source = []
    units = []
    #   open the csv file
    try:
        f = open(infile)
    except IOError:
        print("IO error opening ",infile)
    else:
        #   Parse row into lists that will end up becoming numpy arrays
        for row in csv.reader(f):
            #   skip blank lines and comments
            if len(row) == 0 or len(row[0].strip()) == 0 or row[0][0] == "#":
                print("--1--")
            else:
                print("--2--")
                index.append(row[0].strip())
                name.append(row[1].strip())
                Rho.append(float(row[2].strip()))
                Rhoerr.append(float(row[3].strip()))
                VpK.append(float(row[4].strip()))
                VpKerr.append(float(row[5].strip()))
                VsMu.append(float(row[6].strip()))
                VsMuerr.append(float(row[7].strip()))
                eps.append(float(row[8].strip()))
                epserr.append(float(row[9].strip()))
                delta.append(float(row[10].strip()))
                deltaerr.append(float(row[11].strip()))
                gamma.append(float(row[12].strip()))
                gammaerr.append(float(row[13].strip()))
                priority.append(int(row[14].strip()))
                source.append(row[15].strip())
                units.append(row[16].strip())
        values = np.array((Rho, Rhoerr, VpK, VpKerr, VsMu, VsMuerr, eps, epserr, delta, deltaerr, gamma, gammaerr))
        print(values)    
        return (index, name, priority, source, units, values)