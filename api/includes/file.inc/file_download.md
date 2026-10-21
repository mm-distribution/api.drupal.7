# file_download()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2078–2096 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2078-L2096)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_download()
```

## Documentation

```text
Menu handler for private file transfers.

Call modules that implement hook_file_download() to find out if a file is
accessible and what headers it should be transferred with. If one or more
modules returned headers the download will start with the returned headers.
If a module returns -1 drupal_access_denied() will be returned. If the file
exists but no modules responded drupal_access_denied() will be returned.
If the file does not exist drupal_not_found() will be returned.

@see system_menu()
```

## Code

```php
function file_download() {
  // Merge remainder of arguments from GET['q'], into relative file path.
  $args = func_get_args();
  $scheme = array_shift($args);
  $target = implode('/', $args);
  $uri = $scheme . '://' . $target;
  $uri = file_uri_normalize_dot_segments($uri);
  if (file_stream_wrapper_valid_scheme($scheme) && is_file($uri)) {
    $headers = file_download_headers($uri);
    if (count($headers)) {
      file_transfer($uri, $headers);
    }
    drupal_access_denied();
  }
  else {
    drupal_not_found();
  }
  drupal_exit();
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
