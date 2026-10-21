# trigger_assign_form_submit()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 231–285 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L231-L285)
- **Module/theme:** trigger

## Signature

```php
function trigger_assign_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for trigger_assign_form().

@see trigger_assign_form_validate()
```

## Code

```php
function trigger_assign_form_submit($form, &$form_state) {
  if (!empty($form_state['values']['aid'])) {
    $aid = actions_function_lookup($form_state['values']['aid']);
    $weight = db_query("SELECT MAX(weight) FROM {trigger_assignments} WHERE hook = :hook", array(':hook' => $form_state['values']['hook']))->fetchField();

    // Insert the new action.
    db_insert('trigger_assignments')
      ->fields(array(
        'hook' => $form_state['values']['hook'],
        'aid' => $aid,
        'weight' => $weight + 1,
      ))
      ->execute();

    // If we are not configuring an action for a "presave" hook and this action
    // changes an object property, then we need to save the object, so the
    // property change will persist.
    $actions = actions_list();
    if (strpos($form_state['values']['hook'], 'presave') === FALSE && isset($actions[$aid]['behavior']) && in_array('changes_property', $actions[$aid]['behavior'])) {
      // Determine the corresponding save action name for this action.
      $save_action = strtok($aid, '_') . '_save_action';
      // If no corresponding save action exists, we need to bail out.
      if (!isset($actions[$save_action])) {
        throw new Exception(t('Missing/undefined save action (%save_aid) for %aid action.', array('%save_aid' => $aid, '%aid' => $aid)));
      }
      // Delete previous save action if it exists, and re-add it using a higher
      // weight.
      $save_action_assigned = db_query("SELECT aid FROM {trigger_assignments} WHERE hook = :hook AND aid = :aid", array(':hook' => $form_state['values']['hook'], ':aid' => $save_action))->fetchField();

      if ($save_action_assigned) {
        db_delete('trigger_assignments')
          ->condition('hook', $form_state['values']['hook'])
          ->condition('aid', $save_action)
          ->execute();
      }
      db_insert('trigger_assignments')
        ->fields(array(
          'hook' => $form_state['values']['hook'],
          'aid' => $save_action,
          'weight' => $weight + 2,
        ))
        ->execute();

      // If no save action existed before, inform the user about it.
      if (!$save_action_assigned) {
        drupal_set_message(t('The %label action has been appended, which is required to save the property change.', array('%label' => $actions[$save_action]['label'])));
      }
      // Otherwise, just inform about the new weight.
      else {
        drupal_set_message(t('The %label action was moved to save the property change.', array('%label' => $actions[$save_action]['label'])));
      }
    }
  }
  drupal_static_reset('trigger_get_assigned_actions');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
