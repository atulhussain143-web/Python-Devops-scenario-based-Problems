url="https://api.github.com/v3"

part=url.split('/')

#print(part)


subdomain = part[2]
domain = subdomain.replace("api.", "")
print(domain)