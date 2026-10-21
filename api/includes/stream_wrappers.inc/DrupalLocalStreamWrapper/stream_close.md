# DrupalLocalStreamWrapper::stream_close()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 553–555 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L553-L555)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_close()
```

## Documentation

```text
Support for fclose().

@return
  TRUE if stream was successfully closed.

@see http://php.net/manual/streamwrapper.stream-close.php
```

## Code

```php
  public function stream_close() {
    return fclose($this->handle);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
