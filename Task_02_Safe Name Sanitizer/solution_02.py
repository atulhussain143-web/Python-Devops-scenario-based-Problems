bucket_name= "My Project Backup"

bucket= bucket_name.split(" ")
bucket= bucket_name.replace(" ","_")
bucket= bucket.lower()
print(bucket)
