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
    print("--- Live Data Entry System ---")
    
    # Pedimos los datos al usuario (Data Entry)
    # Usamos float() para que acepte decimales
    s = float(input("Enter Total Sum: "))
    a = float(input("Enter Average: "))
    m = float(input("Enter Max Value: "))

    # Generamos el reporte con los datos que acabas de escribir
    generate_report(s, a, m)
