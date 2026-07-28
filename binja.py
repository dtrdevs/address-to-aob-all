# Created by dtr69
# Supports all underlying functions

from binaryninja import *

ADDRESS = 0x00000000  # Change this to your address
LENGTH = 64           # Bytes


def get_aob(bv, address, length):
    data = bv.read(address, length)
    if data is None or len(data) != length:
        print(f"Failed to read memory at 0x{address:X}")
        return None

    return " ".join(f"{b:02X}" for b in data)


def main():
    bv = BinaryView.current_view()
    if bv is None:
        print("No BinaryView is open.")
        return

    aob = get_aob(bv, ADDRESS, LENGTH)
    if aob is None:
        return

    print(f"Address: 0x{ADDRESS:X}")
    print(f"Length: {LENGTH}")
    print(aob)


if __name__ == "__main__":
    main()
