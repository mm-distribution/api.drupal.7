# DrupalPublicStreamWrapper::getLocalPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 941–957 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L941-L957)
- **Class:** [DrupalPublicStreamWrapper](../DrupalPublicStreamWrapper.md)

## Signature

```php
protected function getLocalPath($uri = NULL)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  protected function getLocalPath($uri = NULL) {
    $path = parent::getLocalPath($uri);

    if (variable_get('sa_core_2022_012_override', FALSE)) {
      return $path;
    }

    $private_path = variable_get('file_private_path', FALSE);
    if ($private_path) {
      $private_path = realpath($private_path);
      if ($private_path && strpos($path, $private_path) === 0) {
        return FALSE;
      }
    }

    return $path;
  }
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
