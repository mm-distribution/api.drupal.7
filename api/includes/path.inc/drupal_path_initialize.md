# drupal_path_initialize()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 15–22 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L15-L22)

## Signature

```php
function drupal_path_initialize()
```

## Documentation

```text
Initialize the $_GET['q'] variable to the proper normal path.
```

## Code

```php
function drupal_path_initialize() {
  // Ensure $_GET['q'] is set before calling drupal_normal_path(), to support
  // path caching with hook_url_inbound_alter().
  if (empty($_GET['q'])) {
    $_GET['q'] = variable_get('site_frontpage', 'node');
  }
  $_GET['q'] = drupal_get_normal_path($_GET['q']);
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
