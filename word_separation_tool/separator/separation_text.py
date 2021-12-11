from typing import List


# 分かち書きテキスト
class SeparationText:
    def __init__(self, words: List[str]) -> None:
        """コンストラクタ

        Parameters
        ----------
        words : List[str]
            分かち書きで分割されたテキスト。リストで保持する。
        """
        self.__words = words

    def get_words(self) -> str:
        """分かち書き文字列をカンマ区切りで返す

        Returns
        -------
        str
            カンマ区切りされた文字列
        """
        return ",".join(self.__words)
