# Import necessary libraries and psutil for system resource monitoring and sys for exit conditions 
import psutil ,time ,sys

# Define thresholds limits for CPU utilization , memory , disk space
cpu_usage_limit = 80
cpu_memory_limit = 80
storage_limit = 85

# to take user input for interval of cpu and system resources monitoring
interval = int(input("Please enter the time interval (in sec) at which monitoring is to be performed : "))

# Function to check CPU usage
def cpu_usage():
 usage = psutil.cpu_percent(interval)
 if usage > cpu_usage_limit:
  print (f" Alert! CPU usage exceeds threshold : {usage}%")
 return usage

# Function to check CPU memory usage
def cpu_mermory():
 memory = psutil.virtual_memory()
 memory_per = memory.percent
 if memory_per > cpu_memory_limit:
  print (f"Alert! memory usage exceeds threshold : {memory_per}%")
 return memory_per

# Function to check disk space
def storage_check():
 storage = psutil.disk_usage('/')
 storage_per = storage.percent
 if storage_per > storage_limit:
  print (f"Alert! Storage usage exceeds threshold{storage_per}%")
 return storage_per

# Main function to monitor the health of the CPU and system resources
def check_cpu_info():
 # To continuously monitor system resources
 while(True):
    # To check CPU usage
    cpu_usage_stat = cpu_usage()
    # To check memory usage
    cpu_mermory_stat = cpu_mermory()
    # To check disk usage
    disk_space_stat = storage_check()

    # printing of the usage values of storage,memory,CPU utilization
    print(f'Monitoring CPU usage: {cpu_usage_stat}%, Memory usage: {cpu_mermory_stat}%, Disk usage: {disk_space_stat}%')

    # To wait for the user specified interval before checking again
    time.sleep(interval)

if __name__ == '__main__' :
    try :
        check_cpu_info()
    # To check if the monitoring is interrupted 
    except KeyboardInterrupt:
      print("System monitoring interrupted , hence exiting")
    # To exit the monitoring after interruption
      sys.exit(0)