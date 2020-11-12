---
layout: minimal
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

# Introduction to Computational Thinking with Data 📊
{: .mb-2 }
Data 94 @ UC Berkeley, Spring 2021
{: .mb-0 .fs-6 .text-grey-dk-000 }





**Instructor:** Suraj Rampure (<a>rampure@berkeley.edu</a>) ⬅️ email with any questions!

[Apply to take the course!](http://tinyurl.com/applydata94){: .btn .btn-outline }

Jump to:
- [Description](#description)
- [Syllabus](#syllabus)
- [Logistics](#logistics)
- [Enrollment](#enrollment)
- [Staff](#staff)

<a name = 'description'>
## Description 📝

<div class="announcement">
  <div class="announcement-body">
  <b>Data 94 is a new class designed to introduce students to programming in Python from the data perspective.</b> In particular, it is meant to be a small, more personal alternative to larger introductory programming courses.
  </div>
</div>

From the course catalog: This course is an introduction to computational thinking and quantitative reasoning, designed to prepare students for further coursework in data science, computer science, and statistics (in particular, Foundations of Data Science, Data C8). This course emphasizes the use of computation to gain insight about quantitative problems with real data from the social sciences.

This class serves a different purposes than several other classes that may sound similar. Specifically:
- **Data 8**: Data 94 does not cover nearly as much statistics and inference as Data 8. Instead, it dives deeper into Python and its applications in data science. After taking this class, you will be well-equipped to take Data 8 and focus on the inference.
- **CS 10**: While CS 10 is also an introductory computing class, it focuses less on Python and data science, and more on abstract ideas in computing. It is a fantastic alternative to Data 94.
- **CS 61A and CS 88**: While these courses also teach Python, they serve a slightly different purpose - namely, they are designed to introduce students to computer science, not to computing in data science. They cover the Python language in far greater detail than we will, but they do not cover how to work with real-world data. They are also substantially more fast-paced than this course.

If you have already taken any of these courses, Data 94 is not the right course for you. But if you haven't -- welcome! We'd be glad to have you 😊

<br>

<a name = 'syllabus'>
## Syllabus 📕
As this is a new course, many of the details are still being finalized. The rough topic breakdown is as follows:

- Weeks 1-4: Python basics in the Jupyter notebook environment.
- Weeks 4-8: Working with real-world tabular data using `datascience` (the library used in Data 8).
- Weeks 9-11: Data visualization.
- Weeks 13-15: Probability and simulation. Special topics, as time permits.

Slides and code will be posted after each lecture, and they will cover everything you are required to know for the course. There is no one textbook that covers the content of this course the way we intend on covering it, though we may link supplementary readings.

<br>

<a name = 'logistics'>
## Logistics 💻
More details will be filled in as we approach the start of the spring semester.

All content for the course will be posted on this website. We will use Piazza for all communication; we will not use bCourses for anything.

### Lecture and Lab
**Class will be held three times a week: on Mondays and Wednesdays from 11AM-12PM, and on Fridays from 11AM-1PM.**
- Lecture is on Mondays, Wednesdays, and Fridays from 11AM-12PM. This is where new ideas are introduced.
- Lab is on Friday from 12-1PM. This is where you will work short exercises and homework assignments with your peers, with assistance from course staff. (Often times, lab will start during the Friday lecture; we view this as one continuous 2-hour block.)

Attendance is expected, though lectures will be recorded and posted on the course website.

### Assignments
Each lecture will be accompanied with a "Quick Check", which is a very short (< 15 min) exercise designed to be completed after coming to lecture. Quick Checks exist to ensure that you're up-to-date with lecture.

This course will have several homework assignments, a few of which will be longer "projects". You will have plenty of time to get help with them in lab and in office hours.

### Exams
We plan on administering three quizzes, in lieu of any midterms. These will roughly be in weeks 4, 8, and 12.

There will also be a final exam.

<br>

<a name = 'enrollment'>
## Enrollment 👋

This course is offered for 3 units, letter graded (though you can opt to take it P/NP). It does not satisfy major requirements for any major.

As this is a small course, we want to ensure that all students enrolled are part of the target audience. As a result, **you cannot enroll in this course automatically - you must first fill out an application.**

We are specifically targeting students who:
- Might be interested in data science
- Have never programmed before
- Do not have time conflicts with the class

If you fit the above criteria and are interested in the course, please fill out the application below.

[Apply to take the course!](http://tinyurl.com/applydata94){: .btn .btn-outline }

Notes about the application process:
- We will filter applications regularly. Spots will be first-come-first-serve; if you apply and you meet the above criteria, you will be emailed a permission code shortly after filling out the form.
- There is no "due date" to apply. The only scenario in which you will not be able to apply is if the waitlist grows very large, and it is clear not everyone will be able to enroll.
- There are X seats available in this class. If more than X students are interested in taking the course (and meet the above criteria), we will maintain a waitlist.
- We are not looking for anything other than whether or not you meet the above criteria. **Nobody is under-qualified to take this course!**

<br>

<a name='staff'>
## Staff 🧑‍🏫

### Instructor

Email the instructor with any questions about the class.

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

### Faculty Advisors

The faculty advisors are helping design the class behind-the-scenes. (Don't email them about this class, but feel free to email them about anything else!)

<div class="role">
  {% assign fa = site.staffers | where: 'role', 'Faculty Advisor' %}
  {% for staffer in fa %}
  {{ staffer }}
  {% endfor %}
</div>

We will also have other course staff members. More details to come!
