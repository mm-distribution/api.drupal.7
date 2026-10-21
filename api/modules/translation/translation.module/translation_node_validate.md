# translation_node_validate()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 402–412 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L402-L412)
- **Module/theme:** translation
- **Implements:** [hook_node_validate()](../../node/node.api.php/hook_node_validate.md)

## Signature

```php
function translation_node_validate($node, $form)
```

## Documentation

```text
Implements hook_node_validate().

Ensures that duplicate translations can't be created for the same source.
```

## Code

```php
function translation_node_validate($node, $form) {
  // Only act on translatable nodes with a tnid or translation_source.
  if (translation_supported_type($node->type) && (!empty($node->tnid) || !empty($form['#node']->translation_source->nid))) {
    $tnid = !empty($node->tnid) ? $node->tnid : $form['#node']->translation_source->nid;
    $translations = translation_node_get_translations($tnid);
    $langcode = entity_language('node', $node);
    if (isset($translations[$langcode]) && $translations[$langcode]->nid != $node->nid ) {
      form_set_error('language', t('There is already a translation in this language.'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
