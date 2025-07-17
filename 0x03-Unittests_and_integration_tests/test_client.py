#!/usr/bin/env python3
"""Parameterize and patch as decorators
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, MagicMock
from fixtures import TEST_PAYLOAD


# Extracting specific payloads from TEST_PAYLOAD for clarity and direct use
org_payload = TEST_PAYLOAD[0][0]
repos_payload = TEST_PAYLOAD[0][1]

# Manually derive expected_repos based on the 'apache-2.0' license from
# the provided repos_payload
expected_repos = []
for repo in repos_payload:
    if repo.get("license") and repo["license"].get("key") == "apache-2.0":
        expected_repos.append(repo.get("name"))


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """test that GithubOrgClient.org returns the correct value"""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with((expected_url))
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock)\
                as mock_org:
            mock_org.return_value = {"repos_url":
                                     "https://api.github.com/orgs/google/"
                                     "repos"
                                     ""}

            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, "https://api.github.com/orgs/google/"
                             "repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = mock_repos_payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "" \
                "https://api.github.com/orgs/testorg/repos"

            client = GithubOrgClient("testorg")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs"
                                                  "/testorg/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for `GithubOrgClient.public_repos` method.
    This class mocks external HTTP requests made by `requests.get` to simulate
    API responses, allowing for testing the complete logic flow of 
    `public_repos`
    without actual network calls.
    """
    # These class attributes will be populated by the @parameterized_class
    # decorator
    org_payload: dict
    repos_payload: list
    expected_repos: list
    apache2_repos: list

    @classmethod
    def setUpClass(cls):
        """
        Sets up the class-level mock for `requests.get`.
        This method is called once before any tests in the class are run.
        It configures `requests.get` to return predefined mock responses
        based on the URL requested.
        """
        # Create a mock response object for the organization payload.
        # When `mock_org_response.json()` is called, it will return
        # `cls.org_payload`.
        mock_org_response = MagicMock()
        mock_org_response.json.return_value = cls.org_payload

        # Create a mock response object for the repositories payload.
        # When `mock_repos_response.json()` is called, it will return
        # `cls.repos_payload`.
        mock_repos_response = MagicMock()
        mock_repos_response.json.return_value = cls.repos_payload

        # Define a `side_effect` function for `requests.get`.
        # This function will be called whenever `requests.get` is invoked.
        # It inspects the `url` argument and returns the appropriate mock
        # response.
        def get_side_effect(url):
            # The base URL for the organization (e.g.,
            # "https://api.github.com/orgs/google")
            # is derived from the 'repos_url' in org_payload.
            org_name_from_url = cls.org_payload["repos_url"].split('/')[-2]
            org_url_base = f"https://api.github.com/orgs/{org_name_from_url}"

            if url == org_url_base:
                return mock_org_response
            # The URL for the repositories list (e.g.,
            # "https://api.github.com/orgs/google/repos")
            elif url == cls.org_payload["repos_url"]:
                return mock_repos_response
            else:
                # Raise an error for any unexpected URL to ensure strict
                # testing.
                # This helps catch unintended network calls or incorrect URL
                # construction.
                raise ValueError(f"Unexpected URL requested by mock: {url}")

        # Start the patcher for `requests.get`.
        # We patch `requests.get` because it's the underlying function called
        # by
        # `get_json`.
        cls.get_patcher = patch('requests.get', side_effect=get_side_effect)
        # Store the started mock object for asserting call details in test
        # methods.
        cls.mock_requests_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher for `requests.get`.
        This method is called once after all tests in the class have run,
        cleaning up the mocked environment and restoring the original
        `requests.get`.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Tests the `public_repos` method of `GithubOrgClient` in an integration
        scenario.
        This test verifies:
        1. That `requests.get` was called with the correct URLs for fetching
           organization and repository data (via `get_json`).
        2. That the `public_repos` method correctly filters the mocked
        repository data
           and returns the expected list of repository names based on
             the license.
        """
        # The organization name ("google") is extracted from the
        # `repos_url` in the `org_payload` fixture.
        org_name = self.org_payload["repos_url"].split('/')[-2]
        client = GithubOrgClient(org_name)

        # Call the `public_repos` method. This method will internally call 
        # `client.org`
        # (which calls `get_json(org_url)`) and then `get_json(repos_url)`.
        repos = client.public_repos()

        # Assert that `requests.get` was called with the organization's 
        # base URL.
        # This call happens when `client.org` property is accessed.
        expected_org_url = f"https://api.github.com/orgs/{org_name}"
        self.mock_requests_get.assert_any_call(expected_org_url)

        # Assert that `requests.get` was called with the repositories URL.
        # This call happens after the `repos_url` is obtained from the org 
        # payload.
        expected_repos_url = self.org_payload["repos_url"]
        self.mock_requests_get.assert_any_call(expected_repos_url)

        # Assert that `requests.get` was called exactly twice,
        # confirming the expected flow.
        self.assertEqual(self.mock_requests_get.call_count, 2)

        # Assert that the list of repository names returned by `public_repos`
        # matches the `expected_repos` derived from the `TEST_PAYLOAD`,
        # confirming the filtering logic is correct.
        self.assertEqual(repos, self.expected_repos)
