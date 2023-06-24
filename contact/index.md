---
layout: default
title: Contact us
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-15
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
listOfIcons: [["", ""], ["", ""]]
---

## {{ page.title }}

We are keen to hear from you, and get the conversation going. You can reach us in multiple ways.

### E-mail

The most convenient way to reach us is via e-mail. Our e-mail address is: `support@project27skills.com`

### Social media

We began to establish, and gradually grow our social media presence. You can follow us at the following platforms.

<div class="row">
{% for profile in site.data.social %}
<div class="col">
<a href="{{ profile.link }}">
<img src="{{ profile.icon | prepend: site.baseurl }}" alt="{{ profile.alt }}" class="social-icon">
</a>
</div>
{% endfor %}
</div>
### PO Box and registered address

We are looking for a suitable location and mail delivery arrangement. Once we have one, we will update this section.

## Frequently asked questions

We were asked the following questions many times. See what we usually say.

<dl>
{% for item in site.data.FAQ %}
<dt>Q: {{ item.question }}</dt>
<dd>A: {{ item.answer }}</dd>
{% endfor %}
</dl>