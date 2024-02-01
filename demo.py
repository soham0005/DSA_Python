def min_flips_to_secure_password(pwd):
    n = len(pwd)
    min_flips = n  # Initialize with maximum possible flips

    for length in range(2, n + 1, 2):
        flips = 0

        for i in range(length):
            if (i % 2 == 0 and pwd[i] != '1') or (i % 2 == 1 and pwd[i] != '0'):
                flips += 1

        min_flips = min(min_flips, flips)

    return min_flips

# Example usage
pwd = "100110"
result = min_flips_to_secure_password(pwd)
print(result)  # Output: 3

