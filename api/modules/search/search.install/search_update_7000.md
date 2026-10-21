# search_update_7000()

- **Type:** Function
- **File:** [`modules/search/search.install`](_file.md), lines 161–182 · [local source](../../../../source/modules/search/search.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.install#L161-L182)
- **Module/theme:** search

## Signature

```php
function search_update_7000()
```

## Documentation

```text
Replace unique keys in 'search_dataset' and 'search_index' by primary keys.
```

## Code

```php
function search_update_7000() {
  db_drop_unique_key('search_dataset', 'sid_type');
  $dataset_type_spec = array(
    'type' => 'varchar',
    'length' => 16,
    'not null' => TRUE,
    'description' => 'Type of item, e.g. node.',
  );
  db_change_field('search_dataset', 'type', 'type', $dataset_type_spec);
  db_add_primary_key('search_dataset', array('sid', 'type'));

  db_drop_index('search_index', 'word');
  db_drop_unique_key('search_index', 'word_sid_type');
  $index_type_spec = array(
    'type' => 'varchar',
    'length' => 16,
    'not null' => TRUE,
    'description' => 'The {search_dataset}.type of the searchable item to which the word belongs.',
  );
  db_change_field('search_index', 'type', 'type', $index_type_spec);
  db_add_primary_key('search_index', array('word', 'sid', 'type'));
}
```

---
_Drupal 7.103 · [modules/search/search.install](https://github.com/drupal/drupal/blob/7.103/modules/search/search.install) · Licensed GPL-2.0-or-later (see LICENSE)._
