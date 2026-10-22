---
layout: page
title: 今日对话
permalink: /topics/
excerpt: "从日常对话里洗出的思考碎片，按时间和标签归档。"
---

日常聊天里那些突然清楚的句子，清洗之后放在这里。发言人主要是 Christina 与 Yvonne，语境和标签一起保留，方便以后顺着一条线往回看。

{% assign quotes = site.data.highlight %}
{% if quotes and quotes.size > 0 %}
{% assign quotes_sorted = quotes | sort: "date" | reverse %}
{% assign tag_blob = "" %}
{% for item in quotes %}
  {% for tag in item.tags %}
    {% capture tag_blob %}{{ tag_blob }}{{ tag }}|{% endcapture %}
  {% endfor %}
{% endfor %}
{% assign tag_list = tag_blob | split: "|" | uniq | sort %}

<p style="color: var(--text-muted-color, #666); font-size: 0.9rem;">
  目前 <strong>{{ quotes.size }}</strong> 条摘录，按日期从新到旧排列。
</p>

<p style="line-height: 2;">
{% for tag in tag_list %}
  {% if tag != "" %}
  <a id="tag-{{ tag }}" href="#tag-{{ tag }}" style="margin-right: 0.6rem; font-size: 0.85rem;">#{{ tag }}</a>
  {% endif %}
{% endfor %}
</p>

{% for item in quotes_sorted %}
<article id="quote-{{ item.id }}" style="margin: 0 0 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border-color, #eee);">
  <p style="font-size: 1.05rem; line-height: 1.7; margin: 0 0 0.75rem;">“{{ item.text }}”</p>
  <p style="margin: 0; font-size: 0.85rem; color: var(--text-muted-color, #666);">
    <strong>{{ item.sender }}</strong>
    <span style="margin: 0 0.45rem;">·</span>
    {{ item.date }}
  </p>
  {% if item.context %}
  <p style="margin: 0.5rem 0 0; font-size: 0.85rem; color: var(--text-muted-color, #777);">{{ item.context }}</p>
  {% endif %}
  {% if item.tags %}
  <p style="margin: 0.45rem 0 0; font-size: 0.8rem;">
    {% for tag in item.tags %}
    <a href="#tag-{{ tag }}" style="margin-right: 0.5rem; color: var(--text-muted-color, #888);">#{{ tag }}</a>
    {% endfor %}
  </p>
  {% endif %}
</article>
{% endfor %}

{% else %}
对话摘录还没有成功载入。请确认 `_data/highlight.json` 是一份完整的 JSON 数组后再重新构建站点。
{% endif %}
