from encode_and_decode_strings import Solution

strs = ["we","say",":","yes","!@#$%^&*()"]
solution = Solution()
encoded = solution.encode(strs)
decoded = solution.decode(encoded)
print("Encoded:", encoded, "Decoded:", decoded)