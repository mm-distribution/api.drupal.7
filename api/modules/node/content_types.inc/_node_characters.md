# _node_characters()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 247–249 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L247-L249)
- **Module/theme:** node

## Signature

```php
function _node_characters($length)
```

## Documentation

```text
Helper function for teaser length choices.
```

## Code

```php
function _node_characters($length) {
  return ($length == 0) ? t('Unlimited') : format_plural($length, '1 character', '@count characters');
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
