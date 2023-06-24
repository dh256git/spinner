---
layout: default
title: Volunteering
tagline: Together we learn, together we grow
author: Daniel Hajas
reviewer: Danielle Garratt
date: 2022-10-02
licence: copyright
buttonStyle: fg-general-vol
backgroundStyle: bg-general-vol
---

{% assign teamLeadership = site.volunteering | where:"team","Management" %}
{% assign teamRnD = site.volunteering | where:"team","RnD" %}
{% assign teamER = site.volunteering | where:"team","ER" %}
{% assign teamContent = site.volunteering | where:"team","Content" %}

## {{ page.title }}: {{ page.tagline }}

Get involved and become a part of our community.
You can contribute as a [volunteer,](#apply-to-volunteer-top) or as a [member,](#membership) and [develop your skills]({% link about/skills.md %}) through hands-on tasks.

{% include global/cover-image.html image="volunteering-cover.jpg" alt="A drawn tree, with handprints as leaves on the branches." %}

## Why should I contribute?

{{ site.brand }} is built by its community.
Here is why you should become a part of it:

1. We need your help. We are not experts or professionals in everything that's needed to keep {{ site.brand }} up and running. There is a lot to do, so a helpful hand is always appreciated.
2. Do it for yourself. We can guarantee, you will learn something new and useful.

<a id="apply-to-volunteer-top" class="{{ page.buttonStyle }}" aria-disabled="false" href="{{ '/volunteering/become-a-volunteer.html' | prepend: site.baseurl }}">Become a volunteer</a>

### What are the benefits of becoming a volunteer?

There are benefits of volunteering in our community, even if you don't want to become a member.

<ol>
<li>
Learn new skills, or improve your existing skills.<div id="volunteer1"></div><div id="morevolunteer1">
{{ site.brand }} is all about learning new skills, and getting better in doing certain things, by practicing, and innovating.
The project offers a wide range of skills to pick up and nurture, and you get to choose which is most valuable to you. All that {{ site.brand }} volunteering roles do, is setting SMART (Specific, Measurable, Achievable, Relevant, and Timely) targets for you to work towards.
</div>
<button onclick="readMoreVolunteering1()" id= "Read-More-BTN1">Read more</button>
</li>

<li>
Use your knowledge and productivity output to help others.<div id= "volunteer2"></div><div id="morevolunteer2">
In the process of learning, you are also contributing to a shared vision.
You could learn on your own, and practice through your personal project.
Wouldn't it be more satisfying though, to help other people in the process?
There are no deadlines, no punishment if something doesn't work out.
It's learning through trial and error, and practice.
What we build together, ultimately helps communities of blind or learning disabled people.
</div>
<button onclick="readMoreVolunteering2()" id="Read-More-BTN2">Read more</button>
</li>

<li>
Be part of a team. <div id= "volunteer3"></div><div id="morevolunteer3">
 Vibrant teams maintain a friendly vibe.
 There will be opportunities to be social by both digital and physical ways.
 Turn up for every, or every fifth team checkin.
 Stay for an hour, or drop in for only ten minutes.
 Being socially proactive is not a must, only an opportunity.
</div>
<button onclick="readMoreVolunteering3()" id="Read-More-BTN3">Read more</button>
</li>

<li>
Satisfy your dopamine with an extra reward. <div id= "volunteer4"></div> <div id="morevolunteer4">
Are you the collector type, gathering and displaying credits, kudos,, acknowledgements, thanks, and all that jazz?

Then you'll also get the rewards on <a href="/about/team/index.html">our team page,</a> as well as in the inner circle of {{ site.brand }}.
</div>
<button onclick="readMoreVolunteering4()" id="Read-More-BTN4">Read more</button>
</li>
</ol>

### When can I become a volunteer?

Applications open on the 1st of October, 2023.
You can submit an application anytime after this date.

Volunteer registration will open with the launch of version 1.0 of the {{ site.brand }} site, on the 31st of January, 2024.

---

## How much time should I commit?

The level of engagement is flexible. You may

+ identify, or ask us for a single challenge, solve it, and you are done.
+ continue working on multiple challenges, whenever you find time, even if only a couple hours in a month.
+ get hooked, and if you have nothing better to do, treat it as a part time role.

### Certified pathways of volunteering {#certification}

We are committed to certifying your contributions. Currently, we offer the following achievements:

Trainee
: after successful completion of 4 tasks (~16 hours of commitment);

Apprentice
: after successful completion of 16 tasks (~16 hours of regular commitment per week, for one month);

Intern
: after successful completion of 48 tasks (~16 hours of regular commitment per week, for three months);

Active member
: after successful completion of 100 tasks (~8 hours of regular commitment per week, for one year)

Active members will be considered for part-time employment at {{ site.brand }} or one of our partners; subject to funding and the legal constitution of the {{ site.brand }} business entity.

---

## What can I work on?

Browse our activity catalogue, and get involved.
Select a team, before viewing a list of available activities.
The activity pages provide an overview of what's expected, as well as a list of very specific tasks to choose from.

{% assign community-teams = site.data.volunteering.community %}
<div class="row">
<div class="col-3">
<p>Team:</p>
</div>
<div class="col-3">
<select onchange="handleChange(this)">
{% for item in community-teams %}
<option value="{{ item.value | prepend: site.baseurl }}" label="{{ item.label }}">{{ item.text }}</option>
{% endfor %}
</select>
</div>
<div class="col-6">
<a data-toggle="collapse" href="#how-it-works" aria-expanded="false" aria-controls="how-it-works">How does it work?</a>
</div>
</div>

<div class="collapse" id="how-it-works">
<h3>How does it work?</h3>

At the moment, we do it all.
And we can't wait to find people who do some of our tasks much better than we do.
That's how {{ site.brand }} grows.
That's also how we build a community of peer support.

We don't have roles, we work on tasks.
As such, we adopted <a href="https://mentorphile.com/2019/03/05/fostering-apples-culture-of-accountability-the-dri/">Apple's Directly Responsible Individual (DRI) way of working.</a>
Everyone in the team is directly responsible for the task assigned to them.

Some tasks are permanent, just like washing up is.
Other tasks may disappear once they are done, just like you would post a letter only once.
When you become a volunteer, you can bid on tasks, using an internal system.
The rest is history.
</div>

<div class="iframe-container">
<iframe src="{{ '/volunteering/research-and-development/index.html' | prepend: site.baseurl }}" title="Research and Development" id="iframe-id" class="responsive-iframe"></iframe>
</div>

{% include spotlight.html %}

---

## Membership at {{ site.brand }} {#membership}


We plan to open a membership application on 1st of January, 2024.
Members will access additional benefits, based on a subscription.


### What are the benefits of becoming a member?

There are multiple benefits to becoming a member. For example, you will

* get 1 credit of [supervision support]({% link support/pricing.md %}) per month;
* get [certifications](#certification) of your contributions;
* be able to join more than 1 team;
* be able to contribute an unlimited number of tasks;
* get access to exclusive content on the {{ site.brand }} {{ site.product }};
* get access to collectable badges to display on your profile;
* get discounts on our community events.

### When can I become a member?

Please, express your interest in becoming a member, by using the button below.
The launch date of membership registration may change depending on your interest.

We plan to open membership registration with the launch of version 2.0 of the {{ site.brand }} site, on the 31st of January, 2025.

<a id="apply-to-volunteer-bottom" class="{{ page.buttonStyle }}" aria-disabled="false" href="{{ '/volunteering/become-a-volunteer.html' | prepend: site.baseurl }}">I'd like to become A member</a>

### How much does membership cost?

Membership is priced slightly differently, depending on the subscription you select.

* paid monthly: £24.99 a month,
* paid yearly: £239.90 a year (£19.99 a month).

---

## What happens after I apply?

Whether you join our community as a volunteer, or as a member, we will set you up for success.
We follow a three step process to ensure you have a great experience of joining the team.

Introduction
: We organise a 30 minute long virtual meeting with you to make introductions, understand your interests, and discuss the tasks you would like to help with.

On-boarding
: During your first week, we ask you to complete our on-boarding workflow, which involves reading through our 'getting started' package.
: A 30 minute long virtual meeting, to get you familiar with our systems.
: A second 30 minute long virtual meeting, to set you up on your first task.

Supervision
: During the first month with us, we offer a [free supervision session]({% link support/pricing.md %}), to make sure you can give us feedback, ask questions, and to help you combat initial difficulties.
: Supervision is optional and flexible. You can choose to take the full hour, take two 30 minute long sessions, or not use it at all.