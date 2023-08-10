---
layout: default
title: Olli archive
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-06-24
licence: copyright
buttonStyle: fg-blog-land
backgroundStyle: bg-blog-land
---

## {{ page.title }}

Find all the knowledge exchange posts related to project Olli in one simple feed below.

<div id="spotlight" class="spotlight">
<div class="featured-feed">
{% for post in site.posts %}
{% if post.tag == "Olli" %}
<div class="row">
<div class="col-3">
{% if post.image %}
<img src="{{ '/assets/images/blog/' | append: post.image | prepend: site.baseurl }}" alt="{{ post.alt }}" class="thumbnail-image-blog1">
{% else %}
<img src="{{ '/assets/images/Project27 logo.png' | prepend: site.baseurl }}" alt="A placeholder image, showing the Project27 logo." class="thumbnail-image-blog">
{% endif %}
</div>
<div class="col-9">
<p><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></p>
<p>{{ post.date | date_to_rfc822 | date: "%d %b %Y" }}</p>
</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>