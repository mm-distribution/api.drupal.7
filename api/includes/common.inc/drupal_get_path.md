# drupal_get_path()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2969–2975 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2969-L2975)

## Signature

```php
function drupal_get_path($type, $name)
```

## Documentation

```text
Returns the path to a system item (module, theme, etc.).

@param $type
  The type of the item (i.e. theme, theme_engine, module, profile).
@param $name
  The name of the item for which the path is requested.

@return
  The path to the requested item or an empty string if the item is not found.
```

## Code

```php
function drupal_get_path($type, $name) {
  if ($filename = drupal_get_filename($type, $name)) {
    return dirname($filename);
  }

  return "";
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
