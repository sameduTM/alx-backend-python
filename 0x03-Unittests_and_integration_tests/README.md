# 0x03. Unittests and Integration Tests

## Table of Contents
- [Unit Tests](#unit-tests)
- [Back-end](#back-end)
- [Integration Tests](#integration-tests)
- [Tasks](#tasks)

## Unit Tests
- UnitTests
- Back-end
- Integration tests

## Tasks

### 0. Parameterize a unit test (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task, you will write the first unit test for `utils.access_nested_map`:

- Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
- Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
- Decorate the method with `@parameterized.expand` to test the function for the following inputs:
    - `nested_map={"a": 1}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a", "b")`
- For each of these inputs, test with `assertEqual` that the function returns the expected result.
- The body of the test method should not be longer than 2 lines.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_utils.py`

---

### 1. Parameterize a unit test (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):

- `nested_map={}, path=("a",)`
- `nested_map={"a": 1}, path=("a", "b")`

Also, make sure that the exception message is as expected.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_utils.py`

---

### 2. Mock HTTP calls (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Familiarize yourself with the `utils.get_json` function.

Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.

- Do not make any actual external HTTP calls. Use `unittest.mock.patch` to patch `requests.get`.
- Make sure it returns a Mock object with a `json` method that returns `test_payload`, which you parametrize alongside the `test_url` that you will pass to `get_json` with the following inputs:
    - `test_url="http://example.com", test_payload={"payload": True}`
    - `test_url="http://holberton.io", test_payload={"payload": False}`
- Test that the mocked `get` method was called exactly once (per input) with `test_url` as argument.
- Test that the output of `get_json` is equal to `test_payload`.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_utils.py`

---

### 3. Parameterize and patch (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Read about memoization and familiarize yourself with the `utils.memoize` decorator.

Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.

Inside `test_memoize`, define the following class:

```python
class TestClass:
        def a_method(self):
                return 42

        @memoize
        def a_property(self):
                return self.a_method()
```

- Use `unittest.mock.patch` to mock `a_method`.
- Test that when calling `a_property` twice, the correct result is returned but `a_method` is only called once using `assert_called_once`.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_utils.py`

---

### 4. Parameterize and patch as decorators (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Familiarize yourself with the `client.GithubOrgClient` class.

In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.

- This method should test that `GithubOrgClient.org` returns the correct value.
- Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but make sure it is not executed.
- Use `@parameterized.expand` as a decorator to parametrize the test with a couple of org examples to pass to `GithubOrgClient`, in this order:
    - `google`
    - `abc`
- No external HTTP calls should be made.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_client.py`

---

### 5. Mocking a property (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

`memoize` turns methods into properties. Read up on how to mock a property.

Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.

- Use `patch` as a context manager to patch `GithubOrgClient.org` and make it return a known payload.
- Test that the result of `_public_repos_url` is the expected one based on the mocked payload.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_client.py`

---

### 6. More patching (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.

- Use `@patch` as a decorator to mock `get_json` and make it return a payload of your choice.
- Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value of your choice.
- Test that the list of repos is what you expect from the chosen payload.
- Test that the mocked property and the mocked `get_json` were called once.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_client.py`

---

### 7. Parameterize (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.

Parametrize the test with the following inputs:

- `repo={"license": {"key": "my_license"}}, license_key="my_license"`
- `repo={"license": {"key": "other_license"}}, license_key="my_license"`

You should also parameterize the expected returned value.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_client.py`

---

### 8. Integration test: fixtures (mandatory)
**Score:** 0.0% (Checks completed: 0.0%)

We want to test the `GithubOrgClient.public_repos` method in an integration test. Only mock code that sends external requests.

- Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` which are part of the `unittest.TestCase` API.
- Use `@parameterized_class` to decorate the class and parameterize it with fixtures found in `fixtures.py`. The file contains the following fixtures:
    - `org_payload`
    - `repos_payload`
    - `expected_repos`
    - `apache2_repos`
- The `setUpClass` should mock `requests.get` to return example payloads found in the fixtures.
- Use `patch` to start a patcher named `get_patcher`, and use `side_effect` to make sure the mock of `requests.get(url).json()` returns the correct fixtures for the various values of `url` that you anticipate to receive.
- Implement the `tearDownClass` class method to stop the patcher.

**Repo:**
- GitHub repository: `alx-backend-python`
- Directory: `0x03-Unittests_and_integration_tests`
- File: `test_client.py`