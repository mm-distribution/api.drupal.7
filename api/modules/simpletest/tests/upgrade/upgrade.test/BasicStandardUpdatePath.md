# BasicStandardUpdatePath

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](_file.md), lines 441–507 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L441-L507)
- **Module/theme:** batch_test

## Signature

```php
class BasicStandardUpdatePath extends UpdatePathTestCase
```

## Documentation

```text
Performs point release update tests on a bare database.

Loads an installation of Drupal 7.0 and runs the update process on it.

The install contains the standard profile (plus all optional) modules
without any content so that an update from any of the modules under this
profile installation can be wholly tested.
```

## Methods (derived index)

- [getInfo()](BasicStandardUpdatePath/getInfo.md)
- [setUp()](BasicStandardUpdatePath/setUp.md)
- [testBasicStandardUpdate()](BasicStandardUpdatePath/testBasicStandardUpdate.md) — Tests a successful point release update.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
