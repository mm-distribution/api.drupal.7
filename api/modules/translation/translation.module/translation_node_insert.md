# translation_node_insert()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 323–357 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L323-L357)
- **Module/theme:** translation
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function translation_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function translation_node_insert($node) {
  // Only act if we are dealing with a content type supporting translations.
  if (translation_supported_type($node->type)) {
    if (!empty($node->translation_source)) {
      if ($node->translation_source->tnid) {
        // Add node to existing translation set.
        $tnid = $node->translation_source->tnid;
      }
      else {
        // Create new translation set, using nid from the source node.
        $tnid = $node->translation_source->nid;
        db_update('node')
          ->fields(array(
            'tnid' => $tnid,
            'translate' => 0,
          ))
          ->condition('nid', $tnid)
          ->execute();

        // Flush the (untranslated) source node from the load cache.
        entity_get_controller('node')->resetCache(array($tnid));
      }

      db_update('node')
        ->fields(array(
          'tnid' => $tnid,
          'translate' => 0,
        ))
        ->condition('nid', $node->nid)
        ->execute();
      // Save tnid to avoid loss in case of resave.
      $node->tnid = $tnid;
    }
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
