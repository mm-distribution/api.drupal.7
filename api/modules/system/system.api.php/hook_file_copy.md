# hook_file_copy()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2944–2953 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2944-L2953)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_copy($file, $source)
```

## Documentation

```text
Respond to a file that has been copied.

@param $file
  The newly copied file object.
@param $source
  The original file before the copy.

@see file_copy()
```

## Code

```php
function hook_file_copy($file, $source) {
  $file_user = user_load($file->uid);
  // Make sure that the file name starts with the owner's user name.
  if (strpos($file->filename, $file_user->name) !== 0) {
    $file->filename = $file_user->name . '_' . $file->filename;
    $file->save();

    watchdog('file', 'Copied file %source has been renamed to %destination', array('%source' => $source->filename, '%destination' => $file->filename));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_copy()".

- [file_test_file_copy()](../../simpletest/tests/file_test.module/file_test_file_copy.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
