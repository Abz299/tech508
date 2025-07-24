import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/ub12aa")

print(type(post_codes_req))
print(post_codes_req)

print(f"Status code: {post_codes_req.status_code}")
print(f"Headers: {post_codes_req.headers}")
print(f"Content: {post_codes_req.content}")
print(f"JSON: {post_codes_req.json()}")
print(f"Data type of JSON: {type(post_codes_req.json())}")

region = post_codes_req.json()['result']['region'] if post_codes_req.json()['status'] == 200 else "N/A"
print(f"Region: {region}")