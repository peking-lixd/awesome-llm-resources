# 🚀 推送到 GitHub 操作指南

## 方法 1: 使用 GitHub Desktop (最简单)

1. 打开 https://github.com/new
2. 仓库名：`awesome-llm-resources`
3. 选择 **Public**
4. **不要**勾选"Add README"等选项
5. 点击"Create repository"
6. 按页面提示运行：
```bash
cd /Users/lxd/.openclaw/workspace/llm-awesome
git remote add origin https://github.com/YOUR_USERNAME/awesome-llm-resources.git
git branch -M main
git push -u origin main
```

---

## 方法 2: 使用命令行

### Step 1: 生成 Personal Access Token

1. 访问 https://github.com/settings/tokens
2. 点击"Generate new token (classic)"
3. 勾选权限：`repo` (全选)
4. 生成后复制 token（只显示一次）

### Step 2: 创建仓库并推送

```bash
# 设置你的 GitHub 用户名
export GITHUB_USERNAME="你的用户名"
export GITHUB_TOKEN="你的 token"

# 创建仓库
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"awesome-llm-resources","description":"🚀 Awesome LLM Resources - 经典论文·热门前沿·开源项目","private":false,"auto_init":false}'

# 添加远程仓库
cd /Users/lxd/.openclaw/workspace/llm-awesome
git remote add origin https://github.com/$GITHUB_USERNAME/awesome-llm-resources.git

# 推送
git branch -M main
git push -u origin main
```

---

## 方法 3: 手动操作（推荐）

### 1. 在 GitHub 创建仓库

访问：https://github.com/new

填写：
- Repository name: `awesome-llm-resources`
- Description: `🚀 Awesome LLM Resources - 经典论文·热门前沿·开源项目`
- 选择：**Public**
- ❌ 不要勾选"Add a README file"
- ❌ 不要勾选"Add .gitignore"
- ❌ 不要勾选"Choose a license"

点击 **Create repository**

### 2. 复制页面底部的命令

页面会显示：
```bash
git remote add origin https://github.com/YOUR_USERNAME/awesome-llm-resources.git
git branch -M main
git push -u origin main
```

### 3. 在终端运行

```bash
cd /Users/lxd/.openclaw/workspace/llm-awesome
git remote add origin https://github.com/YOUR_USERNAME/awesome-llm-resources.git
git branch -M main
git push -u origin main
```

---

## ✅ 推送成功后

### 配置自动更新

1. 进入仓库 → **Settings** 标签
2. 左侧 **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 添加：
   - Name: `DASHSCOPE_API_KEY`
   - Value: `sk-d49f52eee4c64ccd980536fbbf8ec65b`
5. 点击 **Add secret**

### 启用 Actions

1. 点击 **Actions** 标签
2. 找到"Auto Update LLM Resources"
3. 点击 **Enable workflow**

---

## 📊 查看效果

访问：`https://github.com/YOUR_USERNAME/awesome-llm-resources`

---

## 💡 需要我帮你执行吗？

告诉我你的 GitHub 用户名，我可以帮你运行推送命令。
或者你可以手动执行上面的步骤。
