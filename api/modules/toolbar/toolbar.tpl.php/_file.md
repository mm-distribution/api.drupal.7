# modules/toolbar/toolbar.tpl.php

- **Source:** [local](../../../../source/modules/toolbar/toolbar.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.tpl.php) · 40 lines
- **Module/theme:** toolbar

## File documentation

```text
@file
Default template for admin toolbar.

Available variables:
- $classes: String of classes that can be used to style contextually through
  CSS. It can be manipulated through the variable $classes_array from
  preprocess functions. The default value has the following:
  - toolbar: The current template type, i.e., "theming hook".
- $toolbar['toolbar_user']: User account / logout links.
- $toolbar['toolbar_menu']: Top level management menu links.
- $toolbar['toolbar_drawer']: A place for extended toolbar content.

Other variables:
- $classes_array: Array of html class attribute values. It is flattened
  into a string within the variable $classes.

@see template_preprocess()
@see template_preprocess_toolbar()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
