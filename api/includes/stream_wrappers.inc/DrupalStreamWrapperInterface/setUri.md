# DrupalStreamWrapperInterface::setUri()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 136–136 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L136)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public function setUri($uri);
```

## Documentation

```text
Set the absolute stream resource URI.

This allows you to set the URI. Generally is only called by the factory
method.

@param $uri
  A string containing the URI that should be used for this instance.
```

## Code

```php
  public function setUri($uri);
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
