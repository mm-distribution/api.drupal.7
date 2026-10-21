# file_validate_name_length()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1779–1789 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1779-L1789)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate_name_length(stdClass $file)
```

## Documentation

```text
Checks for files with names longer than we can store in the database.

@param $file
  A Drupal file object.

@return
  An array. If the file name is too long, it will contain an error message.
```

## Code

```php
function file_validate_name_length(stdClass $file) {
  $errors = array();

  if (empty($file->filename)) {
    $errors[] = t("The file's name is empty. Please give a name to the file.");
  }
  if (strlen($file->filename) > 240) {
    $errors[] = t("The file's name exceeds the 240 characters limit. Please rename the file and try again.");
  }
  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
