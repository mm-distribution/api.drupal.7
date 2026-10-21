# DrupalLocalStreamWrapper::stream_flush()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 516–518 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L516-L518)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_flush()
```

## Documentation

```text
Support for fflush().

@return
  TRUE if data was successfully stored (or there was no data to store).

@see http://php.net/manual/streamwrapper.stream-flush.php
```

## Code

```php
  public function stream_flush() {
    return fflush($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
