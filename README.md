# Seek and Hit task
Create a **private** GitHub repository for the task and add the user noted in the task email as a collaborator.

Push the initial commit without your changes.

The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units
 - there are no other obstructions on the table surface
 - the robot is free to roam around the surface of the table, but must be prevented from falling to destruction
 - any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed

Create an application that can read in commands of the following form: `PLACE X,Y,F MOVE LEFT RIGHT REPORT`
 - PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST
 - the origin (0,0) can be considered to be the SOUTH WEST most corner
 - the first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command
 - the application should discard all commands in the sequence until a valid PLACE command has been executed
 - MOVE will move the toy robot one unit forward in the direction it is currently facing
 - LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot
 - REPORT will announce the X,Y and orientation of the robot
 - a robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands

Constraints
 - the toy robot must not fall off the table during movement, this also includes the initial placement of the toy robot
 - any move that would cause the robot to fall must be ignored

Example Input and Output
 - `PLACE 0,0,NORTH MOVE REPORT Output: 0,1,NORTH`
 - `PLACE 0,0,NORTH LEFT REPORT Output: 0,0,WEST`
 - `PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT Output: 3,3,NORTH`

Instructions
 - no requirements regarding implementation
 - feel free to add dependencies
 - bonus for tests, your choice how

Push your changes.
