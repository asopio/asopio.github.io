---
---

Welcome to My Home Page. Here are some descriptions of interesting projects that I have been working on. More projects can be found on my [github profile](https://github.com/asopio).

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
