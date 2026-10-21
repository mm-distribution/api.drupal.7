# taxonomy_term_load_multiple()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1327–1329 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1327-L1329)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_load_multiple($tids = array(), $conditions = array())
```

## Documentation

```text
Load multiple taxonomy terms based on certain conditions.

This function should be used whenever you need to load more than one term
from the database. Terms are loaded into memory and will not require
database access if loaded again during the same page request.

@see entity_load()
@see EntityFieldQuery

@param $tids
  An array of taxonomy term IDs.
@param $conditions
  (deprecated) An associative array of conditions on the {taxonomy_term_data}
  table, where the keys are the database fields and the values are the
  values those fields must have. Instead, it is preferable to use
  EntityFieldQuery to retrieve a list of entity IDs loadable by
  this function.

@return
  An array of term objects, indexed by tid. When no results are found, an
  empty array is returned.

@todo Remove $conditions in Drupal 8.
```

## Code

```php
function taxonomy_term_load_multiple($tids = array(), $conditions = array()) {
  return entity_load('taxonomy_term', $tids, $conditions);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
