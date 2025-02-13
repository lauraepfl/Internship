# Getting used to fortran code
This folder is composed of different tests ran to get used to the fortran code. They all run with sedov1d.nml.
- basic_tests is composed of multiple tests of 1d simulation to create graphs out of the data
- test_InitDUP is composed of tests of 1d simulations with different initial values of density, velocity and pressure.
- test_boxlenght is a test with different boxlenght in the parameters
- test_nlevel is a test with different number of cells in the simulation
- test_solver compares the three available sovler algorithms that can be used
- test_units compares graphs in IS units and in AU

In each folder is a text file with deductions i made from observing the graphs