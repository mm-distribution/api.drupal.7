# taxonomy_update_7003()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 324–326 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L324-L326)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7003()
```

## Documentation

```text
Remove the related terms setting from vocabularies.

This setting has not been used since Drupal 6. The {taxonomy_relations} table
itself is retained to allow for data to be upgraded.
```

## Code

```php
function taxonomy_update_7003() {
  db_drop_field('taxonomy_vocabulary', 'relations');
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
