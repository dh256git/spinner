---
title: Research & Development
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

### Research & Development team

Join the Research and Development (R&D) team.
The R&D team members help with the research and development activities of {{ site.brand }}, such as website development or researching solutions to ongoing challenges in the project.

### Activity list

There are {{ teamRnD | size }} available activities.

{% for member in teamRnD %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a target="_blank" rel="noreferrer noopener" href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">{{ member.task }}: View tasks and the activity description</a>
{% else %}
<p>Currently no activities are available in this team.</p>
{% endfor %}