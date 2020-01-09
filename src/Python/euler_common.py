# Common functionality for solutions in Python

class Prime:
  def __iter__(self):
    # TODO: Figure out why the first prime (2) is skipped
    #       from the iterator when we start with it.
    self.a = 1
    return self

  def __next__(self):
    if self.a == 1:
        self.a = 2
    elif self.a == 2:
        self.a = 3
    else:
        x = self.a + 2
        while is_prime(x) == False:
            x += 2
        self.a = x
    return self.a

def is_prime(number):
    if number < 4:
        return number == 2 or number == 3
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True

def is_palindrome(string):
    return string == string[::-1]