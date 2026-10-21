# translation_form_node_type_form_alter()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 119–124 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L119-L124)
- **Module/theme:** translation
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function translation_form_node_type_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for node_type_form().
```

## Code

```php
function translation_form_node_type_form_alter(&$form, &$form_state) {
  // Add translation option to content type form.
  $form['workflow']['language_content_type']['#options'][TRANSLATION_ENABLED] = t('Enabled, with translation');
  // Description based on text from locale.module.
  $form['workflow']['language_content_type']['#description'] = t('Enable multilingual support for this content type. If enabled, a language selection field will be added to the editing form, allowing you to select from one of the <a href="!languages">enabled languages</a>. You can also turn on translation for this content type, which lets you have content translated to any of the installed languages. If disabled, new posts are saved with the default language. Existing content will not be affected by changing this option.', array('!languages' => url('admin/config/regional/language')));
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
