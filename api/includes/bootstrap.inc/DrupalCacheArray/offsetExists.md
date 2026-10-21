# DrupalCacheArray::offsetExists()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 363–365 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L363-L365)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
public function offsetExists($offset)
```

## Documentation

_No docblock in source._

## Code

```php
  public function offsetExists($offset) {
    return $this->offsetGet($offset) !== NULL;
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
