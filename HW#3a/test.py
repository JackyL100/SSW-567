from main import get_commits
from main import get_repos
from main import get_repos_and_commits
import unittest
from unittest.mock import patch, Mock


class TestGithubAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_commits_valid_user_valid_repo(self, mock_get):

        mock_data = [{'id': i} for i in range(30)]
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        result = get_commits('richkempinski', 'hellogitworld')

        self.assertEqual(result, 30)
        mock_get.assert_called_once_with("https://api.github.com/repos/richkempinski/hellogitworld/commits")

    @patch('requests.get')
    def test_get_commits_invalid_user(self, mock_get):
        mock_data = {'message': "Not Found"}
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        result = get_commits('niwvbnirwvnw', 'hellogitworld')

        self.assertEqual(result, 0)
        mock_get.assert_called_once_with("https://api.github.com/repos/niwvbnirwvnw/hellogitworld/commits")

    @patch('requests.get')
    def test_get_commits_invalid_repo(self, mock_get):
        mock_data = {'message': "Not Found"}
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        result = get_commits('richkempinski', 'wiuvbwivnw')

        self.assertEqual(result, 0)
        mock_get.assert_called_once_with("https://api.github.com/repos/richkempinski/wiuvbwivnw/commits")



    @patch('requests.get')
    def test_get_repos(self, mock_get):
        mock_data = [{'name': i} for i in range(9)]
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        result = get_repos('richkempinski')

        self.assertEqual(len(result),9)
        mock_get.assert_called_once_with("https://api.github.com/users/richkempinski/repos")

    @patch('requests.get')
    def test_get_repos_invalid_user(self, mock_get):
        mock_data = [{'name': i} for i in range(9)]
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        result = get_repos('woinvioevn')

        self.assertEqual(len(result),9)
        mock_get.assert_called_once_with("https://api.github.com/users/woinvioevn/repos")

    @patch('main.get_repos')
    @patch('main.get_commits')
    def test_get_valid_repos_and_commits(self, mock_commits, mock_repos):

        mock_repo_data = [i for i in range(9)]
        mock_repos.return_value = mock_repo_data

        mock_commit_data = [i for i in range(9)]
        mock_commits.return_value = mock_commit_data
        result = get_repos_and_commits('richkempinski')
        self.assertEqual(len(result), 9)

    @patch('main.get_repos')
    @patch('main.get_commits')
    def test_get_invvalid_repos_and_commits(self, mock_commits, mock_repos):

        mock_repo_data = []
        mock_repos.return_value = mock_repo_data

        mock_commit_data = 0
        mock_commits.return_value = mock_commit_data
        result = get_repos_and_commits('')
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()