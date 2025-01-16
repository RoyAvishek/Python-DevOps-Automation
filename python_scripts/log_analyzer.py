# Parse and analyze log files of a k8s pod

# import the required libraries
import subprocess

# function to fetch the logs from the pod
def get_logs(pod_name):
    
    try:
        cmd = ["kubectl", "logs", pod_name, "--tail=100"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Error: Not able to get the logs from {pod_name}")
        return []

# funtion to tract the counter of info, warning and error messages
def analyze_logs(logs):
    
    counter = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    
    for log in logs:
        if "INFO" in log:
            counter["INFO"] += 1
        elif "WARNING" in log:
            counter["WARNING"] += 1
        elif "ERROR" in log:
            counter["ERROR"] += 1
        
    return counter

# function to print the result with proper formating
def print_logs(pod_name):
    
    logs = get_logs(pod_name)
    
    if logs:
        result = analyze_logs(logs)
    else:
        print("No such logs found to analze")
        
    print(f"\nLog Analysis Report for {pod_name}")
    print("==================")
    print(f"INFO messages:     {result['INFO']}")
    print(f"WARNING messages:  {result['WARNING']}")
    print(f"ERROR messages:    {result['ERROR']}")
    
    # Simple health check
    if result['ERROR'] > 0:
        print("\nAlert: Errors detected in logs!")
        
    

# main fucntion to call the above functions
def main():
    pod_name = input(print("Please provide the pod name\n"))
    print_logs(pod_name)
    

if __name__ == "__main__":
    main()