# locale_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 366–384 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L366-L384)
- **Module/theme:** locale
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function locale_form_node_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter().
```

## Code

```php
function locale_form_node_form_alter(&$form, &$form_state) {
  if (isset($form['#node']->type) && locale_multilingual_node_type($form['#node']->type)) {
    $form['language'] = array(
      '#type' => 'select',
      '#title' => t('Language'),
      '#default_value' => (isset($form['#node']->language) ? $form['#node']->language : ''),
      '#options' => array(LANGUAGE_NONE => t('Language neutral')) + locale_language_list('name'),
    );
  }
  // Node type without language selector: assign the default for new nodes
  elseif (!isset($form['#node']->nid)) {
    $default = language_default();
    $form['language'] = array(
      '#type' => 'value',
      '#value' => $default->language
    );
  }
  $form['#submit'][] = 'locale_field_node_form_submit';
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
