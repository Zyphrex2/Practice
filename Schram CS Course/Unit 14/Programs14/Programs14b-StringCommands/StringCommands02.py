# StringCommands02.py
# This program uses the <len> command to demonstrate
# a potential problem with multiline string literals.


s1 = """The quick
brown fox
jumps over
the lazy dog."""

s2 = """The quick                                    
brown fox                                            
jumps over                                               
the lazy dog."""                      

print()
print("s1 has",len(s1),"characters.")
print("s2 has",len(s2),"characters.")
 