# NodeQueryAlter

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 2247–2451 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2247-L2451)
- **Module/theme:** node

## Signature

```php
class NodeQueryAlter extends DrupalWebTestCase
```

## Documentation

```text
Tests node_query_node_access_alter().
```

## Properties

### $accessUser

```php
protected $accessUser;
```

```text
User with permission to view content.

@var object
```

### $noAccessUser

```php
protected $noAccessUser;
```

```text
User without permission to view content.

@var object
```

### $noAccessUser2

```php
protected $noAccessUser2;
```

```text
User without permission to view content.

@var object
```

## Methods (derived index)

- [getInfo()](NodeQueryAlter/getInfo.md)
- [setUp()](NodeQueryAlter/setUp.md)
- [testNodeQueryAlterWithUI()](NodeQueryAlter/testNodeQueryAlterWithUI.md) — Tests that node access permissions are followed.
- [testNodeQueryAlterLowLevelWithAccess()](NodeQueryAlter/testNodeQueryAlterLowLevelWithAccess.md) — Tests 'node_access' query alter, for user with access.
- [testNodeQueryAlterLowLevelNoAccess()](NodeQueryAlter/testNodeQueryAlterLowLevelNoAccess.md) — Tests 'node_access' query alter, for user without access.
- [testNodeQueryAlterLowLevelEditAccess()](NodeQueryAlter/testNodeQueryAlterLowLevelEditAccess.md) — Tests 'node_access' query alter, for edit access.
- [testNodeQueryAlterOverride()](NodeQueryAlter/testNodeQueryAlterOverride.md) — Tests 'node_access' query alter override.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
