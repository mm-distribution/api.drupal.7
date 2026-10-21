# hook_file_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2887–2890 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2887-L2890)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_presave($file)
```

## Documentation

```text
Act on a file being inserted or updated.

This hook is called when a file has been added to the database. The hook
doesn't distinguish between files created as a result of a copy or those
created by an upload.

@param $file
  The file that has just been created.

@see file_save()
```

## Code

```php
function hook_file_presave($file) {
  // Change the file timestamp to an hour prior.
  $file->timestamp -= 3600;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_presave()".

- [entity_crud_hook_test_file_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_file_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
