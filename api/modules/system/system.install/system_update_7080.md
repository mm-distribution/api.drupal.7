# system_update_7080()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3333–3342 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3333-L3342)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7080()
```

## Documentation

```text
Convert the 'format' column in {date_format_locale} to case sensitive varchar.
```

## Code

```php
function system_update_7080() {
  $spec = array(
    'description' => 'The date format string.',
    'type' => 'varchar',
    'length' => 100,
    'not null' => TRUE,
    'binary' => TRUE,
  );
  db_change_field('date_format_locale', 'format', 'format', $spec);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
