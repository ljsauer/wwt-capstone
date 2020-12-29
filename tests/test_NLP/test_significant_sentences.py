import unittest

from app.NLP.significant_sentences import SignificantSentences


class TestSignificantSentences(unittest.TestCase):

    def setUp(self) -> None:
        self.text = "This is a test text. Test, test. Text test text, Tex, text. Goodbye, Text."
        self.sig_sents = SignificantSentences(self.text, n_sentences=1)

    def test_gets_significant_sentences(self):
        self.assertEqual(
            self.sig_sents.get_significant_sentences(),
            ["Text test text, Tex, text."]
        )
        self.assertTrue('text' in self.sig_sents.word_ranking.values())
