i used python as programming language ,and one trick in this spiral snail is that
At each step:

Go left => right (top row)

Go top => bottom (right column)

Go right =< left (bottom row)

Go bottom => top (left column)
 and this line of code "if not matrix or not matrix[0]" → handles empty matrix edge case
 and the while loop says:keep looping as long as there are rows and columns left.
