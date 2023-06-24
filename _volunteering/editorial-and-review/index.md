---
title: Editorial & Review
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2020-10-02
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamCC = site.volunteering | where:"team","CC" %}

### Editorial & Review team

Join the Editorial & Review team.
The team of editors and reviewers help us make sure content is relevant and a high quality.

### Activity list

There are {{ teamER | size }} available activities.

{% for member in teamER %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a target="_blank" rel="noreferrer noopener" href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">{{ member.task }}: View tasks and the activity description</a>
{% else %}
<p>Currently no activities are available in this team.</p>
{% endfor %}
