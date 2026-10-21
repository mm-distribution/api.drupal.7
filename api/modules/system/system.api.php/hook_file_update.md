# hook_file_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2922–2932 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2922-L2932)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_update($file)
```

## Documentation

```text
Respond to a file being updated.

This hook is called when file_save() is called on an existing file.

@param $file
  The file that has just been updated.

@see file_save()
```

## Code

```php
function hook_file_update($file) {
  $file_user = user_load($file->uid);
  // Make sure that the file name starts with the owner's user name.
  if (strpos($file->filename, $file_user->name) !== 0) {
    $old_filename = $file->filename;
    $file->filename = $file_user->name . '_' . $file->filename;
    $file->save();

    watchdog('file', '%source has been renamed to %destination', array('%source' => $old_filename, '%destination' => $file->filename));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_update()".

- [entity_crud_hook_test_file_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_file_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [file_test_file_update()](../../simpletest/tests/file_test.module/file_test_file_update.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
