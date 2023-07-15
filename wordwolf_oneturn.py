"""ワードウルフ(1ターンで終了)"""

from random import shuffle
import time


class Word:
    """単語設定のクラス"""
    Words: list[str] = []

    def print_word(self):
        """単語設定の関数定義"""
        # 正しい操作するまでwhileループ
        king = 0
        while king < 1:
            # 2種類の単語を設定
            word1 = input("単語1:")
            word2 = input("単語2:")
            # 同じ単語、空欄の場合はじく
            if word1 == "" or word2 == "":
                print("空欄にはできません。入力し直してください。\n")
                continue
            else:
                pass

            if word1 == word2:
                print("2種類の単語が同じです。入力し直してください。\n")
                continue
            else:
                pass
            print("")
            # スペルミス確認のため、問題なければ「OK」と入力させる
            # print("単語は「{}」と「{}」です。間違いありませんか？\n".format(word1, word2))
            print(f"単語は「{word1}」と「{word2}」です。間違いありませんか？\n")
            confirm = input("OKなら「OK」と入力してください。それ以外入力or空欄の場合修正になります。:")
            if confirm == "OK":
                king += 2
            else:
                print("OKと入力しなかったので、もう一度単語を設定します。\n")
                continue

        # 単語を「Word」のリストに追加(後ほど、最初の要素の方を狼とする)
        Word.Words.append(word1)
        Word.Words.append(word2)
        print("")


class Ninzuu:
    """人数設定のクラス"""
    cards: list[str] = []
    playerlist: list[str] = []

    def print_ninzuu(self):
        """人数の関数定義"""

        # 狼と村の人数を設定(両方とも自然数でない場合、狼≧村の場合はじく)
        # 数設定後、カードリストに設定人数分の単語追加
        # ①狼の単語(Wordリストの0番目)を人数分追加→②村の単語(Wordリストの1番目)を人数分追加
        settings = 0
        while settings < 3:
            jinroo = input("狼側の人数:")
            citizen = input("村側の人数:")
            if jinroo.isdecimal() and citizen.isdecimal():
                for settings in range(int(jinroo)):
                    Ninzuu.cards.append(Word.Words[0])
                for settings in range(int(citizen)):
                    Ninzuu.cards.append(Word.Words[1])
                settings += 1
            else:
                print("入力できるのは自然数のみです。小数・文字列のいずれかが含まれています。入力し直してください。\n")
                continue

            if int(jinroo) >= int(citizen):
                print("狼側の人数が村側以上、あるいは同数です。ゲームが成立しません。入力し直してください。\n")
                Ninzuu.cards = []
                continue
            else:
                pass

            if int(jinroo) <= 0 or int(citizen) <= 0:
                print("0または負の数を入力することはできません。入力し直してください。\n")
                Ninzuu.cards = []
                continue
            else:
                settings += 3  # whileループ終了

        # カードリストをシャッフル
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)
        shuffle(Ninzuu.cards)


