def sbox_1(input_bits):
    sbox = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

    row = int(str(input_bits[0]) + str(input_bits[5]), 2)
    col = int(''.join(map(str, input_bits[1:5])), 2)
    output_value = sbox[row][col]
    
    output_bits = bin(output_value)[2:].zfill(4)
    return [int(bit) for bit in output_bits]

def main():
    input_bits = [1, 0, 1, 0, 1, 0]
    output_bits = sbox_1(input_bits)

    print(f"Input bits: {input_bits}")
    print(f"Output bits: {output_bits}")

if __name__ == "__main__":
    main()
