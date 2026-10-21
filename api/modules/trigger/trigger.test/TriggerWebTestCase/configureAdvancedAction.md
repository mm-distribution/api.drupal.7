# TriggerWebTestCase::configureAdvancedAction()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 25–33 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L25-L33)
- **Class:** [TriggerWebTestCase](../TriggerWebTestCase.md)
- **Module/theme:** trigger

## Signature

```php
protected function configureAdvancedAction($action, $edit)
```

## Documentation

```text
Configures an advanced action.

@param $action
  The name of the action callback. For example: 'user_block_user_action'
@param $edit
  The $edit array for the form to be used to configure.
  Example members would be 'actions_label' (always), 'message', etc.

@return
  the aid (action id) of the configured action, or FALSE if none.
```

## Code

```php
  protected function configureAdvancedAction($action, $edit) {
    // Create an advanced action.
    $hash = drupal_hash_base64($action);
    $this->drupalPost("admin/config/system/actions/configure/$hash", $edit, t('Save'));
    $this->assertText(t('The action has been successfully saved.'));

    // Now we have to find out the action ID of what we created.
    return db_query('SELECT aid FROM {actions} WHERE callback = :callback AND label = :label', array(':callback' => $action, ':label' => $edit['actions_label']))->fetchField();
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
