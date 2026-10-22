---
# 1. 切换为 So Simple 的 home 布局
layout: home

# 2. 配置 home 布局特有参数
entries_layout: list
posts_limit: 5
---

<!-- 开屏黑幕专属响应式样式：解决手机端 100vh 溢出问题 -->
<style>
  .splash-overlay {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background-color: #050814; z-index: 99999;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    color: #ffffff; padding: 1.5rem; box-sizing: border-box;
    transition: opacity 1.2s ease-out; pointer-events: auto;
  }
  .splash-text {
    font-size: 1.15rem; text-align: center; line-height: 1.6; letter-spacing: 1px;
    opacity: 0; transition: opacity 1.2s ease-in;
  }
  .splash-date {
    font-size: 0.85rem; color: #8B949E; margin-top: 20px;
    opacity: 0; transition: opacity 1.2s ease-in;
  }
  @media (min-width: 768px) {
    .splash-text { font-size: 1.4rem; max-width: 80%; }
  }
</style>

<!-- 1. 全屏开屏黑幕 -->
<div id="splash-screen" class="splash-overlay">
    <div id="splash-quote-text" class="splash-text"></div>
    <div id="splash-quote-date" class="splash-date"></div>
</div>

<!-- 2. 首页正文区：去掉了小标题，直接展示卡片 -->
<div class="entries-list" style="margin-bottom: 2.5rem;">
  <article class="archive__item" id="native-quote-card" style="visibility: hidden;">
    <!-- 原生文章标题类，用于放置引用的 text -->
    <h2 class="archive__item-title" id="body-quote-text" style="font-weight: 400; font-style: italic; line-height: 1.6;"></h2>
    
    <!-- 原生文章摘要类，用于放置 sender 和 date -->
    <div class="archive__item-excerpt" style="margin-top: 10px; font-size: 0.85em; color: var(--text-muted-color, #666);">
      <strong id="body-quote-sender" style="color: var(--primary-color);"></strong> 
      <span style="margin: 0 0.5em;">|</span>
      <span id="body-quote-date"></span>
    </div>
  </article>
</div>

<!-- 3. 数据填空与交互脚本 -->
<script>
(function() {
    let quotes = [];
    {% if site.data.highlight %}
      quotes = {{ site.data.highlight | jsonify }};
    {% endif %}

    if (!quotes || quotes.length === 0) {
        quotes = [{
            "text": "除了焦虑型依恋，还有一个原因，就是我觉得他们容易撼动，进而肯定了我的存在。",
            "date": "2026-08-14",
            "sender": "Christina"
        }];
    }

    // 每次刷新随机抽取一条，确保开屏和正文使用同一条数据
    const selected = quotes[Math.floor(Math.random() * quotes.length)];
    
    window.addEventListener('DOMContentLoaded', function() {
        // --- 处理开屏渲染 ---
        const splashText = document.getElementById('splash-quote-text');
        const splashDate = document.getElementById('splash-quote-date');
        const splashScreen = document.getElementById('splash-screen');

        if (splashText && splashDate) {
            splashText.innerText = "「 " + selected.text + " 」";
            splashDate.innerText = "—— " + selected.date + (selected.sender ? " (" + selected.sender + ")" : "");
            
            setTimeout(function() {
                splashText.style.opacity = '1';
                splashDate.style.opacity = '1';
            }, 200);
        }

        // --- 处理正文原生卡片填空 ---
        const bodyText = document.getElementById('body-quote-text');
        const bodySender = document.getElementById('body-quote-sender');
        const bodyDate = document.getElementById('body-quote-date');
        const nativeCard = document.getElementById('native-quote-card');

        if (bodyText && bodySender && bodyDate && nativeCard) {
            bodyText.innerText = "“" + selected.text + "”";
            bodySender.innerText = selected.sender ? selected.sender : "未知";
            bodyDate.innerText = selected.date;
            nativeCard.style.visibility = 'visible';
        }

        // --- 5.5 秒后关闭黑幕 ---
        if (splashScreen) {
            setTimeout(function() {
                splashScreen.style.opacity = '0';
                splashScreen.style.pointerEvents = 'none';
                setTimeout(function() {
                    splashScreen.style.display = 'none';
                }, 1200);
            }, 5500);
        }
    });
})();
</script>
