# DrupalLocalStreamWrapper::dir_rewinddir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 890–896 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L890-L896)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function dir_rewinddir()
```

## Documentation

```text
Support for rewinddir().

@return
  TRUE on success.

@see http://php.net/manual/streamwrapper.dir-rewinddir.php
```

## Code

```php
  public function dir_rewinddir() {
    rewinddir($this->handle);
    // We do not really have a way to signal a failure as rewinddir() does not
    // have a return value and there is no way to read a directory handler
    // without advancing to the next file.
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
