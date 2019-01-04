
**********INTRODUCTION**********

1. Aim of this program is to automate the manual health check of the application post the maintenance related shutdown and startup
2. This program in its first phase, concentrates on reading the log files and checking for keywords and timestamps
3. Also the program checks if the related urls are up and responsive to the requests.
4. The result will be displayed in the terminal in the predefined format with actions needed if any.



**********PRE REQUISITES**********

1. Python 3.x installed in the system.
2. Log files has to be saved in the respective locations and should contain timestamps and keywords.
3. Log files should be uniform in format.



**********HOW TO USE THE PROGRAM**********

1. Save the program in an ideal location in your system where you have enough space
2. Edit the program with the log file names and their paths in the variables(path'x' and file'x')
3. execute the program. (if you are using Unix machine, use the command python <file name>)



**********FEATURES COMING IN NEXT ITERATION**********

1. include the email feature in the code which sends the report to the specified list of people/ group
2. Create a dashboard which shows the health of each components in different colors and shapes and include a facility to click to see the logs.
3. Automate the shut down and bring up procedures within the code. i.e shut down and bring up the application with single click.
4. Include a self maintenance system to repair and bring up the application self in case of issues while bring up. 
