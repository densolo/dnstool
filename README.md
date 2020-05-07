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

Entry the command with host names as arguments to get the resolved.

```
python bin/dnstool.py ya.com google.com upwork.com noexisting-domain.org
```
