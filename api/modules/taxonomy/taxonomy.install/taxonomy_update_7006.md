# taxonomy_update_7006()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 829–836 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L829-L836)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7006()
```

## Documentation

```text
Add {taxonomy_term_data}.format column.
```

## Code

```php
function taxonomy_update_7006() {
  db_add_field('taxonomy_term_data', 'format', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => FALSE,
    'description' => 'The {filter_format}.format of the description.',
  ));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
