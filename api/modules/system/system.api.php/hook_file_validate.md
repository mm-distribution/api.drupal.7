# hook_file_validate()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2862–2873 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2862-L2873)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_validate($file)
```

## Documentation

```text
Check that files meet a given criteria.

This hook lets modules perform additional validation on files. They're able
to report a failure by returning one or more error messages.

@param $file
  The file object being validated.
@return
  An array of error messages. If there are no problems with the file return
  an empty array.

@see file_validate()
```

## Code

```php
function hook_file_validate($file) {
  $errors = array();

  if (empty($file->filename)) {
    $errors[] = t("The file's name is empty. Please give a name to the file.");
  }
  if (strlen($file->filename) > 255) {
    $errors[] = t("The file's name exceeds the 255 characters limit. Please rename the file and try again.");
  }

  return $errors;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_validate()".

- [file_test_file_validate()](../../simpletest/tests/file_test.module/file_test_file_validate.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
