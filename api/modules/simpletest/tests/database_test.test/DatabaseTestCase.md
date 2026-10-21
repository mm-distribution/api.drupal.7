# DatabaseTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 19–185 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L19-L185)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseTestCase extends DrupalWebTestCase
```

## Documentation

```text
Base test class for databases.

Because all database tests share the same test data, we can centralize that
here.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [setUp()](DatabaseTestCase/setUp.md)
- [installTables()](DatabaseTestCase/installTables.md) — Set up several tables needed by a certain test.
- [ensureSampleDataNull()](DatabaseTestCase/ensureSampleDataNull.md) — Set up tables for NULL handling.
- [addSampleData()](DatabaseTestCase/addSampleData.md) — Setup our sample data.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
