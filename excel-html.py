#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import sys

import re


# In[2]:


data = pd.read_excel("box.xlsm", nrows = 81)
data.columns = ['position', 'label', 'selection', 'date', 'geneious', 'addgene', 'genbank', 'benchling', 'verified', 'sequence', 'tm', 'ident', 'comments', 'project']

# # Define a regular expression to match any character that is not allowed in a file name, excluding underscores
# invalid_chars_re = re.compile(r'[<>:"/\\|?*\x00-\x1F ]')

# # Replace any invalid characters (including spaces) with underscores in the string
# cleaned_project_name = re.sub(invalid_chars_re, '_', data['project'][0])

# # Use the cleaned project name in the file name
# output_file_name = f"{cleaned_project_name}.txt"


# In[3]:


first_block = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
/* This code defines styles for a legend, which is typically used to explain what the colors in a visualization mean */

/* First, we define the properties for the container element of the legend */
.legend {
display: flex; /* Use flexbox to arrange the items horizontally */
justify-content: left; /* Align the items to the left of the container */
}

/* Next, we define the properties for the individual items in the legend */
.legend-item {
margin: 5px; /* Add some space between items */
padding: 5px; /* Add some padding to make the items more visually appealing */
font-size: 14px; /* Set the font size of the text */
border: 1px solid #ccc; /* Add a border around each item */
color: white
}

/* Each legend item has a different background color to represent different data categories */
.legend-item.plasmid {
background-color: #cacaaa; / /*Set the background color for the plasmid category */
}

.legend-item.primer {
background-color: #9b9ece; /* Set the background color for the primer category */
}

.legend-item.cells {
background-color: #ed6a5a; /* Set the background color for the cells category */
}

.legend-item.glycerol {
background-color: #5c7457; /* Set the background color for the stabs category */
}

.legend-item.misc {
background-color: #141b41; /* Set the background color for the misc category */
}

.legend-item.empty {
background-color: #A9A9A9; /* Set the background color for empty category */
}

.grid-container {
  background-color: black;
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-gap: 1.5px;
  justify-cotent: center;
  min-width: 0;
  max-width: 100%;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 1px 0;
  font-size 10px;
}

.button {
  background-color: grey;
  border: none;
  color: white;
  padding: 0%;
  text-align: center;
  text-decoation: none;
  display: block;
  font-size: 12px;
  margin: 0px 0px;
  cursor: pointer;
  max-width: 100%;
}


.button:hover {
  opacity: 0.9;
}

.disabled {
  background-color: grey;
  pointer-events: none;
  cursor: not-allowed;
}


* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 50%;
  padding: 10px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 988px) {
  .column {
    width: 100%;
  }
}

/* Define a CSS class called 'data' that is used to style the data to be displayed and hide it by default */
.data {
display: none; /* Hide the data by default */
}

/* Define a CSS class called 'active' that is used to show the data by changing the display property to block */
.data.active {
display: block; /* Change the display property of the data to block to show it */
}

/* Individual button colors based on button type */
    button[type="plasmid"] {
      background-color: #cacaaa;
    }
   
	button[type="primer"] {
	background-color: #9b9ece;
    }
    
	button[type="competent cell"] {
      background-color: #ed6a5a;
    }
    
	button[type="glycerol stock"] {
      background-color: #5c7457;
    }
    
	button[type="misc"] {
      background-color: #141b41;
    }
    
	button[type="empty"] {
      background-color: #A9A9A9;
      pointer-events: none;
      cursor: not-allowed;
    }
</style>
</head>
<body>"""


# In[4]:


second_block = """<div class="legend">
  <div class="legend-item plasmid">plasmid</div>
  <div class="legend-item primer">primer</div>
  <div class="legend-item cells">competent Cells</div>
  <div class="legend-item glycerol">glycerol stock</div>
  <div class="legend-item misc">misc</div>
  <div class="legend-item empty">empty</div>
</div>
<div class="row">
  <div class="column" style="background-color:white;">
  <div class="grid-container">"""


# In[5]:


third_block = """</div>
</div>
<div class="column right" style="display:none">"""


# In[6]:


fourth_block = """</div>
</div>
<script>
  // Get all buttons
  var buttons = document.querySelectorAll('.button');

  // Get all data elements
  var dataElements = document.querySelectorAll('.data');

  // Variable to keep track of whether the button has been clicked before or not
  var hasClicked = false;

  // Loop through buttons and add event listener
  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Remove active class from all buttons
      buttons.forEach(function(btn) {
        btn.classList.remove('active');
      });

      // Add active class to clicked button
      button.classList.add('active');

      // Remove active class from all data elements
      dataElements.forEach(function(dataElement) {
        dataElement.classList.remove('active');
      });

      // Get data target from clicked button and add active class to corresponding data element
      var dataTarget = button.getAttribute('data-target');
      var activeData = document.getElementById(dataTarget);
      activeData.classList.add('active');

      // Show the right column only on the first click
      if (!hasClicked) {
        document.querySelector('.column.right').style.display = 'block';
        hasClicked = true;
      }
    });
  });
