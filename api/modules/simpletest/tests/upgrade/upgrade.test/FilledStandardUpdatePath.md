# FilledStandardUpdatePath

- **Type:** Class
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](_file.md), lines 625–691 · [local source](../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L625-L691)
- **Module/theme:** batch_test

## Signature

```php
class FilledStandardUpdatePath extends UpdatePathTestCase
```

## Documentation

```text
Performs point release update tests on a 'filled' database.

Loads an installation of Drupal 7.0 and runs the update process on it.

The install contains the standard profile (plus all optional) modules
with generated content so that an update from any of the modules under this
profile installation can be wholly tested.
```

## Methods (derived index)

- [getInfo()](FilledStandardUpdatePath/getInfo.md)
- [setUp()](FilledStandardUpdatePath/setUp.md)
- [testFilledStandardUpdate()](FilledStandardUpdatePath/testFilledStandardUpdate.md) — Tests a successful point release update.

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
