'''Problem #1
1. Check whether the given string input is a valid ip address.
Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.'
etc)
Write all constraints.
Get an input as string. Return if it is valid or not. 
Use string functions.'''

'''
An IPv4 address is a string in decimal-dot notation, consisting of four decimal integers in the
inclusive range 0–255, separated by dots (e.g. 192.168.0.1).


An IPv6 address is represented by eight groups of four hexadecimal digits separated by colons, where each group represents 16 bits.
The range value exceeds from 0 to FFFF.

'''


def is_ip4_address(ip):
    print("Input address:",ip)
    address = ip.split(".")
    address = address[:-1]
    for i in address:
        if not i.isdigit():
            print("Invalid address")
            break
        elif not (0 <= int(i) <= 255):
            print("Invalid address range")
            break
    else:
        print("Valid IP4 address")

def is_ip6_address(ip):
    print("Input address:", ip)
    address = ip.lower().split(":")
    address = address[:-1]
    for i in address:
        if not i.isalnum():
            print("Invalid address")
            break
        elif not all(c in "abcdef" for c in i):
            print("Invalid address range")
            break
    else:
        print("Valid IPv6 address")



ip_1 = "192.58.1.3u."
is_ip4_address(ip_1)
ip_2 = "192.58.1.35."
is_ip4_address(ip_2)
ip_3 = "192.58.1.335."
is_ip4_address(ip_3)

ip_4 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
is_ip6_address(ip_4)



OUTPUT:-
Input address: 192.58.1.3u.
Invalid address
Input address: 192.58.1.35.
Valid IP4 address
Input address: 192.58.1.335.
Invalid address range
Input address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Invalid address range

