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

#
#   define an object and fill it from a CSV file
#       type= values (mineral file) or regressions (regressions file)
#
def opencsv(infile, type):
    #   open the csv file
    try:
        f = open(infile)
    except IOError:
        print("IO error opening ",infile)
    else:
        return csv.reader(f)