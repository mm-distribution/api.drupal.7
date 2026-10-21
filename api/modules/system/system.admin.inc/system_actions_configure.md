# system_actions_configure()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3119–3187 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3119-L3187)
- **Module/theme:** system

## Signature

```php
function system_actions_configure($form, &$form_state, $action = NULL)
```

## Documentation

```text
Menu callback; Creates the form for configuration of a single action.

We provide the "Description" field. The rest of the form is provided by the
action. We then provide the Save button. Because we are combining unknown
form elements with the action configuration form, we use an 'actions_' prefix
on our elements.

@param $action
  Hash of an action ID or an integer. If it is a hash, we are
  creating a new instance. If it is an integer, we are editing an existing
  instance.
@return
  A form definition.

@see system_actions_configure_validate()
@see system_actions_configure_submit()
```

## Code

```php
function system_actions_configure($form, &$form_state, $action = NULL) {
  if ($action === NULL) {
    drupal_goto('admin/config/system/actions');
  }

  $actions_map = actions_actions_map(actions_list());
  $edit = array();

  // Numeric action denotes saved instance of a configurable action.
  if (is_numeric($action)) {
    $aid = $action;
    // Load stored parameter values from database.
    $data = db_query("SELECT * FROM {actions} WHERE aid = :aid", array(':aid' => $aid))->fetch();
    $edit['actions_label'] = $data->label;
    $edit['actions_type'] = $data->type;
    $function = $data->callback;
    $action = drupal_hash_base64($data->callback);
    $params = unserialize($data->parameters);
    if ($params) {
      foreach ($params as $name => $val) {
        $edit[$name] = $val;
      }
    }
  }
  // Otherwise, we are creating a new action instance.
  else {
    $function = $actions_map[$action]['callback'];
    $edit['actions_label'] = $actions_map[$action]['label'];
    $edit['actions_type'] = $actions_map[$action]['type'];
  }

  $form['actions_label'] = array(
    '#type' => 'textfield',
    '#title' => t('Label'),
    '#default_value' => $edit['actions_label'],
    '#maxlength' => '255',
    '#description' => t('A unique label for this advanced action. This label will be displayed in the interface of modules that integrate with actions, such as Trigger module.'),
    '#weight' => -10
  );
  $action_form = $function . '_form';
  $form = array_merge($form, $action_form($edit));
  $form['actions_type'] = array(
    '#type' => 'value',
    '#value' => $edit['actions_type'],
  );
  $form['actions_action'] = array(
    '#type' => 'hidden',
    '#value' => $action,
  );
  // $aid is set when configuring an existing action instance.
  if (isset($aid)) {
    $form['actions_aid'] = array(
      '#type' => 'hidden',
      '#value' => $aid,
    );
  }
  $form['actions_configured'] = array(
    '#type' => 'hidden',
    '#value' => '1',
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#weight' => 13
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
