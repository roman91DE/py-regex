#!/usr/bin/env python
# coding: utf-8

# In[32]:


import re


# In[ ]:


"""
IPv4 was the first publicly used Internet Protocol which used 4 byte addresses which 
permitted for 232 addresses. 
The typical format of an IPv4 address is A.B.C.D where A, B, C and D are Integers 
lying between 0 and 255 (both inclusive).
"""


def is_ip4(s: str) -> bool:
    part = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    pattern = rf"^{part}\.{part}\.{part}\.{part}$"
    return re.search(pattern, s) is not None


# In[34]:


def test_is_ip4() -> None:
    assert is_ip4("0.0.0.255")
    assert is_ip4("192.168.1.1")
    assert is_ip4("255.255.255.255")
    assert not is_ip4("256.0.0.1")
    assert not is_ip4("192.168.1.256")
    assert not is_ip4("192.168.1")
    assert not is_ip4("192.168.1.1.1")



# In[56]:


"""
IPv6, with 128 bits was developed to permit the expansion of the address space. 
To quote from the linked article: The 128 bits of an IPv6 address are represented in 8 groups of 16 bits each.
Each group is written as 4 hexadecimal digits and the groups are separated by colons (:). 
The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an example of this representation. 
Consecutive sections of zeros will be left as they are.
An IPv6 value such as "...:0:..." or "...:5:..." is address-wise identical 
to "...:0000:..." or "...:0005:....". Leading zeros may be omitted in writing the address.
"""


def is_ip6(s: str) -> bool:
    hex_number = r"[0-9a-fA-F]{1,4}"
    pattern = rf"^({hex_number}:){{7}}{hex_number}$"
    return re.match(pattern, s) is not None


# In[57]:


def test_is_ip6() -> None:
    assert is_ip6("2001:0db8:0000:0000:0000:ff00:0042:8329")
    assert is_ip6("fe80:0000:0000:0000:0202:b3ff:fe1e:8329")
    assert is_ip6("abcd:ef01:2345:6789:abcd:ef01:2345:6789")
    assert is_ip6("0:0:0:0:0:0:0:1")
    assert not is_ip6("2001:db8:0:0:0:ff00:42:8329:1234")  # too many groups
    assert not is_ip6("2001:db8:0:0:0:ff00:42")  # too few groups
    assert not is_ip6("2001:db8:0:0:0:ff00:42:832g")  # invalid hex digit

