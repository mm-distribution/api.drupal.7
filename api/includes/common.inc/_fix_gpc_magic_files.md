# _fix_gpc_magic_files()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1241–1250 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1241-L1250)

## Signature

```php
function _fix_gpc_magic_files(&$item, $key)
```

## Documentation

```text
Strips slashes from $_FILES items.

Callback for array_walk() within fix_gpc_magic().

The tmp_name key is skipped keys since PHP generates single backslashes for
file paths on Windows systems.

@param $item
  An item from $_FILES.
@param $key
  The key for the item within $_FILES.

@see http://php.net/manual/features.file-upload.php#42280
```

## Code

```php
function _fix_gpc_magic_files(&$item, $key) {
  if ($key != 'tmp_name') {
    if (is_array($item)) {
      array_walk($item, '_fix_gpc_magic_files');
    }
    else {
      $item = stripslashes($item);
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
