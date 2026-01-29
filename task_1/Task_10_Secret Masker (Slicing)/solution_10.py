api_key ="AKIA1234567890EXAMPLE"

visible_part = api_key[:4]

length=len(api_key)

masked_part = "*" * (length - 4)
masked_key = visible_part + masked_part

print(masked_key)