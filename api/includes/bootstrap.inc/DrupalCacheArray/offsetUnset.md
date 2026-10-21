# DrupalCacheArray::offsetUnset()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 392–394 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L392-L394)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
public function offsetUnset($offset)
```

## Documentation

_No docblock in source._

## Code

```php
  public function offsetUnset($offset) {
    unset($this->storage[$offset]);
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
