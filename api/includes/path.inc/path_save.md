# path_save()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 436–458 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L436-L458)

## Signature

```php
function path_save(&$path)
```

## Documentation

```text
Save a path alias to the database.

@param $path
  An associative array containing the following keys:
  - source: The internal system path.
  - alias: The URL alias.
  - pid: (optional) Unique path alias identifier.
  - language: (optional) The language of the alias.
```

## Code

```php
function path_save(&$path) {
  $path += array('language' => LANGUAGE_NONE);

  // Load the stored alias, if any.
  if (!empty($path['pid']) && !isset($path['original'])) {
    $path['original'] = path_load($path['pid']);
  }

  if (empty($path['pid'])) {
    drupal_write_record('url_alias', $path);
    module_invoke_all('path_insert', $path);
  }
  else {
    drupal_write_record('url_alias', $path, array('pid'));
    module_invoke_all('path_update', $path);
  }

  // Clear internal properties.
  unset($path['original']);

  // Clear the static alias cache.
  drupal_clear_path_cache($path['source']);
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
