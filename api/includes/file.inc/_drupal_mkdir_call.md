# _drupal_mkdir_call()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 2590–2597 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L2590-L2597)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function _drupal_mkdir_call($uri, $mode, $recursive, $context)
```

## Documentation

```text
Helper function. Ensures we don't pass a NULL as a context resource to
mkdir().

@see drupal_mkdir()
```

## Code

```php
function _drupal_mkdir_call($uri, $mode, $recursive, $context) {
  if (is_null($context)) {
    return mkdir($uri, $mode, $recursive);
  }
  else {
    return mkdir($uri, $mode, $recursive, $context);
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
