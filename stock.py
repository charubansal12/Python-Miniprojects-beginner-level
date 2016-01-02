from urllib import request

goog_url = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=2&c=2015&d=0&e=2&f=2016&g=d&ignore=.csv"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #Connect python program to the internet, urlopen goes to the url and store the connection to the variable response
    csv = response.read()               #read the data from whatever url you are pointing to 
    csv_str = str(csv)
    lines = csv_str.split("\\n")        #To get the output in different lines
    dest_url = r'goog.csv'                  # r stands for raw, good practice
    fx = open(dest_url, "w")            #MAke a file on a computer
    for line in lines :
        fx.write(line + " \n")
    fx.close()

download_stock_data(goog_url)

    
