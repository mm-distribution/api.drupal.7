# taxonomy_vocabulary_get_names()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1000–1008 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1000-L1008)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_get_names()
```

## Documentation

```text
Get names for all taxonomy vocabularies.

@return
  An associative array of objects keyed by vocabulary machine name with
  information about taxonomy vocabularies. Each object has properties:
  - name: The vocabulary name.
  - machine_name: The machine name.
  - vid: The vocabulary ID.
```

## Code

```php
function taxonomy_vocabulary_get_names() {
  $names = &drupal_static(__FUNCTION__);

  if (!isset($names)) {
    $names = db_query('SELECT name, machine_name, vid FROM {taxonomy_vocabulary}')->fetchAllAssoc('machine_name');
  }

  return $names;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
