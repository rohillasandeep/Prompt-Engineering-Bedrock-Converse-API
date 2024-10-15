import json
import myutils

def read_json_file(file_path):
    # Initialize an empty array to store the JSON objects
    json_array = []

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Clean the JSON string before parsing
                cleaned_line = myutils.clean_json_string(line.strip())
                
                # Now load the cleaned JSON string
                json_object = json.loads(cleaned_line)
                #print(json_object)
                json_array.append(json_object)
            except json.JSONDecodeError as e:
                err = e
                #print(f"Error decoding JSON: {e}")

    # Return the populated json_array for consumption by other modules
    return json_array

# Call the function for testing
if __name__ == "__main__":
    read_json_file('golden-data.txt')
