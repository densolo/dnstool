
import sys
import dns.resolver


def usage():
    print("""
Usage:
    dnstool.py <name>
""")

DNS_SERVERS = [
    '8.8.8.8', 
    '1.1.1.1', 
    '8.8.4.4'
]

ADDITIONAL_RDCLASS = 65535


def main():
    args = sys.argv[1:]

    if not args:
        usage()
        sys.exit()


    name = args[0]
    response = query_name(name)
    print(response.to_text())


def query_name(name):
    last_error = None
    for name_server in DNS_SERVERS:
        try:
            print("Querying '{}' on DNS server {}".format(name, name_server))
            request = dns.message.make_query(name, dns.rdatatype.ANY)
            request.flags |= dns.flags.AD
            request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
                            dns.rdatatype.OPT, create=True, force_unique=True)
            response = dns.query.udp(request, name_server, timeout=10)
            return response
        except dns.exception.DNSException as e:
            print("Query failed to resolve '{}' on {} - {} {}".format(name, name_server, e.__class__, e))
            last_error = e

    raise last_error


if __name__ == '__main__':
    main()
