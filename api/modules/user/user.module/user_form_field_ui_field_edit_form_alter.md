# user_form_field_ui_field_edit_form_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3858–3886 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3858-L3886)
- **Module/theme:** user
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function user_form_field_ui_field_edit_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Add a checkbox for the 'user_register_form' instance settings on the 'Edit
field instance' form.
```

## Code

```php
function user_form_field_ui_field_edit_form_alter(&$form, &$form_state, $form_id) {
  $instance = $form['#instance'];

  if ($instance['entity_type'] == 'user' && !$form['#field']['locked']) {
    $form['instance']['settings']['user_register_form'] = array(
      '#type' => 'checkbox',
      '#title' => t('Display on user registration form.'),
      '#description' => t("This is compulsory for 'required' fields."),
      // Field instances created in D7 beta releases before the setting was
      // introduced might be set as 'required' and 'not shown on user_register
      // form'. We make sure the checkbox comes as 'checked' for those.
      '#default_value' => $instance['settings']['user_register_form'] || $instance['required'],
      // Display just below the 'required' checkbox.
      '#weight' => $form['instance']['required']['#weight'] + .1,
      // Disabled when the 'required' checkbox is checked.
      '#states' => array(
        'enabled' => array('input[name="instance[required]"]' => array('checked' => FALSE)),
      ),
      // Checked when the 'required' checkbox is checked. This is done through
      // a custom behavior, since the #states system would also synchronize on
      // uncheck.
      '#attached' => array(
        'js' => array(drupal_get_path('module', 'user') . '/user.js'),
      ),
    );

    array_unshift($form['#submit'], 'user_form_field_ui_field_edit_form_submit');
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
