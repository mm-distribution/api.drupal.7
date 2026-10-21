# trigger_assign_form()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 121–203 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L121-L203)
- **Module/theme:** trigger
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function trigger_assign_form($form, $form_state, $module, $hook, $label)
```

## Documentation

```text
Returns the form for assigning an action to a trigger.

@param $module
  The name of the trigger group, e.g., 'node'.
@param $hook
  The name of the trigger hook, e.g., 'node_insert'.
@param $label
  A plain English description of what this trigger does.

@see trigger_assign_form_validate()
@see trigger_assign_form_submit()
@ingroup forms
```

## Code

```php
function trigger_assign_form($form, $form_state, $module, $hook, $label) {
  $form['module'] = array(
    '#type' => 'hidden',
    '#value' => $module,
  );
  $form['hook'] = array(
    '#type' => 'hidden',
    '#value' => $hook,
  );
  // All of these forms use the same validate and submit functions.
  $form['#validate'][] = 'trigger_assign_form_validate';
  $form['#submit'][] = 'trigger_assign_form_submit';

  $options = array();
  $functions = array();
  // Restrict the options list to actions that declare support for this hook.
  foreach (actions_list() as $func => $metadata) {
    if (isset($metadata['triggers']) && array_intersect(array($hook, 'any'), $metadata['triggers'])) {
      $functions[] = $func;
    }
  }
  foreach (actions_actions_map(actions_get_all_actions()) as $aid => $action) {
    if (in_array($action['callback'], $functions)) {
      $options[$action['type']][$aid] = $action['label'];
    }
  }

  $form[$hook] = array(
    '#type' => 'fieldset',
    // !description is correct, since these labels are passed through t() in
    // hook_trigger_info().
    '#title' => t('Trigger: !description', array('!description' => $label)),
    '#theme' => 'trigger_display',
  );

  // Retrieve actions that are already assigned to this hook combination.
  $actions = trigger_get_assigned_actions($hook);
  $form[$hook]['assigned']['#type'] = 'value';
  $form[$hook]['assigned']['#value'] = array();
  foreach ($actions as $aid => $info) {
    // If action is defined unassign it, otherwise offer to delete all orphaned
    // actions.
    $hash = drupal_hash_base64($aid, TRUE);
    if (actions_function_lookup($hash)) {
      $form[$hook]['assigned']['#value'][$aid] = array(
        'label' => $info['label'],
        'link' => l(t('unassign'), "admin/structure/trigger/unassign/$module/$hook/$hash"),
      );
    }
    else {
      // Link to system_actions_remove_orphans() to do the clean up.
      $form[$hook]['assigned']['#value'][$aid] = array(
        'label' => $info['label'],
        'link' => l(t('Remove orphaned actions'), "admin/config/system/actions/orphan"),
      );
    }
  }

  $form[$hook]['parent'] = array(
    '#type' => 'container',
    '#attributes' => array('class' => array('container-inline')),
  );
  // List possible actions that may be assigned.
  if (count($options) != 0) {
    $form[$hook]['parent']['aid'] = array(
      '#type' => 'select',
      '#title' => t('List of trigger actions when !description', array('!description' => $label)),
      '#title_display' => 'invisible',
      '#options' => $options,
      '#empty_option' => t('Choose an action'),
    );
    $form[$hook]['parent']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Assign')
    );
  }
  else {
    $form[$hook]['none'] = array(
      '#markup' => t('No actions available for this trigger. <a href="@link">Add action</a>.', array('@link' => url('admin/config/system/actions/manage')))
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
