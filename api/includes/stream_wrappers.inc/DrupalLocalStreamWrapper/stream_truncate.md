# DrupalLocalStreamWrapper::stream_truncate()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 640–642 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L640-L642)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_truncate($new_size)
```

## Documentation

```text
Truncate stream.

Will respond to truncation; e.g., through ftruncate().

@param int $new_size
  The new size.

@return bool
  TRUE on success, FALSE otherwise.
```

## Code

```php
  public function stream_truncate($new_size) {
    return ftruncate($this->handle, $new_size);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
