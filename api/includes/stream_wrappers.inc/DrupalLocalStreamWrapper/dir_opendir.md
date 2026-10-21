# DrupalLocalStreamWrapper::dir_opendir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 863–868 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L863-L868)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function dir_opendir($uri, $options)
```

## Documentation

```text
Support for opendir().

@param $uri
  A string containing the URI to the directory to open.
@param $options
  Unknown (parameter is not documented in PHP Manual).

@return
  TRUE on success.

@see http://php.net/manual/streamwrapper.dir-opendir.php
```

## Code

```php
  public function dir_opendir($uri, $options) {
    $this->uri = $uri;
    $this->handle = opendir($this->getLocalPath());

    return (bool) $this->handle;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
