# DrupalLocalStreamWrapper::mkdir()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 781–798 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L781-L798)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function mkdir($uri, $mode, $options)
```

## Documentation

```text
Support for mkdir().

@param $uri
  A string containing the URI to the directory to create.
@param $mode
  Permission flags - see mkdir().
@param $options
  A bit mask of STREAM_REPORT_ERRORS and STREAM_MKDIR_RECURSIVE.

@return
  TRUE if directory was successfully created.

@see http://php.net/manual/streamwrapper.mkdir.php
```

## Code

```php
  public function mkdir($uri, $mode, $options) {
    $this->uri = $uri;
    $recursive = (bool) ($options & STREAM_MKDIR_RECURSIVE);
    if ($recursive) {
      // $this->getLocalPath() fails if $uri has multiple levels of directories
      // that do not yet exist.
      $localpath = $this->getDirectoryPath() . '/' . $this->getTarget($uri);
    }
    else {
      $localpath = $this->getLocalPath($uri);
    }
    if ($options & STREAM_REPORT_ERRORS) {
      return drupal_mkdir($localpath, $mode, $recursive);
    }
    else {
      return @drupal_mkdir($localpath, $mode, $recursive);
    }
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
