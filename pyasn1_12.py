from pyasn1.type import univ

asn1IntegerValue = univ.Integer(23)
print(asn1IntegerValue - 28)
print(univ.OctetString(b'ALBERT') == b'ALBERT')