class PlayerNameSetting(Ninzuu):
    """プレイヤーに単語を与えるクラス"""
    def print_setting(self):
        """プレイヤーと単語を設定する関数を定義"""
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      # ←行替えがないと画面最大化した時にネタバレになる
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # ↑1人目と2人目の単語が同画面に映るのを防止
        print(input("続いて、プレイヤー名と単語を設定します。\n\n\n\n\n\n\n\n"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # カードリストの要素数分のプレイヤーを設定
        for i in range(len(Ninzuu.cards)):
            name = input("プレーヤーの名前を入力してください:")
            print(input(f"{name}さんの単語を確認します。Enterを押してください。\n\n\n\n\n\n\n\n"))

            # カードリストとプレイヤーリストの要素は対応している
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{name}さんの単語は、「{Ninzuu.cards[i]}」です\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(input("確認したら、「Enter」を押してください。"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # ここでプレイヤーリストを作成
            Ninzuu.playerlist.append(name)
            if i == len(Ninzuu.cards)-1:
                pass
            else:
                print(input("次の方に回してください。回したらEnterを押してください。\n\n\n\n\n\n\n\n\n\n\n\n\n"))
                # ↑最後のプレイヤー以外であれば表示

        print(Ninzuu.playerlist)
        print(input("全員の単語が確認できました。プレイヤーの名前はこちらです↑。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(input("只今から、話し合いの時間です。時間は5分です。(Enterを押して測定開始)"))
        time.sleep(1)     # 設定した秒数だけ一時停止
        print(input("5分経過しました。話し合いを終了してください。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(input("今の話し合いから、狼だと思う人を1人選んで下さい。"))


class Voting(Ninzuu):
    """投票クラス"""
    Vote1: list[int] = []
    maxvote = 0    # 最初は適当に0を設定して後から上書き
    indexes: list[int] = []   # ↑クラス外でも定義できるようにするため

    def print_voting(self):
        """投票用関数"""
        Voting.Vote1 = []   # 再投票で回ってきた場合のため、一旦投票リストを空にする意図
        for i in range(len(Ninzuu.playerlist)):
            Voting.Vote1.append(0)
        print("")

        votenumber = 0
        while votenumber < len(Ninzuu.playerlist):
            print("\n\n\n\n\n\n\n\n\n")
            print(f"{Ninzuu.playerlist[votenumber]}さんの投票です。")
            print("\n\n\n\n\n\n\n\n\n")
            # 投票者を番号で設定
            mojiretsu1list = []
            for i, votetime in enumerate(Ninzuu.playerlist):
                mojiretsu1 = f"{votetime}さんだと思う場合は {i} "
                mojiretsu1list.append(mojiretsu1)
                mojiretsu2 = "を入力してください。"
                print(mojiretsu1+mojiretsu2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # 投票(↑の範囲内の数値しか受け付けない)
            tuihou = input(f"{Ninzuu.playerlist[votenumber]}さんは誰が狼だと思いますか？:")
            if tuihou.isdecimal():   # 数値のみの場合
                tuihou = int(tuihou)
                if tuihou < len(Ninzuu.playerlist):
                    pass
                else:
                    print("回答の範囲外です。もう一度入力してください。")
                    print("")
                    continue
            else:
                print("回答が数値ではありません。もう一度入力してください。")
                print("")
                continue
            # 投票ミスがないよう、問題なければ「OK」と入力させる
            print(f"\n{Ninzuu.playerlist[tuihou]}さんに投票します。よろしいでしょうか？")
            confirm = input("OKなら「OK」と入力してください。それ以外入力or空欄の場合修正になります。:")
            if confirm == "OK":
                Voting.Vote1[tuihou] += 1
                votenumber += 1
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("OKと入力しなかったので、投票し直します。\n")
                continue

            if votenumber == len(Ninzuu.playerlist):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print(input("次の方に回してください。回したらEnterを押してください。\n\n\n\n\n\n\n\n\n\n\n"))
                print("\n\n\n\n\n\n\n")

        # 投票数公開
        for i, hyousuu in enumerate(Ninzuu.playerlist):
            print(f"{hyousuu}さん: {Voting.Vote1[i]}票")
        Voting.maxVote = max(Voting.Vote1)
        # 最大投票数の人のインデックスを取得
        Voting.indexes = [i for i, x in enumerate(Voting.Vote1) if x == Voting.maxVote]
        print("")


class VotingAgain(Voting):
    """投票数が同じ人がいた場合、再投票するクラス"""
    def print_again(self):
        """再投票の関数定義"""
        # 同じ投票者の表示
        print(f"{Voting.maxVote}票で、下記の人の投票数が同じです")
        for i in Voting.indexes:
            print(f"{Ninzuu.playerlist[i]}さん")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print(input("もう一度話し合いをしてください。時間は1分です。「Enter」を押すとカウントされます。"))
        time.sleep(1)
        print(input("1分経過しました。話し合いを終了してください。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(input("今の話し合いから、狼だと思う人を1人選んで下さい。"))

        # 投票方法はVotingクラスと同じため、使いまわす
        touhyou1 = Voting()
        touhyou1.print_voting()


class Result(Voting):
    """結果表示"""
    # カードリストの狼の単語のインデックスと、最大投票数の人のインデックスが同じか判断
    def print_winlose(self):
        """勝敗の関数定義"""
        if Ninzuu.cards.index(Word.Words[0]) == Voting.Vote1.index(Voting.maxVote):
            print("村側の勝利です。\n")
            print("\n勝者")
            # 要素が少数派の単語であるリスト番号を全て取得
            winner = [i for i, x in enumerate(Ninzuu.cards) if x != Word.Words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards) if x == Word.Words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist[lose]}さん")
            print("\n")
        else:
            print("狼側の勝利です。\n")
            print("\n勝者")
            winner = [i for i, x in enumerate(Ninzuu.cards) if x == Word.Words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards) if x != Word.Words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist[lose]}さん")
            print("\n")

    # 回答公開
    # 回答(enumerate関数を用いて表記: 要素番号と要素を同時に取得)
        # i カードリストのインデックス番号　answer カードリストの要素
        print("回答\n")
        for i, answer in enumerate(Ninzuu.cards):
            print(f"{Ninzuu.playerlist[i]}さん: 「{answer}」 ")
            print("")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


class Game:
    """実際のゲームクラス"""
    def play_game(self):
        """ゲームの関数定義"""
        print(input("只今から、ワードウルフを始めます"))

        # 単語設定
        print("まず、単語を設定します。GMの方は2種類の単語を設定してください。")
        word = Word()
        word.print_word()
        # 単語リストを混ぜる(どちらが狼の単語か、設定した人(GM)すらわからない)
        shuffle(Word.Words)
        shuffle(Word.Words)
        shuffle(Word.Words)
        shuffle(Word.Words)

        # 人数設定
        print("続いて、狼側と村側の人数を設定します")
        tango = Ninzuu()
        tango.print_ninzuu()
        print(input("人数の設定が完了しました。"))

        # プレイヤー役割設定・話し合い
        setting = PlayerNameSetting()
        setting.print_setting()

        # 投票
        touhyou = Voting()
        touhyou.print_voting()
        # 同じ投票数の人がいたら、再投票
        while len(touhyou.indexes) != 1:
            touhyou_again = VotingAgain()
            touhyou_again.print_again()
        print(input(f"投票の結果、{tango.playerlist[touhyou.Vote1.index(touhyou.maxVote)]}さんが追放されました。"))
        print(input("Enterを押してください。結果が表示されます。\n\n\n\n\n\n"))

        # 結果表示
        result = Result()
        result.print_winlose()


game = Game()
game.play_game()
