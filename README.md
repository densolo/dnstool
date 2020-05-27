# Overview

This is a simple DNS util to resolve host names into IP addresses 
that use specific DNS servers:     '8.8.8.8', '1.1.1.1', '8.8.4.4'


# Installation

```
git clone https://github.com/densolo/dnstool.git
pip install -r requirements.txt
```

# Usage
Enter the command without arguments so a short help.

Entry the command with a host name.

```
python bin/dnstool.py ya.com
```

# GUI
To start a GUI version use the following command:
```
python bin/dnstool_gui.py
```

# Output
```
Querying 'ya.ru' on DNS server 8.8.8.8
id 29093
opcode QUERY
rcode NOERROR
flags QR RD RA
edns 0
payload 512
;QUESTION
ya.ru. IN ANY
;ANSWER
ya.ru. 3599 IN SOA ns1.yandex.ru. sysadmin.yandex.ru. 2020051400 900 600 2592000 900
ya.ru. 1199 IN TXT "_globalsign-domain-verification=dHoe580bPQ-lfi_vh-BEIwB4NAtUwURIzrzsivByVL"
ya.ru. 1199 IN TXT "v=spf1 redirect=_spf.yandex.ru"
ya.ru. 1199 IN TXT "2289ce337000f818d21158a36da064df7b39e004fd1684e35072b426455b4b0f"
ya.ru. 7199 IN MX 10 mx.yandex.ru.
ya.ru. 599 IN AAAA 2a02:6b8::2:242
ya.ru. 599 IN A 87.250.250.242
ya.ru. 7199 IN NS ns1.yandex.ru.
ya.ru. 7199 IN NS ns2.yandex.ru.
ya.ru. 3599 IN CAA 0 issue "globalsign.com"
ya.ru. 3599 IN CAA 0 issue "yandex.ru"
ya.ru. 3599 IN CAA 0 issuewild "globalsign.com"
ya.ru. 3599 IN CAA 0 issuewild "yandex.ru"
;AUTHORITY
;ADDITIONAL
```