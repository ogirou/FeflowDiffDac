# FeflowDiffDac

## WHAT:
Creates Feflow *.dac file from another *.dac file presenting data values differences with time step 0 instead of absolute data values.
There is a *.dac file to be tested.

## USE:
Simply run:
`python dac2diffDac.py normal_feflow_file.dac`
This keeps normal_feflow_file.dac and creates normal_feflow_file_diffDac.dac .
The use of the scripts is available by running them without arguments.

## DOES IT WORK?
It's possible to test the *_diffDac.dac by running:
`python diffDac2dac.py *_diffDac.dac`
This creates a *_diffDac_reDac.dac file with the sames values as the initial normal_feflow_file.dac .
The 2 files can be compared with diffReDac.py
