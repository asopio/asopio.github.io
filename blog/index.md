---
layout: default
title: "Blog"
description: "Writing on physics, AI, and things I find interesting."
---

<div class="page-header content-container">
  <h1>Blog</h1>
  <p class="lead">Writing on physics, machine learning, trading, and other topics that catch my attention.</p>
</div>

<div class="container" style="padding-bottom: 4rem;">
  <section class="section" style="border-top: none; padding-top: 0;">
    <div class="post-list">
      {% for post in site.posts %}
      <a class="post-item" href="{{ post.url }}">
        <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
        <span class="post-title">{{ post.title }}</span>
      </a>
      {% endfor %}
    </div>
  </section>
</div>
