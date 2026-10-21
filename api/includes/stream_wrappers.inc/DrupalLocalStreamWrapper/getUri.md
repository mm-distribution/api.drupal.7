# DrupalLocalStreamWrapper::getUri()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 276–278 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L276-L278)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
function getUri()
```

## Documentation

```text
Base implementation of getUri().
```

## Code

```php
  function getUri() {
    return $this->uri;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
