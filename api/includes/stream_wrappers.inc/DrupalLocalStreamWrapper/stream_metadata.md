# DrupalLocalStreamWrapper::stream_metadata()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 594–627 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L594-L627)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_metadata($uri, $option, $value)
```

## Documentation

```text
Sets metadata on the stream.

WARNING: Do not call this method directly! It will be called internally by
PHP itself when one of the following functions is called on a stream URL:

@param string $uri
  A string containing the URI to the file to set metadata on.
@param int $option
  One of:
  - STREAM_META_TOUCH: The method was called in response to touch().
  - STREAM_META_OWNER_NAME: The method was called in response to chown()
    with string parameter.
  - STREAM_META_OWNER: The method was called in response to chown().
  - STREAM_META_GROUP_NAME: The method was called in response to chgrp().
  - STREAM_META_GROUP: The method was called in response to chgrp().
  - STREAM_META_ACCESS: The method was called in response to chmod().
@param mixed $value
  If option is:
  - STREAM_META_TOUCH: Array consisting of two arguments of the touch()
    function.
  - STREAM_META_OWNER_NAME or STREAM_META_GROUP_NAME: The name of the owner
    user/group as string.
  - STREAM_META_OWNER or STREAM_META_GROUP: The value of the owner
    user/group as integer.
  - STREAM_META_ACCESS: The argument of the chmod() as integer.

@return bool
  Returns TRUE on success or FALSE on failure. If $option is not
  implemented, FALSE should be returned.

@see touch()
@see chmod()
@see chown()
@see chgrp()
@link http://php.net/manual/streamwrapper.stream-metadata.php
```

## Code

```php
  public function stream_metadata($uri, $option, $value) {
    $target = $this->getLocalPath($uri);
    $return = FALSE;
    switch ($option) {
      case STREAM_META_TOUCH:
        if (!empty($value)) {
          $return = touch($target, $value[0], $value[1]);
        }
        else {
          $return = touch($target);
        }
        break;

      case STREAM_META_OWNER_NAME:
      case STREAM_META_OWNER:
        $return = chown($target, $value);
        break;

      case STREAM_META_GROUP_NAME:
      case STREAM_META_GROUP:
        $return = chgrp($target, $value);
        break;

      case STREAM_META_ACCESS:
        $return = chmod($target, $value);
        break;
    }
    if ($return) {
      // For convenience clear the file status cache of the underlying file,
      // since metadata operations are often followed by file status checks.
      clearstatcache(TRUE, $target);
    }
    return $return;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
