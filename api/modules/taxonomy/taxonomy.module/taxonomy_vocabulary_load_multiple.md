# taxonomy_vocabulary_load_multiple()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1348–1350 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1348-L1350)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_load_multiple($vids = array(), $conditions = array())
```

## Documentation

```text
Load multiple taxonomy vocabularies based on certain conditions.

This function should be used whenever you need to load more than one
vocabulary from the database. Terms are loaded into memory and will not
require database access if loaded again during the same page request.

@see entity_load()

@param $vids
 An array of taxonomy vocabulary IDs, or FALSE to load all vocabularies.
@param $conditions
 An array of conditions to add to the query.

@return
 An array of vocabulary objects, indexed by vid.
```

## Code

```php
function taxonomy_vocabulary_load_multiple($vids = array(), $conditions = array()) {
  return entity_load('taxonomy_vocabulary', $vids, $conditions);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
