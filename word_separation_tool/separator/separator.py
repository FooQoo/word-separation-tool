from janome.tokenizer import Tokenizer
from .separation_text import SeparationText


# テキストを分かち書きに変換する
class Separator:
    def __init__(self) -> None:
        """コンストラクタ
        """
        self.tokenizer = Tokenizer()

    def convert_separation_text(self, words: str) -> SeparationText:
        """文字列を分かち書きして

        Parameters
        ----------
        words : str
            分かち書き対象文字列

        Returns
        -------
        SeparationText
            分かち書き済みのテキストクラス
        """
        tokenized = self.tokenizer.tokenize(words, wakati=True)
        word_list = [str(word) for word in tokenized if type(word) == str]
        return SeparationText(word_list)
