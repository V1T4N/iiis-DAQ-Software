
# 改良版DAQソフトウェア
  ビルド済みソフトウェアはcompiled_softwareのブランチに入っています<br>
  [https://github.com/V1T4N/iiis-DAQ-Software/tree/compiled_software	](https://github.com/V1T4N/iiis-DAQ-Software/tree/compiled_software	)
  <br>
  
  従来通り録画を開始して、録画を終了したときに	avi形式とHDF5形式で保存されます。<br>
  avi形式のファイルは従来通り\dataに保存され、HDF5形式のファイルは\h5dataに保存されます。

## 実行環境
exeの実行にOpenCV2.4.9が必要です。<br>
C:\opencv\opencv\ <br>
     ┣build<br>
     ┣sources<br>
となるようにインストールしてください<br>

HDF5への変換にはpython3.6を用いています。必要なライブラリは以下の通りです。

opencv-python<br>
numpy<br>
h5py<br>



ビルド済みソフトウエアにはpythonの実行環境も同梱しているため、Pythonの環境構築は不要です。

## 更新ログ



v1->v2
動画ファイルが分割されないように変更しました。<br>
h5形式への変換の際に進捗が表示されるようになりました。<br>
<br>
<br>
v2->v3<br>
動画ファイルの分割時間をユーザーが任意で設定できるように修正しました。<br>
右下のSplit Frameから調整できます。<br>
何フレームで分割されるかを調整できます。5FPSの場合1000フレームでおよそ3分です。<br>
また、1000フレームを超える場合、h5形式に変換する際に失敗する可能性があります。<br>
<br>
出力されるh5ファイルにも変更点があります。<br>
分割されたファイル out(日時)splitN.h5に加えて、<br>
すべてを統合したファイル out(日時)_Nfile_merged.hが出力されます。<br>
<br>
<br>
v3->v3.1<br>
左上のCheckボタンを押すことでカメラデバイスが接続されているか確認できるように機能を追加しました。<br>
<br>
device0が接続されている場合、device 0 is connected と表示されます。<br>
