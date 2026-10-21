# node_assign_owner_action_form()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4002–4037 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4002-L4037)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_assign_owner_action_form($context)
```

## Documentation

```text
Generates the settings form for node_assign_owner_action().

@param $context
  Array of additional information about what triggered the action. Includes
  the following elements:
  - 'owner_uid': User ID to assign to the node.

@see node_assign_owner_action_submit()
@see node_assign_owner_action_validate()

@ingroup forms
```

## Code

```php
function node_assign_owner_action_form($context) {
  $description = t('The username of the user to which you would like to assign ownership.');
  $count = db_query("SELECT COUNT(*) FROM {users}")->fetchField();
  $owner_name = '';
  if (isset($context['owner_uid'])) {
    $owner_name = db_query("SELECT name FROM {users} WHERE uid = :uid", array(':uid' => $context['owner_uid']))->fetchField();
  }

  // Use dropdown for fewer than 200 users; textbox for more than that.
  if (intval($count) < 200) {
    $options = array();
    $result = db_query("SELECT uid, name FROM {users} WHERE uid > 0 ORDER BY name");
    foreach ($result as $data) {
      $options[$data->name] = $data->name;
    }
    $form['owner_name'] = array(
      '#type' => 'select',
      '#title' => t('Username'),
      '#default_value' => $owner_name,
      '#options' => $options,
      '#description' => $description,
    );
  }
  else {
    $form['owner_name'] = array(
      '#type' => 'textfield',
      '#title' => t('Username'),
      '#default_value' => $owner_name,
      '#autocomplete_path' => 'user/autocomplete',
      '#size' => '6',
      '#maxlength' => '60',
      '#description' => $description,
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
