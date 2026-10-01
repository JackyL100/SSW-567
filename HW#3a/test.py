from main import get_commits
from main import get_repos
from main import get_repos_and_commits
import unittest


class TestGithubAPI(unittest.TestCase):
    def test_get_commits(self):
        self.assertEqual(get_commits('richkempinski', 'hellogitworld'), 30)
        self.assertEqual(get_commits('niwvbnirwvnw', 'hellogitworld'), 0)
        self.assertEqual(get_commits('richkempinski', 'wiuvbwivnw'), 0)

    def test_get_repos(self):
        self.assertEqual(len(get_repos('richkempinski')),9)
        self.assertEqual(get_repos('woinvioevn'), [])
        self.assertEqual(get_repos(None), [])

    def test_get_repos_and_commits(self):
        self.assertEqual(len(get_repos_and_commits('richkempinski')), 9)
        self.assertEqual(len(get_repos_and_commits('')), 0)

if __name__ == '__main__':
    unittest.main()