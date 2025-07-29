def parse_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            headers = lines[0].strip().split(',')
            data = [line.strip().split(',') for line in lines[1:]]
            
            print("Available columns:", headers)
            col_name = input("Enter column name to average: ")

            if col_name not in headers:
                print("Column not found.")
                return
            
            idx = headers.index(col_name)
            values = []
            for row in data:
                try:
                    values.append(float(row[idx]))
                except ValueError:
                    print(f"Skipping non-numeric value: {row[idx]}")
            
            if values:
                avg = sum(values) / len(values)
                print(f"Average of {col_name}: {avg}")
            else:
                print("No numeric data found.")
    except FileNotFoundError:
        print("CSV file not found.")

# Usage:
# parse_csv('data.csv')
