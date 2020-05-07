
import sys
import dns.resolver


def usage():
    print("""
Usage:
    dnstool.py <dns1> [<dns2> ... ]
""")

DNS_SERVERS = [
    '8.8.8.8', 
    '1.1.1.1', 
    '8.8.4.4'
]

def main():
    args = sys.argv[1:]

    if not args:
        usage()
        sys.exit()

    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '1.1.1.1', '8.8.4.4']
    print("Querying DNS servers: {}".format(", ".join(DNS_SERVERS)))

    failures = []
    for name in args:        
        try:
            answers = resolver.query(name)
            for a in answers:
                print("{:30}: {}".format(name, a.address))
        except Exception as e:
            print("{:30}: FAILURE - {}".format(name, e))
            failures.append(name)

    if failures:
        sys.exit(1)


if __name__ == '__main__':
    main()
