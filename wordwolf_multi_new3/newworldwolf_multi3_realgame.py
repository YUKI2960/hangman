"""ワードウルフ(実際のゲーム)"""

from random import shuffle
import newwordwolf2_multi_function


class Game:
    """実際のゲームクラス"""
    def play_game(self):
        """関数"""
        print(input("只今から、ワードウルフを始めます"))

        # 単語設定
        print("まず、単語を設定します。GMの方は2種類の単語を設定してください。")
        word = newwordwolf2_multi_function.Word()
        word.print_word()
        # 単語リストを混ぜる(どちらが狼の単語か、設定した人(GM)すらわからない)
        shuffle(newwordwolf2_multi_function.Word.words)
        shuffle(newwordwolf2_multi_function.Word.words)
        shuffle(newwordwolf2_multi_function.Word.words)
        shuffle(newwordwolf2_multi_function.Word.words)

        # 人数設定
        print("続いて、少数派と多数派の人数を設定します")
        tango = newwordwolf2_multi_function.Ninzuu()
        tango.print_ninzuu()
        print(input("人数の設定が完了しました。"))

        # プレイヤー役割設定・話し合い
        setting = newwordwolf2_multi_function.PlayerNameSetting()
        setting.print_setting()

        # 議論
        discuss = newwordwolf2_multi_function.Discuss()
        discuss.print_discuss()

        # 投票
        voteoneset = newwordwolf2_multi_function.GameOneset()
        voteoneset.print_oneset()

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # 結果表示
        result = newwordwolf2_multi_function.Result()
        result.print_winlose()

        # 回答(enumerate関数を用いて表記: 要素番号と要素を同時に取得)
        # i カードリストのインデックス番号　answer カードリストの要素
        print("回答\n")
        for i, answer in enumerate(tango.cards0):
            print(f"{tango.playerlist0[i]}さん: 「{answer}」 ")
            print("")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


game = Game()
game.play_game()

### これは作成途中です、更新が必要です。
