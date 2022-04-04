---
layout: default
title: Skills table
datatable: table1
permalink: table/
---
The table below allows you to sort and search the skills as needed. Or you can download all the skills as a CSV file. Or even select some skills to download.

<table id="{{ page.datatable }}" class="stripe">
<thead>
  <th>Title</th>
  <th>Category</th>
  <th>Description</th>
</thead>
{% for skill in site.data.skills %}
  <tr>
  <td>{{ skill.title }}</td>
  <td>{{ skill.category }}</td>
  <td>{{ skill.description }}</td>
  </tr>
{% endfor %}
</table>
