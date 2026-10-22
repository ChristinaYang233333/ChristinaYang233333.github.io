---
layout: page
title: 年度统计
permalink: /stats/
excerpt: "把对话摘录折成数字：谁在说、何时说、反复出现的主题。"
---

把 `_data/highlight.json` 里的摘录折成几组数字，用来看这一年（以及跨年）对话里反复出现的人和主题。数字会随摘录更新自动变化。

{% assign quotes = site.data.highlight %}
{% if quotes and quotes.size > 0 %}

{% assign sender_blob = "" %}
{% assign tag_blob = "" %}
{% assign month_blob = "" %}
{% for item in quotes %}
  {% capture sender_blob %}{{ sender_blob }}{{ item.sender }}|{% endcapture %}
  {% assign m = item.date | slice: 0, 7 %}
  {% capture month_blob %}{{ month_blob }}{{ m }}|{% endcapture %}
  {% for tag in item.tags %}
    {% capture tag_blob %}{{ tag_blob }}{{ tag }}|{% endcapture %}
  {% endfor %}
{% endfor %}
{% assign senders = sender_blob | split: "|" | uniq | sort %}
{% assign months = month_blob | split: "|" | uniq | sort | reverse %}
{% assign tags = tag_blob | split: "|" | uniq | sort %}

<div class="stats-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;margin:1.5rem 0 2.5rem;">
  <div style="padding:1.1rem 1rem;border:1px solid var(--border-color,#eee);border-radius:12px;">
    <div style="font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted-color,#888);">摘录</div>
    <div style="font-size:1.8rem;margin-top:0.35rem;">{{ quotes.size }}</div>
  </div>
  <div style="padding:1.1rem 1rem;border:1px solid var(--border-color,#eee);border-radius:12px;">
    <div style="font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted-color,#888);">发言人</div>
    <div style="font-size:1.8rem;margin-top:0.35rem;">{{ senders.size | minus: 1 }}</div>
  </div>
  <div style="padding:1.1rem 1rem;border:1px solid var(--border-color,#eee);border-radius:12px;">
    <div style="font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted-color,#888);">标签</div>
    <div style="font-size:1.8rem;margin-top:0.35rem;">{{ tags.size | minus: 1 }}</div>
  </div>
  <div style="padding:1.1rem 1rem;border:1px solid var(--border-color,#eee);border-radius:12px;">
    <div style="font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--text-muted-color,#888);">月份跨度</div>
    <div style="font-size:1.8rem;margin-top:0.35rem;">{{ months.size | minus: 1 }}</div>
  </div>
</div>

## 谁在说话

{% for sender in senders %}
{% if sender != "" %}
{% assign n = 0 %}
{% for item in quotes %}
  {% if item.sender == sender %}{% assign n = n | plus: 1 %}{% endif %}
{% endfor %}
<p style="margin:0.35rem 0;">
  <strong>{{ sender }}</strong>
  <span style="color:var(--text-muted-color,#888);"> · {{ n }} 条</span>
</p>
{% endif %}
{% endfor %}

## 按月份

{% for month in months %}
{% if month != "" %}
{% assign n = 0 %}
{% for item in quotes %}
  {% assign m = item.date | slice: 0, 7 %}
  {% if m == month %}{% assign n = n | plus: 1 %}{% endif %}
{% endfor %}
<p style="margin:0.35rem 0;">
  {{ month }}
  <span style="color:var(--text-muted-color,#888);"> · {{ n }} 条</span>
</p>
{% endif %}
{% endfor %}

## 反复出现的主题

<p style="line-height:2.1;">
{% for tag in tags %}
{% if tag != "" %}
{% assign n = 0 %}
{% for item in quotes %}
  {% for t in item.tags %}
    {% if t == tag %}{% assign n = n | plus: 1 %}{% endif %}
  {% endfor %}
{% endfor %}
<a href="/topics/#tag-{{ tag }}" style="margin-right:0.85rem;font-size:0.9rem;">#{{ tag }} <span style="color:var(--text-muted-color,#888);">{{ n }}</span></a>
{% endif %}
{% endfor %}
</p>

<p style="margin-top:2rem;"><a href="/topics/">查看全部摘录 →</a></p>

{% else %}
摘录数据还没有成功载入。请确认 `_data/highlight.json` 是一份完整的 JSON 数组后再重新构建站点。
{% endif %}
