---
layout: default
title: Knowledge exchange
tagline: Don't make the same mistake
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-06-24
licence: copyright
buttonStyle: fg-blog-land
backgroundStyle: bg-blog-land
---
## {{ page.title }}: {{ page.tagline }}

Check out our knowledge exchange feed, including posts from researchers and developers on project learnings, across the {{ site.brand }} portfolio.

### Project Olli

<div id="spotlight" class="spotlight">
<div class="featured-feed">
{% for post in site.posts limit:3 %}
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
{% include global/buttonLink.html url="/blog/Olli/index.html" label="Browse the Olli archive" %}
</div>

### General posts

<div id="spotlight" class="spotlight">
<div class="featured-feed">
{% for post in site.posts limit:3 %}
{% if post.tag == "General" %}
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