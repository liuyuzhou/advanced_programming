from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from chapter14 import stdout_exp

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'python.org'
        expected_url = f'{protocol}://{host}.{domain}\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            stdout_exp.url_print(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)