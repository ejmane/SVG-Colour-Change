import os
import sys

black_codes = {"#000000", "#010101"}
colour_to_replace_with = "#777777"
new_class = """{fill:#777777; stroke}
	path {fill:#777777;}
	line {fill:#777777; stroke:#777777}"""
files = sys.argv[1:]

## Takes in the text for a SVG file and replaces the black colour codes in 
## black_codes with the colour of colour_to_replace_with
def change_black_codes(SVG):
    for codes in black_codes:
        SVG = SVG.replace(codes, colour_to_replace_with)
    return SVG

## Takes in the text and returns the highest class within the text
def find_last_class(SVG):
    a = 0
    while True: 
        if SVG.count("st" + str(a)) == 0:
            return a - 1
        else:
            a += 1
        
## Takes in the text and the last class and adds a new class and extra styling
def add_new_class(text, last_class):
    text_before = text.split("</style>")[0]
    text_after = text.split("</style>")[1]
    return(text_before + "\t.st" + str(last_class + 1) + new_class + "\n</style>" + text_after)

## Takes in the text and replaces polygon points with polygon class="st" points
def change_points(text, last_class):
    text = text.replace("polygon points", "polygon class=\"st" + str(last_class) + "\" points")
    return text

## Takes in the text and removes the rectangle containing the background
def remove_background(text):
    text = text.split("<rect class=\"st0\"", 1)[0] + text.split("<rect class=\"st0\"")[1].split("\"/>", 1)[1]
    ##text = text.split("<rect class=\"st0\"")[1].split("\"/>")[1]
    ##text.split("<rect class=\"st0\"")[1].split("/>")[1]
    ##text = text.split("<rect class=\"st0\"")[0] + text.split("<rect class=\"st0\"")[1].split("/>")[1]
    return text

def main(file):
    ##file = input("Enter the file name: ")
    text = open(file, "r").read()
    text = change_black_codes(text)
    text = add_new_class(text, int(find_last_class(text)))
    text = change_points(text, int(find_last_class(text)))
    text = remove_background(text)
    open(file, "w").write(text)
    return text

for file in files:
    main(file)

##main()