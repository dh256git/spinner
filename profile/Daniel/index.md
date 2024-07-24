---
layout: default
title: My certificates
---

{% assign url_segments = page.url | split: '/' %}
{% assign member = url_segments[2] %}

# {{ member }}'s certificates

{{ member }}! View the list of certificates you have unlocked so far.

{% for person in site.data.members[member] %}
According to our records, {{ person.name }} is a {{ person.type }}.
{% for item in person['certificates'} %}
{% if item.achieved == true %}
<a href="{{ item.link }}">
🔓 {{ item.title }}
</a>
{% else %}
<a class="disabled" aria-disabled="true" href="#">
🔒 {{ item.title }}
</a>
{% endif %}
{% endfor %}
{% endfor %}