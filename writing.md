---
layout: archive
title: "📚 小说与随笔"
permalink: /writing/   # <--- 必须和你导航栏里的 url 一致
author_profile: true
---

{% assign entries = site.categories.writing %}
{% for post in entries %}
  <article class="archive__item">
    <h2 class="archive__item-title">
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h2>
    <p class="archive__item-excerpt">
      {{ post.date | date: "%Y-%m-%d" }} - {{ post.description }}
    </p>
  </article>
{% endfor %}

{% if entries.size == 0 %}
  <p>暂时还没有文章，敬请期待！</p>
{% endif %}
