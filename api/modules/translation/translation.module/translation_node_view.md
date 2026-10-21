# translation_node_view()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 216–268 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L216-L268)
- **Module/theme:** translation
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function translation_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().

Displays translation links with language names if this node is part of a
translation set. If no language provider is enabled, "fall back" to simple
links built through the result of translation_node_get_translations().
```

## Code

```php
function translation_node_view($node, $view_mode) {
  // If the site has no translations or is not multilingual we have no content
  // translation links to display.
  if (isset($node->tnid) && drupal_multilingual() && $translations = translation_node_get_translations($node->tnid)) {
    $languages = language_list('enabled');
    $languages = $languages[1];

    // There might be a language provider enabled defining custom language
    // switch links which need to be taken into account while generating the
    // content translation links. As custom language switch links are available
    // only for configurable language types and interface language is the only
    // configurable language type in core, we use it as default. Contributed
    // modules can change this behavior by setting the system variable below.
    $type = variable_get('translation_language_type', LANGUAGE_TYPE_INTERFACE);
    $custom_links = language_negotiation_get_switch_links($type, "node/$node->nid");
    $links = array();

    foreach ($translations as $langcode => $translation) {
      // Do not show links to the same node, to unpublished translations or to
      // translations in disabled languages.
      if ($translation->status && isset($languages[$langcode]) && $langcode != entity_language('node', $node)) {
        $language = $languages[$langcode];
        $key = "translation_$langcode";

        if (isset($custom_links->links[$langcode])) {
          $links[$key] = $custom_links->links[$langcode];
        }
        else {
          $links[$key] = array(
            'href' => "node/{$translation->nid}",
            'title' => $language->native,
            'language' => $language,
          );
        }

        // Custom switch links are more generic than content translation links,
        // hence we override existing attributes with the ones below.
        $links[$key] += array('attributes' => array());
        $attributes = array(
          'title' => $translation->title,
          'class' => array('translation-link'),
        );
        $links[$key]['attributes'] = $attributes + $links[$key]['attributes'];
      }
    }

    $node->content['links']['translation'] = array(
      '#theme' => 'links__node__translation',
      '#links' => $links,
      '#attributes' => array('class' => array('links', 'inline')),
    );
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
