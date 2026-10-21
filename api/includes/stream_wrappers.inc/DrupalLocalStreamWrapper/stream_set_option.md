# DrupalLocalStreamWrapper::stream_set_option()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 701–704 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L701-L704)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_set_option($option, $arg1, $arg2)
```

## Documentation

```text
Change stream options.

This method is called to set options on the stream.

Since Windows systems do not allow it and it is not needed for most use
cases anyway, this method is not supported on local files and will trigger
an error and return false. If needed, custom subclasses can provide
OS-specific implementations for advanced use cases.

@param int $option
  One of:
  - STREAM_OPTION_BLOCKING: The method was called in response to
    stream_set_blocking().
  - STREAM_OPTION_READ_TIMEOUT: The method was called in response to
    stream_set_timeout().
  - STREAM_OPTION_WRITE_BUFFER: The method was called in response to
    stream_set_write_buffer().
@param int $arg1
  If option is:
  - STREAM_OPTION_BLOCKING: The requested blocking mode:
    - 1 means blocking.
    - 0 means not blocking.
  - STREAM_OPTION_READ_TIMEOUT: The timeout in seconds.
  - STREAM_OPTION_WRITE_BUFFER: The buffer mode, STREAM_BUFFER_NONE or
    STREAM_BUFFER_FULL.
@param int $arg2
  If option is:
  - STREAM_OPTION_BLOCKING: This option is not set.
  - STREAM_OPTION_READ_TIMEOUT: The timeout in microseconds.
  - STREAM_OPTION_WRITE_BUFFER: The requested buffer size.

@return bool
  TRUE on success, FALSE otherwise. If $option is not implemented, FALSE
  should be returned.
```

## Code

```php
  public function stream_set_option($option, $arg1, $arg2) {
    trigger_error('stream_set_option() not supported for local file based stream wrappers', E_USER_WARNING);
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
