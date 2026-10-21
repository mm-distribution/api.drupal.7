# taxonomy_update_7008()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 848–872 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L848-L872)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7008()
```

## Documentation

```text
Change the weight columns to normal int.
```

## Code

```php
function taxonomy_update_7008() {
  db_drop_index('taxonomy_term_data', 'taxonomy_tree');
  db_change_field('taxonomy_term_data', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'The weight of this term in relation to other terms.',
  ), array(
    'indexes' => array(
       'taxonomy_tree' => array('vid', 'weight', 'name'),
    ),
  ));

  db_drop_index('taxonomy_vocabulary', 'list');
  db_change_field('taxonomy_vocabulary', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'The weight of this vocabulary in relation to other vocabularies.',
  ), array(
    'indexes' => array(
      'list' => array('weight', 'name'),
    ),
  ));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
