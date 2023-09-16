class Prime_no_check:

    def __init__(self):

        self.score = 0


    def prime_no_cheker(self):
        choosen_no = int(input ("Please enter a number and check it is prime no or not:\n"))
        for i in range(1,choosen_no):

            if choosen_no % i == 0:
                self.score +=1

        if self.score == 2:
            print(f"{choosen_no} is a prime no ")
        else:
            print(f"{choosen_no} is not a prime no ")
