# shortcut_set_edit_form()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 611–632 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L611-L632)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_set_edit_form($form, &$form_state, $shortcut_set)
```

## Documentation

```text
Form callback: builds the form for editing the shortcut set name.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param object $shortcut_set
  An object representing the shortcut set, as returned from
  shortcut_set_load().

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_set_edit_form_validate()
@see shortcut_set_edit_form_submit()
```

## Code

```php
function shortcut_set_edit_form($form, &$form_state, $shortcut_set) {
  $form['shortcut_set'] = array(
    '#type' => 'value',
    '#value' => $shortcut_set,
  );
  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => t('Set name'),
    '#default_value' => $shortcut_set->title,
    '#maxlength' => 255,
    '#required' => TRUE,
    '#weight' => -5,
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#weight' => 5,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
