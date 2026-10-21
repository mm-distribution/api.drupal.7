# locale_form_node_type_form_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 325–335 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L325-L335)
- **Module/theme:** locale
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function locale_form_node_type_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function locale_form_node_type_form_alter(&$form, &$form_state) {
  if (isset($form['type'])) {
    $form['workflow']['language_content_type'] = array(
      '#type' => 'radios',
      '#title' => t('Multilingual support'),
      '#default_value' => variable_get('language_content_type_' . $form['#node_type']->type, 0),
      '#options' => array(t('Disabled'), t('Enabled')),
      '#description' => t('Enable multilingual support for this content type. If enabled, a language selection field will be added to the editing form, allowing you to select from one of the <a href="!languages">enabled languages</a>. If disabled, new posts are saved with the default language. Existing content will not be affected by changing this option.', array('!languages' => url('admin/config/regional/language'))),
    );
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
