# file_stream_wrapper_get_class()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 189–192 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L189-L192)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_stream_wrapper_get_class($scheme)
```

## Documentation

```text
Returns the stream wrapper class name for a given scheme.

@param $scheme
  Stream scheme.

@return
  Return string if a scheme has a registered handler, or FALSE.
```

## Code

```php
function file_stream_wrapper_get_class($scheme) {
  $wrappers = file_get_stream_wrappers();
  return empty($wrappers[$scheme]) ? FALSE : $wrappers[$scheme]['class'];
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
