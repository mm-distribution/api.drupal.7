# DrupalLocalStreamWrapper::getDirectoryPath()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 264–264 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L264)
- **Class:** [DrupalLocalStreamWrapper](../DrupalLocalStreamWrapper.md)

## Signature

```php
abstract function getDirectoryPath();
```

## Documentation

```text
Gets the path that the wrapper is responsible for.
@TODO: Review this method name in D8 per http://drupal.org/node/701358

@return
  String specifying the path.
```

## Code

```php
  abstract function getDirectoryPath();
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
