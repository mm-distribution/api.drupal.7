# DrupalLocalStreamWrapper::rmdir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 813–821 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L813-L821)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function rmdir($uri, $options)
```

## Documentation

```text
Support for rmdir().

@param $uri
  A string containing the URI to the directory to delete.
@param $options
  A bit mask of STREAM_REPORT_ERRORS.

@return
  TRUE if directory was successfully removed.

@see http://php.net/manual/streamwrapper.rmdir.php
```

## Code

```php
  public function rmdir($uri, $options) {
    $this->uri = $uri;
    if ($options & STREAM_REPORT_ERRORS) {
      return drupal_rmdir($this->getLocalPath());
    }
    else {
      return @drupal_rmdir($this->getLocalPath());
    }
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
