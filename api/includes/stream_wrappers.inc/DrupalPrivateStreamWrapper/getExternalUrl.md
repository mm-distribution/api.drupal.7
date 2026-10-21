# DrupalPrivateStreamWrapper::getExternalUrl()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 980–983 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L980-L983)
- **Class:** [DrupalPrivateStreamWrapper](../DrupalPrivateStreamWrapper.md)

## Signature

```php
function getExternalUrl()
```

## Documentation

```text
Overrides getExternalUrl().

Return the HTML URI of a private file.
```

## Code

```php
  function getExternalUrl() {
    $path = str_replace('\\', '/', $this->getTarget());
    return url('system/files/' . $path, array('absolute' => TRUE));
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
