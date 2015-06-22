import fractions
import random

message = 88734
print "message is: "
print  message
# public
p = 3
# private
q = 11
n = p * q

# Compute totient function phi(n)
# Number of relative primes to n from 1 to n
# Relative primes have greatest common divisor 1 


def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount



totient = phi(n) 
totient2 = (p-1) * (q-1)


# de=1 (mod phi(n)) 	
# (e, phi(n))=1, 

def find_e(totient):
    potential_e = []

    for k in range(1, totient):
        if fractions.gcd(n, k) == 1 and k > (totient / 2):
            potential_e.append(k)

 
    # p != 1(mod e) and q != 1(mod e) so that d exists 
    
    e = random.choice(potential_e)    
    return e

potential_d = []
while not potential_d:
  e = find_e(totient)
  g = lambda x: e * x % totient;
  print "trying to find d"
  for k in range(1, 100):
    if g(k) == 1:
       potential_d.append(k)


print potential_d

d = random.choice(potential_d)

print e, d
print totient
encrypted = ((message ** e) % n) + n * 20
print encrypted

decryption = []
for i in range(1,100000):
  decrypted = ((encrypted ** d) % n) + n*i
  if decrypted == message:
    print "yesss"
    print decrypted


# Send message the public key (e_key, n) is shared public

# The reciever has the private key (d_key, n) stored.
# decrypted = encrypted

