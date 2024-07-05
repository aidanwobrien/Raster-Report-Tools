# Importing the required modules 
import tkinter
from tkinter import filedialog
import pandas as pd
from bs4 import BeautifulSoup

# Make the tkinter dialogue box
from tkinter.filedialog import askopenfilename, asksaveasfile
from pandas.core.frame import DataFrame
filename = askopenfilename()
path = filename
   
# make an empty list
data = []
   
# get the header from the HTML file
list_header = []
soup = BeautifulSoup(open(path),'html.parser')
header = soup.find_all("table")[0].find("tr")
  
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue
  
# get the data from the HTML file
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
  
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

  
# Storing the data into a Pandas dataframe
df = pd.DataFrame(data, columns = ["value", "pixel", "area"])

# Create a dictionary that labels specific values
dict = {"10":"Cloud",
    "20":"Water",
    "30":"Exposed land/barren",
    "34":"Urban/developed",
    "35":"Greenhouses",
    "50":"Shrubland",
    "80":"Wetland",
    "85":"Peatland",
    "110":"Grassland",
    "120":"Agriculture (undifferentiated)",
    "122":"Pasture/forages",
    "130":"Too wet to be seeded",
    "131":"Fallow",
    "132":"Cereals",
    "133":"Barley",
    "134":"Other grains",
    "135":"Millet",
    "136":"Oats",
    "137":"Rye",
    "138":"Spelt",
    "139":"Triticale",
    "140":"Wheat",
    "141":"Switchgrass",
    "142":"Sorghum",
    "143":"Quinoa",
    "145":"Winter wheat",
    "146":"Spring wheat",
    "147":"Corn",
    "148":"Tobacco",
    "149":"Ginseng",
    "150":"Oilseeds",
    "151":"Borage",
    "152":"Camelina",
    "153":"Canola/rapeseed",
    "154":"Flaxseed",
    "155":"Mustard",
    "156":"Safflower",
    "157":"Sunflower",
    "158":"Soybeans",
    "160":"Pulses",
    "161":"Other pulses",
    "162":"Peas",
    "163":"Chickpeas",
    "167":"Beans",
    "168":"Fababeans",
    "174":"Lentils",
    "175":"Vegetables",
    "176":"Tomatoes",
    "177":"Potatoes",
    "178":"Sugarbeets",
    "179":"Other Vegetables",
    "180":"Fruits",
    "181":"Berries",
    "182":"Blueberry",
    "183":"Cranberry",
    "185":"Other berry",
    "188":"Orchards",
    "189":"Other fruits",
    "190":"Vineyards",
    "191":"Hops",
    "192":"Sod",
    "193":"Herbs",
    "194":"Nursery",
    "195":"Buckwheat",
    "196":"Canaryseed",
    "197":"Hemp",
    "198":"Vetch",
    "199":"Other crops",
    "200":"Forest (undifferentiated)",
    "210":"Coniferous",
    "220":"Broadleaf",
    "230":"Mixedwood"}

# Create a new column called "name" with the mapped columns
df["name"] = df["value"].map(dict)

# Create a new column called "ha" with the property area in hectares
df["ha"] = (df["area"].astype(float)) / 10000

# Create a new coloumn called "acres" with the property area in acres
df["ac"] = (df["ha"].astype(float)) * 2.47105

# # Calling your file some name

output_file = input("Enter filename: ")

# Converting Pandas DataFrame into a csv file called "ELC_Summary"
df.to_csv(rf"{output_file}.csv")