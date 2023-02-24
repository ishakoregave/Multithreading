# Multithreading
Python program capable of executing the first 100 steps of a modified cellular life
simulator. This simulator will receive the path to the input file as an argument containing the starting cellular
matrix. The program simulates the next 100 time-steps based on the algorithm discussed ahead. The simulation is guided by a handful of simplistic rules that will result in a seemingly complex
simulation of cellular organisms.

The following rules to dictate what occurs during each time step:
1) Any position in the matrix with a hyphen ‘-’ is considered “dead” during the current time step.
2) Any position in the matrix with a plus sign ‘+’ is considered “alive” during the current time step.
3) If an “alive” square has two, four, or six living neighbors, then it will be “alive” in the next time step.
4) If a “dead” square has a prime number of living neighbors, then it continues to be “alive” in the next
time step.
5) Every other square dies or remains dead, causing it to be “dead” in the next time step.

For this program, a neighbor is defined as any cell that touches the current cell, meaning each current cell,
regardless of position, has 8 neighboring cells. Cells located at the edge should “wrap around” the matrix to find
their other neighbors.
