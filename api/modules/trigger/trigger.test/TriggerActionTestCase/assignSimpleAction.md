# TriggerActionTestCase::assignSimpleAction()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 317–325 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L317-L325)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assignSimpleAction($trigger, $action)
```

## Documentation

```text
Assigns a simple (non-configurable) action to a trigger.

@param $trigger
  The trigger to assign to, like 'user_login'.
@param $action
  The simple action to be assigned, like 'comment_insert'.
```

## Code

```php
  function assignSimpleAction($trigger, $action) {
    $form_name = "trigger_{$trigger}_assign_form";
    $form_html_id = strtr($form_name, '_', '-');
    $edit = array('aid' => drupal_hash_base64($action));
    $trigger_type = preg_replace('/_.*/', '', $trigger);
    $this->drupalPost("admin/structure/trigger/$trigger_type", $edit, t('Assign'), array(), array(), $form_html_id);
    $actions = trigger_get_assigned_actions($trigger);
    $this->assertTrue(!empty($actions[$action]), format_string('Simple action @action assigned to trigger @trigger', array('@action' => $action, '@trigger' => $trigger)));
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
