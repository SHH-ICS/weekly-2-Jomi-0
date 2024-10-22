import requests

# Define the URL to your PHP script
url = 'http://localhost:8000/handler.php'  # Adjust if necessary

# Get radius input from the user
radius = input("Enter the radius: ")
Import "requests" could not be resolved from sourcePylancereportMissingModuleSource
# Prepare data to send in the POST request
data = {'radius': radius}

# Send POST request to the PHP script
response = requests.post(url, data=data)

# Print the response from the PHP script
print("Response from PHP:")
print(response.text)
