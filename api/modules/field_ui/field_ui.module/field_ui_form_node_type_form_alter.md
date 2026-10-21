# field_ui_form_node_type_form_alter()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 388–398 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L388-L398)
- **Module/theme:** field_ui
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function field_ui_form_node_type_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Adds a button 'Save and add fields' to the 'Create content type' form.

@see node_type_form()
@see field_ui_form_node_type_form_submit()
```

## Code

```php
function field_ui_form_node_type_form_alter(&$form, $form_state) {
  // We want to display the button only on add page.
  if (empty($form['#node_type']->type)) {
    $form['actions']['save_continue'] = array(
      '#type' => 'submit',
      '#value' => t('Save and add fields'),
      '#weight' => 45,
    );
    $form['#submit'][] = 'field_ui_form_node_type_form_submit';
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
