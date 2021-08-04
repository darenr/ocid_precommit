#!/usr/bin/env python3

print("ocid_precommit.py")

def main():
    print("HERE")
    return


if __name__ == "__main__":
    rc = main()
    if not rc:
        print("Overall result: fail", file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)
