# Created by dtr69
# Supports all underlying functions

import cutter

ADDRESS = 0x00000000  # Change this to your address
LENGTH = 64           # Bytes


def get_aob(address, length):
    data = cutter.cmdj(f"pxj {length} @ {address}")

    if not data:
        print(f"Failed to read memory at 0x{address:X}")
        return None

    return " ".join(f"{b:02X}" for b in data)


def main():
    aob = get_aob(ADDRESS, LENGTH)

    if aob is None:
        return

    print(f"Address: 0x{ADDRESS:X}")
    print(f"Length: {LENGTH}")
    print(aob)


if __name__ == "__main__":
    main()
