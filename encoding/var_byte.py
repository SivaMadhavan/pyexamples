def variable_byte_encode(numbers):
    encoded_bytes_list = []

    for num in numbers:
        # Keep encoding until the remaining value is greater than 0
        encoded_bytes = []
        while num > 0:
            # Extract the lower 7 bits of the current number
            byte_part = num & 0b01111111
            # Add the continuation bit to the left (if there are more bytes)
            if len(encoded_bytes) > 0:
                byte_part |= 0b10000000
            # Append the byte to the encoded list
            encoded_bytes.append(byte_part)
            # Right shift the number by 7 bits to process the next part
            num >>= 7

        # Reverse the list to maintain the correct order of bytes
        encoded_bytes.reverse()
        # Convert the list of bytes to a bytes object
        encoded_bytes_list.append(bytes(encoded_bytes))

    return encoded_bytes_list

def main():
    # Example usage
    numbers_to_encode = [300, 127, 1024, 5000]

    encoded_result = variable_byte_encode(numbers_to_encode)

    for num, encoded_bytes in zip(numbers_to_encode, encoded_result):
        print(f"Original: {num}, Encoded: {encoded_bytes}")

if __name__ == "__main__":
    main()
