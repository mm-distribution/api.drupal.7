# system_settings_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2824–2837 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2824-L2837)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_settings_form($form)
```

## Documentation

```text
Sets up a form to save information automatically.

This function adds a submit handler and a submit button to a form array. The
submit function saves all the data in the form, using variable_set(), to
variables named the same as the keys in the form array. Note that this means
you should normally prefix your form array keys with your module name, so
that they are unique when passed into variable_set().

If you need to manipulate the data in a custom manner, you can either put
your own submission handler in the form array before calling this function,
or just use your own submission handler instead of calling this function.

@param $form
  An associative array containing the structure of the form.

@return
  The form structure.

@see system_settings_form_submit()

@ingroup forms
```

## Code

```php
function system_settings_form($form) {
  $form['actions']['#type'] = 'actions';
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save configuration'));

  if (!empty($_POST) && form_get_errors()) {
    drupal_set_message(t('The settings have not been saved because of the errors.'), 'error');
  }
  $form['#submit'][] = 'system_settings_form_submit';
  // By default, render the form using theme_system_settings_form().
  if (!isset($form['#theme'])) {
    $form['#theme'] = 'system_settings_form';
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
