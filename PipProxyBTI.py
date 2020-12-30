from os import system 

while 1:
    a = input("\nEnter python module name: ")
    print(system("pip3.7 install --proxy http.proxy http://mir:htcehcs@proxy.bti.secna.ru:8028 {}".format(a)))