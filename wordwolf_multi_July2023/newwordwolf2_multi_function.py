"""ワードウルフ"""
# クラス: 頭文字は大文字、_を使わない、前後2行空ける、次の行に"""をつけて説明
# defの関数定義: 前後1行空ける、次の行に"""をつけて説明　　変数: 全て小文字

from random import shuffle
import random
import time


class Word:
    """単語設定クラス"""
    words: list[str] = []

    def print_word(self):
        """単語設定の関数"""
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
            print(f"単語は「{word1}」と「{word2}」です。間違いありませんか？\n")
            confirm = input("OKなら「OK」と入力してください。それ以外入力or空欄の場合修正になります。:")
            if confirm == "OK" or confirm == "ok" or confirm == "Ok" or confirm == "oK":
                king += 2
            else:
                print("OKと入力しなかったので、もう一度単語を設定します。\n")
                continue

        # 単語を「Word」のリストに追加(後ほど、最初の要素の方を狼とする)
        Word.words.append(word1)
        Word.words.append(word2)

        shuffle(Word.words)
        shuffle(Word.words)
        shuffle(Word.words)
        shuffle(Word.words)
        shuffle(Word.words)
        shuffle(Word.words)
        print("")


class Ninzuu:
    """人数設定のクラス"""
    cards0: list[str] = []
    cards1: list[str] = []
    playerlist0: list[str] = []    # 0 固定
    playerlist1: list[str] = []    # 1 追放者が出たらへる
    OOkamiindexes = 0   # 少数派の単語のリスト番号のみ抽出
    Turnnumber = 1   # ターンの数を定義(初期値は1)
    jinroo = "少数派"    # ターン数を狼(少数派)の人数によって変える

    def print_ninzuu(self):
        """人数設定の関数"""

        # 狼と村の人数を設定(両方とも自然数でない場合、狼≧村の場合はじく)
        # 数設定後、カードリストに設定人数分の単語追加
        # ①狼の単語(Wordリストの0番目)を人数分追加→②村の単語(Wordリストの1番目)を人数分追加
        settings = 0
        while settings < 4:
            Ninzuu.jinroo = input("少数派の人数:")
            citizen = input("多数派の人数:")
            if Ninzuu.jinroo.isdecimal() and citizen.isdecimal():
                for settings in range(int(Ninzuu.jinroo)):
                    Ninzuu.cards0.append(Word.words[0])
                for settings in range(int(citizen)):
                    Ninzuu.cards0.append(Word.words[1])
                settings += 1
            else:
                print("入力できるのは自然数のみです。小数・文字列のいずれかが含まれています。入力し直してください。\n")
                continue

            if int(Ninzuu.jinroo) >= int(citizen):
                print("少数派の人数が多数派以上、あるいは同数です。ゲームが成立しません。入力し直してください。\n")
                Ninzuu.cards0 = []
                continue
            else:
                pass

            if int(Ninzuu.jinroo) <= 0 or int(citizen) <= 0:
                print("0または負の数を入力することはできません。入力し直してください。\n")
                Ninzuu.cards0 = []
                continue
            else:
                settings = 3

            # 人数確認
            print(f"\n少数派が{int(Ninzuu.jinroo)}人の場合、{2 * int(Ninzuu.jinroo)+1}ターンで決着となります。")
            confirm = input("よろしければ「OK」と入力してください。それ以外入力or空欄の場合人数の設定をします。:")
            if confirm == "OK" or confirm == "ok" or confirm == "Ok" or confirm == "oK":
                settings += 1    # whileループ終了
            else:
                print("OKと入力しなかったので、再度人数を設定します。\n")
                Ninzuu.cards0 = []
                continue

        # カードリストをシャッフル
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)
        shuffle(Ninzuu.cards0)

        # シャッフルしたカード0リストと全く同じリストを作成
        Ninzuu.cards1 = Ninzuu.cards0.copy()


