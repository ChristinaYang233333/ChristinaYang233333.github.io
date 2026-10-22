---
layout: page
title: 专业视野
permalink: /categories/business/
excerpt: "关于出海、商业化与智能方案落地的行业复盘。"
---

工作里那些真正能留下来的判断，会写在这里：出海、商业化、智能方案怎么落地，以及落地之后哪些东西其实没那么重要。

{% assign notes = site.categories.business %}
{% if notes and notes.size > 0 %}

目前 {{ notes.size }} 篇：

{% for post in notes %}
<article style="margin:0 0 1.5rem;padding-bottom:1.25rem;border-bottom:1px solid var(--border-color,#eee);">
  <h2 style="margin:0 0 0.35rem;font-size:1.2rem;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p style="margin:0;font-size:0.85rem;color:var(--text-muted-color,#666);">{{ post.date | date: "%Y-%m-%d" }}</p>
  {% if post.excerpt %}
  <p style="margin:0.45rem 0 0;font-size:0.95rem;line-height:1.6;">{{ post.excerpt | strip_html | truncate: 120 }}</p>
  {% endif %}
</article>
{% endfor %}

{% else %}
还没有归入 `business` 分类的复盘。新篇放进 `_posts/`，在 front matter 里写上：

```yaml
categories: [business]
```

发布后会自动出现在这一页。想先看职场气味更重的随笔，站点里已有 {% assign essay = site.posts | where: "title", "28岁，中年老登" | first %}{% if essay %}[{{ essay.title }}]({{ essay.url | relative_url }}){% else %}随笔列表{% endif %}。
{% endif %}
