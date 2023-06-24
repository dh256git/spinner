---
layout: default
title: Roadmap and change log
author: Daniel Hajas
date: 2023-02-19
updated: 2023-02-19
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
logs:
  - name: May 2023 (version 0.4)
    link: /blog/logbook/dev/changes/2023-05.html
  - name: April 2023 (version 0.3)
    link: /blog/logbook/dev/changes/2023-04.html
  - name: March 2023 (version 0.2)
    link: /blog/logbook/dev/changes/2023-03.html
  - name: February 2023 (version 0.1)
    link: /blog/logbook/dev/changes/2023-02.html
  - name: January 2023 (version 0.0)
    link: /blog/logbook/dev/changes/2023-01.html
---

## The roadmap

View our [roadmap on Trello.](https://trello.com/b/0TnZCOLE/issue-tracking)
We have many plans.
If you'd like to have a say in what goes on our roadmap, please submit a [feature request.](https://github.com/dh256git/project27/issues)
You can also help us develop faster, by [becoming a volunteer.]({% link volunteering/become-a-volunteer.md %})

## The change log

Here is what changed on the {{ site.brand }} site.

<ul>
{% for log in page.logs %}
<li>
<a href="{{ log.link | prepend: site.baseurl }}">{{ log.name }}</a>
</li>
{% endfor %}
</ul>

### Versioning

We use a versioning convention where the version number is split to three parts:

1. Version: incremented once a year, typically in January;
2. Sub-version: incremented once a month, typically on the first Sunday of the month;
3. Commit: incremented every time a change has been committed to the live production site.

### Deployment cycle

We aim to merge changes made in the development environment, with the live production site, once a month.
This allows us to collect feedback, develop or update features, and test them, before publishing changes live.
Occasional, quick fixes may be published before a sub-version update is due.

### {{ site.brand }} on Surge

We are using Surge to host our live test site.
If you can't wait to see the latest updates, [check out {{ site.brand }} on Surge.](http://p27skills.surge.sh)
