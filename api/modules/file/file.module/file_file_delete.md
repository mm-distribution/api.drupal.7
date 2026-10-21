# file_file_delete()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 363–365 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L363-L365)
- **Module/theme:** file
- **Implements:** [hook_file_delete()](../../system/system.api.php/hook_file_delete.md)

## Signature

```php
function file_file_delete($file)
```

## Documentation

```text
Implements hook_file_delete().
```

## Code

```php
function file_file_delete($file) {
  // TODO: Remove references to a file that is in-use.
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
