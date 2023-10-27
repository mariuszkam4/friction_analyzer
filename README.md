Friction analyzer

The script is designed to process files with measurement results of friction parameters recorded during tribological studies on a nanotribotester. Conducting long-term studies on this device generates a vast amount of data, hence the need for a tool for their rapid analysis.

The program's task is to extract data regarding the friction coefficient, then average them using a moving average, and save the results in a new file. The script handles all .csv files in the specified directory and then saves the results of its work to one consolidated .csv file.

To verify the accuracy of the performed operations, the program displays the results of the conducted operations in the form of a consolidated line chart at the end.

Steps required to conduct the analysis:

- Run .py script friction_analyzer.py in python interpreter.
- Indicate the path to the folder containing the files for analysis.
- Select the appropriate data range for calculating the moving average.

To avoid errors related to attempting to process other files, ensure that only files exported by the device's measurement system and intended for analysis are located in the specified folder.