---
layout: default
title: Home of Project27
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-08-27
updated: 2023-01-21
licence: copyright
buttonStyle: fg-general-land
backgroundStyle: bg-general-land
listOfIcons: [["fas fa-pencil-alt", ""], ["fas fa-compass", ""], ["fa-solid fa-handshake", ""], ["fa-solid fa-person-chalkboard", ""]]
---

## Why trust us

We help blind or learning disabled people to develop skills that matter.
{{ site.brand }} reduces the frustration caused by inaccessible learning tools, and builds confidence in your abilities.
We do this through peer support, personalised opportunities for learning, creating and discovering new challenges in a safe place, built by it's community.

{% include global/cover-image.html image="founders-cover.jpg" alt="Daniel and Danielle are photographed in the UK Parliament. They are wearing smart clothing. A guide dog is sitting in front of them. In the background multiple signs are visible, such as logos of University College London, World Health Organisation, and GDI Hub. Other signs read 'AT changes lives' and 'Launching the Global Report on Assistive Technology'." %}

{{ site.brand }} is developed by a couple - [Daniel]({% link about/team/Daniel/index.html %}) and [Danielle]({% link about/team/Danielle/index.html %}).
We draw on our lived experiences and professional skills.
Daniel is a scientifically-minded blind person, with an interest in social entrepreneurship.
Danielle is a sociable learning disabled person, with an interest in art, media, gaming, and self-advocacy.

{% include global/buttonLink.html url="/about/index.html" label="Read more about us" %}

{% include global/testimonials.html %}

---

## What we do

We engage in four key activities to support our mission.

{% assign dataFile = site.data.what-we-do %}
{% assign gridLimit = 4 %}
{% include global/grid-generator-2.html heading="h4" %}

{% include spotlight.html %}
