# DrupalLocalStreamWrapper::rename()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 735–737 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L735-L737)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function rename($from_uri, $to_uri)
```

## Documentation

```text
Support for rename().

@param $from_uri,
  The URI to the file to rename.
@param $to_uri
  The new URI for file.

@return
  TRUE if file was successfully renamed.

@see http://php.net/manual/streamwrapper.rename.php
```

## Code

```php
  public function rename($from_uri, $to_uri) {
    return rename($this->getLocalPath($from_uri), $this->getLocalPath($to_uri));
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
