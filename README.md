
Coordinate Location Finder
This simple Python script takes user-inputted values for x and y coordinates and determines their location in a Cartesian plane. It categorizes the location as Origin, X-axis, Y-axis, or one of the four quadrants (I, II, III, IV).

Usage
Run the script in a Python environment.
Enter the values for x and y when prompted.
The script will determine the location based on the entered coordinates and display the result.
Code Explanation
The script consists of three main functions:

get_values()
This function attempts to get user-inputted numeric values for x and y coordinates. It handles the case where non-numeric values are entered and provides appropriate feedback.

determine_location(x, y)
This function categorizes the location of the coordinates based on their values, classifying them into categories like Origin, X-axis, Y-axis, or one of the four quadrants.

main()
The main function coordinates the flow of the program. It gets user input, determines the location, and prints the result. It also handles errors when obtaining input values.

Conclusion
This script demonstrates a basic use case of determining the location of coordinates in a Cartesian plane. It can serve as a foundation for more complex applications involving coordinate geometry. The modular structure allows for easy modification and extension, making it a starting point for further development.
