# file_upload_max_size()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2269–2284 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2269-L2284)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_upload_max_size()
```

## Documentation

```text
Determines the maximum file upload size by querying the PHP settings.

@return
  A file size limit in bytes based on the PHP upload_max_filesize and
  post_max_size
```

## Code

```php
function file_upload_max_size() {
  static $max_size = -1;

  if ($max_size < 0) {
    // Start with post_max_size.
    $max_size = parse_size(ini_get('post_max_size'));

    // If upload_max_size is less, then reduce. Except if upload_max_size is
    // zero, which indicates no limit.
    $upload_max = parse_size(ini_get('upload_max_filesize'));
    if ($upload_max > 0 && $upload_max < $max_size) {
      $max_size = $upload_max;
    }
  }
  return $max_size;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
