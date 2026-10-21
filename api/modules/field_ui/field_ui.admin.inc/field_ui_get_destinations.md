# field_ui_get_destinations()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 2105–2112 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L2105-L2112)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_get_destinations($destinations)
```

## Documentation

```text
Extracts next redirect path from an array of multiple destinations.

@see field_ui_next_destination()
```

## Code

```php
function field_ui_get_destinations($destinations) {
  $path = array_shift($destinations);
  $options = drupal_parse_url($path);
  if ($destinations) {
    $options['query']['destinations'] = $destinations;
  }
  return array($options['path'], $options);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
