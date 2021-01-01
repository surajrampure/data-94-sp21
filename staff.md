---
layout: page
title: Staff
nav_order: 3
description: A listing of all the course staff members.
---

# Staff 🧑‍🏫

## Instructor

Email the instructor with any questions about the class.

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

## Staff

Our GSI, tutor, and lab assistants help in running all aspects of the class.

{% assign staff = site.staffers | where: 'role', 'Staff' %}
<div class="role">
  {% for staffer in staff %}
  {{ staffer }}
  {% endfor %}
</div>

## Faculty Advisors

The faculty advisors are helping design the class behind-the-scenes. (Don't email them about this class, but feel free to email them about anything else!)

<div class="role">
  {% assign fa = site.staffers | where: 'role', 'Faculty Advisor' %}
  {% for staffer in fa %}
  {{ staffer }}
  {% endfor %}
</div>
