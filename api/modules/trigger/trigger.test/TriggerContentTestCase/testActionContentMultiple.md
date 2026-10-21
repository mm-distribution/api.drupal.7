# TriggerContentTestCase::testActionContentMultiple()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 113–136 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L113-L136)
- **Class:** [TriggerContentTestCase](../TriggerContentTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionContentMultiple()
```

## Documentation

```text
Tests multiple node actions.

Verifies that node actions are fired for each node individually, if acting
on multiple nodes.
```

## Code

```php
  function testActionContentMultiple() {
    // Assign an action to the node save/update trigger.
    $test_user = $this->drupalCreateUser(array('administer actions', 'administer nodes', 'create page content', 'access administration pages', 'access content overview'));
    $this->drupalLogin($test_user);
    $nodes = array();

    for ($index = 0; $index < 3; $index++) {
      $nodes[] = $this->drupalCreateNode(array('type' => 'page'));
    }

    $action_id = 'trigger_test_generic_any_action';
    $hash = drupal_hash_base64($action_id);
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/node', $edit, t('Assign'), array(), array(), 'trigger-node-update-assign-form');

    $edit = array(
      'operation' => 'unpublish',
      'nodes[' . $nodes[0]->nid . ']' => TRUE,
      'nodes[' . $nodes[1]->nid . ']' => TRUE,
    );
    $this->drupalPost('admin/content', $edit, t('Update'));
    $count = variable_get('trigger_test_generic_any_action', 0);
    $this->assertTrue($count == 2, format_string('Action was triggered 2 times. Actual: %count', array('%count' => $count)));
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
