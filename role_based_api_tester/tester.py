import requests
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def create_role_tokens(num_roles):
    tokens = {}
    for i in range(num_roles):
        role = input(f"Enter name for role {i + 1}: ").strip().lower()
        token = input(f"Enter JWT token for {role}: ").strip()
        
        # Optionally: Add token validation logic here
        tokens[role] = token
    return tokens

def create_endpoints():
    endpoints = []
    num_endpoints = int(input("How many API endpoints do you want to test? "))
    for i in range(num_endpoints):
        endpoint = input(f"Enter URL for API endpoint {i + 1}: ").strip()
        if not is_valid_url(endpoint):
            print(f"Invalid URL: {endpoint}. Please enter a valid URL.")
            continue
        endpoints.append(endpoint)
    return endpoints

def test_access(endpoints, tokens):
    results = {}
    for role, token in tokens.items():
        results[role] = {}
        for endpoint in endpoints:
            headers = {'Authorization': f'Bearer {token}'}
            try:
                response = requests.get(endpoint, headers=headers, timeout=10)  # Add timeout for requests
                status_code = response.status_code

                # Store the result
                if response.ok:  # 200-299 range
                    results[role][endpoint] = f"Access granted: {status_code}"
                else:
                    results[role][endpoint] = f"Access denied: {status_code}"

            except requests.RequestException as e:
                results[role][endpoint] = f"Request failed: {str(e)}"
    
    return results

def main():
    num_roles = int(input("How many roles do you want to test? "))
    role_tokens = create_role_tokens(num_roles)
    
    endpoints = create_endpoints()
    
    results = test_access(endpoints, role_tokens)

    # Print the results without sensitive information
    for role, endpoints in results.items():
        print(f"\nResults for {role}:")
        for endpoint, result in endpoints.items():
            print(f"{endpoint}: {result}")

if __name__ == "__main__":
    main()
