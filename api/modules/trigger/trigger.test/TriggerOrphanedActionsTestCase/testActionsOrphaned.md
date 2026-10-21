# TriggerOrphanedActionsTestCase::testActionsOrphaned()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 707–741 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L707-L741)
- **Class:** [TriggerOrphanedActionsTestCase](../TriggerOrphanedActionsTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsOrphaned()
```

## Documentation

```text
Tests logic around orphaned actions.
```

## Code

```php
  function testActionsOrphaned() {
    $action = 'trigger_test_generic_any_action';
    $hash = drupal_hash_base64($action);

    // Assign an action from a disable-able module to a trigger, then pull the
    // trigger, and make sure the actions fire.
    $test_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($test_user);
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/node', $edit, t('Assign'), array(), array(), 'trigger-node-presave-assign-form');

    // Create an unpublished node.
    $web_user = $this->drupalCreateUser(array('create page content', 'edit own page content', 'access content', 'administer nodes'));
    $this->drupalLogin($web_user);
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = '!SimpleTest test node! ' . $this->randomName(10);
    $edit["body[$langcode][0][value]"] = '!SimpleTest test body! ' . $this->randomName(32) . ' ' . $this->randomName(32);
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $this->assertRaw(t('!post %title has been created.', array('!post' => 'Basic page', '%title' => $edit["title"])), 'Make sure the Basic page has actually been created');

    // Action should have been fired.
    $this->assertTrue(variable_get('trigger_test_generic_any_action', FALSE), 'Trigger test action successfully fired.');

    // Disable the module that provides the action and make sure the trigger
    // doesn't white screen.
    module_disable(array('trigger_test'));
    $loaded_node = $this->drupalGetNodeByTitle($edit["title"]);
    $edit["body[$langcode][0][value]"] = '!SimpleTest test body! ' . $this->randomName(32) . ' ' . $this->randomName(32);
    $this->drupalPost("node/$loaded_node->nid/edit", $edit, t('Save'));

    // If the node body was updated successfully we have dealt with the
    // unavailable action.
    $this->assertRaw(t('!post %title has been updated.', array('!post' => 'Basic page', '%title' => $edit["title"])), 'Make sure the Basic page can be updated with the missing trigger function.');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
