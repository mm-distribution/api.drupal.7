# file_transfer()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2043–2064 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2043-L2064)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_transfer($uri, $headers)
```

## Documentation

```text
Transfers a file to the client using HTTP.

Pipes a file through Drupal to the client.

@param $uri
  String specifying the file URI to transfer.
@param $headers
  An array of HTTP headers to send along with file.
```

## Code

```php
function file_transfer($uri, $headers) {
  if (ob_get_level()) {
    ob_end_clean();
  }

  foreach ($headers as $name => $value) {
    drupal_add_http_header($name, $value);
  }
  drupal_send_headers();
  $scheme = file_uri_scheme($uri);
  // Transfer file in 1024 byte chunks to save memory usage.
  if ($scheme && file_stream_wrapper_valid_scheme($scheme) && $fd = fopen($uri, 'rb')) {
    while (!feof($fd)) {
      print fread($fd, 1024);
    }
    fclose($fd);
  }
  else {
    drupal_not_found();
  }
  drupal_exit();
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
