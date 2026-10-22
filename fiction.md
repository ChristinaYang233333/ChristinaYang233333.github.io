---
layout: page
title: 造梦空间
permalink: /categories/fiction/
excerpt: "在日常的对话与留白中，让角色长出血肉。"
---

小说和虚构角色会放在这个分类里。对话摘录是素材库，这里才是它们长成故事之后的去处。

{% assign stories = site.categories.fiction %}
{% if stories and stories.size > 0 %}

目前 {{ stories.size }} 篇：

{% for post in stories %}
<article style="margin:0 0 1.5rem;padding-bottom:1.25rem;border-bottom:1px solid var(--border-color,#eee);">
  <h2 style="margin:0 0 0.35rem;font-size:1.2rem;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p style="margin:0;font-size:0.85rem;color:var(--text-muted-color,#666);">{{ post.date | date: "%Y-%m-%d" }}</p>
  {% if post.excerpt %}
  <p style="margin:0.45rem 0 0;font-size:0.95rem;line-height:1.6;">{{ post.excerpt | strip_html | truncate: 120 }}</p>
  {% endif %}
</article>
{% endfor %}

{% else %}
还没有归入 `fiction` 分类的文章。新篇放进 `_posts/`，在 front matter 里写上：

```yaml
categories: [fiction]
```

发布后会自动出现在这一页。眼下可以先读已有的随笔：{% for post in site.posts limit: 3 %} [{{ post.title }}]({{ post.url | relative_url }}){% unless forloop.last %}、{% endunless %}{% endfor %}。
{% endif %}
