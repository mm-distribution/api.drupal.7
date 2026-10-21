# _update_manager_cache_directory()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 944–953 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L944-L953)
- **Module/theme:** update

## Signature

```php
function _update_manager_cache_directory($create = TRUE)
```

## Documentation

```text
Returns the directory where update archive files should be cached.

@param $create
  (optional) Whether to attempt to create the directory if it does not
  already exist. Defaults to TRUE.

@return
  The full path to the temporary directory where update file archives should
  be cached.
```

## Code

```php
function _update_manager_cache_directory($create = TRUE) {
  $directory = &drupal_static(__FUNCTION__, '');
  if (empty($directory)) {
    $directory = 'temporary://update-cache-' . _update_manager_unique_identifier();
    if ($create && !file_exists($directory)) {
      mkdir($directory);
    }
  }
  return $directory;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
