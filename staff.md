---
layout: page
title: Staff
nav_exclude: True
description: A listing of all the course staff members.
---

# Staff

### Instructor

<div class="role">
  {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

<!-- <a name = 'tas'></a>

### Teaching Assistant

<div class="role">
  {% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
  {% for staffer in teaching_assistants %}
  {{ staffer }}
  {% endfor %}
</div>

<a name = 'tutors'></a>

### Tutor

<div class="role">
  {% assign readers = site.staffers | where: 'role', 'Tutor' %}
  {% for staffer in readers %}
  {{ staffer }}
  {% endfor %}
</div> -->

### Faculty Advisors

<div class="role">
  {% assign fa = site.staffers | where: 'role', 'Faculty Advisor' %}
  {% for staffer in fa %}
  {{ staffer }}
  {% endfor %}
</div>
