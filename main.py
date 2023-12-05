from PasswordGenerator import PasswordGenerator


def main():
    while True:
        try:
            my_pass = PasswordGenerator()
            my_pass.user_preferences()
            password_file = open('Passwords.txt', 'w')
            while True:
                my_pass.generate_password()
                password_file.write(f'{my_pass.get_password()}\n')
                print('Your generated password: ', my_pass)
                if input("Generate another password? (y/n): ").lower() == 'y':
                    if input("Update preferences? (y/n): ").lower() == 'y':
                        my_pass.user_preferences()
                else:
                    print("View generated passwords in Passwords.txt file")
                    password_file.close()
                    break
            if password_file.closed:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            retry = input(
                "Do you want to run the program again? (y/n): ").lower()
            if retry != 'y':
                print("Exiting the program.")
                break


if __name__ == '__main__':
    main()
