# DrupalLocalStreamWrapper::stream_open()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 405–421 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L405-L421)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_open($uri, $mode, $options, &$opened_path)
```

## Documentation

```text
Support for fopen(), file_get_contents(), file_put_contents() etc.

@param $uri
  A string containing the URI to the file to open.
@param $mode
  The file mode ("r", "wb" etc.).
@param $options
  A bit mask of STREAM_USE_PATH and STREAM_REPORT_ERRORS.
@param $opened_path
  A string containing the path actually opened.

@return
  Returns TRUE if file was opened successfully.

@see http://php.net/manual/streamwrapper.stream-open.php
```

## Code

```php
  public function stream_open($uri, $mode, $options, &$opened_path) {
    $this->uri = $uri;
    $path = $this->getLocalPath();
    if ($path === FALSE) {
      if ($options & STREAM_REPORT_ERRORS) {
        trigger_error('stream_open() filename cannot be empty', E_USER_WARNING);
      }
      return FALSE;
    }
    $this->handle = ($options & STREAM_REPORT_ERRORS) ? fopen($path, $mode) : @fopen($path, $mode);

    if ((bool) $this->handle && $options & STREAM_USE_PATH) {
      $opened_path = $path;
    }

    return (bool) $this->handle;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
