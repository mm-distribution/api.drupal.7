# translation_node_prepare()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 273–318 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L273-L318)
- **Module/theme:** translation
- **Implements:** [hook_node_prepare()](../../node/node.api.php/hook_node_prepare.md)

## Signature

```php
function translation_node_prepare($node)
```

## Documentation

```text
Implements hook_node_prepare().
```

## Code

```php
function translation_node_prepare($node) {
  // Only act if we are dealing with a content type supporting translations.
  if (translation_supported_type($node->type) &&
    // And it's a new node.
    empty($node->nid) &&
    // And the user has permission to translate content.
    user_access('translate content') &&
    // And the $_GET variables are set properly.
    isset($_GET['translation']) &&
    isset($_GET['target']) &&
    is_numeric($_GET['translation'])) {

    $source_node = node_load($_GET['translation']);
    if (empty($source_node) || !node_access('view', $source_node)) {
      // Source node not found or no access to view. We should not check
      // for edit access, since the translator might not have permissions
      // to edit the source node but should still be able to translate.
      return;
    }

    $language_list = language_list();
    $langcode = $_GET['target'];
    if (!isset($language_list[$langcode]) || ($source_node->language == $langcode)) {
      // If not supported language, or same language as source node, break.
      return;
    }

    // Ensure we don't have an existing translation in this language.
    if (!empty($source_node->tnid)) {
      $translations = translation_node_get_translations($source_node->tnid);
      if (isset($translations[$langcode])) {
        drupal_set_message(t('A translation of %title in %language already exists, a new %type will be created instead of a translation.', array('%title' => $source_node->title, '%language' => $language_list[$langcode]->name, '%type' => $node->type)), 'error');
        return;
      }
    }

    // Populate fields based on source node.
    $node->language = $langcode;
    $node->translation_source = $source_node;
    $node->title = $source_node->title;

    // Add field translations and let other modules module add custom translated
    // fields.
    field_attach_prepare_translation('node', $node, $langcode, $source_node, $source_node->language);
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
