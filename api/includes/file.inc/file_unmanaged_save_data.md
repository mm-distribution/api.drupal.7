# file_unmanaged_save_data()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2021–2031 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2021-L2031)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmanaged_save_data($data, $destination = NULL, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Saves a string to the specified destination without invoking file API.

This function is identical to file_save_data() except the file will not be
saved to the {file_managed} table and none of the file_* hooks will be
called.

@param $data
  A string containing the contents of the file.
@param $destination
  A string containing the destination location. This must be a stream wrapper
  URI. If no value is provided, a randomized name will be generated and the
  file will be saved using Drupal's default files scheme, usually
  "public://".
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE - Replace the existing file.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
                         unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  A string with the path of the resulting file, or FALSE on error.

@see file_save_data()
```

## Code

```php
function file_unmanaged_save_data($data, $destination = NULL, $replace = FILE_EXISTS_RENAME) {
  // Write the data to a temporary file.
  $temp_name = drupal_tempnam('temporary://', 'file');
  if (file_put_contents($temp_name, $data) === FALSE) {
    drupal_set_message(t('The file could not be created.'), 'error');
    return FALSE;
  }

  // Move the file to its final destination.
  return file_unmanaged_move($temp_name, $destination, $replace);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
