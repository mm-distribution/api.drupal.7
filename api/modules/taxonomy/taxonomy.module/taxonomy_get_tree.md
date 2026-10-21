# taxonomy_get_tree()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1118–1212 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1118-L1212)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_get_tree($vid, $parent = 0, $max_depth = NULL, $load_entities = FALSE)
```

## Documentation

```text
Create a hierarchical representation of a vocabulary.

@param $vid
  Which vocabulary to generate the tree for.
@param $parent
  The term ID under which to generate the tree. If 0, generate the tree
  for the entire vocabulary.
@param $max_depth
  The number of levels of the tree to return. Leave NULL to return all levels.
@param $load_entities
  If TRUE, a full entity load will occur on the term objects. Otherwise they
  are partial objects queried directly from the {taxonomy_term_data} table to
  save execution time and memory consumption when listing large numbers of
  terms. Defaults to FALSE.

@return
  An array of all term objects in the tree. Each term object is extended
  to have "depth" and "parents" attributes in addition to its normal ones.
  Results are statically cached. Term objects will be partial or complete
  depending on the $load_entities parameter.
```

## Code

```php
function taxonomy_get_tree($vid, $parent = 0, $max_depth = NULL, $load_entities = FALSE) {
  $children = &drupal_static(__FUNCTION__, array());
  $parents = &drupal_static(__FUNCTION__ . ':parents', array());
  $terms = &drupal_static(__FUNCTION__ . ':terms', array());

  // We cache trees, so it's not CPU-intensive to call taxonomy_get_tree() on a
  // term and its children, too.
  if (!isset($children[$vid])) {
    $children[$vid] = array();
    $parents[$vid] = array();
    $terms[$vid] = array();

    $query = db_select('taxonomy_term_data', 't');
    $query->join('taxonomy_term_hierarchy', 'h', 'h.tid = t.tid');
    $result = $query
      ->addTag('translatable')
      ->addTag('taxonomy_term_access')
      ->fields('t')
      ->fields('h', array('parent'))
      ->condition('t.vid', $vid)
      ->orderBy('t.weight')
      ->orderBy('t.name')
      ->execute();

    foreach ($result as $term) {
      $children[$vid][$term->parent][] = $term->tid;
      $parents[$vid][$term->tid][] = $term->parent;
      $terms[$vid][$term->tid] = $term;
    }
  }

  // Load full entities, if necessary. The entity controller statically
  // caches the results.
  if ($load_entities) {
    $term_entities = taxonomy_term_load_multiple(array_keys($terms[$vid]));
  }

  $max_depth = (!isset($max_depth)) ? count($children[$vid]) : $max_depth;
  $tree = array();

  // Keeps track of the parents we have to process, the last entry is used
  // for the next processing step.
  $process_parents = array();
  $process_parents[] = $parent;

  // Loops over the parent terms and adds its children to the tree array.
  // Uses a loop instead of a recursion, because it's more efficient.
  while (count($process_parents)) {
    $parent = array_pop($process_parents);
    // The number of parents determines the current depth.
    $depth = count($process_parents);
    if ($max_depth > $depth && !empty($children[$vid][$parent])) {
      $has_children = FALSE;
      $child = current($children[$vid][$parent]);
      do {
        if (empty($child)) {
          break;
        }
        $term = $load_entities ? $term_entities[$child] : $terms[$vid][$child];
        if (isset($parents[$vid][$term->tid])) {
          // Clone the term so that the depth attribute remains correct
          // in the event of multiple parents.
          $term = clone $term;
        }
        $term->depth = $depth;
        unset($term->parent);
        $term->parents = $parents[$vid][$term->tid];
        $tree[] = $term;
        if (!empty($children[$vid][$term->tid])) {
          $has_children = TRUE;

          // We have to continue with this parent later.
          $process_parents[] = $parent;
          // Use the current term as parent for the next iteration.
          $process_parents[] = $term->tid;

          // Reset pointers for child lists because we step in there more often
          // with multi parents.
          reset($children[$vid][$term->tid]);
          // Move pointer so that we get the correct term the next time.
          next($children[$vid][$parent]);
          break;
        }
      } while ($child = next($children[$vid][$parent]));

      if (!$has_children) {
        // We processed all terms in this hierarchy-level, reset pointer
        // so that this function works the next time it gets called.
        reset($children[$vid][$parent]);
      }
    }
  }

  return $tree;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
