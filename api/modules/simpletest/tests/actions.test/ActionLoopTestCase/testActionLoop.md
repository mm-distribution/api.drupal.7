# ActionLoopTestCase::testActionLoop()

- **Type:** Method
- **File:** [`modules/simpletest/tests/actions.test`](../_file.md), lines 85–102 · [local source](../../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L85-L102)
- **Class:** [ActionLoopTestCase](../ActionLoopTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testActionLoop()
```

## Documentation

```text
Set up a loop with 3 - 12 recursions, and see if it aborts properly.
```

## Code

```php
  function testActionLoop() {
    $user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($user);

    $hash = drupal_hash_base64('actions_loop_test_log');
    $edit = array('aid' => $hash);
    $this->drupalPost('admin/structure/trigger/actions_loop_test', $edit, t('Assign'));

    // Delete any existing watchdog messages to clear the plethora of
    // "Action added" messages from when Drupal was installed.
    db_delete('watchdog')->execute();
    // To prevent this test from failing when xdebug is enabled, the maximum
    // recursion level should be kept low enough to prevent the xdebug
    // infinite recursion protection mechanism from aborting the request.
    // See http://drupal.org/node/587634.
    variable_set('actions_max_stack', 7);
    $this->triggerActions();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
