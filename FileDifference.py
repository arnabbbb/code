"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if line1 == line2:
        return IDENTICAL
    
    elif line2 in line1:
        length_of_line2 = len(line2)
        return length_of_line2
    
    elif line1 in line2:
        length_of_line1 = len(line1)
        return length_of_line1
    
    else:
        for counter in range(len(line1)):
            if line1[counter] == line2[counter]:
                continue
            else:
                return counter

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\r" in line1 or "\n" in line2 or "\r" in line2 or idx > len(line1) or idx > len(line2) or idx < 0:
        return ""
    else:
        return  (line1 + ("\n" + "=" * idx + "^" + "\n") + line2 + "\n")
        
            


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    check1 = all(item in lines1 for item in lines2)
    check2 = all(item in lines2 for item in lines1)
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    
    elif check1 == True:
        return(len(lines2),0)
    
    elif check2 == True:
        return(len(lines1),0)
    else:
        for num in range(len(lines1)):
            if singleline_diff(lines1[num], lines2[num]) == -1:
                continue
            else:
                return (num,singleline_diff(lines1[num], lines2[num]))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    theText = []
    datafile = open(filename, "rt")
    for line in datafile.readlines():
        theText.append(line.strip())
        
    return theText


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    text1 = get_file_lines(filename1)
    text2 = get_file_lines(filename2)
    positions = multiline_diff(text1, text2)
    if positions == (-1,-1):
        return "No differences\n"
    elif text2 == []:
        return ("Line 0:\n" + text1[0] + "\n^\n\n") 
    else:
        str1 = "=" * (positions[1])
        return ("Line " + str(positions[0]) + ":\n" + text1[positions[0]] + "\n" + str1 + "^\n" + text2[positions[0]] + "\n")
    
    

print(singleline_diff("abcdefg", "abedefg"))
print(singleline_diff_format("abcdefghh", "abedefghh", 2))
print(multiline_diff(["abc","dqef","xyzj"], ["abc","def","xyz"]))

