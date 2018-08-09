x=13
print((x & 0xAAAAAAAA)>>1)
print((x & 0x55555555)<<1)
print(((x & 0xAAAAAAAA)>>1) | ((x & 0x55555555)<<1))
