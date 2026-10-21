# NodeSaveTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 1320–1475 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1320-L1475)
- **Module/theme:** node

## Signature

```php
class NodeSaveTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests node save related functionality, including import-save.
```

## Properties

### $web_user

```php
protected $web_user;
```

## Methods (derived index)

- [getInfo()](NodeSaveTestCase/getInfo.md)
- [setUp()](NodeSaveTestCase/setUp.md)
- [testImport()](NodeSaveTestCase/testImport.md) — Checks whether custom node IDs are saved properly during an import operation.
- [testTimestamps()](NodeSaveTestCase/testTimestamps.md) — Verifies accuracy of the "created" and "changed" timestamp functionality.
- [testDeterminingChanges()](NodeSaveTestCase/testDeterminingChanges.md) — Tests determing changes in hook_node_presave() and verifies the static node load cache is cleared upon save.
- [testNodeSaveOnInsert()](NodeSaveTestCase/testNodeSaveOnInsert.md) — Tests saving a node on node insert.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
