# Most spreadsheet and database applications can export data to a file format known as CSV, which stands for comma separated values. Each line in a CSV file contains a row of data items that are separated by commas. For example, suppose an instructor keeps her students’ test scores in a spreadsheet. Each row in the spreadsheet holds the test scores for one student, and each student has five test scores. Example of spreadsheet:

# 87,79,91,82,94 
# 72,79,81,74,88 
# 94,92,81,89,96 
# 77,56,67,81,79 
# 79,82,85,81,90
# Write a Python program that reads each line from the file, tokenizing the line using the comma character as the delimiter. Once you have extracted the tokens from a line, you can perform any type of operation you need using the tokens. In particular, we want to compute the average score for each student.