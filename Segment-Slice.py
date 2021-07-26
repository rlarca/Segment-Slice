#Segment-Slice
#useful in text analysis where the authorship is in question paragraph by paragraph but paragraphs are too small of a sample size
#Made entirely by Robert Larca


print('Please enter the name of the file you would like to segment (remember to include the extension of the file (".txt") and to have the desired file in the same folder as this python file)')
filename = input()
f = open(filename, "r")
fLines = f.readlines()
fLength = len(fLines)
print("There are " + str(fLength) + " lines, how many paragraphs should each segment contain?")
thickness = int(input())
filename = str(filename[:filename.index(".")])
filename = filename +'@SegSlice@'

i = 0
while i + thickness <= fLength:
    if thickness== 1:
        slicefilename = filename + str(i+1) + ".txt"
    elif thickness > 1:
        slicefilename = filename + str(i+1) + "-" + str(i+thickness) + ".txt"
    with open(slicefilename, 'w') as fp:

        for j in range(0, thickness):
            fp.write(fLines[(i + j)])
        pass
    i += 1








