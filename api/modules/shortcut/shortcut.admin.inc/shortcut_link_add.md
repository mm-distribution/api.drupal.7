# shortcut_link_add()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 419–427 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L419-L427)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_link_add($form, &$form_state, $shortcut_set)
```

## Documentation

```text
Form callback: builds the form for adding a new shortcut link.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param $shortcut_set
  An object representing the shortcut set to which the link will be added.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_link_edit_validate()
@see shortcut_link_add_submit()
```

## Code

```php
function shortcut_link_add($form, &$form_state, $shortcut_set) {
  drupal_set_title(t('Add new shortcut'));
  $form['shortcut_set'] = array(
    '#type' => 'value',
    '#value' => $shortcut_set,
  );
  $form += _shortcut_link_form_elements();
  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
