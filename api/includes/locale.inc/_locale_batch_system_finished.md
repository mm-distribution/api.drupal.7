# _locale_batch_system_finished()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2381–2385 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2381-L2385)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function _locale_batch_system_finished($success, $results)
```

## Documentation

```text
Implements callback_batch_finished().

Finished callback of system page locale import batch.
Inform the user of translation files imported.
```

## Code

```php
function _locale_batch_system_finished($success, $results) {
  if ($success) {
    drupal_set_message(format_plural(count($results), 'One translation file imported for the newly installed modules.', '@count translation files imported for the newly installed modules.'));
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
