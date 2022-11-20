---
layout: default
title: Spinner home page
---

# Welcome to Spinner

Spinner Group is the home for the Project27 platform. Our mission is to accelerate impact by spinning out research projects, which aim to help blind and learning disabled people.

## Project27

View our projects.


<select onchange="handleChange(this)">
<option value="{{ '/project-Anna.html' | prepend: site.baseurl }}" label="Project27.1: Anna">Project27.1: Anna</option>
<option value="{{ '/project-Olli.html' | prepend: site.baseurl }}" label="Project27.2: Olli">Project27.2: Olli</option>
</select>

<h3 id="frame-heading">Select a project</h3>

<iframe src="{{ '/project-Anna.html' | prepend: site.baseurl }}" title="Project gallery" id="iframe-id" height="500" width="800"></iframe>

<!--script for select pop-up -->
<script defer src="{{ '/pop-up.js' | prepend: site.baseurl }}"></script>