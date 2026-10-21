# TriggerOtherTestCase::testActionsUser()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 566–618 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L566-L618)
- **Class:** [TriggerOtherTestCase](../TriggerOtherTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsUser()
```

## Documentation

```text
Tests triggering on user create and user login.
```

## Code

```php
  function testActionsUser() {
    // Assign an action to the create user trigger.
    $test_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($test_user);
    $action_id = 'trigger_test_generic_action';
    $hash = drupal_hash_base64($action_id);
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/user', $edit, t('Assign'), array(), array(), 'trigger-user-insert-assign-form');

    // Set action variable to FALSE.
    variable_set($action_id, FALSE);

    // Create an unblocked user
    $web_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($web_user);
    $name = $this->randomName();
    $pass = user_password();
    $edit = array();
    $edit['name'] = $name;
    $edit['mail'] = $name . '@example.com';
    $edit['pass[pass1]'] = $pass;
    $edit['pass[pass2]'] = $pass;
    $edit['status'] = 1;
    $this->drupalPost('admin/people/create', $edit, t('Create new account'));

    // Verify that the action variable has been set.
    $this->assertTrue(variable_get($action_id, FALSE), 'Check that creating a user triggered the test action.');

    // Reset the action variable.
    variable_set($action_id, FALSE);

    $this->drupalLogin($test_user);
    // Assign a configurable action 'System message' to the user_login trigger.
    $action_edit = array(
      'actions_label' => $this->randomName(16),
      'message' => t("You have logged in:") . $this->randomName(16),
    );

    // Configure an advanced action that we can assign.
    $aid = $this->configureAdvancedAction('system_message_action', $action_edit);
    $edit = array('aid' => drupal_hash_base64($aid));
    $this->drupalPost('admin/structure/trigger/user', $edit, t('Assign'), array(), array(), 'trigger-user-login-assign-form');

    // Verify that the action has been assigned to the correct hook.
    $actions = trigger_get_assigned_actions('user_login');
    $this->assertEqual(1, count($actions), 'One Action assigned to the hook');
    $this->assertEqual($actions[$aid]['label'], $action_edit['actions_label'], 'Correct action label found.');

    // User should get the configured message at login.
    $contact_user = $this->drupalCreateUser(array('access site-wide contact form'));;
    $this->drupalLogin($contact_user);
    $this->assertText($action_edit['message']);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
