# DrupalPublicStreamWrapper::getExternalUrl()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 933–936 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L933-L936)
- **Class:** [DrupalPublicStreamWrapper](../DrupalPublicStreamWrapper.md)

## Signature

```php
function getExternalUrl()
```

## Documentation

```text
Overrides getExternalUrl().

Return the HTML URI of a public file.
```

## Code

```php
  function getExternalUrl() {
    $path = str_replace('\\', '/', $this->getTarget());
    return $GLOBALS['base_url'] . '/' . self::getDirectoryPath() . '/' . drupal_encode_path($path);
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
