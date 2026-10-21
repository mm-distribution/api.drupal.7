# translation_node_get_translations()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 486–505 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L486-L505)
- **Module/theme:** translation

## Signature

```php
function translation_node_get_translations($tnid)
```

## Documentation

```text
Gets all nodes in a given translation set.

@param $tnid
  The translation source nid of the translation set, the identifier of the
  node used to derive all translations in the set.

@return
  Array of partial node objects (nid, title, language) representing all
  nodes in the translation set, in effect all translations of node $tnid,
  including node $tnid itself. Because these are partial nodes, you need to
  node_load() the full node, if you need more properties. The array is
  indexed by language code.
```

## Code

```php
function translation_node_get_translations($tnid) {
  if (is_numeric($tnid) && $tnid) {
    $translations = &drupal_static(__FUNCTION__, array());

    if (!isset($translations[$tnid])) {
      $translations[$tnid] = array();
      $result = db_select('node', 'n')
        ->fields('n', array('nid', 'type', 'uid', 'status', 'title', 'language'))
        ->condition('n.tnid', $tnid)
        ->addTag('node_access')
        ->execute();

      foreach ($result as $node) {
        $langcode = entity_language('node', $node);
        $translations[$tnid][$langcode] = $node;
      }
    }
    return $translations[$tnid];
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
