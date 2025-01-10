# Graph Plotter & Line Intersection Visualizer
This project is a Graph Plotting and Visualization Tool built using Python's tkinter library. It allows users to plot points, draw lines, visualize parabolas, and calculate the intersection of two lines on a Cartesian plane.

Features
Plot Points
Enter coordinates (x, y) to plot points on the graph.
Points are displayed with random colors.
Draw Lines

Define lines using the equation format y = mx + b.
Two lines can be drawn, and the intersection point is calculated (if applicable).
Plot Parabolas

Visualize quadratic equations in the form y = ax² + bx + c.
Grid and Axes

A grid is displayed with labeled axes for better visualization.
Centered origin (0, 0) with labels for x and y axes.
Interactive Interface

User-friendly interface with text boxes and buttons for input and actions.

How to Use
1. Running the Program
Run the script using Python 3.x:
bash
Copy code
python graph_plotter.py

2. Features Overview

Plot Points
Enter x and y coordinates in the respective text boxes.
Click the "Plot Point" button to visualize the point on the graph.

Draw Lines
Enter slope (m) and intercept (b) values for Line 1 and Line 2.
Click "Draw Line 1" and "Draw Line 2" to visualize the lines.
The intersection point will be displayed if the lines are not parallel.

Plot Parabolas
Enter coefficients a, b, and c for the quadratic equation.
Click the "Plot Graph" button to visualize the parabola.

Code Structure
Global Variables
Define canvas dimensions, grid properties, and plot parameters.
Functions
plot(): Plots individual points.
drawline(): Draws Line 1 based on y = mx + b.
drawline2(): Draws Line 2 and calculates the intersection point.
drawpoi(): Checks for parallel lines and calculates the intersection.
drawpara(): Plots a parabola using quadratic equations.
drawstuff(): Generates grid and axis labels.
Graphical User Interface (GUI)
Built using tkinter.
Includes buttons, labels, and input fields for interaction.

Author
Aathithya Ananth
A beginner developer passionate about data visualization and Python programming.

Let me know if you'd like to make further adjustments!
