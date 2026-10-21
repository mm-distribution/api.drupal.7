# _aggregator_characters()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 141–143 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L141-L143)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_characters($length)
```

## Documentation

```text
Creates display text for teaser length option values.

Callback for drupal_map_assoc() within
aggregator_form_aggregator_admin_form_alter().

@param $length
  The desired length of teaser text, in bytes.

@return
  A translated string explaining the teaser string length.
```

## Code

```php
function _aggregator_characters($length) {
  return ($length == 0) ? t('Unlimited') : format_plural($length, '1 character', '@count characters');
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
