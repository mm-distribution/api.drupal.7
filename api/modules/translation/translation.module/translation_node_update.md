# translation_node_update()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 362–395 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L362-L395)
- **Module/theme:** translation
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function translation_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function translation_node_update($node) {
  // Only act if we are dealing with a content type supporting translations.
  if (translation_supported_type($node->type)) {
    $langcode = entity_language('node', $node);
    if (isset($node->translation) && $node->translation && !empty($langcode) && $node->tnid) {
      // Update translation information.
      db_update('node')
        ->fields(array(
          'tnid' => $node->tnid,
          'translate' => $node->translation['status'],
        ))
        ->condition('nid', $node->nid)
        ->execute();

      if (!empty($node->translation['retranslate'])) {
        // This is the source node, asking to mark all translations outdated.
        $translations = db_select('node', 'n')
          ->fields('n', array('nid'))
          ->condition('nid', $node->nid, '<>')
          ->condition('tnid', $node->tnid)
          ->execute()
          ->fetchCol();

        db_update('node')
          ->fields(array('translate' => 1))
          ->condition('nid', $translations, 'IN')
          ->execute();

        // Flush the modified translation nodes from the load cache.
        entity_get_controller('node')->resetCache($translations);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
