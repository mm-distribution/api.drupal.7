# _locale_batch_language_finished()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2393–2397 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2393-L2397)
- **Topics:** [locale-autoimport](../../topics/locale-autoimport.md)

## Signature

```php
function _locale_batch_language_finished($success, $results)
```

## Documentation

```text
Implements callback_batch_finished().

Finished callback of language addition locale import batch.
Inform the user of translation files imported.
```

## Code

```php
function _locale_batch_language_finished($success, $results) {
  if ($success) {
    drupal_set_message(format_plural(count($results), 'One translation file imported for the enabled modules.', '@count translation files imported for the enabled modules.'));
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
