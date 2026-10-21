# DrupalLocalStreamWrapper::getLocalPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 371–386 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L371-L386)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
protected function getLocalPath($uri = NULL)
```

## Documentation

```text
Returns the canonical absolute path of the URI, if possible.

@param string $uri
  (optional) The stream wrapper URI to be converted to a canonical
  absolute path. This may point to a directory or another type of file.

@return string|false
  If $uri is not set, returns the canonical absolute path of the URI
  previously set by the DrupalStreamWrapperInterface::setUri() function.
  If $uri is set and valid for this class, returns its canonical absolute
  path, as determined by the realpath() function. If $uri is set but not
  valid, returns FALSE.
```

## Code

```php
  protected function getLocalPath($uri = NULL) {
    if (!isset($uri)) {
      $uri = $this->uri;
    }
    $path = $this->getDirectoryPath() . '/' . $this->getTarget($uri);
    $realpath = realpath($path);
    if (!$realpath) {
      // This file does not yet exist.
      $realpath = realpath(dirname($path)) . '/' . drupal_basename($path);
    }
    $directory = realpath($this->getDirectoryPath());
    if (!$realpath || !$directory || strpos($realpath, $directory) !== 0) {
      return FALSE;
    }
    return $realpath;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
