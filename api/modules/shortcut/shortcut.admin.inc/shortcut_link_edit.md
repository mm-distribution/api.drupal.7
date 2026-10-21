# shortcut_link_edit()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 446–454 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L446-L454)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_link_edit($form, &$form_state, $shortcut_link)
```

## Documentation

```text
Form callback: builds the form for editing a shortcut link.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param $shortcut_link
  An array representing the link that is being edited.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_link_edit_validate()
@see shortcut_link_edit_submit()
```

## Code

```php
function shortcut_link_edit($form, &$form_state, $shortcut_link) {
  drupal_set_title(t('Editing @shortcut', array('@shortcut' => $shortcut_link['link_title'])));
  $form['original_shortcut_link'] = array(
    '#type' => 'value',
    '#value' => $shortcut_link,
  );
  $form += _shortcut_link_form_elements($shortcut_link);
  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
