import csv

def read_csv_file(file_path):
    # Initialize an empty array to store the CSV data
    data_array = []

    print("file_path: "+file_path)
    # Open and read the CSV file
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csv_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row (which is a dictionary) to the data array
            data_array.append({
                "teamname": row["teamname"],
                "userinput": row["userinput"],
                "result": row["result"],
                "url": row["url"],
                "userinputid": row["userinputid"],
                "response_time": float(row["response_time"]),
                "status_code": int(row["status_code"])
            })
            #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            #print(row)
            #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        
    # Return the populated array for consumption by other modules
    return data_array

# Call the function for testing
if __name__ == "__main__":
    read_csv_file('8f3994d0-2620-4075-8af1-6d11b95c50a7-test.csv')