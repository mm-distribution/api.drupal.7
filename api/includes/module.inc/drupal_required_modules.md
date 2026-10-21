# drupal_required_modules()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 986–1001 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L986-L1001)

## Signature

```php
function drupal_required_modules()
```

## Documentation

```text
Returns an array of modules required by core.
```

## Code

```php
function drupal_required_modules() {
  $files = drupal_system_listing('/^' . DRUPAL_PHP_FUNCTION_PATTERN . '\.info$/', 'modules', 'name', 0);
  $required = array();

  // An installation profile is required and one must always be loaded.
  $required[] = drupal_get_profile();

  foreach ($files as $name => $file) {
    $info = drupal_parse_info_file($file->uri);
    if (!empty($info) && !empty($info['required']) && $info['required']) {
      $required[] = $name;
    }
  }

  return $required;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
