# file_unmanaged_move()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1139–1145 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1139-L1145)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmanaged_move($source, $destination = NULL, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Moves a file to a new location without database changes or hook invocation.

@param $source
  A string specifying the filepath or URI of the original file.
@param $destination
  A string containing the destination that $source should be moved to.
  This must be a stream wrapper URI. If this value is omitted, Drupal's
  default files scheme will be used, usually "public://".
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE - Replace the existing file.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
      unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  The URI of the moved file, or FALSE in the event of an error.

@see file_move()
```

## Code

```php
function file_unmanaged_move($source, $destination = NULL, $replace = FILE_EXISTS_RENAME) {
  $filepath = file_unmanaged_copy($source, $destination, $replace);
  if ($filepath == FALSE || file_unmanaged_delete($source) == FALSE) {
    return FALSE;
  }
  return $filepath;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
