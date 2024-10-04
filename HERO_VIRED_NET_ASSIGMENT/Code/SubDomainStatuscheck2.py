import requests
from tabulate import tabulate
from datetime import datetime
import time

# User defined subdomains
subdomains = [] 

# function to check subdomains status 
def subdomains_status():
    # User defined subdomains current status list
    subdomains_status_list = []
    # Get the current time for status check
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for subdomain in subdomains:
        try:
            response=requests.get(subdomain,timeout=5)
            if response.status_code == 200:
                subdomains_status_list.append([subdomain,"UP and Running",current_time])
            else:
                subdomains_status_list.append([subdomain,"Down and Unreachable",current_time])
        except requests.RequestException:
            subdomains_status_list.append([subdomains,"Down and Unreachable",current_time])

    print(tabulate(subdomains_status_list, headers=["Subdomain", "Status","TimeStamp"],tablefmt="grid",numalign="center"))

if __name__ == '__main__':
    No_of_domains = int(input('Enter the max number of number of domains : '))
    for i in range (0,No_of_domains):
        usersubdomain = input("Enter the main domain (e.g., https://subdomain.example.com):")
        subdomains.append(usersubdomain)

    time_int = int(input("Please enter the time interval in seconds : "))
    while True:
        print("\nChecking subdomains status...\n")
        subdomains_status()
        print("\nNext check in ",time_int," seconds...")
        time.sleep(time_int)