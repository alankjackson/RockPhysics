#============================================================================
#   FILE NAME:  TestInputs.csv
#----------------------------------------------------------------------------
# PURPOSE:
#  Test that RockValues.csv and RockReg.csv contain sensible values
#
#   Requirements:
#       1. Test values against sensible ranges 
#               1 < Rho < 3 (gm/cc)
#            1500 < Vp < 8000 (m/s)
#             300 < Vs < 6000 (m/s)
#       2. Generate crossplots for comparison
#               Vp vs. Vs
#               Vp vs. Rho
#               Vp vs. Phi
#               Vs vs. Phi
#
#----------------------------------------------------------------------------
# HISTORY:
#
#   Date     Author               Notes
# --------  ----------------  -----------------------------------------------
# 08Mar15   A. K. Jackson     Initial Implementation.
#============================================================================

#   To do

#   import routines that will actually do all the work

#import RockPhysics as RP
#import RockPhysicsPlots as RPPlot
import ManageRPDB as RPDB

minerals_csv = "RockValues.csv"
regressions_csv = "RockReg.csv"

try:
    (index, name, priority, source, units, values) = RPDB.openMincsv(minerals_csv)
except IOError:
    print("opencsv returns IOError")
else:
    # do stuff
    pass
