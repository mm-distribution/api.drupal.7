# system_actions_manage_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3069–3088 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3069-L3088)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_actions_manage_form($form, &$form_state, $options = array())
```

## Documentation

```text
Define the form for the actions overview page.

@param $form_state
  An associative array containing the current state of the form; not used.
@param $options
  An array of configurable actions.
@return
  Form definition.

@ingroup forms
@see system_actions_manage_form_submit()
```

## Code

```php
function system_actions_manage_form($form, &$form_state, $options = array()) {
  $form['parent'] = array(
    '#type' => 'fieldset',
    '#title' => t('Create an advanced action'),
    '#attributes' => array('class' => array('container-inline')),
  );
  $form['parent']['action'] = array(
    '#type' => 'select',
    '#title' => t('Action'),
    '#title_display' => 'invisible',
    '#options' => $options,
    '#empty_option' => t('Choose an advanced action'),
  );
  $form['parent']['actions'] = array('#type' => 'actions');
  $form['parent']['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Create'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
