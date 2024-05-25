import numpy as np

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv

def encrypt(message, K):
    encrypted = ""
    message_in_numbers = [letter_to_index[letter] for letter in message]

    split_P = [message_in_numbers[i : i + int(K.shape[0])] for i in range(0, len(message_in_numbers), int(K.shape[0]))]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index["x"])[:, np.newaxis]  # Padding with 'x'
        numbers = np.dot(K, P) % len(alphabet)
        encrypted += ''.join(index_to_letter[int(numbers[idx, 0])] for idx in range(numbers.shape[0]))
    
    return encrypted

def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = [letter_to_index[letter] for letter in cipher]

    split_C = [cipher_in_numbers[i : i + int(Kinv.shape[0])] for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        decrypted += ''.join(index_to_letter[int(numbers[idx, 0])] for idx in range(numbers.shape[0]))
    
    return decrypted

def get_key_matrix():
    try:
        n = int(input("Enter the size of the key matrix (e.g., 2 for 2x2, 3 for 3x3): "))
        print(f"Enter the elements of the {n}x{n} key matrix row by row (space-separated):")
        elements = []
        for i in range(n):
            row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
            if len(row) != n:
                raise ValueError("Invalid row length.")
            elements.extend(row)
        key_matrix = np.array(elements).reshape(n, n)
        return key_matrix
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    message = "rijangurung"

    K = get_key_matrix()
    if K is None:
        return

    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)

main()
