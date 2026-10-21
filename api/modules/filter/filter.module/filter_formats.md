# filter_formats()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 419–452 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L419-L452)
- **Module/theme:** filter

## Signature

```php
function filter_formats($account = NULL)
```

## Documentation

```text
Retrieves a list of text formats, ordered by weight.

@param $account
  (optional) If provided, only those formats that are allowed for this user
  account will be returned. All formats will be returned otherwise. Defaults
  to NULL.

@return
  An array of text format objects, keyed by the format ID and ordered by
  weight.

@see filter_formats_reset()
```

## Code

```php
function filter_formats($account = NULL) {
  global $language;
  $formats = &drupal_static(__FUNCTION__, array());

  // All available formats are cached for performance.
  if (!isset($formats['all'])) {
    if ($cache = cache_get("filter_formats:{$language->language}")) {
      $formats['all'] = $cache->data;
    }
    else {
      $formats['all'] = db_select('filter_format', 'ff')
        ->addTag('translatable')
        ->fields('ff')
        ->condition('status', 1)
        ->orderBy('weight')
        ->execute()
        ->fetchAllAssoc('format');

      cache_set("filter_formats:{$language->language}", $formats['all']);
    }
  }

  // Build a list of user-specific formats.
  if (isset($account) && !isset($formats['user'][$account->uid])) {
    $formats['user'][$account->uid] = array();
    foreach ($formats['all'] as $format) {
      if (filter_access($format, $account)) {
        $formats['user'][$account->uid][$format->format] = $format;
      }
    }
  }

  return isset($account) ? $formats['user'][$account->uid] : $formats['all'];
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
