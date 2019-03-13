# PR
This repository contains code related to the Plaxis Racer.
The file 'assignment.py' contains the algorithms for iterating over a list of multi-body automobiles (Car, Bus, Truck) and detecting collisions between the objects.
The multi-body automobiles are comprised of independent Shapes (Circle, Square, Rectangle).
Using this design, it is possible to add new Shapes, and in turn add new multi-body automobile types can be defined. 
There is no limit to how many shapes can be in a multi-body automobile.

The development of this design was aided by using Test Driven Development. As such, a series of unit tests were created and added to with each delivery. An overall component test was created and added too as a requirement for integrating a branch.

Base classes and derived classes are in the sub dir 'src'
Test code is in the sub dir 'tests'
The algorithms used to detect collisions and are in the file assignment.py: COMoverlap(), circleXcircle(), quadXquad() and circleXquad(). 

The most up to date code is in the 'Master' branch.
Branches used during development were tested and when all tests were OK, the branches were integrated to 'Master'.
As such, a complete history of all commits per branch, all test results and an overview of what each branch delivered can be found in the commit history of this repository.
Branches used during development:
-refactor-branch01
-refactor-branch02
-refactor-branch03
-documentation-branch01
-documentation-branch02
-fileRestructure-branch01

Design documentation can be found in the sub dir 'Documentation'

Please check out the repository and to execute the unit tests, cd to tests and execute:
python3 unitTests.py -v

To run the component test, cd to the tests dir and execute:
python3 componentTest.py

CI has been added to this repository, until this is verified to be working, manual testing will still be required.


