# NodeCreationTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 600–706 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L600-L706)
- **Module/theme:** node

## Signature

```php
class NodeCreationTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests creating and saving a node.
```

## Methods (derived index)

- [getInfo()](NodeCreationTestCase/getInfo.md)
- [setUp()](NodeCreationTestCase/setUp.md)
- [testNodeCreation()](NodeCreationTestCase/testNodeCreation.md) — Creates a "Basic page" node and verifies its consistency in the database.
- [testFailedPageCreation()](NodeCreationTestCase/testFailedPageCreation.md) — Verifies that a transaction rolls back the failed creation.
- [testUnpublishedNodeCreation()](NodeCreationTestCase/testUnpublishedNodeCreation.md) — Create an unpublished node and confirm correct redirect behavior.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
