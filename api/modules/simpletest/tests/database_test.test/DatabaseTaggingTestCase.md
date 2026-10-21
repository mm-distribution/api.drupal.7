# DatabaseTaggingTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/database_test.test`](_file.md), lines 2793–2915 · [local source](../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2793-L2915)
- **Module/theme:** batch_test

## Signature

```php
class DatabaseTaggingTestCase extends DatabaseTestCase
```

## Documentation

```text
Select tagging tests.

Tags are a way to flag queries for alter hooks so they know
what type of query it is, such as "node_access".
```

## Methods (derived index)

- [getInfo()](DatabaseTaggingTestCase/getInfo.md)
- [testHasTag()](DatabaseTaggingTestCase/testHasTag.md) — Confirm that a query has a "tag" added to it.
- [testHasAllTags()](DatabaseTaggingTestCase/testHasAllTags.md) — Test query tagging "has all of these tags" functionality.
- [testHasAnyTag()](DatabaseTaggingTestCase/testHasAnyTag.md) — Test query tagging "has at least one of these tags" functionality.
- [testExtenderHasTag()](DatabaseTaggingTestCase/testExtenderHasTag.md) — Confirm that an extended query has a "tag" added to it.
- [testExtenderHasAllTags()](DatabaseTaggingTestCase/testExtenderHasAllTags.md) — Test extended query tagging "has all of these tags" functionality.
- [testExtenderHasAnyTag()](DatabaseTaggingTestCase/testExtenderHasAnyTag.md) — Test extended query tagging "has at least one of these tags" functionality.
- [testMetaData()](DatabaseTaggingTestCase/testMetaData.md) — Test that we can attach meta data to a query object.

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
