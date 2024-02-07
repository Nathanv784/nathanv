def countdown(n):
    print("Starting countdown!")
    while n > 0:
        yield n
        n -= 1
        
    print("Countdown finished!")
countdown_gen = countdown(5)
print("1")
for i in countdown_gen:
    print("Countdown:", i)
