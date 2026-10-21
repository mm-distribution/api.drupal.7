# filter_get_formats_by_role()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 495–504 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L495-L504)
- **Module/theme:** filter

## Signature

```php
function filter_get_formats_by_role($rid)
```

## Documentation

```text
Retrieves a list of text formats that are allowed for a given role.

@param $rid
  The user role ID to retrieve text formats for.

@return
  An array of text format objects that are allowed for the role, keyed by
  the text format ID and ordered by weight.
```

## Code

```php
function filter_get_formats_by_role($rid) {
  $formats = array();
  foreach (filter_formats() as $format) {
    $roles = filter_get_roles_by_format($format);
    if (isset($roles[$rid])) {
      $formats[$format->format] = $format;
    }
  }
  return $formats;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
