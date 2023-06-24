---
layout: default
title: Dashboard
buttonStyle: fg-general-chap
backgroundStyle: bg-general-chap
listOfIcons: [["", ""], ["", ""]]
burndownData: /about/dashboard/burndown-data/current-sprint.csv
---
## {{ page.title }}

Welcome to the project dashboard.
You will find our roadmap and you can view status updates below.

**Accessibility notice**:

* Currently, the burndown chart is not accessible on mobile platforms.
* The roadmap is not an easy read.

### Roadmap

The roadmap of {{ site.brand }} starts on 6th of October, 2019 with setting the cornerstone.
The road ahead is made up of four milestones, separated by five year intervals.

{% capture rm2020 %}
Collecting physics notes and recipes scattered around the hard-drive into a single,  accessible, and usable platform.
{% endcapture %}

{% capture rm2025 %}
<h4>2025 milestone</h4></p>
<p>
Theme: Development of a private site based on product requirements of the product owner.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: {{ site.brand }} is developed by the product owner. Contributions are made by trusted friends and family.</li>
<li>Research and Development (R&D): Learning basic web development skills, and developing v0.1.</li>
<li>Project management (PM) & business development (BD) : Learning basic project management and business development skills, and setting a workflow up.</li>
<li>R&D: Documenting the challenges and solutions occurred during the experimentation with methods of creating accessible content for  technical documents.</li>
<li>Content: Expanding original content with reviewed written notes and posts, external links, and external multimedia.</li>
</ul>
<p>
The key performance indicators are:
</p>
<ul>
<li>How much do people in the organisation engage with the initiatives of the current milestone?</li>
<li>Is {{ site.brand }} a stable release of a coherent, usable, and easy-to-maintain website architecture?</li>
<li>Are basic project management procedures and business development strategies established in a sustainable framework?</li>
<li>How regularly are R&D challenges and solutions executed and documented?;</li>
<li>How many reviewed "notes" and "posts" are published in individual Guide "chapters", and Blog "categories" respectively?</li>
<li>Does the next milestone and its initiatives reflect the latest requirements, and are Keep Performance Indicators (KPIs) updated?</li>
</ul>
<p>Moving on...
{% endcapture %}

{% capture rm2030 %}
<h4>2030 milestone</h4></p>
<p>
Theme: Pivoting towards requirements set by stakeholders.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: The product owner and a business partner works together to adapt the product to new requirements set by stakeholders. Contributions are made by three {{ site. brand }} teams: the R&D team, the editorial and review team, and the content creation team.</li>
<li>R&D: Exploring challenges and solutions for accessible data visualisations, figures, and videos of technical nature.</li>
<li>Content: Expanding notes and posts in existing volumes and branches. Considering new volumes based on stakeholder requirements.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2035 %}
<h4>2035 milestone</h4></p>
<p>
Theme: Consolidating operations.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Team: Establishing organisational structure. The CEO oversees the content creation, funding and marketing tasks. The CTO is responsible for quality assurance of the web architecture including accessibility and functionality, as well as exploring new technological solutions in line with the vision and mission statements.</li>
<li>Community: associate editors are appointed to take care of individual volumes, and content authors are recruited for creative and review tasks.</li>
<li>Content: Volumes are expanded by content authors. User requirements are used to design content.</li>
<li>R&D: A system is developed for submitting user authored content and its distribution for peer-review.</li>
</ul><p>
Moving on...
{% endcapture %}

{% capture rm2050 %}
<h4>2050 milestone</h4></p>
<p>
Theme: {{ site.brand }} opens for public contributions, which are published after peer-review.
</p>
<p>
The key initiatives towards the milestone are:
</p>
<ul>
<li>Community: Operation starts as conventional journals with editor, associate editors,-reviewers, and authors.</li>
<li>Project management "PM" & business development "BD": Strategy is developed for harnessing revenue streams from the tools developed and the team expertise, reinvesting in advancing {{ site.brand }} R&D initiatives.</li>
</ul><p>
If the project has got as far as this, the roadmap will be extended.
{% endcapture %}

{% include global/collapseable.html trigger="2020 cornerstone" paragraph=rm2020 ID="R2020" %}
{% include global/collapseable.html trigger="2025 milestone" paragraph=rm2025 ID="R2025" %}
{% include global/collapseable.html trigger="2030 milestone" paragraph=rm2030 ID="R2030" %}
{% include global/collapseable.html trigger="2035 milestone" paragraph=rm2035 ID="R2035" %}
{% include global/collapseable.html trigger="2050 milestone" paragraph=rm2050 ID="R2050" %}

#### The roadmap explained

The time between the cornerstone and the first milestone is used to learn, experiment, and set the scene for a scalable project.
Although one of the key objective at the personal level is to learn web development, expanding the Research and Development (R&D) team with a professional web developer who is able to innovate through modern technological solutions, would be desirable.

The second milestone introduces the project and its stakeholders to each other, updating product requirements, with a business partner on board.
The project management (PM) & business development (BD) team is formed.

The third milestone transfers ownership parts of the product to associate editors, and reviewers are recruited to make up the {{ site.brand }} community.
Content is heavily influenced by user requirements.

In the final milestone, the project is community driven, by means of peer-reviewed contributions. Content is managed by associate editors, while the management team looks after sustainability, scalability, and reinvestment in R&D initiatives.

#### Issue tracking

{{ site.brand }} tracks known issues on inaccurate information, as well as known accessibility bugs around the scientific content.
This is done through the GitHub repository and the LogBook posts.

### Latest sprint - progress chart

{% include dashboard/burndown.html %}