</script>


</body>
</html>
"""


# In[7]:

with open("index.html", "w") as f:
    # Redirect stdout to the file
    sys.stdout = f
    
    # Your existing code to be redirected to the file
    i = 0

    print(first_block)

    print("<h2>{}</h2>".format(data['project'][0]))

    print(second_block)
    i = 1

    for i, row in data.iterrows():
        position = row['position']
        label = row['label']
        selection = row['selection']
        if pd.isna(row['ident']):
            ident = 'empty'
            string = '<button class="button disabled" data-target="data{}" type="{}">{}</button>'.format(i+1,ident,i+1)
        else:
            type = row['ident']
            string = '<button class="button" data-target="data{}" type="{}"><p>{}</p><p>{}<br>{}</p></button>'.format(i+1,type,position, label, selection)
        print(string)

        i += 1

    print(third_block)

    i = 0

    def plasmid(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <p>position:{}</p>
        <h2>{} {}</h2>
        <p>{}</p>
        <p>{}</p>
        {}
        {}
        {}
        <p>{}</p>
    </div>
        """.format(position, position, ident, label, date, selection, geneious, genbank, addgene, comments))

    def primer(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <p>position:{}</p>
        <h2>{} {}</h2>
        <p>{}</p>
        <p>{} {}</p>
        {}
        {}
        {}
        <p>{}</p>
    </div>
        """.format(position, position, ident, label, date, sequence, tm, geneious, genbank, benchling, comments))

    def glycerol_stock(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <p>position:{}</p>
        <h2>{} {}</h2>
        <p>{}</p>
        <p>{}</p>
        {}
        {}
        {}
        {}
        <p>{}</p>
    </div>
        """.format(position, position, ident, label, date, selection, addgene, geneious, genbank, benchling, comments))

    def comp_cell(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <p>position:{}</p>
        <h2>{} {}</h2>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
    </div>
        """.format(position, position, ident, label, date, selection, comments))

    def misc(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <p>position:{}</p>
        <h2>{} {}</h2>
        <p>{}</p>
        <p>{}</p>
        {}
        {}
        {}
        {}
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
    </div>
        """.format(position, position, ident, label, date, selection, addgene, geneious, genbank, benchling,verified, sequence, ident, tm, comments))

    def empty(input):
        print("""<div class=\"data active\" id=\"data{}\">
        <h2>Data {}</h2>
        <p>Add data for {}..</p>
    </div>
    """.format(position, position, position))


    for i, row in data.iterrows():
        if pd.isna(row['geneious']):
            geneious = ''
        else:
            geneious = '<p><a href=\"{}target="_blank"\">Geneious Link</a></p>'.format(row['geneious'])

        if pd.isna(row['benchling']):
            benchling = ''
        else:
            benchling = '<p><a href=\"{}"\target="_blank">Benchling</a></p>'.format(row['benchling'])

        if pd.isna(row['genbank']):
            genbank = ''
        else:
            genbank = '<p><a href=\"{}\" download=\"Plasmid.gb\">Download</a></p>'.format(row['genbank'])

        if pd.isna(row['addgene']):
            addgene = ''
        else:
            addgene = '<p><a href=\"{}\"target="_blank">AddGene</a></p>'.format(row['addgene'])

        if pd.isna(row['position']):
            position = ''
        else:
            position = row['position']
        if pd.isna(row['label']):
                label = ''
        else:
                label = row['label']
        if pd.isna(row['selection']):
                selection = ''
        else:
                selection = row['selection']
        if pd.isna(row['date']):
                date = ''
        else:
                date = row['date']
        if pd.isna(row['verified']):
                verified = ''
        else:
                verified = row['verified']
        if pd.isna(row['sequence']):
                sequence = ''
        else:
                sequence = row['sequence']
        if pd.isna(row['tm']):
                tm = ''
        else:
                tm = row['tm']
        if pd.isna(row['ident']):
                ident = 'empty'
        else:
                ident = row['ident']
        if pd.isna(row['comments']):
                comments = ''
        else:
                comments = row['comments']
        if ident=="plasmid":
            plasmid(i)
        if ident=="primer":
            primer(i)
        if ident=="misc":
            misc(i)
        if ident=='empty':
            empty(i)
        if ident=='competent cell':
            comp_cell(i)
        if ident=='glycerol stock':
            glycerol_stock(i)

    print(fourth_block)
    
# Reset stdout to the console
sys.stdout = sys.__stdout__


# In[ ]:




