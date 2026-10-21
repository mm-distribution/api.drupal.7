# TriggerOtherTestCase::testActionsComment()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 623–647 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L623-L647)
- **Class:** [TriggerOtherTestCase](../TriggerOtherTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testActionsComment()
```

## Documentation

```text
Tests triggering on comment save.
```

## Code

```php
  function testActionsComment() {
    // Assign an action to the comment save trigger.
    $test_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($test_user);
    $action_id = 'trigger_test_generic_action';
    $hash = drupal_hash_base64($action_id);
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/comment', $edit, t('Assign'), array(), array(), 'trigger-comment-insert-assign-form');

    // Set action variable to FALSE.
    variable_set($action_id, FALSE);

    // Create a node and add a comment to it.
    $web_user = $this->drupalCreateUser(array('create article content', 'access content', 'skip comment approval', 'post comments'));
    $this->drupalLogin($web_user);
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $edit = array();
    $edit['subject'] = $this->randomName(10);
    $edit['comment_body[' . LANGUAGE_NONE . '][0][value]'] = $this->randomName(10) . ' ' . $this->randomName(10);
    $this->drupalGet('comment/reply/' . $node->nid);
    $this->drupalPost(NULL, $edit, t('Save'));

    // Verify that the action variable has been set.
    $this->assertTrue(variable_get($action_id, FALSE), 'Check that creating a comment triggered the action.');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
