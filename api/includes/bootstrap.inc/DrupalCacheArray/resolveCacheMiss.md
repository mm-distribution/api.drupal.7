# DrupalCacheArray::resolveCacheMiss()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 428–428 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L428)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
abstract protected function resolveCacheMiss($offset);
```

## Documentation

```text
Resolves a cache miss.

When an offset is not found in the object, this is treated as a cache
miss. This method allows classes implementing the interface to look up
the actual value and allow it to be cached.

@param $offset
  The offset that was requested.

@return
  The value of the offset, or NULL if no value was found.
```

## Code

```php
  abstract protected function resolveCacheMiss($offset);
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
