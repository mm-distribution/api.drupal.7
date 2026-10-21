# drupal_delete_file_if_stale()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3975–3980 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3975-L3980)

## Signature

```php
function drupal_delete_file_if_stale($uri)
```

## Documentation

```text
Callback to delete files modified more than a set time ago.
```

## Code

```php
function drupal_delete_file_if_stale($uri) {
  // Default stale file threshold is 30 days.
  if (REQUEST_TIME - filemtime($uri) > variable_get('drupal_stale_file_threshold', 2592000)) {
    file_unmanaged_delete($uri);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
