# DrupalStreamWrapperInterface::dirname()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 219–219 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L219)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public function dirname($uri = NULL);
```

## Documentation

```text
Gets the name of the directory from a given path.

This method is usually accessed through drupal_dirname(), which wraps
around the normal PHP dirname() function, which does not support stream
wrappers.

@param $uri
  An optional URI.

@return
  A string containing the directory name, or FALSE if not applicable.

@see drupal_dirname()
```

## Code

```php
  public function dirname($uri = NULL);
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
