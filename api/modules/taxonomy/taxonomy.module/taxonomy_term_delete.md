# taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 708–750 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L708-L750)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_delete($tid)
```

## Documentation

```text
Delete a term.

@param $tid
  The term ID.
@return
  Status constant indicating deletion.
```

## Code

```php
function taxonomy_term_delete($tid) {
  $transaction = db_transaction();
  try {
    $tids = array($tid);
    while ($tids) {
      $children_tids = $orphans = array();
      foreach ($tids as $tid) {
        // See if any of the term's children are about to be become orphans:
        if ($children = taxonomy_get_children($tid)) {
          foreach ($children as $child) {
            // If the term has multiple parents, we don't delete it.
            $parents = taxonomy_get_parents($child->tid);
            if (count($parents) == 1) {
              $orphans[] = $child->tid;
            }
          }
        }

        if ($term = taxonomy_term_load($tid)) {
          db_delete('taxonomy_term_data')
            ->condition('tid', $tid)
            ->execute();
          db_delete('taxonomy_term_hierarchy')
            ->condition('tid', $tid)
            ->execute();

          field_attach_delete('taxonomy_term', $term);
          module_invoke_all('taxonomy_term_delete', $term);
          module_invoke_all('entity_delete', $term, 'taxonomy_term');
          taxonomy_terms_static_reset();
        }
      }

      $tids = $orphans;
    }
    return SAVED_DELETED;
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('taxonomy', $e);
    throw $e;
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
