
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
