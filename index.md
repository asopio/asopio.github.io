---
---

Welcome to My Home Page. Here are some interesting projects that I have been working on [link](https://github.com/asopio).

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
