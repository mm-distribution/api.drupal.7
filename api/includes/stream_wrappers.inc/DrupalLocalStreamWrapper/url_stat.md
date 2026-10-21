# DrupalLocalStreamWrapper::url_stat()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 837–848 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L837-L848)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function url_stat($uri, $flags)
```

## Documentation

```text
Support for stat().

@param $uri
  A string containing the URI to get information about.
@param $flags
  A bit mask of STREAM_URL_STAT_LINK and STREAM_URL_STAT_QUIET.

@return
  An array with file status, or FALSE in case of an error - see fstat()
  for a description of this array.

@see http://php.net/manual/streamwrapper.url-stat.php
```

## Code

```php
  public function url_stat($uri, $flags) {
    $this->uri = $uri;
    $path = $this->getLocalPath();
    // Suppress warnings if requested or if the file or directory does not
    // exist. This is consistent with PHP's plain filesystem stream wrapper.
    if ($flags & STREAM_URL_STAT_QUIET || !file_exists($path)) {
      return @stat($path);
    }
    else {
      return stat($path);
    }
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
