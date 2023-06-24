---
layout: default
title: News archive
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-16
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

## {{ page.title }}

All the {{ site.brand }} news in one place.

---

<div class="feed">
{% for news in site.data.news %}
<div class="row">
<div class="col-3">
<img src="{{ '/assets/images/news/' | append: news.thumbnail | prepend: site.baseurl }}" alt="{{ news.thumbnailAlt }}" class="thumbnail-image">
</div>
<div class="col-9">
<p><a href="{{ news.link | prepend: site.baseurl }}">{{ news.headline }}</a></p>
<p>{{ news.date | date_to_rfc822 | date: "%d %b %Y" }}</p>
</div>
</div>
{% endfor %}
</div>