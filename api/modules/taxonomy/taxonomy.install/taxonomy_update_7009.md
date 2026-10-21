# taxonomy_update_7009()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 877–884 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L877-L884)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7009()
```

## Documentation

```text
Change {taxonomy_term_data}.format into varchar.
```

## Code

```php
function taxonomy_update_7009() {
  db_change_field('taxonomy_term_data', 'format', 'format', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the description.',
  ));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
