# taxonomy_get_parents()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1020–1036 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1020-L1036)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_parents($tid)
```

## Documentation

```text
Finds all parents of a given term ID.

@param $tid
  A taxonomy term ID.

@return
  An array of term objects which are the parents of the term $tid, or an
  empty array if parents are not found.
```

## Code

```php
function taxonomy_get_parents($tid) {
  $parents = &drupal_static(__FUNCTION__, array());

  if ($tid && !isset($parents[$tid])) {
    $query = db_select('taxonomy_term_data', 't');
    $query->join('taxonomy_term_hierarchy', 'h', 'h.parent = t.tid');
    $query->addField('t', 'tid');
    $query->condition('h.tid', $tid);
    $query->addTag('taxonomy_term_access');
    $query->orderBy('t.weight');
    $query->orderBy('t.name');
    $tids = $query->execute()->fetchCol();
    $parents[$tid] = taxonomy_term_load_multiple($tids);
  }

  return isset($parents[$tid]) ? $parents[$tid] : array();
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
