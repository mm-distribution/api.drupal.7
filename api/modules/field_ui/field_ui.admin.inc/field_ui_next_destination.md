# field_ui_next_destination()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 2117–2129 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L2117-L2129)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_next_destination($entity_type, $bundle)
```

## Documentation

```text
Returns the next redirect path in a multipage sequence.
```

## Code

```php
function field_ui_next_destination($entity_type, $bundle) {
  $destinations = !empty($_REQUEST['destinations']) ? $_REQUEST['destinations'] : array();
  if (!empty($destinations)) {
    unset($_REQUEST['destinations']);
  }
  // Remove any external URLs.
  $destinations = array_diff($destinations, array_filter($destinations, 'url_is_external'));
  if ($destinations) {
    return field_ui_get_destinations($destinations);
  }
  $admin_path = _field_ui_bundle_admin_path($entity_type, $bundle);
  return $admin_path . '/fields';
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
