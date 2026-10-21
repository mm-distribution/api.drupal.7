# DrupalLocalStreamWrapper::stream_cast()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 661–663 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L661-L663)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
public function stream_cast($cast_as)
```

## Documentation

```text
Retrieve the underlying stream resource.

This method is called in response to stream_select().

@param int $cast_as
  Can be STREAM_CAST_FOR_SELECT when stream_select() is calling
  stream_cast() or STREAM_CAST_AS_STREAM when stream_cast() is called for
  other uses.

@return resource|false
  The underlying stream resource or FALSE if stream_select() is not
  supported.

@see stream_select()
@link http://php.net/manual/streamwrapper.stream-cast.php
```

## Code

```php
  public function stream_cast($cast_as) {
    return $this->handle ? $this->handle : FALSE;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
