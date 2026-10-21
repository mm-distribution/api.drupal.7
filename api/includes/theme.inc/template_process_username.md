# template_process_username()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 3039–3053 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L3039-L3053)

## Signature

```php
function template_process_username(&$variables)
```

## Documentation

```text
Processes variables for theme_username().

@see template_preprocess_username()
```

## Code

```php
function template_process_username(&$variables) {
  // Finalize the link_options array for passing to the l() function.
  // This is done in the process phase so that attributes may be added by
  // modules or the theme during the preprocess phase.
  if (isset($variables['link_path'])) {
    // $variables['attributes_array'] contains attributes that should be applied
    // regardless of whether a link is being rendered or not.
    // $variables['link_attributes'] contains attributes that should only be
    // applied if a link is being rendered. Preprocess functions are encouraged
    // to use the former unless they want to add attributes on the link only.
    // If a link is being rendered, these need to be merged. Some attributes are
    // themselves arrays, so the merging needs to be recursive.
    $variables['link_options']['attributes'] = array_merge_recursive($variables['link_attributes'], $variables['attributes_array']);
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
