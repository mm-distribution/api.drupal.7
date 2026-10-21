# file_build_uri()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 990–993 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L990-L993)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_build_uri($path)
```

## Documentation

```text
Constructs a URI to Drupal's default files location given a relative path.
```

## Code

```php
function file_build_uri($path) {
  $uri = file_default_scheme() . '://' . $path;
  return file_stream_wrapper_uri_normalize($uri);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
