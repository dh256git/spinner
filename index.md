---
layout: default
title: Project27 - Solutions that work
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-06-24
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
listOfIcons: [["fas fa-pencil-alt", ""], ["fas fa-compass", ""], ["fa-solid fa-handshake", ""], ["fa-solid fa-person-chalkboard", ""]]
---

## Why trust us?

Because we are trustworthy.

## What we do?

{{ site.brand }} is the research and innovation arm of the {{ site.organisation }}.
We work in partnership with researchers and businesses interested in disability inclusion.

{% assign dataFile = site.data.what-we-do %}
{% assign gridLimit = 3 %}
{% include global/grid-generator-2.html heading="h4" %}