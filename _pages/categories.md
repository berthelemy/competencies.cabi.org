---
layout: default
title: Categories
permalink: categories/
---

{% assign all_categories_str = "" %}
{% for skill in site.data.skills %}
  {% assign all_categories_str = all_categories_str | append:skill.category | append: "," %}
{% endfor %}
{% assign all_categories = all_categories_str | split: "," %}
{% assign uniq_categories = all_categories | uniq %}
{% assign count = 0 %}{% assign n = 0 %}
{% for category in uniq_categories %}
  {% if count == 0 %}<div class="row">{% endif %}
  {% assign count = count | plus: 1 %}
  <div class="col-4 col-12-narrower col-12-mobilep">
  <h4>{{ category }}</h4>
  {% for skill in site.data.skills %}
    {% if skill.category == category %}
    {% assign n = n | plus: 1 %}
    <p><a href="#ex{{ n }}" rel="modal:open">{{ skill.title }}</a></p>
    <!-- The Modal -->
    <div id="ex{{ n }}" class="modal">
      <h4>{{ skill.title }}</h4>
      <h5>Description</h5>
      <p>{{ skill.description }}</p>
      <div class="categories">
        <h5>Category</h5>
        <p><span class="category {{ skill.category | slugify }}">{{ skill.category }}</span></p>
      </div>

      <div class="roles">
        <h5>Roles</h5>
        {% for role in skill.roles %}
        <p><span class="role {{ role | slugify }}">{{ role }}</span></p>
        {% endfor %}
      </div>
      <h5>Levels</h5>
      <div class="levels">
        {% for level in skill.levels %}
        <p><span class="level {{ level | slugify }}">{{ level }}</span></p>
        {% endfor %}
      </div>
      <a href="#" rel="modal:close">Close</a>
    </div><!-- end modal-->
    {% endif %}
  {% endfor %}
  </div>
  {% if count == 3 %}{% assign count = 0 %}</div>{% endif %}
{% endfor %}
