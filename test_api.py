import requests

# Define the base URL of your FastAPI application
base_url = 'http://localhost:8008'

# Define the endpoint URL for users
users_url = base_url + '/users'

# Sample user data for testing
sample_user = {
    'name': 'John Doe',
    'email': 'john@example.com'
}

# Function to send a POST request to create a new user
def create_user(data):
    response = requests.post(users_url, json=data)
    return response.json()

# Function to send a GET request to retrieve all users
def get_users():
    response = requests.get(users_url)
    return response.json()

# Function to send a GET request to retrieve a specific user by ID
def get_user(user_id):
    response = requests.get(f'{users_url}/{user_id}')
    return response.json()

# Function to send a PUT request to update a user by ID
def update_user(user_id, data):
    response = requests.put(f'{users_url}/{user_id}', json=data)
    return response.json()

# Function to send a DELETE request to delete a user by ID
def delete_user(user_id):
    response = requests.delete(f'{users_url}/{user_id}')
    return response.json()

if __name__ == '__main__':
    # Test creating a new user
    new_user = create_user(sample_user)
    print('Created user:', new_user)

    # Test retrieving all users
    all_users = get_users()
    print('All users:', all_users)

    # Test retrieving a specific user by ID
    user_id = new_user['id']
    specific_user = get_user(user_id)
    print('Specific user:', specific_user)

    # Test updating a user by ID
    updated_data = {'name': 'Jane Doe'}
    updated_user = update_user(user_id, updated_data)
    print('Updated user:', updated_user)

    # Test deleting a user by ID
    deleted_user = delete_user(user_id)
    print('Deleted user:', deleted_user)
