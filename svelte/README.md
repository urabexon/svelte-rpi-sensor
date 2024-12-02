# Svelte

このプロジェクトは、Svelte アプリ用のテンプレートです。[sveltejs/template](https://github.com/sveltejs/template) にホストされています。

## 新しいプロジェクトの作成

`degit` を使用してこのテンプレートを基にした新しいプロジェクトを作成するには、以下の手順を実行します。

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

> **注意**: [Node.js](https://nodejs.org/) を事前にインストールしておいてください。

---

## 始め方

### 依存関係のインストール

```bash
cd svelte-app
npm install
```

### 開発サーバーの起動

```bash
npm run dev
```

ブラウザで `http://localhost:5000` にアクセスしてください。アプリが動作しているのが確認できます。`src` フォルダ内のコンポーネントファイルを編集し、保存してからページをリロードすると変更が反映されます。

他のコンピュータから接続を許可する場合は、`package.json` の `sirv` コマンドに `--host 0.0.0.0` オプションを追加してください。

---

## 本番環境用ビルド

### アプリのビルド

```bash
npm run build
```

### 本番環境用ビルドの実行

```bash
npm run start
```

このコマンドは `sirv` を使用します。`sirv` は `package.json` の依存関係に含まれており、Heroku などのプラットフォームにデプロイする際にも利用可能です。

---

## シングルページアプリケーション (SPA) モード

デフォルトでは、`sirv` は `public` フォルダ内のファイルに対応するリクエストのみを処理します。複数のルートを持つ SPA を構築する場合は、`package.json` 内の `start` コマンドを以下のように編集してください。

```json
"start": "sirv public --single"
```

---

## TypeScript の使用

このテンプレートには、TypeScript をセットアップするスクリプトが含まれています。テンプレートをクローンした後、以下のコマンドを実行してください。

```bash
node scripts/setupTypeScript.js
```

スクリプトを削除するには、以下のコマンドを実行してください。

```bash
rm scripts/setupTypeScript.js
```

---

## Web へのデプロイ

### Vercel を使用したデプロイ

1. Vercel をグローバルにインストールします。

   ```bash
   npm install -g vercel
   ```

2. プロジェクトフォルダ内で以下を実行します。

   ```bash
   cd public
   vercel deploy --name my-project
   ```

---

### Surge を使用したデプロイ

1. Surge をグローバルにインストールします。

   ```bash
   npm install -g surge
   ```

2. 以下のコマンドを実行してビルドとデプロイを行います。

   ```bash
   npm run build
   surge public my-project.surge.sh
   ```

---

詳細については、[公式 Svelte ドキュメント](https://svelte.dev/) を確認してください。
