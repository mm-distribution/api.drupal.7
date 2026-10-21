# ActionLoopTestCase::triggerActions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/actions.test`](../_file.md), lines 109–125 · [local source](../../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L109-L125)
- **Class:** [ActionLoopTestCase](../ActionLoopTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function triggerActions()
```

## Documentation

```text
Create an infinite loop by causing a watchdog message to be set,
which causes the actions to be triggered again, up to actions_max_stack
times.
```

## Code

```php
  protected function triggerActions() {
    $this->drupalGet('<front>', array('query' => array('trigger_actions_on_watchdog' => TRUE)));
    $expected = array();
    $expected[] = 'Triggering action loop';
    for ($i = 1; $i <= variable_get('actions_max_stack', 35); $i++) {
      $expected[] = "Test log #$i";
    }
    $expected[] = 'Stack overflow: too many calls to actions_do(). Aborting to prevent infinite recursion.';

    $result = db_query("SELECT message FROM {watchdog} WHERE type = 'actions_loop_test' OR type = 'actions' ORDER BY wid");
    $loop_started = FALSE;
    foreach ($result as $row) {
      $expected_message = array_shift($expected);
      $this->assertEqual($row->message, $expected_message, t('Expected message %expected, got %message.', array('%expected' => $expected_message, '%message' => $row->message)));
    }
    $this->assertTrue(empty($expected), t('All expected messages found.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
