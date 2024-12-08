
# Log File Analyzer

This script analyzes a web server log file to extract and summarize key information such as request counts per IP address, frequently accessed endpoints, and failed login attempts. The results are saved into a CSV file and printed to the terminal for easy inspection.

## Features
- **IP Address Analysis:** Count the number of requests made by each IP address.
- **Endpoint Analysis:** Identify the most frequently accessed endpoints on the server.
- **Failed Login Detection:** Flag IP addresses with repeated failed login attempts (default threshold: 10 attempts).
- **CSV Output:** Export results to a CSV file for easy further analysis.

## Prerequisites
- Python 3.x installed.
- Required Python packages: `csv`, `re`.

## How to Use

1. Clone or download the repository.
2. Save your log data in a file named `sample.log`.
3. Run the script with:
   ```bash
   python log_analyzer.py
   ```
4. The results will be displayed in the terminal and saved to `log_analysis_results.csv`.

## CSV Output Format
- **Requests per IP Address:** Columns: `IP Address`, `Request Count`
- **Most Accessed Endpoint:** Columns: `Endpoint`, `Access Count`
- **Suspicious Activity (Failed Login Attempts):** Columns: `IP Address`, `Failed Login Count`

## Example Output

```
IP Address           Request Count
192.168.1.1          234
203.0.113.5          187
10.0.0.2             92

Most Frequently Accessed Endpoint:
/home (Accessed 403 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
192.168.1.100        56
203.0.113.34         12
```

## Evaluation Criteria
- **Functionality:** The script processes the log file correctly and fulfills all requirements.
- **Code Quality:** Clear, well-organized, and modular code with meaningful variable names and comments.
- **Performance:** The script is efficient for large log files.
- **Output:** Correctly formatted output in both the terminal and CSV file.

## License
This project is licensed under the MIT License.
