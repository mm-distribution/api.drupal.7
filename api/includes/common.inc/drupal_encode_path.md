# drupal_encode_path()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 635–637 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L635-L637)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_encode_path($path)
```

## Documentation

```text
Encodes a Drupal path for use in a URL.

For aesthetic reasons slashes are not escaped.

Note that url() takes care of calling this function, so a path passed to that
function should not be encoded in advance.

@param $path
  The Drupal path to encode.
```

## Code

```php
function drupal_encode_path($path) {
  return str_replace('%2F', '/', rawurlencode((string) $path));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
