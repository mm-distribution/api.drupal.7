# DrupalTemporaryStreamWrapper::getExternalUrl()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 1005–1008 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L1005-L1008)
- **Class:** [DrupalTemporaryStreamWrapper](../DrupalTemporaryStreamWrapper.md)

## Signature

```php
public function getExternalUrl()
```

## Documentation

```text
Overrides getExternalUrl().
```

## Code

```php
  public function getExternalUrl() {
    $path = str_replace('\\', '/', $this->getTarget());
    return url('system/temporary/' . $path, array('absolute' => TRUE));
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
