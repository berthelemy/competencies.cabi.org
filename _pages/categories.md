---
layout: default
title: Categories
permalink: /categories/
---

{% assign all_categories_str = "" %}
{% for skill in site.data.skills %}
  {% assign all_categories_str = all_categories_str | append:skill.category | append: "," %}
{% endfor %}
{% assign all_categories = all_categories_str | split: "," %}
{% assign uniq_categories = all_categories | uniq %}
{% assign count = 0 %}
{% for category in uniq_categories %}
  {% assign count = count | plus: 1 %}
  <div class="col_4">
  <h4>{{ category }}</h4>
  {% for skill in site.data.skills %}
    {% if skill.category == category %}
    <p>{{ skill.title }}</p>
    {% endif %}
  {% endfor %}
  </div>
  {% if count == 3 %}{% assign count = 0 %}<div class="clear"></div>{% endif %}
{% endfor %}
