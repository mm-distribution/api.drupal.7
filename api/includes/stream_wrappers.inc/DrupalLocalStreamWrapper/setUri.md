# DrupalLocalStreamWrapper::setUri()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 269–271 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L269-L271)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
function setUri($uri)
```

## Documentation

```text
Base implementation of setUri().
```

## Code

```php
  function setUri($uri) {
    $this->uri = $uri;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
