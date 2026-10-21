# taxonomy_update_7010()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 889–897 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L889-L897)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7010()
```

## Documentation

```text
Change {taxonomy_index}.created to support signed int.
```

## Code

```php
function taxonomy_update_7010() {
  db_change_field('taxonomy_index', 'created', 'created', array(
    'description' => 'The Unix timestamp when the node was created.',
    'type' => 'int',
    'unsigned' => FALSE,
    'not null' => TRUE,
    'default'=> 0,
  ));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
