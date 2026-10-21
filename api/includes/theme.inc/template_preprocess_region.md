# template_preprocess_region()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2969–2976 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2969-L2976)

## Signature

```php
function template_preprocess_region(&$variables)
```

## Documentation

```text
Preprocess variables for region.tpl.php

Prepares the values passed to the theme_region function to be passed into a
pluggable template engine. Uses the region name to generate a template file
suggestions. If none are found, the default region.tpl.php is used.

@see drupal_region_class()
@see region.tpl.php
```

## Code

```php
function template_preprocess_region(&$variables) {
  // Create the $content variable that templates expect.
  $variables['content'] = $variables['elements']['#children'];
  $variables['region'] = $variables['elements']['#region'];

  $variables['classes_array'][] = drupal_region_class($variables['region']);
  $variables['theme_hook_suggestions'][] = 'region__' . $variables['region'];
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
