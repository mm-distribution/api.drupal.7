# DatabaseBasicSyntaxTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 3381–3477 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3381-L3477)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseBasicSyntaxTestCase extends DatabaseTestCase
```

## Documentation

```text
Test how the current database driver interprets the SQL syntax.

In order to ensure consistent SQL handling throughout Drupal
across multiple kinds of database systems, we test that the
database system interprets SQL syntax in an expected fashion.
```

## Methods (derived index)

- [getInfo()](DatabaseBasicSyntaxTestCase/getInfo.md)
- [setUp()](DatabaseBasicSyntaxTestCase/setUp.md)
- [testBasicConcat()](DatabaseBasicSyntaxTestCase/testBasicConcat.md) — Test for string concatenation.
- [testFieldConcat()](DatabaseBasicSyntaxTestCase/testFieldConcat.md) — Test for string concatenation with field values.
- [testLikeEscape()](DatabaseBasicSyntaxTestCase/testLikeEscape.md) — Test escaping of LIKE wildcards.
- [testLikeBackslash()](DatabaseBasicSyntaxTestCase/testLikeBackslash.md) — Test LIKE query containing a backslash.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
