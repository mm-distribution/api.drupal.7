# DrupalLocalStreamWrapper::realpath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 353–355 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L353-L355)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
function realpath()
```

## Documentation

```text
Base implementation of realpath().
```

## Code

```php
  function realpath() {
    return $this->getLocalPath();
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
