from user_interst import User_interest
from prime_no import Prime_no_check

prime_no_check = Prime_no_check()
Userinterst = User_interest()
Userinterst.check_prime_no = True

while Userinterst.check_prime_no:

    prime_no_check.prime_no_cheker()

    Userinterst.user_interest_checker()




