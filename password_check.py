CORRECT = "iamgod"


# function to check password
# the while loop handles making sure the correct password matches the users new password input
# function returns True if the passwords match and False if they don't
def pass_checker():
    correct = CORRECT
    tries = 3
    keep_going = True
    while keep_going:
        pass_input = input("type password here: ")
        if pass_input == correct:
            keep_going = False
            return True
        else:
            tries -= 1
            print(f"You have {tries} tries left")

        if tries < 1:
            return False


a = pass_checker()

# Works with the value pass_checker() returns
if a is True:
    print("welcome to zhu-NET")
else:
    print("...... You need the right password to continue")