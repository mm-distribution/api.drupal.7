# hook_file_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2984–2987 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2984-L2987)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_delete($file)
```

## Documentation

```text
Respond to a file being deleted.

@param $file
  The file that has just been deleted.

@see file_delete()
```

## Code

```php
function hook_file_delete($file) {
  // Delete all information associated with the file.
  db_delete('upload')->condition('fid', $file->fid)->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_delete()".

- [entity_crud_hook_test_file_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_file_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [file_test_file_delete()](../../simpletest/tests/file_test.module/file_test_file_delete.md) — `modules/simpletest/tests/file_test.module`
- [file_file_delete()](../../file/file.module/file_file_delete.md) — `modules/file/file.module`
- [image_file_delete()](../../image/image.module/image_file_delete.md) — `modules/image/image.module`
- [user_file_delete()](../../user/user.module/user_file_delete.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
