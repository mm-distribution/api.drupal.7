# DrupalStreamWrapperInterface::chmod()

- **Type:** Method
- **File:** [`includes/stream_wrappers.inc`](../_file.md), lines 188–188 · [local source](../../../../source/includes/stream_wrappers.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc#L188)
- **Class:** [DrupalStreamWrapperInterface](../DrupalStreamWrapperInterface.md)

## Signature

```php
public function chmod($mode);
```

## Documentation

```text
Changes permissions of the resource.

PHP lacks this functionality and it is not part of the official stream
wrapper interface. This is a custom implementation for Drupal.

@param $mode
  Integer value for the permissions. Consult PHP chmod() documentation
  for more information.

@return
  Returns TRUE on success or FALSE on failure.
```

## Code

```php
  public function chmod($mode);
```

---
_Drupal 7.103 · [includes/stream_wrappers.inc](https://github.com/drupal/drupal/blob/7.103/includes/stream_wrappers.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
