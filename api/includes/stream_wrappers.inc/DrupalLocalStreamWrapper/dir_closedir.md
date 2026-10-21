# DrupalLocalStreamWrapper::dir_closedir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 906–911 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L906-L911)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function dir_closedir()
```

## Documentation

```text
Support for closedir().

@return
  TRUE on success.

@see http://php.net/manual/streamwrapper.dir-closedir.php
```

## Code

```php
  public function dir_closedir() {
    closedir($this->handle);
    // We do not really have a way to signal a failure as closedir() does not
    // have a return value.
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
