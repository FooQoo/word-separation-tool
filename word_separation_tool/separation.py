from separator.separator import Separator
import logging
import sys
import argparse


# ロギング設定
logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)

# ロギングのフォーマット設定
fmt = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    "%Y-%m-%dT%H:%M:%S")
sh.setFormatter(fmt)
logger.addHandler(sh)

# コマンドライン引数設定
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="分かち書き対象文字列", type=str)
args = parser.parse_args()


def separtion(input: str) -> str:
    """分かち書き実行関数

    Parameters
    ----------
    input : str
        入力値

    Returns
    -------
    str
        カンマ区切り文字列
    """
    separator = Separator()
    separation_text = separator.convert_separation_text(input)
    logger.info(f"入力文字列:{input}")
    logger.info(f"分かち書き文字列:{separation_text.get_words()}")

    return separation_text.get_words()


if __name__ == '__main__':
    input = args.input
    sepration_words = separtion(input)
    print(f"分かち書き結果:{sepration_words}")
