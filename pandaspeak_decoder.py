from cryptography.fernet import Fernet


class BytesIntEncoder:
    @staticmethod
    def encode(b: bytes) -> int:
        return int.from_bytes(b, byteorder='big')

    @staticmethod
    def decode(i: int) -> bytes:
        return i.to_bytes(((i.bit_length() + 7) // 8), byteorder='big')

while True:
    data = input("Paste panda text here: ")
    file = open('real_key.key', 'rb')
    key = file.read()
    file.close()

    cleaned_data = ""
    data_list = data.split(" ")
    for item in data_list:
        trimmed = item[2:-2]
        cleaned_data = cleaned_data + trimmed

    encoded = ""
    for i in cleaned_data:
        encoded = encoded + str(ord(i)-97)

    encoded0 = BytesIntEncoder.decode(int(encoded))
    f = Fernet(key)

    plain_text = f.decrypt(encoded0)
    print(plain_text)