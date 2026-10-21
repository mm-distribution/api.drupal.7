# UpdaterException

- **Type:** Class
- **File:** [`includes/updater.inc`](_file.md), lines 423–424 · [local source](../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L423-L424)

## Signature

```php
class UpdaterException extends Exception
```

## Documentation

```text
Exception class for the Updater class hierarchy.

This is identical to the base Exception class, we just give it a more
specific name so that call sites that want to tell the difference can
specifically catch these exceptions and treat them differently.
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
