#IMPORT RELEVANT LIBRARIES
import sys
import wand 
from wand.image import Image
import os
import gmplot

# http://docs.wand-py.org/en/0.4.2/

##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################



# Function to get files in the given directory
def getFiles():
  
        directory = raw_input("Please Enter Directory Path: ")#set "directory" as the user input (asks user to enter directory)
        items = os.listdir(directory)#set "items" to list all the elements inside of "directory"
         
        newlist = []#declare array called "newlist"
        for names in items:#for each item inside of the directory
            if names.endswith(".jpg"):#if the file ends with ".jpg"
                newlist.append(names)#add the filename to newlist
        print (newlist)#print out all items from newlist
        for items in newlist:#for each item in newlist
            getexif(items)#send items to exif function
        
##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################  
            
            
def getexif(items):#get items 
    # Get Exif data from files
      exif = {}#declare exif array
      coord = []#declare coordinates array
      lats = []
      longs = []
      with Image(filename=items) as image:#for every file given (items)
              exif.update((k[5:], v) for k, v in image.metadata.items()#get all metadata from file "items" - each jpg file
                               if k.startswith('exif:'))#get exif metadata from metadata
                              
              #return (exif)
              print("-----------------------")
              print("-----------------------")
              print("---" + items + "----")#print filename
              lat = exif['GPSLatitude']#get latitude 
              lat_ref = exif['GPSLatitudeRef'].strip()
              lon = exif['GPSLongitude']#get longitude 
              lon_ref = exif['GPSLongitudeRef'].strip()
              lat = convert(lat, lat_ref)#convert data to get latitude
              lon = convert(lon, lon_ref)#convert data to get longitude
              print ("Coordinates = ") , (lat,lon)#print coordinates as lat,lon
              print ("http://maps.google.com/?q=")+str(lat)+","+str(lon)#print google maps link for the location
              #coord.append[lat,lon]#set coord to long and lat
              #print (coord)
              lats.append(lat)
              longs.append(lon)
              
              #plot_map(lats,longs)#call plot map and pass in coordinates
      
##############################################################################################################
##############################################################################################################2
##############################################################################################################        
##############################################################################################################
##############################################################################################################
              
              
              
def convert(num, ref):
    # Parse the longitude or lattitude passed, and convert to decimal
    num_split = num.split(",")#split the number given at the comma (seperating lat and long)
    coord = []#set coord as an array    
    for num in num_split:#for each number (long and lat)
        num = num.lstrip()#take long at lat from it
        num_0 = num.split("/")#place "/" between long and lat
        numX = float(num_0[0])/float(num_0[1])#convert to positive
        coord.append(numX)#add numX to coordinates
    
    d = coord[0]#days = 1st item in coord array
    m = coord[1]#minutes = 2nd item in coord array
    s = coord[2]#seconds = third item in coord array
    
    value = d + (m / 60.0) + (s / 3600.0)#calculaton to get coordinates
    if ref == 'W':
            value = 0 - value#if coordinates are WEST, set the longitude to negative
    if ref == 'S':
            value = 0 - value#if coordinates are SOUTH, set lattitude to negative
    return(value)

        
##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################
    
    
    
def plot_map (lat,lon):
    
    # Coordinates to map
    
    latList = [lat]
    lonList = [lon]
    coordinate_list = [lat,lon]#list of coordinates = coordinates passed to function
    print (coordinate_list)
    
    # Initial View Point on Map: Lat, Lon, Zoom
    gmap = gmplot.GoogleMapPlotter(53.47194722222223, -2.240013888888889, 8) 
    
    
    #Markers to plot
#    for l in coordinate_list:
#        lat, lon = l#get lat and long from array        
#        print (lat, lon)#printg lat and long
    gmap.marker(latList, lonList, 'blue')#set markers to blue
    gmap.draw( "map.html" )#make file and call it map.html


##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################
    
    
    
def main():
    getFiles()#initialise getFiles function

##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################
    
    

main()

##############################################################################################################
##############################################################################################################
##############################################################################################################        
##############################################################################################################
##############################################################################################################