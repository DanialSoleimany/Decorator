# Simulated user authentication status
authenticated_user = True

def authenticate(func):
    def wrapper(*args, **kwargs):
        if authenticated_user:
            return func(*args, **kwargs)
        else:
            return "Access denied. Please log in."
    
    return wrapper

# Apply the decorator to protect the 'dashboard' view function
@authenticate
def dashboard(username):
    return f"Welcome to the dashboard, {username}!"

@authenticate
def profile(username):
    return f"Viewing profile for {username}."


# Simulate a non-authenticated user
authenticated_user = False
print(dashboard("Danial Soleimany"))  # Output: Access denied. Please log in.
