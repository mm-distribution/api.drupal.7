# BasicMinimalUpdatePath

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](_file.md), lines 517–614 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L517-L614)
- **Module/theme:** batch_test

## Signature

```php
class BasicMinimalUpdatePath extends UpdatePathTestCase
```

## Documentation

```text
Performs point release update tests on a bare database.

Loads an installation of Drupal 7.0 and runs the update process on it.

The install contains the minimal profile modules (without any generated
content) so that an update from of a site under this profile may be tested.
```

## Methods (derived index)

- [getInfo()](BasicMinimalUpdatePath/getInfo.md)
- [setUp()](BasicMinimalUpdatePath/setUp.md)
- [testBasicMinimalUpdate()](BasicMinimalUpdatePath/testBasicMinimalUpdate.md) — Tests a successful point release update.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
