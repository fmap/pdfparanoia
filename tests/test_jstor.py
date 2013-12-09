# -*- coding: utf-8 -*-

import unittest
import pdfparanoia
from pdfparanoia.parser import parse_content
from pdfminer.pdfparser import PDFSyntaxError

class JSTORTestCase(unittest.TestCase):
    def test_jstor(self):
        file_handler = open("tests/samples/jstor/0271404496b9cb5d981c10ea6aa27dd6.pdf", "rb")
        content = file_handler.read()
        file_handler.close()
        self.assertIn("\n19 0 obj\n", content)

        output = pdfparanoia.plugins.JSTOR.scrub(content)

        # FlateDecode should be replaced with a decompressed section
        self.assertIn("\n19 0 obj\n<</Length 2788", output)

        try: 
            parse_content(output)
        except PDFSyntaxError:
            self.fail("The JSTOR scrubber corrupted content.")
