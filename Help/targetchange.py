search_text = "a href"
replace_text = "a target=\"sag\" href"
  
# Opening our text file in read only
# mode using the open() function
with open(r'icindekiler.html', 'r') as file:
  
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
  
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_text, replace_text)
  
# Opening our text file in write only
# mode to write the replaced content
with open(r'icindekiler.html', 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)

# create index.html file.
indexhtml= """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>PyNar Help</title>
</head>
<body>

     <iframe src="icindekiler.html" name="sol" frameborder="0" scrolling="yes" seamless="seamless" style="display:block; width:35%; height:97vh;" align="left"> </iframe>  
    
     <iframe src="Yardim_Bolum1.html" name="sag" frameborder="0" scrolling="yes" seamless="seamless" style="display:block; width:64%; height:97vh;" align="right">
        </iframe>
</body>
</html>
"""

with open(r'index.html', 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(indexhtml)


# Printing Text replaced
print("Completed.")