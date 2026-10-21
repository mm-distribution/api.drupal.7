# taxonomy_get_children()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1075–1094 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1075-L1094)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_children($tid, $vid = 0)
```

## Documentation

```text
Finds all children of a term ID.

@param $tid
  A taxonomy term ID.
@param $vid
  An optional vocabulary ID to restrict the child search.

@return
  An array of term objects that are the children of the term $tid, or an
  empty array when no children exist.
```

## Code

```php
function taxonomy_get_children($tid, $vid = 0) {
  $children = &drupal_static(__FUNCTION__, array());

  if ($tid && !isset($children[$tid])) {
    $query = db_select('taxonomy_term_data', 't');
    $query->join('taxonomy_term_hierarchy', 'h', 'h.tid = t.tid');
    $query->addField('t', 'tid');
    $query->condition('h.parent', $tid);
    if ($vid) {
      $query->condition('t.vid', $vid);
    }
    $query->addTag('taxonomy_term_access');
    $query->orderBy('t.weight');
    $query->orderBy('t.name');
    $tids = $query->execute()->fetchCol();
    $children[$tid] = taxonomy_term_load_multiple($tids);
  }

  return isset($children[$tid]) ? $children[$tid] : array();
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
