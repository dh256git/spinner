---
title: Management
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

### Management & Leadership team

Join the Management & Leadership team.
 We need to plan the future, while coordinating our work in the present.

Members of the management team help with business activities and other key tasks.
Managers lead by example, supporting volunteers of other teams.
Team members can break down  their tasks, and recruit new members to work on these smaller tasks.
By doing so, they can also create new, senior leadership roles in the C-suite of {{ site.brand }} for themselves.

### Activity list

There are {{ teamLeadership | size }} available activities.

{% for member in teamLeadership %}
<h4>{{ member.task }}</h4>

<p>{{ member.excerpt }}</p>

<a target="_blank" rel="noreferrer noopener" href="{{ member.url | prepend: site.baseurl }}" class="{{ page.buttonStyle }}">{{ member.task }}: View tasks and the activity description</a>
{% else %}
<p>Currently no activities are available in this team.</p>
{% endfor %}