# Role Based API Tester

**Role Based API Tester** is a Python library designed for cybersecurity professionals to dynamically test API access controls using roles and JWT tokens. It helps you ensure robust role-based access control (RBAC) in APIs and detects potential privilege escalation issues.

## Introduction

Role Based API Tester enables you to validate the security of API endpoints by testing the access levels granted to various user roles using JWT tokens. This helps identify misconfigurations that could allow unauthorized users to gain higher privileges, a critical aspect of API security in preventing attacks such as privilege escalation.

## Installation

To use Role Based API Tester, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/RoleBasedAPITester.git
    cd RoleBasedAPITester
    ```

2. Install the necessary dependencies:

    ```bash
    pip install .
    ```

## Usage

Once the library is installed, you can use it to test APIs with different roles and JWT tokens:

1. Run the script:

    ```bash
    role_based_api_tester
    ```

2. Follow the prompts to:
   - Enter the number of roles and their names.
   - Input the JWT tokens for each role.
   - Provide the list of API endpoints you want to test.

3. The tool will output whether each role can access specific endpoints and identify any unauthorized access.

Example of usage:
```bash
# Run the script
role_based_api_tester
