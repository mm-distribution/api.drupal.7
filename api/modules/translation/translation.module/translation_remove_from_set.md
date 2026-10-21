# translation_remove_from_set()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 430–470 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L430-L470)
- **Module/theme:** translation

## Signature

```php
function translation_remove_from_set($node)
```

## Documentation

```text
Removes a node from its translation set and updates accordingly.

@param $node
  A node object.
```

## Code

```php
function translation_remove_from_set($node) {
  if (isset($node->tnid) && $node->tnid) {
    $query = db_update('node')
      ->fields(array(
        'tnid' => 0,
        'translate' => 0,
      ));

    // Determine which nodes to apply the update to.
    $set_nids = db_query('SELECT nid FROM {node} WHERE tnid = :tnid', array(':tnid' => $node->tnid))->fetchCol();
    if (count($set_nids) == 1) {
      // There is only one node left in the set: remove the set altogether.
      $query
        ->condition('tnid', $node->tnid)
        ->execute();

      $flush_set = TRUE;
    }
    else {
      $query
        ->condition('nid', $node->nid)
        ->execute();

      // If the node being removed was the source of the translation set,
      // we pick a new source - preferably one that is up to date.
      if ($node->tnid == $node->nid) {
        $new_tnid = db_query('SELECT nid FROM {node} WHERE tnid = :tnid ORDER BY translate ASC, nid ASC', array(':tnid' => $node->tnid))->fetchField();
        db_update('node')
          ->fields(array('tnid' => $new_tnid))
          ->condition('tnid', $node->tnid)
          ->execute();

        $flush_set = TRUE;
      }
    }

    // Flush the modified nodes from the load cache.
    $nids = !empty($flush_set) ? $set_nids : array($node->nid);
    entity_get_controller('node')->resetCache($nids);
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
