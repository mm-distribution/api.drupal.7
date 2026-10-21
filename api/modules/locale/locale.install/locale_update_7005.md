# locale_update_7005()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 207–215 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L207-L215)
- **Module/theme:** locale
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function locale_update_7005()
```

## Documentation

```text
Increase {locales_languages}.formula column's length.
```

## Code

```php
function locale_update_7005() {
  db_change_field('languages', 'formula', 'formula', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'description' => 'Plural formula in PHP code to evaluate to get plural indexes.',
  ));
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
