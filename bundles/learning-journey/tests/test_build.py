import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('journey_build', ROOT / 'build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildTests(unittest.TestCase):
    def test_config(self):
        config = json.loads((ROOT / 'pack.json').read_text())
        build.validate_config(config)
        self.assertFalse(config['live_db11_sync'])
        self.assertFalse(config['automatic_telemetry'])
        self.assertEqual(config['tested_products'], [])

    def test_unsafe_modules_rejected(self):
        config = json.loads((ROOT / 'pack.json').read_text())
        config['runtime_modules'] = ['../secret']
        with self.assertRaises(ValueError):
            build.validate_config(config)

    def test_email_rejected(self):
        email = 'private' + '@' + 'example.org'
        with self.assertRaises(ValueError):
            build.privacy_check({'note.txt': email.encode()})

    def test_private_link_rejected(self):
        private = 'collection' + '://' + 'private-source'
        with self.assertRaises(ValueError):
            build.privacy_check({'note.txt': private.encode()})

    def test_credential_rejected(self):
        secret = 'ghp_' + 'a' * 24
        with self.assertRaises(ValueError):
            build.privacy_check({'note.txt': secret.encode()})

    def test_path_traversal_rejected(self):
        for name in ['../note.txt', '/note.txt', 'sub/../../note.txt', 'sub\\note.txt']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                build.privacy_check({name: b'ordinary text'})

    def test_ordinary_text_allowed(self):
        build.privacy_check({'note.txt': b'Use synthetic training facts.'})

    def test_runtime_integrity_and_separation(self):
        config, payload, _, _ = build.source_inputs()
        prompt = build.make_prompt(config, payload).decode()
        self.assertIn(build.END_MARKER, prompt)
        for stage in range(9):
            self.assertIn('J' + str(stage) + '/8', prompt)
        self.assertNotIn('Private observation worksheet', prompt)
        self.assertNotIn('## Refresh protocol', prompt)
        self.assertIn('Learner self-report', prompt)
        self.assertIn('session preferences — provisional', prompt)
        self.assertIn('Stop pauses immediately', prompt)
        self.assertIn('one short question', prompt)

    def test_manifest_and_generated_prompt(self):
        config, payload, _, inputs = build.source_inputs()
        manifest = json.loads((ROOT / 'manifest.json').read_text())
        self.assertEqual(inputs, manifest['input_sha256'])
        self.assertEqual((ROOT / 'START-HERE.txt').read_bytes(), build.make_prompt(config, payload))
        self.assertEqual(manifest['target_product_trial'], 'pending')

    def test_zip_complete_and_hashes(self):
        config = json.loads((ROOT / 'pack.json').read_text())
        archive = ROOT / 'dist' / f"ai-learning-journey-v{config['version']}.zip"
        manifest = json.loads((ROOT / 'manifest.json').read_text())
        with zipfile.ZipFile(archive) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(len(z.namelist()), len(set(z.namelist())))
            self.assertEqual(set(z.namelist()), set(manifest['files_sha256']) | {'manifest.json'})
            for name, sha in manifest['files_sha256'].items():
                self.assertEqual(build.digest(z.read(name)), sha, name)
            for skill in json.loads(z.read('LIBRARY-INDEX.json'))['skills']:
                self.assertIn('LIBRARY/skill-seeds/prompts/' + skill['id'] + '.md', z.namelist())

    def test_corrupt_and_duplicate_zip_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / 'bad.zip'
            archive.write_bytes(b'not a zip')
            with self.assertRaises(zipfile.BadZipFile):
                build.verify_zip(archive, {'a.txt': b'A'})
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('a.txt', b'A')
                z.writestr('extra.txt', b'extra')
            with self.assertRaises(ValueError):
                build.verify_zip(archive, {'a.txt': b'A'})

    def test_payload_tamper_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / 'tampered.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('a.txt', b'changed')
            with self.assertRaises(ValueError):
                build.verify_zip(archive, {'a.txt': b'original'})


if __name__ == '__main__':
    unittest.main()
