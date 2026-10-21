# trigger_unassign()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 55–84 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L55-L84)
- **Module/theme:** trigger
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function trigger_unassign($form, $form_state, $module, $hook = NULL, $aid = NULL)
```

## Documentation

```text
Form constructor for confirmation page for removal of an assigned action.

@param $module
  The tab of triggers the user will be directed to after successful
  removal of the action, or if the confirmation form is cancelled.
@param $hook
  The name of the trigger hook, e.g., 'node_insert'.
@param $aid
  The action ID.

@see trigger_unassign_submit()
@ingroup forms
```

## Code

```php
function trigger_unassign($form, $form_state, $module, $hook = NULL, $aid = NULL) {
  if (!isset($hook, $aid)) {
    drupal_goto('admin/structure/trigger');
  }

  $form['hook'] = array(
    '#type' => 'value',
    '#value' => $hook,
  );
  $form['module'] = array(
    '#type' => 'value',
    '#value' => $module,
  );
  $form['aid'] = array(
    '#type' => 'value',
    '#value' => $aid,
  );

  $action = actions_function_lookup($aid);
  $actions = actions_get_all_actions();

  $destination = 'admin/structure/trigger/' . $module;

  return confirm_form($form,
    t('Are you sure you want to unassign the action %title?', array('%title' => $actions[$action]['label'])),
    $destination,
    t('You can assign it again later if you wish.'),
    t('Unassign'), t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
