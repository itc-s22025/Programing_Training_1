# programing Training 1 の課題

 色々探りながらの制作だったのでとても大変でした。最初は全然仕組みがわからなくてなんなんだこれは！という感じでしたが、理解が進むごとに制作が楽しくなりました。
 ようやく少しずつ理解できてきたかな？という感じなので、もう一度１から作り直したらもしかするともうちょっときれいなものができたのかもしれませんが、とりあえず提出します。


●やったこと
・タイマー機能の追加：　60秒でゲームがFinishになるようにしました。
・スコア機能の追加：　パドルにボールが当たるとスコア(ポイント)が+1ずつ増えていくようにしました。
・ボールが地面についたときの画面遷移：　ボールがパドルに当たらずに地面についたとき、failedの画面に遷移します。また、rキーを押すことでボールが落ちたその画面に戻れるようにしました。
・タイマーが0になったときの画面遷移：　ゲームがスタートして一分経つと、強制的にFinish画面に遷移します。その際、遷移前の画面でボールが動き続けないようにしました。
・プログラム終了ボタンの設置：　Finish画面のOKボタンをクリックすることでGame画面が閉じるようにしました。
