# NodeRevisionPermissionsTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 2652–2762 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2652-L2762)
- **Module/theme:** node

## Signature

```php
class NodeRevisionPermissionsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests user permissions for node revisions.
```

## Properties

### $node_revisions

```php
protected $node_revisions = array();
```

```text
Nodes used by the test.

@var array
```

### $accounts

```php
protected $accounts = array();
```

```text
Users with different revision permission used by the test.

@var array
```

### $map

```php
protected $map = array(
    'view' => 'view revisions',
    'update' => 'revert revisions',
    'delete' => 'delete revisions',
  );
```

```text
Map revision permission names to node revision access ops.

@var array
```

## Methods (derived index)

- [getInfo()](NodeRevisionPermissionsTestCase/getInfo.md)
- [setUp()](NodeRevisionPermissionsTestCase/setUp.md)
- [testNodeRevisionAccess()](NodeRevisionPermissionsTestCase/testNodeRevisionAccess.md) — Tests the _node_revision_access() function.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
