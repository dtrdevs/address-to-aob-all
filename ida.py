# Created by dtr69
# Supports sub_ , data_ , qword_ and fastflags

import ida_bytes
import ida_idaapi

ADDRESS = 0x0000000 # change this to your address
LENGTH = 64 # bytes

def get_aob(address, length):
    data = ida_bytes.get_bytes(address, length)
    if data is None:
        print(f"Failed to read memory at 0x{address:X}")
        return
    return " ".join(f"{b:02X}" for b in data)

def main():
    if ADDRESS == ida_idaapi.BADADDR:
        print("Invalid address.")
        return

    aob = get_aob(ADDRESS, LENGTH)
    if aob is None:
        return

    print(f"Address: 0x{ADDRESS:X}")
    print(f"Length: {LENGTH}")
    print(aob)

if __name__ == "__main__":
    main()
