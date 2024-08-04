import requests
import time
from prettytable import PrettyTable #this library helps to create a table view to show the statuses of UP or DOWN time of the subdomains

SDs = ["subdomain1.abc.com", "subdomain2.abc.com", "subdomain3.abc.com"] #I have taken examples of sample subdomains

def check_status(subdomain): #first function to check whether the domain is up or down depending upon the status code of 200
    try:
        response = requests.get(f"http://{subdomain}") #fetching the response from subdomain if its is working or not
        if response.status_code == 200: #CRITERIA to check UP/DOWN time
            return "Up"
        else:
            return "Down"
    except requests.ConnectionError:
        return "Down"

def monitor_subdomains(subdomains): #second function to capture the status of the subdomains each 60 seconds
    while True:
        statuses = []
        for subdomain in subdomains:
            status = check_status(subdomain)
            statuses.append((subdomain, status)) #appending the status of the subdomain in the status list
        
        display_status(statuses) #forwarding the status to the function to be beautified
        time.sleep(60)

def display_status(statuses): #third function to display status aggregated from the sample subdomains
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]
    
    for sd, stat in statuses: #loop to iterate through the status and respective subdomain
        table.add_row([sd, stat])
    
    print(table)

if __name__ == "__main__":
    monitor_subdomains(SDs)
