# DrupalStreamWrapperInterface::realpath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 202–202 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L202)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public function realpath();
```

## Documentation

```text
Returns canonical, absolute path of the resource.

Implementation placeholder. PHP's realpath() does not support stream
wrappers. We provide this as a default so that individual wrappers may
implement their own solutions.

@return
  Returns a string with absolute pathname on success (implemented
  by core wrappers), or FALSE on failure or if the registered
  wrapper does not provide an implementation.
```

## Code

```php
  public function realpath();
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
