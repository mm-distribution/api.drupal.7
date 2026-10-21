# taxonomy_update_7002()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 291–316 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L291-L316)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_update_7002()
```

## Documentation

```text
Add {vocabulary}.machine_name column.
```

## Code

```php
function taxonomy_update_7002() {
  $field = array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
    'default' => '',
    'description' => 'The vocabulary machine name.',
  );

  db_add_field('taxonomy_vocabulary', 'machine_name', $field);

  // Do a direct query here, rather than calling taxonomy_get_vocabularies(),
  // in case Taxonomy module is disabled.
  $vids = db_query('SELECT vid FROM {taxonomy_vocabulary}')->fetchCol();
  foreach ($vids as $vid) {
    $machine_name = 'vocabulary_' . $vid;
    db_update('taxonomy_vocabulary')
      ->fields(array('machine_name' => $machine_name))
      ->condition('vid', $vid)
      ->execute();
  }

  // The machine_name unique key can only be added after we ensure the
  // machine_name column contains unique values.
  db_add_unique_key('taxonomy_vocabulary', 'machine_name', array('machine_name'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
