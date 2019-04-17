# NetworkMode

## Description
This is the repository that will be used for the MTP Network Mode competition. It will be developed in Python language, using the appropriate libraries.

## Instructions
The initial structure of the project will be the following:

  * The main.py file will be the one executed. It will wait until it gets assigned a role and will wait for the GO sign. Once that happens, it will continue its execution depending on the assigned role.
  * The tx_mode and rx_mode packages will include all the methods that will be called for each role in the network. Such modularization has been done in order to ease the development, so that **only one developer will be working on a file**.
  * The util package has been created for the functions that do not identify with any of the roles (ie. cheking the role or reading to the GO/STOP sign).

## Coding standards
For simplifying the development of the project, some recommendations are given:

  * Use an Integrated Development Environment (ie. PyCharm) for writing and self correcting the code.
  * Always pull before pushing code to the repository
  * Give explanatory comments to the commits, many people will read them!
  
## Authors
  * **Ibai Ros** - Team B - Initial work
