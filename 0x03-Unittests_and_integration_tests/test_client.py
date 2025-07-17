#!/usr/bin/env python3
"""Parameterize and patch as decorators
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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
