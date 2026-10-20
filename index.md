---
layout: page
title: 今日对话
---

<!-- 开屏闪出黑幕容器 -->
<div id="splash-screen" style="
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background-color: #050814; z-index: 9999;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    color: white; font-family: sans-serif;
    transition: opacity 1.5s ease-out;
">
    <!-- 金句文本展示区 -->
    <div id="quote-text" style="
        font-size: 1.5rem; max-width: 80%; text-align: center;
        opacity: 0; transition: opacity 1.5s ease-in; line-height: 1.8; letter-spacing: 1px;
    "></div>
    <div id="quote-date" style="
        font-size: 0.9rem; color: #8B949E; margin-top: 20px;
        opacity: 0; transition: opacity 1.5s ease-in;
    "></div>
</div>

<!-- 闪出动画结束后的常规内容（这里目前保持留白） -->
<div style="margin-top: 50px; text-align: center; color: #666;">
  <p>这是今天的思考留白。</p>
</div>

<!-- 随机提取金句并执行动画的 JS 脚本 -->
<script>
document.addEventListener("DOMContentLoaded", function() {
    // Jekyll 编译时会将 JSON 数据直接注入到这里
    const quotes = {{ site.data.highlights | jsonify }};
    
    if (quotes && quotes.length > 0) {
        // 随机抽取一条
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const selectedQuote = quotes[randomIndex];
        
        const textElement = document.getElementById('quote-text');
        const dateElement = document.getElementById('quote-date');
        const splashScreen = document.getElementById('splash-screen');
        
        textElement.innerText = "「 " + selectedQuote.text + " 」";
        dateElement.innerText = "—— " + selectedQuote.date;
        
        // 0.3秒后触发文字渐显
        setTimeout(() => {
            textElement.style.opacity = 1;
            dateElement.style.opacity = 1;
        }, 300);

        // 3.5秒后全屏黑幕渐隐消失，露出 So Simple 主题原本的白色/浅色页面
        setTimeout(() => {
            splashScreen.style.opacity = 0;
            setTimeout(() => {
                splashScreen.style.display = 'none';
            }, 1500); 
        }, 3500); 
    } else {
        document.getElementById('splash-screen').style.display = 'none';
    }
});
</script>
