# file_validate_extensions()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1805–1813 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1805-L1813)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate_extensions(stdClass $file, $extensions)
```

## Documentation

```text
Checks that the filename ends with an allowed extension.

@param $file
  A Drupal file object.
@param $extensions
  A string with a space separated list of allowed extensions.

@return
  An array. If the file extension is not allowed, it will contain an error
  message.

@see hook_file_validate()
```

## Code

```php
function file_validate_extensions(stdClass $file, $extensions) {
  $errors = array();

  $regex = '/\.(' . preg_replace('/ +/', '|', preg_quote($extensions)) . ')$/i';
  if (!preg_match($regex, $file->filename)) {
    $errors[] = t('Only files with the following extensions are allowed: %files-allowed.', array('%files-allowed' => $extensions));
  }
  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
