# taxonomy_update_7001()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 278–286 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L278-L286)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7001()
```

## Documentation

```text
Rename taxonomy tables.
```

## Code

```php
function taxonomy_update_7001() {
  db_rename_table('term_data', 'taxonomy_term_data');
  db_rename_table('term_hierarchy', 'taxonomy_term_hierarchy');
  db_rename_table('term_node', 'taxonomy_term_node');
  db_rename_table('term_relation', 'taxonomy_term_relation');
  db_rename_table('term_synonym', 'taxonomy_term_synonym');
  db_rename_table('vocabulary', 'taxonomy_vocabulary');
  db_rename_table('vocabulary_node_types', 'taxonomy_vocabulary_node_type');
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
