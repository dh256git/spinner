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

We are keen to hear from you, and get the conversation going.
You can reach us in one of the following ways.

### E-mail

The fastest, and most convenient way to contact us is by e-mail.
Our e-mail address is: `support@project27skills.com`

### Phone and WhatsApp message

Give us a call during our responsive hours, or drop a WhatsApp message to: 
`+44 (0) 74 244 50 325`

Our responsive hours are:

- Tuesday, between 16:00 and 18:00,
- Wednesday, between 18:00 and 20:00,
- Thursday, between 16:00 and 18:00,
- Sunday, between 13:00 and 17:00.

### Social media

We began to establish, and gradually grow our social media presence.
Follow us at the following platforms.

<div class="row">
{% for profile in site.data.social-side %}
<div class="col">
{% if profile.link contains "dragonscave.space" %}
<a target="_blank" rel="me" href="{{ profile.link }}">
<img src="{{ profile.icon | prepend: site.baseurl }}" alt="{{ profile.name }}" class="img-follow-us-new">
</a>
{% else %}
<a target="_blank" rel="noopenner noreferrer" href="{{ profile.link }}">
<img src="{{ profile.icon | prepend: site.baseurl }}" alt="{{ profile.name }}" class="img-follow-us-new">
</a>
{% endif %}
</div>
{% endfor %}
</div>

### Registered and postal address

You can send us hand-written or printed letters to the following address:

```Project27 Consultancy Group C.I.C.,
Unit 7, Hove Business Centre,
Fonthill Rd, Hove, England,
BN3 6HA.```

---

## Frequently asked questions

We were asked the following questions many times. See what we usually say.

<dl>
{% for item in site.data.FAQ %}
<dt>Q: {{ item.question }}</dt>
<dd>A: {{ item.answer }}</dd>
{% endfor %}
</dl>