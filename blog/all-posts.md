---
layout: default
author: Daniel Hajas
title: All posts
buttonStyle: fg-blog-sect
backgroundStyle: bg-blog-sect
---

{% assign categoryLink = '' %}
{% assign devLink = '/blog/logbook/dev/index.html' %}
{% assign issuesLink = '/blog/logbook/issues/index.html' %}
{% assign latexLink = '/blog/logbook/LaTeX-to-MathML/index.html' %}
{% assign mathmlLink = '/blog/logbook/MathML-usability/index.html' %}
{% assign disabilitiesLink = '/blog/twist/disabilities/index.html' %}
{% assign identitiesLink = '/blog/twist/identities/index.html' %}
{% assign nanotipLink = '/blog/twist/nanotip/index.html' %}
{% assign readingLink = '/blog/twist/reading/index.html' %}
{% assign specialLink = '/blog/twist/special-interests/index.html' %}

## All posts

All the {{ site.brand }} blog posts in one place.

---

<div class="blog-feed">
{% for post in site.posts %}
{% if post.url contains "guide" or post.url contains "grapheel" %}
{% continue %}
{% endif %}
<div class="row">
<div class="col-3">
{% if post.image %}
<img src="{{ '/assets/images/blog/' | append: post.image | prepend: site.baseurl }}" alt="{{ post.alt }}" class="thumbnail-image-blog">
{% else %}
<img src="{{ '/assets/images/Project27 logo.png' | prepend: site.baseurl }}" alt="A placeholder image, showing the Project27 logo." class="thumbnail-image-blog">
{% endif %}
</div>
<div class="col-9">
<p><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></p>
<p>Posted in 
{% if post.url contains "/dev/" %}
{% assign categoryLink = devLink %}
{% elsif post.url contains "issues" %}
{% assign categoryLink = issuesLink %}
{% elsif post.url contains "latex-to-mathml" %}
{% assign categoryLink = latexLink %}
{% elsif post.url contains "mathml-usability" %}
{% assign categoryLink = mathmlLink %}
{% elsif post.url contains "disabilities" %}
{% assign categoryLink = disabilitiesLink %}
{% elsif post.url contains "identities" %}
{% assign categoryLink = identitiesLink %}
{% elsif post.url contains "nanotip" %}
{% assign categoryLink = nanotipLink %}
{% elsif post.url contains "reading" %}
{% assign categoryLink = readingLink %}
{% elsif post.url contains "special-interests" %}
{% assign categoryLink = specialLink %}
{% else %}
{% assign categoryLink = '/404.html' %}
{% endif %}
<a href="{{ categoryLink | prepend: site.baseurl }}">
{{ post.tag }}
</a>
, on {{ post.date | date_to_rfc822 | date: "%d %b %Y" }}.</p>
</div>
</div>
{% endfor %}
</div>