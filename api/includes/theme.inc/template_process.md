# template_process()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2565–2576 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2565-L2576)

## Signature

```php
function template_process(&$variables, $hook)
```

## Documentation

```text
Adds helper variables derived from variables defined during preprocessing.

When preparing variables for a theme hook implementation, all 'preprocess'
functions run first, then all 'process' functions (see theme() for details
about the full sequence).

This function serializes array variables manipulated during the preprocessing
phase into strings for convenient use by templates. As with
template_preprocess(), this function does not get called for theme hooks
implemented as functions.

@see theme()
@see template_preprocess()
```

## Code

```php
function template_process(&$variables, $hook) {
  // Flatten out classes.
  $variables['classes'] = implode(' ', $variables['classes_array']);

  // Flatten out attributes, title_attributes, and content_attributes.
  // Because this function can be called very often, and often with empty
  // attributes, optimize performance by only calling drupal_attributes() if
  // necessary.
  $variables['attributes'] = $variables['attributes_array'] ? drupal_attributes($variables['attributes_array']) : '';
  $variables['title_attributes'] = $variables['title_attributes_array'] ? drupal_attributes($variables['title_attributes_array']) : '';
  $variables['content_attributes'] = $variables['content_attributes_array'] ? drupal_attributes($variables['content_attributes_array']) : '';
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
