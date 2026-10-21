# TriggerContentTestCase::actionInfo()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 149–183 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L149-L183)
- **Class:** [TriggerContentTestCase](../TriggerContentTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function actionInfo($action)
```

## Documentation

```text
Returns some info about each of the content actions.

This is helper function for testActionsContent().

@param $action
  The name of the action to return info about.

@return
  An associative array of info about the action.
```

## Code

```php
  function actionInfo($action) {
    $info = array(
      'node_publish_action' => array(
        'property' => 'status',
        'expected' => 1,
        'name' => t('publish content'),
      ),
      'node_unpublish_action' => array(
        'property' => 'status',
        'expected' => 0,
        'name' => t('unpublish content'),
      ),
      'node_make_sticky_action' => array(
        'property' => 'sticky',
        'expected' => 1,
        'name' => t('make content sticky'),
      ),
      'node_make_unsticky_action' => array(
        'property' => 'sticky',
        'expected' => 0,
        'name' => t('make content unsticky'),
      ),
      'node_promote_action' => array(
        'property' => 'promote',
        'expected' => 1,
        'name' => t('promote content to front page'),
      ),
      'node_unpromote_action' => array(
        'property' => 'promote',
        'expected' => 0,
        'name' => t('remove content from front page'),
      ),
    );
    return $info[$action];
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
