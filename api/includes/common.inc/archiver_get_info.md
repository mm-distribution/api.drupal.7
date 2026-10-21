# archiver_get_info()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8561–8579 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8561-L8579)

## Signature

```php
function archiver_get_info()
```

## Documentation

```text
Retrieves a list of all available archivers.

@see hook_archiver_info()
@see hook_archiver_info_alter()
```

## Code

```php
function archiver_get_info() {
  $archiver_info = &drupal_static(__FUNCTION__, array());

  if (empty($archiver_info)) {
    $cache = cache_get('archiver_info');
    if ($cache === FALSE) {
      // Rebuild the cache and save it.
      $archiver_info = module_invoke_all('archiver_info');
      drupal_alter('archiver_info', $archiver_info);
      uasort($archiver_info, 'drupal_sort_weight');
      cache_set('archiver_info', $archiver_info);
    }
    else {
      $archiver_info = $cache->data;
    }
  }

  return $archiver_info;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
