# -*- coding: utf-8 -*-

import unittest
from pdfparanoia.eraser import remove_object_by_id, find_xref_section_offset

class EraserTestCase(unittest.TestCase):
    def test_remove_object_by_id(self):
        content = ""
        output = remove_object_by_id(content, 1)
        self.assertEqual(content, output)

        content = ""
        output = remove_object_by_id(content, 2)
        self.assertEqual(content, output)

        content = ""
        output = remove_object_by_id(content, 100)
        self.assertEqual(content, output)

        content = "1 0 obj\nthings\nendobj\nleftovers"
        output = remove_object_by_id(content, 2)
        self.assertEqual(content, output)

        content = "1 0 obj\nthings\nendobj\nleftovers"
        output = remove_object_by_id(content, 1)
        self.assertEqual("leftovers", output)
    def test_find_xref_section_offset(self):
        file_handler = open("tests/samples/jstor/0271404496b9cb5d981c10ea6aa27dd6.pdf", "rb")
        content = file_handler.read()
        file_handler.close()
        output = find_xref_section_offset(content)
        self.assertEqual(2290213, output)
        file_handler = open("tests/samples/jstor/231a515256115368c142f528cee7f727.pdf", "rb")
        content = file_handler.read()
        file_handler.close()
        output = find_xref_section_offset(content)
        self.assertEqual(191784, output)
