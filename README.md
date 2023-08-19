# Decorator in Python
What is Decorator in Python?

A decorator is a higher-order function that takes another function as its input and extends the behavior of the input function without explicitly modifying its code. Decorators are often used to add functionality to functions or methods, such as logging, timing, authentication, etc., without altering their original implementation.

authenticated_user = True: This line simulates the authentication status of a user. In the example, the user is initially authenticated.

Let's take the example of a simple authentication system for a web application. We'll create a decorator that checks whether a user is authenticated before allowing them to access a specific view function. We'll use *args and **kwargs to pass any arguments the view function might require.
You can find the example in Decorator.py file.
Here I want to explain the code step by step:

def authenticate(func): This defines a decorator named authenticate. It takes a single argument, which is the function to be decorated.
Inside the authenticate decorator:

def wrapper(*args, **kwargs): This defines a wrapper function that wraps the original function. The *args and **kwargs syntax allows the wrapper to accept any number of positional and keyword arguments.

if authenticated_user: This checks if the user is authenticated (the authenticated_user is True).
return func(*args, **kwargs): If the user is authenticated, it calls the original function (func) with the provided arguments and keyword arguments.
else: If the user is not authenticated:
return "Access denied. Please log in.": It returns a message indicating that access is denied and the user should log in.

@authenticate: This is a decorator application. It means that the authenticate decorator is applied to the following function, modifying its behavior.

def dashboard(username): This defines a function named dashboard that takes a username argument. This function is meant to represent a dashboard page in a web application.

return f"Welcome to the dashboard, {username}!": This is the return statement of the dashboard function. It returns a formatted string welcoming the user to the dashboard.

Similarly, @authenticate is applied to the profile function, ensuring that access to the profile page is also authenticated.

authenticated_user = False: This simulates a scenario where the user is not authenticated.

print(dashboard("Danial Soleimany")): This attempts to call the dashboard function with the argument "Danial Soleimany". However, since the authenticated_user is False, the decorator prevents the actual dashboard function from being executed and instead returns the "Access denied. Please log in." message.

In summary, the code defines a decorator authenticate that checks the authentication status of a user. If the user is authenticated, the original function is executed, and if not, an access denied message is returned. The decorator is applied to both the dashboard and profile functions, but when the authenticated_user status is changed to False, access is denied when trying to call the dashboard function.
 main
