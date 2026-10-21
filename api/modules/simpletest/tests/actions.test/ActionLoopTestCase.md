# ActionLoopTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/actions.test`](_file.md), lines 69–126 · [local source](../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L69-L126)
- **Module/theme:** batch_test

## Signature

```php
class ActionLoopTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test actions executing in a potential loop, and make sure they abort properly.
```

## Methods (derived index)

- [getInfo()](ActionLoopTestCase/getInfo.md)
- [setUp()](ActionLoopTestCase/setUp.md)
- [testActionLoop()](ActionLoopTestCase/testActionLoop.md) — Set up a loop with 3 - 12 recursions, and see if it aborts properly.
- [triggerActions()](ActionLoopTestCase/triggerActions.md) — Create an infinite loop by causing a watchdog message to be set, which causes the actions to be triggered again, up to actions_max_stack times.

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
