# ELC-Summary
Converts a Southern Ontario Land Resource Information System (SOLRIS) raster HTML report generated from QGIS to a CSV.

Save the .html raster report that is generated when running the "Raster Layer Unique Report" in QGIS.

Run the script and use the dialogue box to point to the .html file.

Enter the name would like to save the file as.

The translated data is now saved in your directory as ELC_Summary.csv.

*Note* this script will work for all .html tables, but a dictionary is coded specifically for use with the Southern Ontario Land Resource Information System data.
*Note* this script requires the beautifulsoup4 library to be installed on your machine. pip install beautifulsoup4 to install the library.
*Note* Acre and Hectare conversions will only be accurate if the map projection units are in metres

# ACI Calc
Converts a AAFC Annual Crop Inventory raster HTML report generated from QGIS to a CSV.

Save the .html raster report that is generated when running the "Raster Layer Unique Report" in QGIS.

Run the script and use the dialogue box to point to the .html file.

Enter the name would like to save the file as.

The translated data is now saved in your working directory
