from prime_no import Prime_no_check

prime_no_Check= Prime_no_check()
class User_interest:

    def __init__(self):

        self. check_prime_no = True

    def user_interest_checker(self):
        User_opinion = input("Do you want to check another no yes/no").lower()

        if User_opinion == "no":
            self.check_prime_no = False
        elif User_opinion !="yes":
            print("invalid entry try again")
            self.user_interest_checker()


