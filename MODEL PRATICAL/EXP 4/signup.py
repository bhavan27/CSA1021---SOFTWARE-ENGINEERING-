def signup(username, password):
    if not username:
        return "Username cannot be empty"
    if len(password) < 6:
        return "Password must be at least 6 characters"
    return "Signup successful"

if __name__ == "__main__":
    print(signup("student", "pass123"))
    print(signup("student", "123"))
