import json
import csv
import datetime

def generate_report(sum_val, avg_val, max_val):
    timestamp = str(datetime.datetime.now())
    
    # 1. Generate JSON Report (For modern APIs)
    report_data = {
        "project": "Data-Processor-Core",
        "timestamp": timestamp,
        "status": "Success",
        "metrics": {
            "sum": sum_val, 
            "average": avg_val, 
            "max": max_val
        }
    }
    with open('output_report.json', 'w') as f:
        json.dump(report_data, f, indent=4)

    # 2. Generate CSV Report (For Enterprise/Excel integration)
    with open('output_report.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Headers and Data row
        writer.writerow(["Project", "Timestamp", "Status", "Sum", "Average", "Max"])
        writer.writerow(["Data-Processor-Core", timestamp, "Success", sum_val, avg_val, max_val])
    
    print("\n[✔] Success: JSON and CSV reports generated successfully.")

if __name__ == "__main__":
    print("--- Enterprise Data Entry System ---")
    print("Please enter the metrics processed by the C++ Core:")
    
    try:
        # Live Data Entry
        s = float(input("Enter Total Sum: "))
        a = float(input("Enter Average: "))
        m = float(input("Enter Max Value: "))

        # Execution
        generate_report(s, a, m)
        
    except ValueError:
        print("[✘] Error: Please enter valid numeric values.")
