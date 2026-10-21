# filter_update_7010()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 477–490 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L477-L490)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7010()
```

## Documentation

```text
Change {filter_format}.format and {filter}.format into varchar.
```

## Code

```php
function filter_update_7010() {
  db_change_field('filter_format', 'format', 'format', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'description' => 'Primary Key: Unique machine name of the format.',
  ));
  db_change_field('filter', 'format', 'format', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'description' => 'Foreign key: The {filter_format}.format to which this filter is assigned.',
  ));
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
