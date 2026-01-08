import psutil
import time
import csv

with open("cpu_metrics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "cpu_percent"])

    for _ in range(240):
        writer.writerow([time.time(), psutil.cpu_percent(interval=1)])
