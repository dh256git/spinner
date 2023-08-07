---
layout: default
title: Portfolio
tagline: From academic projects to scalable solutions
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-06-24
licence: copyright
buttonStyle: fg-guide-land
backgroundStyle: bg-guide-land
listOfIcons: ["", "olli-logo.png"]
---

## {{ page.title }}: {{ page.tagline }}

Browse a list of research and innovation projects we are involved in.
All of the solutions in our portfolio have been [co-designed with researchers,]({% link for-researchers/index.md %}) and the projects are grounded in peer reviewed science.
To maximise impact, we are working with businesses on [diffusing innovation that works.]({% link for-businesses/index.md %})

{% assign dataFile = site.data.projects %}
{% include global/grid-generator.html heading="h3" %}