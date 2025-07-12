# title: Pyxel MML Music Player (In-Game Music Only)
# desc: A simple music player to test MML (Music Macro Language) strings with Pyxel.
# original author: Takashi Kitao
# version: 1.1

import pyxel


class MMLPlayer:
    """
    PyxelのMML（Music Macro Language）を再生するためのシンプルなプレーヤーです。
    プレイ中のBGMのみを再生するように変更されています。
    """

    def __init__(self):
        # Pyxelを初期化します。ウィンドウサイズは任意です。
        pyxel.init(160, 120, title="Pyxel MML Player", fps=60)

        # MMLデータをサウンドに設定します。
        self.init_sound()

        # プレイ中の音楽(ミュージック1)を再生します。
        pyxel.playm(0, loop=False)

        # メインループを開始します。
        pyxel.run(self.update, self.draw)

    def init_sound(self):
        # --- ここからMMLデータ ---
        t = "T135"
        l1 = "["
        l2 = "]"

        a1 = t + "@2 @VIB 1{32, 32, 48} @ENV 1{100,10,20} V80 L8Q100O4"
        a2 = "ccccc< Q80g16g16r16 Q100a-Q80b16> c16c16Q100cccc<Q80g16g16r16Q100a-Q80b16"
        a3 = "V80L8 >Q100c1 @GLI 1{-1200,24}@ENV 2{40,10,20} >c1 @GLI 0 @ENV 1"
        a4 = "@ENV 1 V80 O5 gcfc16e-.cdc r16<c16d16e-16dc16e-16&e-cdc"
        a5 = "a-.>c16re-4<a->ce-< b-.>d16rf4<b->df"
        a6 = "O4 g.br16>d2r8 d.fr16g4.r16 V40g16a-16b-16"
        a7 = "L16O5 [V40cgfge-gdgcg<b>gcgdg V60cgfge-gdgcg<b>gcgdg V80cgfge-gdgcg<b>gcgdg V80rde-fg8fgrgrgg8b8]2"
        a8 = "V70[e-de-de-8ce-8.c8d8c8]2 V80L8 e-.c.e-f.d.f g.f.gb-.a-.b- V80>c1r1"

        b1 = t + "@0 @ENV 1{100,20,10} V80L8 Q100O3"
        b2 = "ccccc<Q80g16g16r16 Q100a-Q80b16> c16c16Q100cccc<Q80g16g16r16Q100a-Q80b16>"
        b3 = "L8 [cccccce-f]4"
        b4 = "<a-a-a-a-a-a-b->c< b-b-b-b-b-b->cd"
        b5 = "[O2gggggga-b-]2"
        b6 = "O3L16 c8>cc<c8>c8<c8>cc<cc>cc<< b-8>b-b-<b-8>b-8<b-8>b-b-<b-b->b-b-< a-8>a-a-<a-8>a-8<a-8>a-a-<a-a->a-a-< g8>gg<g8>g8<g8>gg<gg>gg<"
        b7 = "O3L8 [c]7<b- [a-]6gg ffffgggg [a-]4[b-]4"
        b8 = (
            ">ccccc<Q80g16g16r16 Q100a-Q80b16> c16c16Q100cccc<Q80g16g16r16Q100a-Q80b16>"
        )
        c1 = t + "@2 @VIB 1{40, 28, 40} @ENV 1{100,8,30} V80 L8Q100O4"
        c2 = "Y10 ccccc< Q80g16g16r16 Q100a-Q80b16> c16c16Q100cccc<Q80g16g16r16Q100a-Q80b16"
        c3 = "V80 L8 Q100g1@GLI 1{-1200,24}@ENV 2{40,10,20} >g1 @GLI 0 @ENV 1"
        c4 = "@ENV 1 V80 O5 c<g>c<g16>c8.<gbg r16c16d16e-16dc16e-16&e-cdc"
        c5 = "e-.a-16r>c4<e-a->c< f.b-16r>d4<fb->d<"
        c6 = "d.gr16g2r g.>dr16d4.r16< V40g16a-16b-16"
        c7 = "L16O5 [r V10 cgfg e-gdg cg<b>g cgdg V30cgfge-gdgcg<b>gcgdg V40cgfg e-gdg cg<b>g cgd V80<rgbb>d8ddrdrdd8d8]2"
        c8 = "V80 O4L8 c2.r<b- a-2.g4 f2g2 a-2b-2 O5 g1r1"

        d1 = t + "@1L8 @3 @ENV 5{100,8,20,20,0}"
        d2 = ""
        # d2 = "V10[O8a8]"

        pyxel.sounds[0].mml(
            a1 + a2 + l1 + a3 + a4 + a4 + a5 + a4 + a4 + a5 + a6 + a7 + a8 + l2
        )
        pyxel.sounds[1].mml(
            b1 + b2 + l1 + b2 + b3 + b4 + b3 + b4 + b5 + b6 + b6 + b7 + b8 + l2
        )
        pyxel.sounds[2].mml(
            c1 + c2 + l1 + c3 + c4 + c4 + c5 + c4 + c4 + c5 + c6 + c7 + c8 + l2
        )
        pyxel.sounds[3].mml(d1)

        # 3つのサウンドを組み合わせてミュージック1を作成
        pyxel.musics[0].set([0], [1], [2], [3])

        # --- MMLデータはここまで ---

    def update(self):
        """
        毎フレームの更新処理。キー入力を受け付けます。
        """
        # Qキーが押されたらプログラムを終了します。
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        """
        毎フレームの描画処理。操作方法などを表示します。
        """
        # 画面を黒でクリアします。
        pyxel.cls(0)

        # タイトルと操作説明を表示します。
        pyxel.text(40, 20, "Pyxel MML Player", 7)
        pyxel.text(42, 50, "Now Playing...", 13)
        pyxel.text(48, 80, "Press Q: Quit", 13)


# アプリケーションを起動します。
MMLPlayer()
