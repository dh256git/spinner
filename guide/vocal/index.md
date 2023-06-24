---
layout: default
title: Vocal
volume: vocal
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["fas fa-microphone", ""], ["fas fa-broadcast-tower", ""]]
levelToOpen: chapter
---

## Vocal - An album of voices

Vocal is a volume of short biographies and audio recorded conversations with family, friends, and acquaintances of the {{ site.brand }} author. The album's key objective is to portray multiple life stories and honour the storytellers.

{% include guide/latest.html %}

---

## Chapters in this volume

We begin editing this volume by including two chapters. First, notes on capturing stories. Second, a collection of stories to share.

{% assign dataFile = site.data.chapters.vocal %}
{% include global/grid-generator.html heading="h3" %}
