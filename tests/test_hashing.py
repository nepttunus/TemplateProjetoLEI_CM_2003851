from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path
import unittest

from src.hashing import sha256_file


class TestHashing(unittest.TestCase):
    def test_sha256_file_matches_hashlib(self) -> None:
        content = b"teste de integridade"
        expected = hashlib.sha256(content).hexdigest()

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sample.txt"
            file_path.write_bytes(content)
            self.assertEqual(sha256_file(file_path), expected)


if __name__ == "__main__":
    unittest.main()
