def defangIPaddr(address: str) -> str:
        x = ''
        for c in address:
            if c == '.':
                x += '[.]'
            else:
                x += c
        return x

if __name__ == "__main__":
    address = input('> ')
    print(defangIPaddr(address))