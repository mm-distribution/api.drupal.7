# NodeRevisionsTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 155–298 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L155-L298)
- **Module/theme:** node

## Signature

```php
class NodeRevisionsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the node revision functionality.
```

## Properties

### $nodes

```php
protected $nodes;
```

```text
Nodes used by the test.

@var array
```

### $logs

```php
protected $logs;
```

```text
The revision messages for node revisions created in the test.

@var array
```

## Methods (derived index)

- [getInfo()](NodeRevisionsTestCase/getInfo.md)
- [setUp()](NodeRevisionsTestCase/setUp.md)
- [testRevisions()](NodeRevisionsTestCase/testRevisions.md) — Checks node revision related operations.
- [testNodeRevisionWithoutLogMessage()](NodeRevisionsTestCase/testNodeRevisionWithoutLogMessage.md) — Checks that revisions are correctly saved without log messages.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
