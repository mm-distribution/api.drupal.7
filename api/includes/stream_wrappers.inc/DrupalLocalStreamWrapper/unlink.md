# DrupalLocalStreamWrapper::unlink()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 717–720 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L717-L720)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function unlink($uri)
```

## Documentation

```text
Support for unlink().

@param $uri
  A string containing the URI to the resource to delete.

@return
  TRUE if resource was successfully deleted.

@see http://php.net/manual/streamwrapper.unlink.php
```

## Code

```php
  public function unlink($uri) {
    $this->uri = $uri;
    return drupal_unlink($this->getLocalPath());
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
