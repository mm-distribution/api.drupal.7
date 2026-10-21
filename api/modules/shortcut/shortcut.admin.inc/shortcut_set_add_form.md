# shortcut_set_add_form()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 208–223 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L208-L223)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_set_add_form($form, &$form_state)
```

## Documentation

```text
Form callback: builds the form for adding a shortcut set.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_set_add_form_validate()
@see shortcut_set_add_form_submit()
```

## Code

```php
function shortcut_set_add_form($form, &$form_state) {
  $form['new'] = array(
    '#type' => 'textfield',
    '#title' => t('Set name'),
    '#description' => t('The new set is created by copying items from your default shortcut set.'),
    '#required' => TRUE,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Create new set'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
