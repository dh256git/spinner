---
layout: default
title: Project27 Skills
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2023-01-07
updated: 2023-02-04
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
---

{% assign skills = site.data.skills %}

## {{ page.title }}

Developing {{ site.brand }} is an extensive source of learning and enjoyment.
There are a range of topics that matter to us in the team.
We use these topics to facilitate the development of our own skills, while building the {{ site.brand }} {{ site.product }}.
As a result, we get better at doing things, and record an ever growing list of skills that matter to us.
If you find a skill set, or a particular skill on the list that matters to you, and you want to learn by getting involved, please [check out our volunteer opportunities.]({% link volunteering/index.md %})

### Skills that matter to us: {{ skills | size }} and counting

So far, we learnt {{ skills | size }} skills, across the following skill sets:

- [accessibility,](#accessibility-skills)
- [web development,](#web-dev-skills)
- [digital skills,](#digital-skills)
- [entrepreneurship,](#entrepreneurship)
- [social skills,](#social-skills)
- [personal competencies,](#personal)
- [journalism,](#journalism) and
- [research.](#research)

#### Accessibility

The accessibility skill set is useful to anyone, who wants to learn how to make web content accessible to screen reader users, as well as learning disabled and low vision visitors. We strive to develop the best user experience, making our space disability inclusive.

<ul id="accessibility-skills">
{% for item in skills %}
{% if item.Category == 'Accessibility' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Web development

Web development is a very valuable skill set in the 2020s. Knowing how to develop a web space, enabled us to make {{ site.brand }} available on multiple devices, such as your smart phone or desktop computer. 

<ul id="web-dev-skills">
{% for item in skills %}
{% if item.Category == 'Web development' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Digital skills

Web development is an essential skill set that matters to us; however, we also needed to learn additional digital skills to be able to build and manage {{ site.brand }}.

<ul id="digital-skills">
{% for item in skills %}
{% if item.Category == 'Digital skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Entrepreneurship

Entrepreneurship enables us to evaluate the viability of working on {{ site.brand }} as a social enterprise. It is the entrepreneurial skills that transform our hobby behind closed doors into a safe-space for all to participate in learning. 

<ul id="entrepreneurship">
{% for item in skills %}
{% if item.Category == 'Entrepreneurship' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Social skills

No doubt, we have picked up many technical skills on the way, but in the process we also strengthened our social skills.

<ul id="social-skills">
{% for item in skills %}
{% if item.Category == 'Social skills' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Personal competencies

In general, we became more confident, more productive, happier people. As the project grows, we grow too.

<ul id="personal">
{% for item in skills %}
{% if item.Category == 'Personal competencies' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Journalism

We value community, and the life stories within. To capture and share these stories appropriately, we started developing a skill set of journalism.

<ul id="journalism">
{% for item in skills %}
{% if item.Category == 'Journalism' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

#### Research

True to our origins from university life, we continue to develop our research skills, let it be academic, user, or market research.

<ul id="research">
{% for item in skills %}
{% if item.Category == 'Research' %}
<li>
{{ item.Skill }}
</li>
{% endif %}
{% endfor %}
</ul>

---

### Skills that matter to you

Do you have a unique set of skills you would like to get better at, involve others, and share your achievements?
Are you interested in building your braille art gallery?
Are you working on a video game?
Do you want to create your library of accessible comic-books?

If the {{ site.brand }} {{ site.product }} does not include a topic you are interested in, and the skills that matter to us exclude the skills you want to develop, we may still be able to support you.

Using our skills in web development and entrepreneurship, we can help you create your own safe-space, similar to {{ site.brand }}.
We are committed to host, and let you showcase your very own project on our community platform.
The platform allows you to write your own project blog, organise your resources and content, recruit contributors, as well as offer your support within your project community.

To find out more, contact us:

- via e-mail: support@project27skills.com.