# hook_file_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2904–2910 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2904-L2910)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_insert($file)
```

## Documentation

```text
Respond to a file being added.

This hook is called after a file has been added to the database. The hook
doesn't distinguish between files created as a result of a copy or those
created by an upload.

@param $file
  The file that has been added.

@see file_save()
```

## Code

```php
function hook_file_insert($file) {
  // Add a message to the log, if the file is a jpg
  $validate = file_validate_extensions($file, 'jpg');
  if (empty($validate)) {
    watchdog('file', 'A jpg has been added.');
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_insert()".

- [entity_crud_hook_test_file_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_file_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [file_test_file_insert()](../../simpletest/tests/file_test.module/file_test_file_insert.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
