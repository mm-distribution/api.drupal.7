# taxonomy_get_parents_all()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1041–1061 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1041-L1061)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_parents_all($tid)
```

## Documentation

```text
Find all ancestors of a given term ID.
```

## Code

```php
function taxonomy_get_parents_all($tid) {
  $cache = &drupal_static(__FUNCTION__, array());

  if (isset($cache[$tid])) {
    return $cache[$tid];
  }

  $parents = array();
  if ($term = taxonomy_term_load($tid)) {
    $parents[] = $term;
    $n = 0;
    while ($parent = taxonomy_get_parents($parents[$n]->tid)) {
      $parents = array_merge($parents, $parent);
      $n++;
    }
  }

  $cache[$tid] = $parents;

  return $parents;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
