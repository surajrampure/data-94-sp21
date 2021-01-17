---
layout: page
title: Home
nav_order: 1
description: >-
    A week-to-week description of the content covered in the course.
---

# Introduction to Computational Thinking with Data 📊
{: .mb-2 }
UC Berkeley, Spring 2021
{: .mb-2 .fs-6 .text-grey-dk-000 }

{: .mb-2 }
**Instructor:** Suraj Rampure (<a>rampure@berkeley.edu</a>)
{: .mb-0 .fs-5 .text-grey-dk-000 }

{: .mb-3 }
**Lecture:** MWF 11AM-12PM, **Lab:** F 12-1PM, **Office Hours:** See [Ed](https://edstem.org/us/courses/3251/discussion/201908)
{: .mb-0 .fs-5 .text-grey-dk-000 }

<!-- {% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div> -->

[Syllabus](syllabus){: .btn .btn-blue } [Zoom links](https://edstem.org/us/courses/3251/discussion/201908){: .btn .btn-purple } [Interested in enrolling? Read this!](enrollment){: .btn .btn-green }

The following breakdown is tentative. All assignments are available for public consumption on our [GitHub](https://github.com/surajrampure/data-94-sp21/).

{% for module in site.modules %}
{{ module }}
{% endfor %}
