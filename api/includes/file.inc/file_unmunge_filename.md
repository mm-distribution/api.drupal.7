# file_unmunge_filename()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1227–1229 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1227-L1229)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmunge_filename($filename)
```

## Documentation

```text
Undoes the effect of file_munge_filename().

@param $filename
  String with the filename to be unmunged.

@return
  An unmunged filename string.
```

## Code

```php
function file_unmunge_filename($filename) {
  return str_replace('_.', '.', $filename);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
