"""
Script to calculate stuff

Folmula from Wikipedia
the spherical law of cosines formula
"""


import math
import json
import urllib.request
from os import path


OFC_LAT,OFC_LONG = 53.339428, -6.257664
EARTH_RADIUS = 6371.009
RANGE = 100



class CloseToUs():

    #local processing variables
    _filename = None
    _file_exists = False
    _file_content = None
    _localFile = True
    #hold decoded customers from json data
    customers = None
    _valid_json = 0
    _invalid_json = 0
    #lat, long of office
    ofclat,ofclon = OFC_LAT,OFC_LONG
    #data for result
    _inviting = 0
    _not_inviting = 0
    close_customers = []

    
    """
    Function to read file
    - Invokes helper function to load data from local/url
    Returns:
    {
        success: [True,False],
        payload: [loaded data, or, Error]
    }
    """
    def read_file(self):
        if self._filename is not None:
            try:
                if self._localFile:
                    rd_f = self.read_from_local()
                else:
                    rd_f = self.read_from_link()
                return {'success': True, 'payload':self._file_content }
                
            except:
                error = 'Error reading the file. Make sure you provide correct path.'+self._filename
        else:
            error = 'No file available to read.'
        print(error)
        exit()
        #return {'success': False, 'payload':error }
        
    
    """
    Function to read the file from local
    - loads data from file to variable: _file_content 
    Returns:
    {
        success: [True,False],
        payload: [loaded data, or, Error]
    }
    """
    def read_from_local(self):
        if self._filename is not None and self._localFile==True:
            
            #read file
            f = open(self._filename,'r')
            self._file_content = f.readlines()
            self._file_exists = True
            f.close()
        else:
            return {'success': False, 'payload': 'Error: Make sure to provide valid path to text file.'}
    
    """
    Function to read the file from url
    - loads data from file to variable: _file_content 
    Returns:
    {
        success: [True,False],
        payload: [loaded data, or, Error]
    }
    
    """
    def read_from_link(self):
        if self._localFile == False and self._filename is not None:
            #self._filename = link
            file_content = urllib.request.urlopen(self._filename)
            self._file_content = []
            for ln in file_content:
                self._file_content.append(ln.decode('utf-8'))
        else:
            print('Error: Make sure to provide a URL to text file.')
            exit()
            #return {'success': False, 'payload': 'Error: Make sure to provide a URL to text file.'}
    
    """
    Function to decode json
    - loads filtered data to customers variable
    - also counts, valid and invalid json entries
    Returns:
    {
        success: [True,False],
        valid: int (default 0),
        invalid: int (default 0)
    }
    """
    def decode_json(self):
        self.customers = []
        for c in self._file_content:
            try:
                self.customers.append(json.loads(c))
                self._valid_json += 1
            except:
                self._invalid_json += 1
        
        return {
            'success': True, 
            'valid':self._valid_json, 
            'invalid': self._invalid_json
            }
        
    
    """
    Function to calculate distance
    args: lat1,lon1 = latlong of location1, lat2,lon2 = lat,long on location2
    Returns: distance between 2 lat,long in km
     -- If there is any issue with calculation, returns Max_range+1 
     -- This falure return makes sure the it does not affect code run

    Uses: the spherical law of cosines formula
    """
    def distance(self, lat1, lon1, lat2, lon2):
        try:
            sin_exp = math.sin(math.radians(float(lat1))) * math.sin(math.radians(float(lat2)))
            cos_exp = math.cos(math.radians(float(lat1))) * math.cos(math.radians(float(lat2)))

            delta_ld = float(lon2) - float(lon1)

            processed_cos_exp = cos_exp * math.cos(math.radians(delta_ld))

            dd = math.acos(sin_exp + processed_cos_exp)

            result = dd * EARTH_RADIUS
            return round(result)
        except:
            return RANGE+1
    
    """
    Function to find closest  customer
    Returns: sorted list of customer based on user_id or None
    """
    def closest_customer(self):
        if self.customers:
            return_list = {}
            result = []
            for customer in self.customers:
                if self.distance(self.ofclat,self.ofclon,float(customer['latitude']),float(customer['longitude'])) <= RANGE :
                    return_list[customer['user_id']] = {'user_id':customer['user_id'],'name':customer['name']}
                    self._inviting += 1
                else:
                    self._not_inviting += 1
        
        #data collected return if return_list is not empty
        #sort the data based on user id
        if return_list:
            for key in sorted(return_list.keys()):
                result.append(return_list[key])
            return result
        else:
            print("No customers in the range of 100km")
            exit()
    
    def write_result(self,result):
        if len(result)> 0 and self._outfile is not None:
            #open a file
            f = open(self._outfile,'w')
            for l in result:
                f.write(json.dumps(l)+"\n")
            print("Please check result in "+ self._outfile)
            f.close()
        elif len(result)> 0 and self._outfile is None:
            for l in result:
                print(json.dumps(l))
        else:
            print("No valid result to write.")
            exit()

    """
    Returns None if closest_customer() fails.
    Output: sorted list or None
    """
    def run(self):
        #read file
        read_file = self.read_file()
        if read_file['success']:
            #On success: decode the json lines
            decode_json = self.decode_json()
            if decode_json['success']:
                #on successful decode: find closes customers 
                if len(self.customers) > 0:
                    result = self.closest_customer()
                    #write result of sorted list to outfile
                    if len(result)>0 and result is not None:
                        self.write_result(result)

    
    def __init__(self,filename,localFile=True,outfile=None):
        if filename or (localFile and path.exists(filename)):
            self._filename = filename
            self._localFile = localFile
            self._outfile = outfile
        else:
            print("File doesnt exist.")
            exit()
            


















