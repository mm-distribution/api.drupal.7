# hook_file_move()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2965–2974 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2965-L2974)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_move($file, $source)
```

## Documentation

```text
Respond to a file that has been moved.

@param $file
  The updated file object after the move.
@param $source
  The original file object before the move.

@see file_move()
```

## Code

```php
function hook_file_move($file, $source) {
  $file_user = user_load($file->uid);
  // Make sure that the file name starts with the owner's user name.
  if (strpos($file->filename, $file_user->name) !== 0) {
    $file->filename = $file_user->name . '_' . $file->filename;
    $file->save();

    watchdog('file', 'Moved file %source has been renamed to %destination', array('%source' => $source->filename, '%destination' => $file->filename));
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_move()".

- [file_test_file_move()](../../simpletest/tests/file_test.module/file_test_file_move.md) — `modules/simpletest/tests/file_test.module`
- [image_file_move()](../../image/image.module/image_file_move.md) — `modules/image/image.module`
- [user_file_move()](../../user/user.module/user_file_move.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
