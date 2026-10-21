# TriggerContentTestCase::testActionsContent()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 61–105 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L61-L105)
- **Class:** [TriggerContentTestCase](../TriggerContentTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsContent()
```

## Documentation

```text
Tests several content-oriented trigger issues.

These are in one function to assure they happen in the right order.
```

## Code

```php
  function testActionsContent() {
    global $user;
    $content_actions = array('node_publish_action', 'node_unpublish_action', 'node_make_sticky_action', 'node_make_unsticky_action', 'node_promote_action', 'node_unpromote_action');

    $test_user = $this->drupalCreateUser(array('administer actions'));
    $web_user = $this->drupalCreateUser(array('create page content', 'access content', 'administer nodes'));
    foreach ($content_actions as $action) {
      $hash = drupal_hash_base64($action);
      $info = $this->actionInfo($action);

      // Assign an action to a trigger, then pull the trigger, and make sure
      // the actions fire.
      $this->drupalLogin($test_user);
      $edit = array('aid' => $hash);
      $this->drupalPost('admin/structure/trigger/node', $edit, t('Assign'), array(), array(), 'trigger-node-presave-assign-form');
      // Create an unpublished node.
      $this->drupalLogin($web_user);
      $edit = array();
      $langcode = LANGUAGE_NONE;
      $edit["title"] = '!SimpleTest test node! ' . $this->randomName(10);
      $edit["body[$langcode][0][value]"] = '!SimpleTest test body! ' . $this->randomName(32) . ' ' . $this->randomName(32);
      $edit[$info['property']] = !$info['expected'];
      $this->drupalPost('node/add/page', $edit, t('Save'));
      // Make sure the text we want appears.
      $this->assertRaw(t('!post %title has been created.', array('!post' => 'Basic page', '%title' => $edit["title"])), 'Make sure the Basic page has actually been created');
      // Action should have been fired.
      $loaded_node = $this->drupalGetNodeByTitle($edit["title"]);
      $this->assertTrue($loaded_node->{$info['property']} == $info['expected'], format_string('Make sure the @action action fired.', array('@action' => $info['name'])));
      // Leave action assigned for next test

      // There should be an error when the action is assigned to the trigger
      // twice.
      $this->drupalLogin($test_user);
      // This action already assigned in this test.
      $edit = array('aid' => $hash);
      $this->drupalPost('admin/structure/trigger/node', $edit, t('Assign'), array(), array(), 'trigger-node-presave-assign-form');
      $this->assertRaw(t('The action you chose is already assigned to that trigger.'), 'Check to make sure an error occurs when assigning an action to a trigger twice.');

      // The action should be able to be unassigned from a trigger.
      $this->drupalPost('admin/structure/trigger/unassign/node/node_presave/' . $hash, array(), t('Unassign'));
      $this->assertRaw(t('Action %action has been unassigned.', array('%action' => ucfirst($info['name']))), format_string('Check to make sure the @action action can be unassigned from the trigger.', array('@action' => $info['name'])));
      $assigned = db_query("SELECT COUNT(*) FROM {trigger_assignments} WHERE aid IN (:keys)", array(':keys' => $content_actions))->fetchField();
      $this->assertFalse($assigned, 'Check to make sure unassign worked properly at the database level.');
    }
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
