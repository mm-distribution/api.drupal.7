# shortcut_link_delete()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 735–749 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L735-L749)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_link_delete($form, &$form_state, $shortcut_link)
```

## Documentation

```text
Form callback: builds the confirmation form for deleting a shortcut link.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param $shortcut_link
  An array representing the link that will be deleted.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_link_delete_submit()
```

## Code

```php
function shortcut_link_delete($form, &$form_state, $shortcut_link) {
  $form['shortcut_link'] = array(
    '#type' => 'value',
    '#value' => $shortcut_link,
  );

  return confirm_form(
    $form,
    t('Are you sure you want to delete the shortcut %title?', array('%title' => $shortcut_link['link_title'])),
    'admin/config/user-interface/shortcut/' . $shortcut_link['menu_name'],
    t('This action cannot be undone.'),
    t('Delete'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
