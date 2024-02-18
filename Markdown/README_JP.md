# 電子書籍検索システム - EbookDatabase ————— FROM CHATGPT4

[ENGLISH](README_EN.md) | [日本語](README_JP.md)

## 概要

これはローカライズされた電子書籍検索システムで、高度な検索機能を利用してクエリを行うことができます。

このプロジェクトはFastAPIとSQLiteデータベースを使用して構築され、本プロジェクトの配布パッケージを通じて簡単にデプロイすることができます。

本プロジェクトが提供するデータベースは、多くのチャネルを通じて集められたもので、情報不足などの問題が発生することがありますが、ご理解いただければ幸いです。

データベースの内容に誤りがある、または共有したい良いコンテンツがある場合は、私に連絡してください。

参加者が多ければ、データベースは定期的に更新されます。人々のために私があり、私のために人々がいます。

趣味の仲間と交流するためのグループチャットに参加することもできます。

QQグループ：942385978

![ホームページ](image/img.png)
![ホームページ](image/img_1.png)

## データベースのバックアップ

### [データベースリストを見るにはこちらをクリック](Markdown/データベースダウンロードドキュメント.md)

## クイックスタート

ビデオ：

YouTube：https://youtu.be/-jD8OsF6di4

bilibili：https://www.bilibili.com/video/BV1fN4y1r7fP/

他のリポジトリアドレス：https://gitee.com/etojsyc/EbookDatabase

### ローカルでの実行

---

#### 方法1（推奨！配布パッケージを使用して実行）

1. 本プロジェクトが配布したソフトウェアパッケージをダウンロードします。

2. ダウンロードしたソフトウェアパッケージを解凍します。

3. 本プロジェクトのデータベースファイルをダウンロードし、instanceフォルダに保存します。

4. exeをダブルクリックして、このプロジェクトを一発で起動します。

5. その後、http://127.0.0.1:10223/ で使用できます。

---

#### 方法2（ソースコードを使用して実行）

1. ターミナルまたはコマンドプロンプトを開き、プロジェクトのルートディレクトリにナビゲートします。

2. 新しい仮想環境を作成します。次のコマンドを使用できます。

```python
python -m venv venv
```

これにより、プロジェクトのルートディレクトリに`venv`という名前の新しい仮想環境が作成されます。

3. 仮想環境をアクティベートします。Windowsでは、次のコマンドを使用します。

```python
venv\Scripts\activate
```

macOSとLinuxでは、次のコマンドを使用します。

```python
source venv/bin/activate
```

仮想環境がアクティベートされると、ターミナルのプロンプトに仮想環境名が表示され、仮想環境がアクティベートされていることが示されます。

4. 次に、プロジェクトに必要な依存関係をインストールします。次のコマンドを使用して、仮想環境に依存関係をインストールします。

```python
pip install -r requirements.txt
```

これにより、`requirements.txt`ファイルに基づいてプロジェクトに必要なすべての依存関係がインストールされ、これらの依存関係は仮想環境内でのみ使用可能になります。

5. 最後に、アプリケーションを実行します。次のコマンドを使用してアプリケーションを起動します。

```python
python app.py
```
これにより、仮想環境内でアプリケーションが実行され、http://127.0.0.1:10223/ で使用できるようになります。

---
#### 方法3（ソースコードを使用してWindows実行可能ファイルをビルド）

ソースコードを使用してWindows実行可能ファイルをビルドします。

1. この手順を実行する際には、Windows上で行う必要があります。

2. 方法2と同様の操作を行いますが、5番目の手順で次のコマンドを使用してアプリケーションをビルドします。

```python
python setup.py build
```

これにより、プロジェクトのルートディレクトリに`build`という新しいディレクトリが作成され、ビルドされたアプリケーションが含まれます。

---
#### 方法4（Dockerを使用してデプロイ）

1. dockerhubから直接イメージをプルします。

   ```bash
   docker push hellohistory/ebookdatabase:tagname
   ```
2. ビルドが完了したら、次のコマンドを実行して

コンテナを起動します。

   ```bash
   docker run -v /path/to/instance:/app/instance -v /path/to/logs:/app/logs  -p 10223:10223 ebookdatabase
   ```
   /path/to/instanceをあなたのローカルのデータベースファイルの保存パスに、/path/to/logsをあなたのローカルのログファイルの保存パスに置き換える必要があります。

   これにより、`ebookdatabase`という名前のDockerコンテナが起動し、コンテナの10223ポートがホストの同じポートにマップされます。

3. ブラウザで `http://127.0.0.1:10223/` にアクセスしてアプリを使用します。

---
#### 方法5（Dockerコンテナを自己構築して使用）

Dockerコンテナを自己構築して使用します。

1. システムにDockerがインストールされていることを確認します。まだインストールされていない場合は、[Docker公式ウェブサイト](https://www.docker.com/)のインストールガイドを参照してください。

2. 本プロジェクトのソースコードをローカル環境にクローンまたはダウンロードします。`Dockerfile`ファイルがプロジェクトのルートディレクトリにあることを確認してください。

3. ターミナルまたはコマンドプロンプトでプロジェクトのルートディレクトリにナビゲートし、次のコマンドを実行してDockerイメージをビルドします。

   ```bash
   docker build -t ebookdatabase .
   ```

4. ビルドが完了したら、次のコマンドを実行してコンテナを起動します。

   ```bash
   docker run -v /path/to/instance:/app/instance  -p 10223:10223 ebookdatabase
   ```
   /path/to/instanceをあなたのローカルのデータベースファイルの保存パスに置き換える必要があります。

   これにより、`ebookdatabase`という名前のDockerコンテナが起動し、コンテナの10223ポートがホストの同じポートにマップされます。

5. ブラウザで `http://127.0.0.1:10223/` にアクセスしてアプリを使用します。

---

## 機能

- ローカルでの基本検索と高度な検索をサポート
- 曖昧検索と正確検索をサポート
- ページ分割で結果を表示

![検索結果ページ](image/img_3.png)
![検索結果ページ](image/img_4.png)

## バグフィードバック

このプロジェクトを実行中に問題が発生した場合は、issuesでフィードバックを提出してください。フィードバックの形式は以下のとおりです。
```bash
1.実行環境

2.使用した検索条件

3.エラー画面のスクリーンショット
```

## 声明
   ```
本プロジェクトは学習交流のためにのみ使用され、商業シーンでの使用は禁止されています

本プロジェクトは、いかなる形式でも商業目的で使用するための許可を与えることは絶対にありません。商業シーンで本プロジェクトを使用していると主張するものはすべて偽りです。

権利を侵害する場合は、本プロジェクトを削除するようにご連絡ください。

本プロジェクトはいかなる責任も負いません。責任はすべて使用者が負うものとします。詳細はライセンスファイルをお読みください。
   ```