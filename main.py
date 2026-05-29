import json
import datetime

def generate_report(sum_val, avg_val, max_val):
    report = {
        "project": "Data-Processor-Core",
        "timestamp": str(datetime.datetime.now()),
        "status": "Success",
        "metrics": {
            "sum": sum_val,
            "average": avg_val,
            "max": max_val
        }
    }
    
    # Save the results as a JSON file (standard for backend)
    with open('output_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    print("Python Integration: Report generated successfully in 'output_report.json'")

if __name__ == "__main__":
    # Simulating data received from the C++ Core
    generate_report(133.85, 22.30, 45.1)
