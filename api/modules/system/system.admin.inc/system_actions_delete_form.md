# system_actions_delete_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3223–3235 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3223-L3235)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_actions_delete_form($form, &$form_state, $action)
```

## Documentation

```text
Create the form for confirmation of deleting an action.

@see system_actions_delete_form_submit()
@ingroup forms
```

## Code

```php
function system_actions_delete_form($form, &$form_state, $action) {
  $form['aid'] = array(
    '#type' => 'hidden',
    '#value' => $action->aid,
  );
  return confirm_form($form,
    t('Are you sure you want to delete the action %action?', array('%action' => $action->label)),
    'admin/config/system/actions/manage',
    t('This cannot be undone.'),
    t('Delete'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
