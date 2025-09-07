class AccountDetails:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


accounts = []  # list to store all registered accounts


class Signup(AccountDetails):
    def __init__(self):
        print("\n--- Signup ---")
        username = input("Create your username (e.g Ali Khan): ").strip()
        email = input("Enter the email you want to use: ").strip()
        password = input("Create a strong password: ").strip()

        if username and email and password:  # check all fields
            super().__init__(username, email, password)
            accounts.append(self)  # save this account
            print("✅ Account created successfully!\n")
        else:
            print("❌ All fields are required.")


class Login:
    def __init__(self):
        print("\n--- Login ---")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        for acc in accounts:  # check against stored accounts
            if acc.email == email and acc.password == password:
                print(f"✅ Welcome back, {acc.username}! Login Successful.\n")
                return
        print("❌ Invalid Credentials, Try again.")


# Main program loop
while True:
    option = input("\nWelcome to FaceBook\n1. Login\n2. Signup\n3. Exit\nChoose option: ")

    if option == "1":
        if accounts:  # only allow login if at least one account exists
            Login()
        else:
            print("❌ No accounts found. Please sign up first.")
    elif option == "2":
        Signup()
    elif option == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option, please try again.")
