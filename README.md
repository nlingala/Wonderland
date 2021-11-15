# Wonderland
Spring 2022 ECE 3872 Design Project Framework

Things to do:
1. Need another input argument(number of connections) for handler function
2. Test case for Robot application - half complete (print the file)
3. Design Doc - images, video
4. Need more pis and a laptop now

Team Computer - Directior:
Framework complete:
- Transfer zip file containing script files in the format [(ROBOT#)_(CueTime in Milliseconds)] for example: [R01_1000]

Director - Robot:
Framework in working condition
- Needs few more updates
- Multithreading file transfer application from server to specific robot.
- The files will be queued into a buffer and sent to the proper robot at the corresponding time

Questions:
1. Testing on same device (file transfer is quick for even large files <10ms): Need to check on network
2. Currently downloads new file to robot: should I create a return value for it or is it better to have the students write that portion of file io?
3. 
