# translation_language_switch_links_alter()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 543–576 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L543-L576)
- **Module/theme:** translation
- **Implements:** [hook_language_switch_links_alter()](../../system/language.api.php/hook_language_switch_links_alter.md)

## Signature

```php
function translation_language_switch_links_alter(array &$links, $type, $path)
```

## Documentation

```text
Implements hook_language_switch_links_alter().

Replaces links with pointers to translated versions of the content.
```

## Code

```php
function translation_language_switch_links_alter(array &$links, $type, $path) {
  $language_type = variable_get('translation_language_type', LANGUAGE_TYPE_INTERFACE);

  if ($type == $language_type && preg_match("!^node/(\d+)(/.+|)!", $path, $matches)) {
    $node = node_load((int) $matches[1]);

    if (empty($node->tnid)) {
      // If the node cannot be found nothing needs to be done. If it does not
      // have translations it might be a language neutral node, in which case we
      // must leave the language switch links unaltered. This is true also for
      // nodes not having translation support enabled.
      if (empty($node) || entity_language('node', $node) == LANGUAGE_NONE || !translation_supported_type($node->type)) {
        return;
      }
      $langcode = entity_language('node', $node);
      $translations = array($langcode => $node);
    }
    else {
      $translations = translation_node_get_translations($node->tnid);
    }

    foreach ($links as $langcode => $link) {
      if (isset($translations[$langcode]) && $translations[$langcode]->status) {
        // Translation in a different node.
        $links[$langcode]['href'] = 'node/' . $translations[$langcode]->nid . $matches[2];
      }
      else {
        // No translation in this language, or no permission to view.
        unset($links[$langcode]['href']);
        $links[$langcode]['attributes']['class'][] = 'locale-untranslated';
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
