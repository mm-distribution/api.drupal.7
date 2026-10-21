# modules/user/user-profile-category.tpl.php

- **Source:** [local](../../../../source/modules/user/user-profile-category.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user-profile-category.tpl.php) · 34 lines
- **Module/theme:** user

## File documentation

```text
@file
Default theme implementation to present profile categories (groups of
profile items).

Categories are defined when configuring user profile fields for the site.
It can also be defined by modules. All profile items for a category will be
output through the $profile_items variable.

@see user-profile-item.tpl.php
     where each profile item is rendered. It is implemented as a definition
     list by default.
@see user-profile.tpl.php
     where all items and categories are collected and printed out.

Available variables:
- $title: Category title for the group of items.
- $profile_items: All the items for the group rendered through
  user-profile-item.tpl.php.
- $attributes: HTML attributes. Usually renders classes.

@see template_preprocess_user_profile_category()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
