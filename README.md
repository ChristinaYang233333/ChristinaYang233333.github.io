# Christina's 数字花园

Christina 的个人站点源码，用来整理日常对话、随笔与思考脉络。

在线访问：[www.christinayxr.com](https://www.christinayxr.com)

站点标题为 **Christina's数字花园**。作者定位是小说作者 / 数据拾荒者：把和密友的聊天素材清洗存档，同时记录随笔、摄影与行业观察。

## 当前内容

导航与首页入口对应这些板块：

| 板块 | 路径 | 现状 |
| --- | --- | --- |
| 今日对话 / 思考话题 | `/topics/` | 页面已建，内容建设中 |
| 年度统计 | `/stats/` | 导航已挂，页面尚未落地 |
| 图库（镜头侧写） | `/gallery/` | 首页入口已挂，图库尚未落地 |
| 造梦空间 | `/categories/fiction/` | 首页入口已挂，小说分类文章尚未发布 |
| 专业视野 | `/categories/business/` | 首页入口已挂，行业复盘尚未发布 |
| 关于作者 | `/about/` | 已上线，含联系方式 |
| 随笔文章 | `_posts/` | 已有两篇：建站记录《十二月一则》、随笔《28岁，中年老登》 |

对话摘录存放在 `_data/highlight.json`，按日期、发言人、语境和标签归档（目前主要是 Christina 与 Yvonne 的对话）。首页卡片配置在 `_data/home_bolcks.yml`。

另有 `/privacy/`、`/terms/` 作为隐私政策与服务条款。

## 仓库结构

```
├── _config.yml              # 站点标题、主题、插件与作者信息
├── _data/
│   ├── navigation.yml       # 主导航
│   ├── home_bolcks.yml      # 首页入口卡片
│   ├── highlight.json       # 对话摘录
│   └── text.yml             # 主题文案（中英）
├── _posts/                  # 随笔与文章
├── _layout/home.html        # 首页布局（待补）
├── about.md / topic.md      # 关于、思考话题
├── privacy.md / terms.md    # 法律页面
├── images/logo.png          # 站点 Logo
└── CNAME                    # 自定义域名 www.christinayxr.com
```

## 技术栈

- 静态站点：[Jekyll](https://jekyllrb.com/)，语言为简体中文（`zh-CN`）
- 托管：[GitHub Pages](https://pages.github.com/)
- 主题：[So Simple Theme](https://github.com/mmistakes/so-simple-theme)（`remote_theme: mmistakes/so-simple-theme`）
- 插件：`jekyll-remote-theme`、`jekyll-seo-tag`、`jekyll-sitemap`、`jekyll-feed`、`jekyll-paginate`

本地预览（需已安装 Ruby 与 Bundler）：

```bash
bundle exec jekyll serve
```

GitHub Pages 会按 `_config.yml` 拉取远程主题并构建，无需把主题源码放进本仓库。

## 版权

除另有说明外，文字与图片为 Christina 原创。代码遵循 MIT；内容遵循 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)。
