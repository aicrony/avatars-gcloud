from flask import Request
import json
import main as main

# Create a mock request object
data = {
    "user": {
        "id": "123",
        "name": "Lola Doe",
        "email": "lola.doe@example.com"
    }
}
mock_request = Request.from_values(
    content_type="application/json",
    data=json.dumps(data),
)

# Call the function and print the result
response = main.set_user(mock_request)
print(response)
