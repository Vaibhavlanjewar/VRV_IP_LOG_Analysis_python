import re
import csv
from collections import defaultdict

# Input log file
log_file = "sample.log"

# Output CSV file
output_csv = "log_analysis_results.csv"

def parse_log(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

def analyze_logs(lines):
    ip_count = defaultdict(int)
    endpoint_count = defaultdict(int)
    failed_logins = defaultdict(int)
    
    for line in lines:
        ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        endpoint_match = re.search(r'"(?:GET|POST|PUT|DELETE) (.*?) HTTP', line)
        status_match = re.search(r' (\d{3}) ', line)
        
        if ip_match:
            ip = ip_match.group(1)
            ip_count[ip] += 1
        
        if endpoint_match:
            endpoint = endpoint_match.group(1)
            endpoint_count[endpoint] += 1
        
        if status_match:
            status = status_match.group(1)
            if status == "401":
                if ip_match:
                    ip = ip_match.group(1)
                    failed_logins[ip] += 1

    # Sort results
    sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
    sorted_endpoints = sorted(endpoint_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_ips, sorted_endpoints, failed_logins

def save_results_to_csv(ip_data, endpoint_data, failed_login_data):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # IP Address request count
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_data)
        
        # Endpoint access count
        writer.writerow([])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerows(endpoint_data)
        
        # Failed login count
        writer.writerow([])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(failed_login_data.items())

def display_results(ip_data, endpoint_data, failed_login_data):
    print("IP Address Request Counts:")
    for ip, count in ip_data:
        print(f"{ip} - {count}")
    
    print("\nEndpoint Access Counts:")
    for endpoint, count in endpoint_data:
        print(f"{endpoint} - {count}")
    
    print("\nFailed Login Counts:")
    for ip, count in failed_login_data.items():
        print(f"{ip} - {count}")

if __name__ == "__main__":
    log_lines = parse_log(log_file)
    ip_data, endpoint_data, failed_login_data = analyze_logs(log_lines)
    
    display_results(ip_data, endpoint_data, failed_login_data)
    save_results_to_csv(ip_data, endpoint_data, failed_login_data)
    print(f"\nResults saved to {output_csv}")
