# file_get_content_headers()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2732–2740 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2732-L2740)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_get_content_headers($file)
```

## Documentation

```text
Examines a file object and returns appropriate content headers for download.

@param $file
  A file object.

@return
  An associative array of headers, as expected by file_transfer().
```

## Code

```php
function file_get_content_headers($file) {
  $type = mime_header_encode($file->filemime);

  return array(
    'Content-Type' => $type,
    'Content-Length' => $file->filesize,
    'Cache-Control' => 'private',
  );
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
