# DrupalLocalStreamWrapper::chmod()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 342–348 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L342-L348)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
function chmod($mode)
```

## Documentation

```text
Base implementation of chmod().
```

## Code

```php
  function chmod($mode) {
    $output = @chmod($this->getLocalPath(), $mode);
    // We are modifying the underlying file here, so we have to clear the stat
    // cache so that PHP understands that URI has changed too.
    clearstatcache();
    return $output;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
