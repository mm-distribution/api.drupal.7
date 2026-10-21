# TriggerCronTestCase::testActionsCron()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 209–250 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L209-L250)
- **Class:** [TriggerCronTestCase](../TriggerCronTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsCron()
```

## Documentation

```text
Tests assigning multiple actions to the cron trigger.

This test ensures that both simple and multiple complex actions
succeed properly. This is done in the cron trigger test because
cron allows passing multiple actions in at once.
```

## Code

```php
  function testActionsCron() {
    // Create an administrative user.
    $test_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($test_user);

    // Assign a non-configurable action to the cron run trigger.
    $edit = array('aid' => drupal_hash_base64('trigger_test_system_cron_action'));
    $this->drupalPost('admin/structure/trigger/system', $edit, t('Assign'), array(), array(), 'trigger-cron-assign-form');

    // Assign a configurable action to the cron trigger.
    $action_label = $this->randomName();
    $edit = array(
      'actions_label' => $action_label,
      'subject' => $action_label,
    );
    $aid = $this->configureAdvancedAction('trigger_test_system_cron_conf_action', $edit);
    // $aid is likely 3 but if we add more uses for the sequences table in
    // core it might break, so it is easier to get the value from the database.
    $edit = array('aid' => drupal_hash_base64($aid));
    $this->drupalPost('admin/structure/trigger/system', $edit, t('Assign'), array(), array(), 'trigger-cron-assign-form');

    // Add a second configurable action to the cron trigger.
    $action_label = $this->randomName();
    $edit = array(
      'actions_label' => $action_label,
      'subject' => $action_label,
    );
    $aid = $this->configureAdvancedAction('trigger_test_system_cron_conf_action', $edit);
    $edit = array('aid' => drupal_hash_base64($aid));
    $this->drupalPost('admin/structure/trigger/system', $edit, t('Assign'), array(), array(), 'trigger-cron-assign-form');

    // Force a cron run.
    $this->cronRun();

    // Make sure the non-configurable action has fired.
    $action_run = variable_get('trigger_test_system_cron_action', FALSE);
    $this->assertTrue($action_run, 'Check that the cron run triggered the test action.');

    // Make sure that both configurable actions have fired.
    $action_run = variable_get('trigger_test_system_cron_conf_action', 0) == 2;
    $this->assertTrue($action_run, 'Check that the cron run triggered both complex actions.');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
