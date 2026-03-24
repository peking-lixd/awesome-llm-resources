#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
"""
LLM 资源搜集脚本
- 每周热门论文
- 每月热门论文
- 新兴开源项目
"""

import subprocess
import json
import os
from datetime import datetime, timedelta
import re

# 配置
PAPERS_DIR = "/Users/lxd/.openclaw/workspace/llm-awesome/papers"
PROJECTS_DIR = "/Users/lxd/.openclaw/workspace/llm-awesome/projects"
MEMORY_DIR = "/Users/lxd/.openclaw/workspace/llm-awesome/memory"
API_KEY = "sk-d49f52eee4c64ccd980536fbbf8ec65b"


def fetch_hot_papers(timeframe="week"):
    """搜索热门论文"""
    try:
        if timeframe == "week":
            time_desc = "最近 7 天"
        else:
            time_desc = "最近 30 天"
        
        cmd = [
            "curl", "-s", "-X", "POST",
            "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
            "-H", f"Authorization: Bearer {API_KEY}",
            "-H", "Content-Type: application/json",
            "-d", json.dumps({
                "model": "qwen3.5-flash",
                "messages": [
                    {"role": "system", "content": "返回 JSON 数组，每篇包含：title, authors, arxiv, date, hot_score (1-5 星), one_liner。只返回 JSON。"},
                    {"role": "user", "content": f"搜索大语言模型领域{time_desc}最热门的 10 篇论文，要求：\n1. arXiv 新发布\n2. 高关注度\n3. 有重要创新\n\n返回格式：[{{\"title\": \"...\", \"authors\": \"...\", \"arxiv\": \"...\", \"date\": \"2026-03-xx\", \"hot_score\": 5, \"one_liner\": \"...\"}}]"}
                ]
            })
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            json_match = re.search(r'\[[\s\S]+\]', content)
            if json_match:
                return json.loads(json_match.group())
    except Exception as e:
        print(f"搜索论文失败：{e}")
    
    return []


def fetch_hot_projects():
    """搜索热门开源项目"""
    try:
        cmd = [
            "curl", "-s", "-X", "POST",
            "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
            "-H", f"Authorization: Bearer {API_KEY}",
            "-H", "Content-Type: application/json",
            "-d", json.dumps({
                "model": "qwen3.5-flash",
                "messages": [
                    {"role": "system", "content": "返回 JSON 数组，每篇包含：name, github_url, stars (估计), category, one_liner。只返回 JSON。"},
                    {"role": "user", "content": "搜索最近 1 个月 LLM/AI 领域值得关注的新兴开源项目 (GitHub)，要求：\n1. 有实用性\n2. 增长快\n3. 覆盖工具/框架/应用\n\n返回 10 个：[{\"name\": \"...\", \"github_url\": \"https://github.com/...\", \"stars\": \"1k+\", \"category\": \"工具\", \"one_liner\": \"...\"}]"}
                ]
            })
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            json_match = re.search(r'\[[\s\S]+\]', content)
            if json_match:
                return json.loads(json_match.group())
    except Exception as e:
        print(f"搜索项目失败：{e}")
    
    return []


def generate_hot_markdown(papers, timeframe="week"):
    """生成热门论文 Markdown"""
    now = datetime.now()
    if timeframe == "week":
        title = "🔥 本周热门论文"
        desc = "最近 7 天最受关注的 LLM 论文"
    else:
        title = "🔥 本月热门论文"
        desc = "最近 30 天最受关注的 LLM 论文"
    
    md = f"""# {title}

> {desc}

**更新时间**: {now.strftime('%Y-%m-%d')}

---

| # | 论文 | arXiv | 热度 | 简介 |
|---|------|-------|------|------|
"""
    
    for i, paper in enumerate(papers, 1):
        stars = "⭐" * paper.get("hot_score", 3)
        arxiv_id = paper.get("arxiv", "")
        md += f"| {i} | **{paper.get('title', 'N/A')}**<br>{paper.get('authors', '')} | [📄 {arxiv_id}](https://arxiv.org/abs/{arxiv_id}) | {stars} | {paper.get('one_liner', '-')} |\n"
    
    md += f"\n---\n\n**最后更新**: {now.strftime('%Y-%m-%d %H:%M')}\n"
    
    filename = f"hot_this_{timeframe}.md"
    filepath = os.path.join(PAPERS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    
    return len(papers)


def generate_projects_markdown(projects):
    """生成项目 Markdown"""
    now = datetime.now()
    
    md = f"""# 🆕 新兴项目推荐

> 最近 1 个月值得关注的 LLM 开源项目

**更新时间**: {now.strftime('%Y-%m-%d')}

---

| 项目 | GitHub | Stars | 类别 | 简介 |
|------|---------|-------|------|------|
"""
    
    for proj in projects:
        md += f"| **{proj.get('name', 'N/A')}** | [🔗 GitHub]({proj.get('github_url', '#')}) | {proj.get('stars', '-')} | {proj.get('category', '工具')} | {proj.get('one_liner', '-')} |\n"
    
    md += f"\n---\n\n**最后更新**: {now.strftime('%Y-%m-%d %H:%M')}\n"
    
    filepath = os.path.join(PROJECTS_DIR, "new_this_month.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    
    return len(projects)


def update_readme_stats(week_count, month_count, project_count):
    """更新 README 统计"""
    readme_path = "/Users/lxd/.openclaw/workspace/llm-awesome/README.md"
    now = datetime.now().strftime('%Y-%m-%d')
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 更新统计表格
    content = re.sub(
        r'\| 本周热门 \| - \| 待更新 \|',
        f'| 本周热门 | {week_count} | {now} |',
        content
    )
    content = re.sub(
        r'\| 本月热门 \| - \| 待更新 \|',
        f'| 本月热门 | {month_count} | {now} |',
        content
    )
    content = re.sub(
        r'\| 开源项目 \| - \| 待更新 \|',
        f'| 开源项目 | {project_count} | {now} |',
        content
    )
    content = re.sub(
        r'\| \*\*总计\*\* \| \*\*20\+\*\* \| \*\*.*\*\* \|',
        f'| **总计** | **{20 + week_count + month_count + project_count}+** | **{now}** |',
        content
    )
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)


def save_memory(week_papers, month_papers, projects):
    """保存更新记录"""
    record = {
        "last_update": datetime.now().isoformat(),
        "week_papers": len(week_papers),
        "month_papers": len(month_papers),
        "projects": len(projects)
    }
    os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(os.path.join(MEMORY_DIR, "last_update.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)


def main():
    print(f"=== LLM 资源搜集 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ===")
    
    # 搜集本周热门
    print("搜集本周热门论文...")
    week_papers = fetch_hot_papers("week")
    print(f"找到 {len(week_papers)} 篇")
    
    # 搜集本月热门
    print("搜集本月热门论文...")
    month_papers = fetch_hot_papers("month")
    print(f"找到 {len(month_papers)} 篇")
    
    # 搜集新兴项目
    print("搜集新兴开源项目...")
    projects = fetch_hot_projects()
    print(f"找到 {len(projects)} 个")
    
    # 生成 Markdown
    print("\n生成文档...")
    week_count = generate_hot_markdown(week_papers, "week")
    month_count = generate_hot_markdown(month_papers, "month")
    proj_count = generate_projects_markdown(projects)
    
    # 更新 README
    update_readme_stats(week_count, month_count, proj_count)
    
    # 保存记录
    save_memory(week_papers, month_papers, projects)
    
    print(f"\n✅ 完成！")
    print(f"   本周热门：{week_count} 篇")
    print(f"   本月热门：{month_count} 篇")
    print(f"   新兴项目：{proj_count} 个")
    print("=== 搜集完成 ===")


if __name__ == "__main__":
    main()
