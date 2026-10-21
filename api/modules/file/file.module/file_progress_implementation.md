# file_progress_implementation()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 343–358 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L343-L358)
- **Module/theme:** file

## Signature

```php
function file_progress_implementation()
```

## Documentation

```text
Determines the preferred upload progress implementation.

@return
  A string indicating which upload progress system is available. Either "apc"
  or "uploadprogress". If neither are available, returns FALSE.
```

## Code

```php
function file_progress_implementation() {
  static $implementation;
  if (!isset($implementation)) {
    $implementation = FALSE;

    // We prefer the PECL extension uploadprogress because it supports multiple
    // simultaneous uploads. APC only supports one at a time.
    if (extension_loaded('uploadprogress')) {
      $implementation = 'uploadprogress';
    }
    elseif (extension_loaded('apc') && ini_get('apc.rfc1867')) {
      $implementation = 'apc';
    }
  }
  return $implementation;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