class PlayerNameSetting(Ninzuu):
    """プレイヤーと単語を設定するクラス"""
    def print_setting(self):
        """プレイヤー・単語設定の関数"""
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      # ←行替えがないと画面最大化した時にネタバレになる
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # ↑1人目と2人目の単語が同画面に映るのを防止
        print(input("続いて、プレイヤー名と単語を設定します。\n\n\n\n\n\n\n\n\n\n\n"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # カードリストの要素数分のプレイヤーを設定
        for i, playername in enumerate(Ninzuu.cards0):
            name = input("プレーヤーの名前を入力してください:")
            print(input(f"{name}さんの単語を確認します。Enterを押してください。\n\n\n\n\n\n\n\n"))

            # カードリストとプレイヤーリストの要素は対応している
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{name}さんの単語は、「{playername}」です\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(input("確認したら、「Enter」を押してください。"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # ここでプレイヤーリストを作成
            Ninzuu.playerlist0.append(name)
            Ninzuu.playerlist1.append(name)
            if i == len(Ninzuu.cards0)-1:
                pass
            else:
                # 最後のプレイヤー以外であれば表示
                print(input("次の方に回してください。回したらEnterを押してください。\n\n\n\n\n\n\n\n\n\n\n\n\n"))

        print(Ninzuu.playerlist1)
        print(input("全員の単語が確認できました。プレイヤーの名前はこちらです↑。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # 要素が少数派の単語であるリスト番号を全て取得
        Ninzuu.OOkamiindexes = [i for i, x in enumerate(Ninzuu.cards0) if x == Word.words[0]]


class Discuss():
    """議論のクラス"""
    def print_discuss(self):
        """議論の関数"""
        print("只今から議論の時間です。GMも議論に参加します。")
        print("(GMが知っているのは2つの単語のみで、誰が少数派の単語か、どちらの単語が少数派かは知りません。)")
        print(input("時間は2分です。(Enterを押して測定開始)"))
        time.sleep(1)
        print(input("指定の時間が経過しました。話し合いを終了してください。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(input("今の話し合いから、少数派だと思う人を1人選んで下さい。"))


class DiscussAgain():
    """ゲームが続く場合の再議論クラス"""
    def print_discussagain(self):
        """再議論の関数"""
        print(input("もう一度話し合いをしてください。話し合いは1分半です。「Enter」を押すとカウントされます。"))
        time.sleep(1)
        print(input("1分経過しました。話し合いを終了してください。"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(input("今の話し合いから、少数派だと思う人を1人選んで下さい。"))


class Voting(Ninzuu):
    """投票クラス"""
    Vote1: list[int] = []
    maxvote = 0    # 最初は適当に0を設定して後から上書き
    indexes: list[int] = []    # ↑クラス外でも定義できるようにするため
    voteturn = 0    # 投票回数(2回目にもつれた場合決戦投票)

    def print_voting(self):
        """投票の関数定義"""
        Voting.Vote1 = []   # 再投票で回ってきた場合のため、一旦投票リストを空にする意図
        for i in range(len(Ninzuu.playerlist1)):
            Voting.Vote1.append(0)
        print("")

        votenum = 0
        while votenum < len(Ninzuu.playerlist1):
            print("\n\n\n\n\n\n\n\n\n")
            print(f"{Ninzuu.playerlist1[votenum]}さんの投票です。")
            print("\n\n\n\n\n\n\n\n\n")

            # 投票者を番号で設定
            mojiretsu1list = []
            for i, votetime in enumerate(Ninzuu.playerlist1):
                mojiretsu1 = f"{votetime}さんだと思う場合は {i} "
                mojiretsu1list.append(mojiretsu1)
                mojiretsu2 = "を入力してください。"
                print(mojiretsu1+mojiretsu2)
            print(f"残りプレイヤー: {Ninzuu.playerlist1}")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # 投票(↑の範囲内の数値しか受け付けない)
            tuihou = input(f"{Ninzuu.playerlist1[votenum]}さんは誰が少数派だと思いますか？:")
            if tuihou.isdecimal():   # 数値のみの場合
                tuihou = int(tuihou)
                if tuihou < len(Ninzuu.playerlist1):
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
            print(f"\n{Ninzuu.playerlist1[tuihou]}さんに投票します。よろしいでしょうか？")
            confirm = input("OKなら「OK」と入力してください。それ以外入力or空欄の場合修正になります。:")
            if confirm == "OK" or confirm == "ok" or confirm == "Ok" or confirm == "oK":
                Voting.Vote1[tuihou] += 1
                votenum += 1
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("OKと入力しなかったので、投票し直します。\n")
                continue

            if votenum == len(Ninzuu.playerlist1):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                # 最後のプレイヤー以外であれば表示
                print(input("次の方に回してください。回したらEnterを押してください。\n\n\n\n\n\n\n\n\n\n\n"))
                print("\n\n\n\n\n\n\n")

        # 投票数公開
        for i, hyousuu in enumerate(Ninzuu.playerlist1):
            print(f"{hyousuu}さん: {Voting.Vote1[i]}票")
        Voting.maxVote = max(Voting.Vote1)
        # 最大投票数の人のインデックスを取得
        Voting.indexes = [i for i, x in enumerate(Voting.Vote1) if x == Voting.maxVote]
        print("")


class VotingAgain(Voting):
    """投票数が同じ人がいた場合、再投票"""
    finalvote: list[str] = []

    def print_again(self):
        """再投票の関数"""
        # 同じ投票者の表示
        VotingAgain.finalvote = []   # 再投票対象者を表示前に空にする(前のターンの分を消す)
        print(f"{Voting.maxVote}票で、下記の人の投票数が同じです")
        for i in Voting.indexes:
            print(f"{Ninzuu.playerlist1[i]}さん")
            VotingAgain.finalvote.append(Ninzuu.playerlist1[i])   # 同じ最大投票者のリスト作成
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        discuss_again = DiscussAgain()
        discuss_again.print_discussagain()

        Voting.Vote1 = []   # 再投票で回ってきた場合のため、一旦投票リストを空にする意図
        for i in range(len(VotingAgain.finalvote)):
            Voting.Vote1.append(0)
        print("")

        votenum2 = 0
        while votenum2 < len(Ninzuu.playerlist1):
            print("\n\n\n\n\n\n\n\n\n")
            print(f"{Ninzuu.playerlist1[votenum2]}さんの投票です。")
            print("\n\n\n\n\n\n\n\n\n")

            # 投票者を番号で設定(決選投票)
            mojiretsu1list = []
            for i, votetime in enumerate(VotingAgain.finalvote):
                mojiretsu1 = f"{votetime}さんだと思う場合は {i} "
                mojiretsu1list.append(mojiretsu1)
                mojiretsu2 = "を入力してください。"
                print(mojiretsu1+mojiretsu2)
            print(f"投票対象者: {VotingAgain.finalvote}")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # 投票(↑の範囲内の数値しか受け付けない)
            tuihou = input(f"{Ninzuu.playerlist1[votenum2]}さんは誰が少数派だと思いますか？:")
            if tuihou.isdecimal():   # 数値のみの場合
                tuihou = int(tuihou)
                if tuihou < len(VotingAgain.finalvote):
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
            print(f"\n{VotingAgain.finalvote[tuihou]}さんに投票します。よろしいでしょうか？")
            confirm = input("OKなら「OK」と入力してください。それ以外入力or空欄の場合修正になります。:")
            if confirm == "OK" or confirm == "ok" or confirm == "Ok" or confirm == "oK":
                Voting.Vote1[tuihou] += 1
                votenum2 += 1
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("OKと入力しなかったので、投票し直します。\n")
                continue

            if votenum2 == len(Ninzuu.playerlist1):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                # 最後のプレイヤー以外であれば表示
                print(input("次の方に回してください。回したらEnterを押してください。\n\n\n\n\n\n\n\n\n\n\n"))
                print("\n\n\n\n\n\n\n")

        # 投票数公開
        for i, hyousuu2 in enumerate(VotingAgain.finalvote):
            print(f"{hyousuu2}さん: {Voting.Vote1[i]}票")
        Voting.maxVote = max(Voting.Vote1)
        # 最大投票数の人のインデックスを取得
        Voting.indexes = [i for i, x in enumerate(Voting.Vote1) if x == Voting.maxVote]
        print("")

        # 2回目で票が割れた場合、ランダムに追放者を決める
        if len(Voting.indexes) != 1:
            randomindex = random.choice(Voting.indexes)   # 最大投票数の人から1人のindexをランダムで取得
            randomchoice = VotingAgain.finalvote[randomindex]  # 決戦投票者リストの追放者を指定
            print(randomindex)
            print(randomchoice)

            print(f"投票の結果、{randomchoice}さんが追放されました。")
            print(input("Enterを押してください。ゲームの継続・終了を判断します。\n\n\n\n\n\n"))

            # 追放者の名前と単語を削除
            Ninzuu.cards1.pop(Ninzuu.playerlist1.index(randomchoice))    # cardから先に消す(後から消すとエラー)
            Ninzuu.playerlist1.pop(Ninzuu.playerlist1.index(randomchoice))
        else:
            print(f"投票の結果、{Ninzuu.playerlist1[Voting.Vote1.index(Voting.maxVote)]}さんが追放されました。")
            print(input("Enterを押してください。ゲームの継続・終了を判断します。\n\n\n\n\n\n"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

            # 追放者の名前と単語を削除
            Ninzuu.cards1.pop(Voting.Vote1.index(Voting.maxVote))
            Ninzuu.playerlist1.pop(Voting.Vote1.index(Voting.maxVote))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")


class Vanish(Voting):
    """追放クラス"""

    def print_vanish(self):
        """追放の関数"""
        print(f"投票の結果、{Ninzuu.playerlist1[Voting.Vote1.index(Voting.maxVote)]}さんが追放されました。")
        print(input("Enterを押してください。ゲームの継続・終了を判断します。\n\n\n\n\n\n"))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # 追放者の名前と単語を削除
        Ninzuu.cards1.pop(Voting.Vote1.index(Voting.maxVote))
        Ninzuu.playerlist1.pop(Voting.Vote1.index(Voting.maxVote))


class GameOneset(Vanish):
    """投票・追放をまとめたクラス"""
    def print_oneset(self):
        """投票・追放がセットになった関数"""
        touhyou = Voting()
        touhyou.print_voting()

        if len(touhyou.indexes) != 1:
            touhyou_again = VotingAgain()
            touhyou_again.print_again()
        else:
            vvanish = Vanish()
            vvanish.print_vanish()


class Result(Vanish):
    """結果表示クラス"""
    # 追放後の残った単語・プレイヤーから、ゲームの継続・勝利陣営を判断
    def print_winlose(self):
        """勝敗・継続を判断する関数"""
        # 狼(少数派)が完全にいなくなった場合、決着(村の勝ち)
        if Word.words[0] not in Ninzuu.cards1:
            print("ここで、少数派の人はいなくなりました。多数派の勝利です。\n")
            print("\n勝者")
            # 要素が少数派の単語であるリスト番号を全て取得
            winner = [i for i, x in enumerate(Ninzuu.cards0) if x != Word.words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist0[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards0) if x == Word.words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist0[lose]}さん")
            print("\n")
            return
        else:
            pass

        # 狼と村側の人数が同数になった場合、決着(狼の勝ち)
        if Ninzuu.cards1.count(Word.words[0]) == Ninzuu.cards1.count(Word.words[1]):
            print("ここで、少数派と多数派の人数が同数になりました。少数派の勝利です。\n")
            print("\n勝者")
            winner = [i for i, x in enumerate(Ninzuu.cards0) if x == Word.words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist0[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards0) if x != Word.words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist0[lose]}さん")
            print("\n")
            return
        else:
            pass

        # 狼(少数派)の人をカウント
        ookamiindexes1 = [i for i, x in enumerate(Ninzuu.cards1) if x == Word.words[0]]

        # 2*{Ninzuu.jinroo}ターンの時点で狼が複数残っていたら狼の勝ち(3人以上の対応が必要)
        if Ninzuu.Turnnumber >= 2 * int(Ninzuu.jinroo) and len(ookamiindexes1) >= 2:
            print(f"{2 * int(Ninzuu.jinroo)}ターン過ぎましたが、少数派が{2}人残っています。")
            print("この時点で少数派の勝利です。\n")
            print("\n勝者")
            winner = [i for i, x in enumerate(Ninzuu.cards0) if x == Word.words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist0[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards0) if x != Word.words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist0[lose]}さん")
            print("\n")
            return
        else:
            pass

        # 2*{Ninzuu.jinnro}+1ターン追放して終わらなかったら少数派の勝ち
        if Ninzuu.Turnnumber >= 2 * int(Ninzuu.jinroo) + 1:
            print(f"{2 * int(Ninzuu.jinroo)+1}ターン以内に少数派を全員追放できませんでした。少数派の勝利です。\n")
            print("\n勝者")
            winner = [i for i, x in enumerate(Ninzuu.cards0) if x == Word.words[0]]
            for i, win in enumerate(winner):
                print(f"{Ninzuu.playerlist0[win]}さん")
            print("\n敗者")
            loser = [i for i, x in enumerate(Ninzuu.cards0) if x != Word.words[0]]
            for i, lose in enumerate(loser):
                print(f"{Ninzuu.playerlist0[lose]}さん")
            print("\n")
            return
        else:
            print("\n\n\n\n\n\n\nゲームはまだ続きます。(Enterで次へ)\n\n")
            Ninzuu.Turnnumber += 1     # ターン数を1増やす

            # 議論
            discuss_again2 = DiscussAgain()
            discuss_again2.print_discussagain()

            # 投票・追放
            vote_oneset2 = GameOneset()
            vote_oneset2.print_oneset()

            # 結果又は継続
            result2 = Result()
            result2.print_winlose()
