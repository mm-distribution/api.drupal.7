# DrupalLocalStreamWrapper::getTarget()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 296–305 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L296-L305)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
protected function getTarget($uri = NULL)
```

## Documentation

```text
Returns the local writable target of the resource within the stream.

This function should be used in place of calls to realpath() or similar
functions when attempting to determine the location of a file. While
functions like realpath() may return the location of a read-only file, this
method may return a URI or path suitable for writing that is completely
separate from the URI used for reading.

@param $uri
  Optional URI.

@return
  Returns a string representing a location suitable for writing of a file,
  or FALSE if unable to write to the file such as with read-only streams.
```

## Code

```php
  protected function getTarget($uri = NULL) {
    if (!isset($uri)) {
      $uri = $this->uri;
    }

    list($scheme, $target) = explode('://', $uri, 2);

    // Remove erroneous leading or trailing, forward-slashes and backslashes.
    return trim($target, '\/');
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
