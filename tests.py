from typograf import typografy_text
import unittest


class TypografTestCase(unittest.TestCase):
	def test_check_single_guotes(self):
		text = 'Привет "Развивайся"'
		self.assertEqual(typografy_text(text), 
			'Привет «Развивайся»')

	def test_double_quotes(self):
		text = 'АО "НИИ "Путь""'
		self.assertEqual(typografy_text(text),
			'АО «НИИ "Путь"»')

	def test_digits_are_equal(self):
		text = '12-25-85'
		self.assertEqual(typografy_text(text),
			'12-25-85')

	def test_replace_hephen_with_dash_dash_in_phone_numbers(self):
		text = '+7—123—456—78—90'
		self.assertEqual(typografy_text(text),
			'+7-123-456-78-90')

	def test_remove_extra_spaces(self):
		text = 'очень   много   пробелов'
		self.assertEqual(typografy_text(text),
			'очень много пробелов')

	def test_remove_extra_line_breaks(self):
		text = 'много пустых\n\n\nстрок'
		self.assertEqual(typografy_text(text),
			'много пустых\nстрок')


if __name__ == '__main__':
	unittest.main()