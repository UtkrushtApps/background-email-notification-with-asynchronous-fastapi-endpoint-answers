# Solution Steps

1. Create a new FastAPI app (main.py).

2. Define a Pydantic model for user registration input with fields: 'username', 'email', and 'password'.

3. Set up a simple in-memory storage (dictionary) to simulate a user database.

4. Implement a function 'send_welcome_email' that simulates sending an email (can use print and time.sleep to mock this).

5. Refactor the POST '/register' endpoint to accept a BackgroundTasks parameter.

6. In the '/register' endpoint, perform checks to ensure the username and email are unique.

7. Save the new user to the in-memory store if validations pass.

8. Schedule 'send_welcome_email' as a background task (using background_tasks.add_task) so it does not block the API response.

9. Return a response to the client immediately after scheduling the welcome email task.

10. Test by registering a user and observing that the response is immediate while the email is sent in the background (printed after a delay).

