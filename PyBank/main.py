# Homework assignment (Part 1: "PyBank")
# UT-TOR-DATA-PT-01-2020-U-C / 03-Python
# (c) Boris Smirnov

import os
import csv

# Initializing stats variables

month_cnt = 0       # Months counter
prev_amount = 0     # Profit/Loss of the previous month
total = 0           # Total amount Profit/Losses
total_change = 0    # Sum of all changes month by month (for calculating average)
avg_change = 0.0    # Average change over the entire period
delta = 0           # diffrence of amounts between to months
greatest_inc = 0    # Greatest Increase in profits
greatest_dec = 0    # Greatest Decrease in profits
greatest_inc_date = ''  # Date of the Greatest Increase in profits
greatest_dec_date = ''  # Date of the Greatest Decrease in profits

# Reading CSV file

fname = os.path.join("Resources", "budget_data.csv")

with open(fname, newline='') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skipping the header
        next(csvreader)

        # Analysis loop
        for row in csvreader:
            month_str = row[0]
            amount = int(row[1])

            # Months counter
            month_cnt +=1

            # Total amount Profit/Losses
            total += amount

            # Changes month by month
            if month_cnt > 1:
                delta = amount - prev_amount
                total_change += delta
            prev_amount = amount

            # Greatest Increase/Decrease in profit
            if delta > greatest_inc:
                greatest_inc = delta
                greatest_inc_date = month_str
            elif delta < greatest_dec:
                greatest_dec = delta
                greatest_dec_date = month_str

if month_cnt:
    avg_change = float(total_change) / (month_cnt - 1)

# Generating report

report_str = "\nFinancial Analysis\n" + "----------------------------\n"
report_str += "Total Months: {}\n".format(month_cnt)
report_str += "Total: ${:,}\n".format(total)
report_str += "Average  Change: ${:,.2f}\n".format(avg_change)
report_str += "Greatest Increase in Profits: {} (${: ,})\n".format(greatest_inc_date, greatest_inc)
report_str += "Greatest Decrease in Profits: {} (${:,})\n".format(greatest_dec_date, greatest_dec)
print(report_str)

# Dump report to the file
with open("report.txt", "w") as f:
    f.write(report_str)

# Done