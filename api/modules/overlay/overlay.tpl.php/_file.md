# modules/overlay/overlay.tpl.php

- **Source:** [local](../../../../source/modules/overlay/overlay.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.tpl.php) · 40 lines
- **Module/theme:** overlay

## File documentation

```text
@file
Default theme implementation to display a page in the overlay.

Available variables:
- $title: the (sanitized) title of the page.
- $page: The rendered page content.
- $tabs (array): Tabs linking to any sub-pages beneath the current page
  (e.g., the view and edit tabs when displaying a node).

Helper variables:
- $classes_array: Array of html class attribute values. It is flattened
  into a string within the variable $classes.

@see template_preprocess()
@see template_preprocess_overlay()
@see template_process()

@ingroup themeable
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
