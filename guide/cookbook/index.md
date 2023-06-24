---
layout: default
title: Cookbook
volume: cookbook
buttonStyle: fg-guide-vol
backgroundStyle: bg-guide-vol
listOfIcons: [["fas fa-ice-cream", ""], ["fas fa-fish", ""], ["fas fa-drumstick-bite", ""], ["", "Pasta.png"], ["", "Risotto.png"], ["fas fa-carrot", ""], ["", "Soup.png"],  ["", "Wrap.png"]]
levelToOpen: chapter
---

## Cookbook: recipes from     the {{ site.brand }} household

Cookbook is a volume of recipes frequently cooked by the {{ site.brand }} team. Instructions are catered in a way that anybody can recreate these dishes regardless their abilities. The key ingredients are positive attitude and commitment.

{% include guide/latest.html %}

---

## Chapters in this volume

We organised this volume into eight chapters.

{% assign dataFile = site.data.chapters.cookbook %}
{% assign gridHide = "Freezer inventory" %}
{% include global/grid-generator.html heading="h3" %}
