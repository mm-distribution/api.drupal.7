# profile_form_alter()

- **Type:** Function
- **File:** [`modules/profile/profile.module`](_file.md), lines 378–467 · [local source](../../../../source/modules/profile/profile.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module#L378-L467)
- **Module/theme:** profile
- **Implements:** [hook_form_alter()](../../system/system.api.php/hook_form_alter.md)

## Signature

```php
function profile_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Implements hook_form_alter().
```

## Code

```php
function profile_form_alter(&$form, &$form_state, $form_id) {
  if (!($form_id == 'user_register_form' || $form_id == 'user_profile_form')) {
    return;
  }
  $form['#validate'][] = 'profile_user_form_validate';
  $account = $form['#user'];
  $result = _profile_get_fields($form['#user_category'], $form['#user_category'] == 'register');
  $weight = 1;
  foreach ($result as $field) {
    $category = $field->category;
    if (!isset($form[$category])) {
      $form[$category] = array('#type' => 'fieldset', '#title' => check_plain($category), '#weight' => $weight++);
    }
    switch ($field->type) {
      case 'textfield':
      case 'url':
        $form[$category][$field->name] = array(
          '#type' => 'textfield',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#maxlength' => 255,
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
        );
        if ($field->autocomplete) {
          $form[$category][$field->name]['#autocomplete_path'] = "profile/autocomplete/" . $field->fid;
        }
        break;

      case 'textarea':
        $form[$category][$field->name] = array(
          '#type' => 'textarea',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
        );
        break;

      case 'list':
        $form[$category][$field->name] = array(
          '#type' => 'textarea',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
        );
        break;

      case 'checkbox':
        $form[$category][$field->name] = array(
          '#type' => 'checkbox',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
        );
        break;

      case 'selection':
        $options = array();
        $lines = preg_split("/[\n\r]/", $field->options);
        foreach ($lines as $line) {
          if ($line = trim($line)) {
            $options[$line] = $line;
          }
        }
        $form[$category][$field->name] = array(
          '#type' => 'select',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#options' => $options,
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
          '#empty_value' => 0,
        );
        break;

      case 'date':
        $form[$category][$field->name] = array(
          '#type' => 'date',
          '#title' => check_plain($field->title),
          '#default_value' => isset($account->{$field->name}) ? $account->{$field->name} : '',
          '#description' => _profile_form_explanation($field),
          '#required' => $field->required,
        );
        break;
    }
  }
}
```

---
_Drupal 7.103 · [modules/profile/profile.module](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.module) · Licensed GPL-2.0-or-later (see LICENSE)._
